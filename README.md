## Introduction

RSChroVer is a pyproject plugin to create a strictly chronological
version (yyyymmdd.hhmmss) from current Git version or time now.

Implemented for [Hatch](https://github.com/pypa/hatch), currently.

## Usage

Add this to `pyproject.toml`:

```toml
[build-system]
requires = ["hatchling", "rschronver"]
build-backend = "hatchling.build"

[tool.hatch.version]
source = "rschronver"
```

Creates a file `_rschronver.py` in the project root as an artifact.
Import this into `__init__.py` as follows:

```py
import ._rschronver

__version__ = _rschronver.__version__
```
