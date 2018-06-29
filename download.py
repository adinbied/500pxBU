#!/usr/bin/python
# -*- encoding: utf-8 -*-
from pxmeta import Download_Meta
from pximage import Download_Image
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
urls = args.file.readlines()
for i in urls:
	Download_Image(i)
	Download_Meta(i)
