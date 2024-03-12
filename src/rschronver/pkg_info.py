"""Get version from PKG-INFO

Used when building a wheel from an sdist, because the git diretory no longer is there.

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""

def version():
    try:
        with open("PKG-INFO", "rt") as f:
            m = re.search(r"^Version:\s*(\S+)", f.read(), re.MULTILINE)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None
