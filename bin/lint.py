#!/usr/bin/env python

import lintian
import json
import sys

print json.dumps(lintian.lint(sys.argv[1]))
