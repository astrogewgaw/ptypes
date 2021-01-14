import numpy as np  # type: ignore

from construct import (  # type: ignore
    bytes2bits,
    BitsInteger,
    GreedyRange,
)


def unpack(
    nbit: int,
    bytes: bytes,
) -> np.ndarray:

    """"""

    packed = [1, 2, 4]
    unpacked = [8, 16, 32, 64, 128]

    if nbit in packed:
        bint = BitsInteger(nbit)
        cons = GreedyRange(bint)
        bits = bytes2bits(bytes)
        data = cons.parse(bits)
        return np.asarray(data, dtype=np.uint8)
    elif nbit in unpacked:
        dtype = {
            8: np.unint8,
            16: np.int16,
            32: np.float32,
            64: np.float64,
            128: np.float128,
        }[nbit]
        return np.asarray(data, dtype=dtype)
    else:
        raise ValueError("{} bit format file not supported. Exiting...".format(nbit))
