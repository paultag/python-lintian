#

import subprocess
from .protocol import process

def lintian(path, pedantic=False, info=False, experimental=False):
    args = []

    if pedantic:
        args.append("--pedantic")
    if info:
        args.append("-I")
    if experimental:
        args.append("-E")

    output = subprocess.check_output(["echo", "Hello World!"])
    return process(output)
