#!/bin/python3
"""
PMON [Python3 CLI Version]

A tool which monitors the changes in a python script file and then re-launches the python script if there are any changes noticed. For more information, checkout the README.md file.

Author : Rishav Das (https://github.com/rdofficial)
Created on : May 15, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
from sys import argv as ARGUMENTS
from subprocess import Popen

def main():
	# Checking wheter the user has entered the file contents through arguments or not
	if len(ARGUMENTS) < 2:
		# If the user has not entered the filename as argument, then we continue to ask for the filename manually

		filename = input('Enter the filename : ')
	else:
		# If the user entered more or equal to 2 arguments, then we continue with the argument

		filename = ARGUMENTS[1]

	# Reading the file contents
	fileOriginalContents = open(filename, 'r').read()

	# Launching a background process executing the script filename as per defined
	process = Popen(['python3', f'{filename}'])

	# Running an infinite loop checking for changes in the file
	while True:
		# Reading the contents of the file again in order to compare changes
		fileChangedContents = open(filename, 'r').read()

		if fileOriginalContents != fileChangedContents:
			# If the contents of the file are changed, then we continue to kill the previous process and launching another new process with the updated script file

			# Killing the previously launched process
			process.kill()

			# Changing the original files contents to the newer file contents
			fileOriginalContents = fileChangedContents

			# Re-launching the process with the newly updated script file
			process = Popen(['python3', f'{filename}'])

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message on the console screen

		input(f'[ Error : {e} ]\nPress enter key to continue...')
