#!/usr/bin/env python
#
# Copyright (c) 2016, Heinrich Schuchardt <xypron.glpk@gmx.de>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from distutils.core import setup
import setuptools

import sispm

setup(
	name='pysispm',
	version='0.1-rc2',
	description='Python library for EnerGenie EG-PMS',
	author='Heinrich Schuchardt',
	author_email='xypron.glpk@gmx.de',
	license = 'BSD',
	url='https://github.com/xypron/pysispm',
	packages=['sispm'],
	install_requires=["pyusb >= 1.0.0a"],
	long_description =
"""
PySisPM is a library to control the EnerGenie EG-PMS multiple socket outlet.

The EG-PMS has an USB interface. Four outlets can be switched on and off via USB.

The library depends on PyUSB (https://github.com/walac/pyusb).
""",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: POSIX'
		'Programming Language :: Python :: 3',
		'Topic :: System :: Hardware :: Hardware Drivers'
	]
)
