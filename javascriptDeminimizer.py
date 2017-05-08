# Code written by Jack Clark
# Copyright 2017(c) the M.I.T. License
# This code is a script to deminimize code according to the Epicenter Code Standards,
# The standards can be found the in the Epicenter Design Documents
import os
import sys
import platform

class File(filename, output):
	def __init__(self, filename, output):
		self._filename = filename
		self._output = output
	file = open(_filename, "r") # 


# Program should be ran in main
if __name__ == "__main__":
	# Welkommen Freund!
	print("Welcome to the JavaScript Deminimizer, glad to help!\n\n")
	# Get info
	filename_ = input("Filename:")
	output_ = input("Output to:")
	# Do the things
	file = File(filename_, output_)
# Just realized that all of this code is not even needed
# I feel so fucking stupid because of this