from typing import IO, Generator
from os import SEEK_CUR, SEEK_SET


def chunkify(
    fobj: IO,
    nbit: int,
    nsamp: int,
    nchan: int,
    jump: int = 0,
    gulp: int = 1,
    header: int = 0,
    footer: int = 0,
) -> Generator:

    """"""

    gulp = min(nsamp, gulp)

    if abs(jump) >= gulp:
        errmsg = (
            "Number of samples to be read in each "
            "gulp must be greater than  the jump "
            "value. "
        )
        raise ValueError(errmsg)

    nread = nsamp // (gulp - jump)
    lread = nsamp % (gulp - jump)

    sizes = [gulp * nchan] * nread
    skips = [jump * nchan] * nread

    if lread != 0:
        sizes.append(lread * nchan - footer)
        skips.append(0)

    fobj.seek(header, SEEK_SET)

    for size, skip in zip(sizes, skips):
        chunk = fobj.read(size)
        fobj.seek(skip * nbit, SEEK_CUR)
        yield chunk
