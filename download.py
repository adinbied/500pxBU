#!/usr/bin/python
# -*- encoding: utf-8 -*-
from pxmeta import Download_Meta
from pximage import Download_Image
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-u", "--url", dest="myFilenameVariable",
					help="URL To Scrape", metavar="URL")
args = parser.parse_args()
inputurl = str((args.myFilenameVariable))
Download_Image(str(inputurl))
Download_Meta(str(inputurl))
