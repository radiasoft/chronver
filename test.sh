#!/bin/bash
#
# Check for no pykern in package and run ci
#
set -euo pipefail

test_err() {
    echo "$@" 1>&2
    return 1
}

test_main() {
    if grep -r -i pykern rschronver; then
        test_err "rschronver python files may not use/mention pykern"
    fi
    # workaround https://github.com/radiasoft/pykern/issues/453
    trap 'rm -f setup.py' EXIT
    touch setup.py
    pykern ci run
}

test_main "$@"