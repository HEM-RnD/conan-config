#!/usr/bin/env python3

import sys

preReleaseTagFile = open(".version/PreReleaseTag.txt", "r")
preReleaseTag = preReleaseTagFile.read()

channel = "development"

if preReleaseTag == "":
    channel = "stable"
elif "alpha." in preReleaseTag or "beta." in preReleaseTag or "rc." in preReleaseTag:
    channel = "testing"

sys.stdout.write(channel)
sys.stdout.flush()
sys.exit(0)