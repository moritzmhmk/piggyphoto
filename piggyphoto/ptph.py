#!/usr/bin/python3

import re

with open("ptp.h") as inp, open("ptp.py", "w") as out:
    out.write("# Constants extracted from gphoto2's ptp.h\n\n")

    re.sub(r"#define[ \t]+([a-zA-Z0-9_]+)[ \t]+([^\n]*)\n",
        lambda match: str(out.write("%s = %s\n" % (match.groups()[0], match.groups()[1].replace("/*", "#"))))
        , inp.read())
