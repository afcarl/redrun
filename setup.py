#!/bin/env python
# Copyright (c) 2017 NVIDIA CORPORATION. All rights reserved.
# See the LICENSE file for licensing terms (BSD-style).

from __future__ import print_function
from distutils.core import setup  # , Extension, Command

scripts = """
    redrun
    redc
""".split()

setup(
    name='redaemon',
    version='v0.0',
    author="Thomas Breuel",
    description="A Redis-based distributed process manager.",
    # packages=["somepackage"],
    # data_files= [('somefile', models)],
    scripts=scripts,
)
