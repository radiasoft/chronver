"""Chronological version hooks for setuptools builds

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import rschronver.git
import rschronver.pkg_info

def set_version(dist):
    """Try Git and fallback to PKG-INFO or date
    """
    v = rschronver.git.version() or rschronver.pkg_info.version()
    if v is None:
        raise LookupError(
            f"rschronver was unable to detect version for {dist.metadata.name}.\n\n"
            "Make sure you're either building from a fully intact git repository "
            "or PyPI tarballs. Most other sources (such as GitHub's tarballs, a "
            "git checkout without the .git folder) don't contain the necessary "
            "metadata and will not work.\n\n"
            "For example, if you're using pip, instead of "
            "https://github.com/user/proj/archive/master.zip "
            "use git+https://github.com/user/proj.git#egg=proj"
        )
    dist.metadata.version = v
