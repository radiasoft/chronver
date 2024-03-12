"""determine own version

This only works if build-system.backend-path is respected

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
# Actual build system: "_own_version:build_meta"
from setuptools import build_meta as build_meta
import re
import rschronver.git


def __getattr__(name):
    if name == "from_git":
        try:
            return rschronver.git.version()
        except Exception as e:
            try:
                with open("PKG-INFO", "rt") as f:
                    m = re.search(r"^Version:\s*(\S+)", f.read(), re.MULTILINE)
                if m:
                    return m.group(1)
            except Exception:
                pass
            raise
    raise AttributeError(name)
