# ptypes

## Like ctypes, but for pulsars.

[![Build Status][travis-badge]][travis]
[![codecov][codecov-badge]][codecov]
[![Code style: black][black-badge]][black]

**ptypes** is a Python package that aims to help pulsar astronomers process their data files with ease. Astronomers are notorious for having too many different formats for storing their data, and pulsar astronomy is no exception. Every data processing tool we use has its own data formats (although the situation ha started, thanks to the PSRFITS format!). **ptypes** can read and write files in several of the most used formats (primarily from the **SIGPROC** and **PRESTO** tools) and also help you process them! But isn't Python *slow*? Well, it is, but thanks to [**pybind11**][pybind11], we can use C++ under the hood to do all our data processing.

This project is still very much in development. If you want to experiment with it, do so at your own risk, because there will be frequent breaking changes. I am planning to come out with a 0.1.0 release soon, once I have implemented some of the most basic data processing operations and have fixed the API for all the data formats that we are trying to deal with here.

If you have any ideas, send me an email and we can talk!

[travis]: https://travis-ci.org/astrogewgaw/ptypes
[codecov]: https://codecov.io/gh/astrogewgaw/ptypes
[black]: https://github.com/psf/black
[pybind11]: https://github.com/pybind/pybind11

[travis-badge]: https://travis-ci.org/astrogewgaw/ptypes.svg?branch=release
[codecov-badge]: https://codecov.io/gh/astrogewgaw/ptypes/branch/release/graph/badge.svg
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
