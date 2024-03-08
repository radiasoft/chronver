"""RadiaSoft chronological versioning plugin for pyproject.toml

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""

# To update, run python __init__.py
__version__ = "20240308.222315"


def _main():
    """Overwrites ``__version__`` in file with `utcnow`"""
    import datetime, pkg_resources, re, sys

    def _version():
        return datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")

    v = _version()
    with open(__file__, "rt+") as f:
        t = re.sub(r"(\d{8}\.\d+)", v, f.read())
        f.seek(0)
        f.write(t)
    sys.stderr.write(f"Set version={v} in {__file__}\n")


if __name__ == "__main__":
    _main()
