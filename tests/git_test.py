"""test git version

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""


def test_basic():
    from pykern import pkunit
    from rschronver import git
    import datetime
    import os
    import time

    with pkunit.save_chdir_work():
        a = git.version()
        pkunit.pkeq(None, a)
        e = datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")
        pkunit.pkeq(
            0,
            os.system("git init && echo x > x && git add x && git commit -m x"),
        )
        a = git.version()
        pkunit.pkeq(len(e), len(a))
        pkunit.pkok(e <= a, "expect={} is greater than actual={}", e, a)
        time.sleep(1)
        with open("x", "wt") as f:
            f.write("change")
        b = git.version()
        pkunit.pkok(a < b, "expect={} should be older than={}", a, b)
