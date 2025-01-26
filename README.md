# TrackedTimeTotaller

This is a Python program I've written to help me add up the times I've tracked in my notes when working on freelance projects.\
Admittedly, I don't have the best tracking system. To date, I've been recording the times as a series of strings in a cell of an Excel spreadsheet.\
These take the format "dd/mm hh:mm-hh:mm", where dd/mm stands in for the day/month and hh:mm for the starting and finishing times of each session. So e.g.:\
12/01 14:35-17:45\
14/01 15:25-16:55\
14/01 17:15-18:25\
...etc.\
\
To make these easier to add up, I've created this fairly rudimentary program, where such time logs can be entered line by line and the cumulative total of hours and minutes is then displayed after each new input. The program does this by slicing the characters of the string that correspond to the starting and ending hours and minutes, converting these to integers, then subtracting the starting time component from the respective ending time component to obtain a duration to add to the total. Where the starting time component exceeds the ending time component, e.g. due to overruns into new days (14/01 23:35-00:45) or minute values that are lower in the ending time (e.g. 17/01 15:55-16:40), this is accounted for via the necessary mathematical operations (in the first case, addition of 24 hours to the ending hours; in the second case, addition of 60 minutes to the ending minutes and reducing the hour duration accordingly by adding one hour to the starting hours).\
\
Entering "R" for the input will reset the hours and minutes counters back to zero; entering "X" will exit the program. (Both these inputs are case-insensitive.) If neither of these inputs are entered and the input string does not match the format specified above, an error message will be shown and the user will be prompted to enter a new input.\
\
There are much likely easier ways to implement this program, e.g. involving packages specially designed for working with time - but this is just a functional solution I've come with for the time being. I've also used it as an opportunity to revise writing code in Python, using regex, string manipulation, mathematical problem solving etc.

## To Modify The Program

The program can be modified as desired to accept a string in a different format. For example, if the times were tracked without the date in each case and the strings were simply logged in the format "hh:mm-hh:mm", the following changes would need to be made:\
1. Change the raw string for the regex pattern in line 28 from r'^\d{2}\/\d{2}\s\d{2}:\d{2}-\d{2}:\d{2}$' to r'^\d{2}:\d{2}-\d{2}:\d{2}$'
2. Subtract 6 from all the slice values in lines 37-40 (i.e. start_hour = int(s[0:2]) start_min = int(s[3:5]) end_hour = int(s[6:8]) end_min = int(s[9:11]))
3. Ideally, also change the prompted format in the printed instruction string in line 52 to 'hh:mm-hh:mm'
