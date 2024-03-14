## Introduction

RSChronVer is a
[setuptools.meta_build](https://setuptools.pypa.io/en/latest/build_meta.html)
plugin to add a
[chronological version](https://www.robnagler.com/2015/04/11/Major-Release-Syndrome.html)
(yyyymmdd.hhmmss)
to a Python package's metadata from the current Git commit.
This ensures a unique, sortable version for packages on [PiPI](https://pypi.org).

[RadiaSoft](https://radiasoft.net) uses chronological versioning for all its packages.

A chronological version is distinct from a
[CalVer](https://calver.org), because it is strictly and meaningfully
sortable.  There are no major, minor, micro, or modifier
numbers. Releases are a flow from one to the other. We do adopt a
stricter view of CalVer's tag line: Versioning gets better with time.

## Usage

Add this to your `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61", "rschronver"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["version"]
```

If you are using Python 3.8 or above, include this code in your
``<your_package>.__init__.py``:

```py
import importlib.metadata

try:
    __version__ = importlib.metadata.version("your_package")
except importlib.metadata.PackageNotFoundError:
    # A package only has a version once it has been built or installed.
    # By not defining __version__, clients will fail fast if they
    # require __version__ (unlikely).
    pass
```

If you are using a Python before 3.8, use the backport
[`importlib_metadata`](https://importlib-metadata.readthedocs.io).

## Releases without breakage (almost)

At RadiaSoft we strive to maintain backward compatability for as long
as our users require it.  This is why there are no major or minor
release numbers in chronological versions; there are no breaking API
changes (except defects, of course) with each release. We feel it is
our obligation to not break uses by clients of our APIs.

There are times when this is impossible or impractical, such as the
move away from Python 2. In those cases, we give clients warnings and
an upgrade path and sometimes a tool that upgrades their data or code
automatically. This is an obligation that comes with chronological
versioning that RadiaSoft takes seriously.

Finally, we try to ensure breakage (and failures due to defects) is
[fail fast](https://en.wikipedia.org/wiki/Fail-fast_system). We don't
want our client's code continuing (doing damage) if it is using one
RadiaSoft's packages incorrectly.
