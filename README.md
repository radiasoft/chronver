## Introduction

ChronVer is a
[setuptools.meta_build](https://setuptools.pypa.io/en/latest/build_meta.html)
plugin to add a
[chronological version](https://www.robnagler.com/2015/04/11/Major-Release-Syndrome.html)
(yyyymmdd.hhmmss)
to a Python package's metadata from the current Git commit of `HEAD`.
This ensures a unique, sortable version for packages on [PyPI](https://pypi.org).

In development, if there are modifications, the current time will be
returned. This ensures that `pip install` works, because there's
always a new, increasing version.

## Usage

Add this to your `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61", "chronver"]
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

[RadiaSoft](https://radiasoft.net) uses chronological versioning for
all its releases. This means no major releases, which implies breaking
changes.  To make this happen, we strive to maintain backward
compatibility for as long as our users require it.

This is why there are no major or minor release numbers in
chronological versions; there are no breaking API changes (except
defects, of course) with each release. We feel it is our obligation to
not break our client's code.

There are times when this is impossible or impractical, such as the
move away from Python 2. In those cases, we give clients warnings and
an upgrade path and sometimes a tool that upgrades their data or code
automatically. This is an obligation that comes with chronological
versioning that RadiaSoft takes seriously.

## Why another versioning scheme?

ChronVer is a new implementation of our existing
[setup.py versioning module](https://github.com/radiasoft/pykern/blob/eaea8492e1e8485c8b35aee67ad1204e8838da97/pykern/pksetup.py#L684)
so it is not new at all. RadiaSoft has been using chronological
versioning for Python, Docker images, packaging (RPMs), etc. for over
a decade. Before that @robnagler (primary author) was using
chronlogical versioning since at least 2000. So there's a long history
here, and it has worked well for us.

[SemVer](https://semver.org) makes many assumptions about how software
works that conflicts with how we develop. In our model, software flows
like time, and releases are arbitary points on the time axis. SemVer
divides software releases into fixed epochs: major, minor, patch, and
additional labels. This requires people make complicated decisions
about these different kinds of epochs, which adds work and we think
adds little value. This can result in
[Major Release Syndrome](https://www.robnagler.com/2015/04/11/Major-Release-Syndrome.html),
which is an impediment to continuous software development and
deployment.

[CalVer](https://calver.org) has a great tag line: "Versioning gets
better with time." We agree! In CalVer, "time" means "date", that is,
days are the time quantum. This granularity does not allow for same
day releases, which we happen to do on occasion. A second is
ChronVer's time quantum for this reason. CalVer tries to be SemVer
compliant, which as noted above, is not how we develop software.

There are benefits to simplifying version strings to always being
lexicographically sortable. Any two ChronVers can be compared with a
single operator `v1 < v2`. We have a lot internal devops tooling in
multiple languages, and all languages support simple lexicographic
comparison of strings. A ChronVer is compatible with Python's `float`,
which is useful in some cases.

A ChronVer identifies any commit in any SCM. We use Git now. We used
to use CVS (which does not have a SHA), and ChronVer worked just as
well. All SCM's (that we know of) answer the question: what was the
commit at this timestamp?  SemVer and CalVer have various schemes for
doing this, but they are awkward and break lexicographic comparison.

For more complete reasoning, refer to
[Major Release Syndrome](https://www.robnagler.com/2015/04/11/Major-Release-Syndrome.html).
