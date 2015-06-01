#!/usr/bin/python
# Copyright (C) 2015  - Pedro Alves
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Contact: pdroalves (at) gmail.com

import sys
import exifread
import re

def main(input):
    # Open image file for reading (binary mode)
    f = open(input, 'rb')
    # Return Exif tags
    exif = exifread.process_file(f)

    if not exif.has_key("Image DateTime"):
        exit(1);
    dt = exif["Image DateTime"].values

    match = re.match("(\d\d\d\d):(\d\d):(\d\d)",dt)
    if match:
        print "%s-%s-%s" % match.groups()

if __name__ == "__main__":
    main(sys.argv[1])
