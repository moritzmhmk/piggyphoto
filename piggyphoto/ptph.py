#!/usr/bin/python3

import re

regex = re.compile(r"^#define\s+([a-zA-Z0-9_]+)\s+(.*)")

with open("ptp.py", "w") as out:
    out.write("# Constants extracted from gphoto2's ptp.h\n\n")

    with open("ptp.h") as inp:
        for line in (line.strip() for line in inp.readlines() if line.startswith("#define")):
            match = regex.match(line)
            if match:
                name, value = match.groups()
                value = value.replace("/*", "#").replace("//", "#")
                out.write("%s = %s\n" % (name, value))
