import os, csv
from psychopy import core
import sys

# might be nice to have an auto quit that closes all windows....


# This script uses only a subset of features: Send_hourglass_command.
# to use it, update the tasklist.txt file with a single column of tasks. time limit is assumed to be 6m.
# run script.


	
def cmd_arg_assign(default,argument_number=1):
	# tries to assign sys_arg value; if not, then sets a default.
	try:
		return(int(sys.argv[argument_number]))
	except:
		return(default)
	
task_time = cmd_arg_assign(default = 5, argument_number = 1)
break_time = cmd_arg_assign(default = 3, argument_number = 2)

time_unit = "m"

def Send_hourglass_command(task_description="work",time=6,counter=1):
	# open hourglass and insert time and task name
	cur_string = "Hourglass -l off -e on -t \"{0}_{1}\" {2}{3}".format(counter,task_description,str(time),time_unit)
	# print cur_string
	os.system(cur_string)

def Open_project_file(filename):
	# open file
	os.system("Notepad.exe {0}".format(filename))
	
def Close_notepad():
	#save and close file
	
	# save.

	# close file
	os.system("taskkill /IM Notepad.exe") # force quit

def Git_commit(task_description,filename):
	# commit change on git
	# auto commits all changes.
	os.system("git commit -a -m '{0}_{1}'".format(filename,task_description))
	# home desktop doesn't recognize git from command line...


# read from .csv filename time and task name
try:
	os.system("taskkill /IM Hourglass.exe")
except:
	pass
with open('tasklist.txt') as f:
	reader = csv.reader(f)
	counter = 0
	for row in reader:
		
		# set variables
		# filename = row[0]
		counter+=1
		task_description = row[0]
		print(row[0:2])
		try:
			time = int(row[:2])
		except:
			pass
		if "break" in row:
			time = break_time
		else:
			time = task_time
		
		# Open_project_file(filename)
		
		#internal and external timers
		Send_hourglass_command(task_description,time,counter)	
		# core.wait(time*60)
		
		# Close_notepad()
		# Git_commit()


