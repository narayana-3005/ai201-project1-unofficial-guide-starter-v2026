"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def _split_long_paragraph(paragraph: str, limit: int) -> list[str]:
    """Break one paragraph that is longer than `limit` on sentence ends."""
    sentences = re.split(r"(?<=[.!?])\s+", paragraph)
    pieces: list[str] = []
    current = ""
    for sentence in sentences:
        if current and len(current) + 1 + len(sentence) > limit:
            pieces.append(current)
            current = sentence
        else:
            current = f"{current} {sentence}".strip()
    if current:
        pieces.append(current)
    return pieces


def _join(group: list[tuple[str, int]]) -> str:
    """Glue pieces back together: a space inside a paragraph, a blank line between."""
    text = group[0][0]
    for (piece, number), (_, previous) in zip(group[1:], group):
        text += (" " if number == previous else "\n\n") + piece
    return text


def _length(group: list[tuple[str, int]]) -> int:
    return len(_join(group))


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split each post on its paragraph breaks, keeping the title on every chunk.

    Every campus_life document is a short title line, a blank line, then one
    to three short paragraphs. The title is the only place the building or
    course is named, so a paragraph cut loose from it can't answer anything
    on its own.

      1. The first paragraph is the title if it's short and has no full stop.
      2. The remaining paragraphs are packed together, in order, until adding
         the next would pass MAX_CHUNK_CHARS. A paragraph is never cut unless
         it alone is over the limit; then it is cut on sentence ends.
      3. A body shorter than MIN_CHUNK_CHARS is folded into its neighbour.
      4. The title is put back on top of every chunk instead of a character
         overlap.
    """
    limit = config.MAX_CHUNK_CHARS
    minimum = config.MIN_CHUNK_CHARS

    chunks: list[Chunk] = []
    for doc in documents:
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", doc.text) if p.strip()]

        title = ""
        if len(paragraphs) > 1 and len(paragraphs[0]) <= 80 and "." not in paragraphs[0]:
            title = paragraphs.pop(0)

        pieces: list[tuple[str, int]] = []
        for number, paragraph in enumerate(paragraphs):
            pieces.extend((piece, number) for piece in _split_long_paragraph(paragraph, limit))

        groups: list[list[tuple[str, int]]] = []
        for piece in pieces:
            if groups and _length(groups[-1]) + 2 + len(piece[0]) <= limit:
                groups[-1].append(piece)
            else:
                groups.append([piece])

        merged: list[list[tuple[str, int]]] = []
        for group in groups:
            if merged and _length(group) < minimum:
                merged[-1].extend(group)
            else:
                merged.append(group)
        if len(merged) > 1 and _length(merged[0]) < minimum:
            first = merged.pop(0)
            merged[0] = first + merged[0]

        for index, group in enumerate(merged):
            body = _join(group)
            text = f"{title}\n\n{body}" if title else body
            chunks.append(
                Chunk(
                    text=text,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
