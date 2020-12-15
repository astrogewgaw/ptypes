import attr
import pprint
import typing

from pathlib import Path
from astropy import units as uu  # type: ignore
from astropy.coordinates import SkyCoord  # type: ignore
from typing import Any, Type, List, Dict, Tuple, TypeVar, Optional, Callable

from .formats import infread, infwrite, sigread, sigwrite


M = TypeVar("M", bound="Metadata")


class NoMeta(Exception):

    """"""

    pass


class Metadata(dict):

    """"""

    def __init__(self, items: Dict = {}):
        super(Metadata, self).__init__(items)

        for key, val in self.items():
            setattr(
                self,
                key,
                val,
            )

    @property
    def coords(self) -> SkyCoord:

        """"""

        try:
            coords = SkyCoord(
                self["raj"],
                self["decj"],
                unit=(uu.hour, uu.degree),
                frame="icrs",
            )
        except KeyError:
            pass

        return coords

    @classmethod
    def frominf(
        cls: Type[M],
        f: str,
    ) -> M:

        """"""

        d = infread(f)
        d["fname"] = f
        return cls.fromdict(d)

    @classmethod
    def fromhdr(
        cls: Type[M],
        f: str,
    ) -> M:

        """"""

        d = sigread(f)
        d["fname"] = f
        return cls.fromdict(d)

    @classmethod
    def fromfits(
        cls: Type[M],
        f: str,
    ) -> M:

        """"""

        d = fitsread(f)
        d["fname"] = f
        return cls.fromdict(d)

    @classmethod
    def fromgup(
        cls: Type[M],
        f: str,
    ) -> M:

        """"""

        d = gupread(f)
        d["fname"] = f
        return cls.fromdict(d)

    @classmethod
    def fromdict(
        cls: Type[M],
        d: Dict[
            str,
            Any,
        ],
    ) -> M:

        """"""

        return cls(d)

    def toinf(
        self,
        f: str,
    ) -> None:

        """"""

        attrs = self.todict()
        infwrite(attrs, f)

    def tohdr(
        self,
        f: str,
    ) -> None:

        """"""

        attrs = self.todict()
        sigwrite(attrs, f)

    def tofits(
        self,
        f: str,
    ) -> None:

        """"""

        attrs = self.todict()
        fitswrite(attrs, f)

    def togup(
        self,
        f: str,
    ) -> None:

        """"""

        attrs = self.todict()
        gupwrite(attrs, f)

    def todict(self) -> Dict[str, Any]:

        """"""

        return dict(self)

    def requires(
        self,
        params: List[str],
    ) -> Callable:

        """"""

        def inner(f: Callable) -> Callable:
            def wrapper(
                *args: List,
                **kwargs: Dict,
            ) -> Callable:

                for param in params:
                    p = self.get(param, None)
                    if p is not None:
                        continue
                    else:
                        raise NoMeta("Metadata missing. Exiting...")
                return f(*args, **kwargs)

            return wrapper

        return inner
