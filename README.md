# tasklist-timer
hourglass wrapper enabling multiple, labeled timers in series.

Hourglass is a minimalist timer with cmd line functions and portability, allowing a few key features, including a description to accompany timers. 

For example, 

- "Spend 5 minutes writing a dream grocery list" 

To facilitate rapid-fire tasks and aggregate overhead work, I built this wrapper. Instead of manually creating a timer or inputting descriptions between timer resets, this script allows a single list of tasks to be read in, and presents them serially for the duration of time specified. 

For example,

This list of tasks:  
- "Spend 5 minutes writing dream grocery list" 
- "Spend 5 minutes replacing 25% of junk food items with healthy alternatives." 
- "Spend 5 minutes replacing expensive options with healthy alternatives." 

When you run the script, the first task (_dream groceries..._) description will appear with a 5 minute timer. After 5 minutes, the alarm will sound, and the next task (_less junk food_) will appear with a 5 minute timer, etc.

Tested on windows 7 and 10.
Not tested with python 3+

# setup

A. Install [Hourglass](https://chris.dziemborowicz.com/apps/hourglass/) is windows only, unfortunately.
B. make sure hourglass and python are on PATH
C. make sure .txt and .py file are in same directory.

# runtime

1.update `tasklist.txt` with a single column of tasks (spaces allowed). 

2. run .py script from command line.
e.g. `python tasklist_timer.py`

default time limit per task is 6 minutes.

3. to modify time limits and break time
add cmd line args for running python script:
with task time as argument 1 and break time as argument 2.

For example, 10 minutes per task with a 20 minute break after every X task:

`python tasklist_timer.py 10 20`

## pause timer
simply pause the timer within Hourglass.

## skip task
close the current hourglass timer window. Note the script will behave as if the task is completed, and this task will not reappear.

# next
current build only uses Send_hourglass_command.
i.e. does not interface with read/write files.

might be nice to have an auto quit that closes all windows....


