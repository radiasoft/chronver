# Update by running python __init__.py
__version__ = "20240308.205422"


def _main():
    import datetime, pkg_resources, re, sys

    def _version():
        return str(
            pkg_resources.parse_version(
                datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")
            )
        )

    v = _version()
    with open(__file__, "rt+") as f:
        t = re.sub(r"(\d{8}\.\d+)", v, f.read())
        f.seek(0)
        f.write(t)
    sys.stderr.write(f"setting __version__ = {v} in {__file__}\n")


if __name__ == "__main__":
    _main()
