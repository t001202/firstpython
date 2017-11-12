#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import shutil
import zipfile
import os

new_path = os.getcwd()
filepath = os.path.join(new_path, "xml04.py")

flag = os.path.isfile(filepath)
print(flag)
shutil.make_archive(new_path, "zip", root_dir='\\repo\\OldBoy\\phase02\\module\\day18\\xml04.py')


def zip_dir(dirname, zipfilename):
	filelist = []
	if os.path.isfile(dirname):
		filelist.append(dirname)
	else:
		for root, dirs, files in os.walk(dirname):
			for name in files:
				filelist.append(os.path.join(root, name))

	zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
	for tar in filelist:
		arcname = tar[len(dirname):]
		print(arcname)
		zf.write(tar, arcname)
	zf.close()


def unzip_dir(zipfilename, unzipdirname):
	fullzipfilename = os.path.abspath(zipfilename)
	fullunzipdirname = os.path.abspath(unzipdirname)
	print("Start to unzip file %s to folder %s ..." % (zipfilename, unzipdirname))
	# Check input ...
	if not os.path.exists(fullzipfilename):
		print("Dir/File %s is not exist, Press any key to quit..." % fullzipfilename)
		inputStr = input()
		return
	if not os.path.exists(fullunzipdirname):
		os.mkdir(fullunzipdirname)
	else:
		if os.path.isfile(fullunzipdirname):
			print("File %s is exist, are you sure to delet it first ? [Y/N]" % fullunzipdirname)
			while 1:
				inputStr = input()
				if inputStr.lower() == 'n':
					return
				else:
					if inputStr.lower() == "y":
						os.remove(fullunzipdirname)
						print("Continue to unzip files ...")
						break
					# Start extract files ...
	srcZip = zipfile.ZipFile(fullzipfilename, "r")
	for eachfile in srcZip.namelist():
		print("Unzip file %s ..." % eachfile)
		eachfilename = os.path.normpath(os.path.join(fullunzipdirname, eachfile))
		eachdirname = os.path.dirname(eachfilename)
		if not os.path.exists(eachdirname):
			os.makedirs(eachdirname)
		fd = open(eachfilename, "wb")
		fd.write(srcZip.read(eachfile))
		fd.close()
	srcZip.close()
	print("Unzip file succeed !!!")
