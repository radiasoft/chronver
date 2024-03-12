"""determine own version

This only works if build-system.backend-path is respected

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
# Actual build system: "_own_version:build_meta"
from setuptools import build_meta as build_meta
import rschronver.git


def __getattr__(name):
    if name == "from_git":
        return rschronver.git.version()
    raise AttributeError(name)
