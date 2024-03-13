## Introduction

RSChronVer is a pyproject plugin to create a strictly chronological
version (yyyymmdd.hhmmss) from current Git version or time now.

Implemented for [Setuptools](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

## Usage

Add this to `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61", "rschronver"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["version"]
```

For ``__init__.py`` use this:

```py
import importlib.metadata

try:
    __version__ = importlib.metadata.version("pykern")
except importlib.metadata.PackageNotFoundError:
    # We only have a version once the package is installed.
    pass
```
