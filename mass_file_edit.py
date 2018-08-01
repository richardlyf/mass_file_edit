#!/usr/bin/env python 

# Mass file Edit
# Jul 12, 2018
# Richard Lin

# The purpose of this script is to edit multiple files in a directory that share a common error
# Example: Many files in caffe directory have the wrong #include "hdf5/serial/hdf5.h" and needs to be changed to #include "hdf5.h" instead.

import os, re

def edit_files_in_dir(directoryPath, regex1, regex2, correction1, correction2):
	#print(directoryPath)
	directory = os.listdir(directoryPath)
	os.chdir(directoryPath)
	
	for file in directory:
		if os.path.isfile(file):
			#print(file)	
			open_file = open(file, 'r')
			read_file = open_file.read()
			read_file = regex1.sub(correction1, read_file)
			read_file = regex2.sub(correction2, read_file)
			write_file = open(file, 'w')
			write_file.write(read_file)
		else:
			newPath = directoryPath + file + '/'
			edit_files_in_dir(newPath, regex1, regex2, correction1, correction2)
			os.chdir(directoryPath)

def main():
	homeDirectory = '/home/yifengl/python_testing_env/data/'
	#homeDirectory = '/home/yifengl/Code/caffe/'
	error1 = '#include "hdf5/serial/hdf5.h"'
	error2 = '#include "hdf5/serial/hdf5_hl.h"'	
	correction1 = '#include "hdf5.h"'
        correction2 = '#include "hdf5_hl.h"'

	regex1 = re.compile(error1)
	regex2 = re.compile(error2)
	
	edit_files_in_dir(homeDirectory, regex1, regex2, correction1, correction2)
	print("completed")

if __name__ == '__main__':
	main()
