#

import subprocess
from .protocol import process

def lintian(path, pedantic=False, info=False, experimental=False):
    args = ["lintian", "--show-overrides"]

    if pedantic:
        args.append("--pedantic")
    if info:
        args.append("-I")
    if experimental:
        args.append("-E")

    args.append(path)
    big_error = False

    try:
        output = subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        output = e.output
        big_error = True

    return process(output)
