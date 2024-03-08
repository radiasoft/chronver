"""Get version from Git

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import datetime
import locale
import os.path
import re
import subprocess
import sys


def version():
    """Chronological version string for most recent commit or time of newer file.

    Finds the commit date of the most recent branch. Uses ``git
    ls-files`` to find files under git control which are modified or
    to be deleted, in which case we assume this is a developer, and we
    should just use the current time for the version. It will be newer
    than any committed version, which is all we care about for upgrades.

    Returns:
        str: canonicalized "yyyymmdd.hhmmss"
    """

    def _fmt(value):
        return value.strftime("%Y%m%d.%H%M%S")

    def _head():
        return datetime.datetime.fromtimestamp(
            float(
                _sh(
                    (
                        "git",
                        "log",
                        "-1",
                        "--format=%ct",
                        _sh(("git", "rev-parse", "--abbrev-ref", "HEAD")),
                    ),
                ),
            ),
        )

    def _is_edited():
        return bool(
            _sh(
                ("git", "ls-files", "--modified", "--deleted"),
            ),
        )

    def _is_repo():
        return os.path.isdir(".git")

    def _sh(cmd):
        try:
            res = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            if isinstance(res, bytes):
                return res.decode(locale.getpreferredencoding()).rstrip()
            return None
        except subprocess.CalledProcessError as e:
            if hasattr(e, "output") and len(e.output):
                sys.stderr.write(e.output)
            raise

    if not _is_repo():
        raise ValueError("Must have a git repo or an source distribution")
    sys.stderr.write(str(sys.path) + " xxxx\n")
    return _fmt(datetime.datetime.utcnow() if _is_edited() else _head())
