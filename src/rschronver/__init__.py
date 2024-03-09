"""RadiaSoft chronological versioning plugin for pyproject.toml

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""

# To update, run python __init__.py
__version__ = "20240308.225804"


def _main():
    """Overwrites ``__version__`` in file with `utcnow`"""
    import datetime, pathlib, re, sys

    def _write(path, version):
        with path.open("rt+") as f:
            t = re.sub(r'(version_*\s*=\s*")(\d{8}\.\d+)', rf"\g<1>{version}", f.read())
            f.seek(0)
            f.write(t)
        sys.stderr.write(f"Set version={version} in {path}\n")

    def _version():
        return datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")

    v = _version()
    p = pathlib.Path(__file__)
    _write(p, v)
    # Writing this directly avoids setuptools_scm complaining on the build, which is confusing
    _write(p.parent.parent.joinpath("pyproject.toml"), v)

if __name__ == "__main__":
    _main()
