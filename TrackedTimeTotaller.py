"""
---TrackedTimeTotaller---

A rudimentary program designed to accept strings
of tracked time logged in the format 'dd/mm hh:mm-hh:mm'
and display the accumulated total of hours and minutes
from the entered strings.

- Created by Chris Vidler 26/01/25
"""

import re

input_string = ""
total_hours = 0
total_mins = 0


def reset_time():
    """Return values of 0 to update/reset total_hours and total_mins count."""
    h = 0
    m = 0
    return h, m


def check_string_input(s):
    """Check entered string matches specified format, return None if not."""
    x = re.search(r'^\d{2}\/\d{2}\s\d{2}:\d{2}-\d{2}:\d{2}$', s)
    if x is None:
        return None
    else:
        return x.string


def get_values(s):
    """Get values for start/end hours and minutes from entered string."""
    start_hour = int(s[6:8])
    start_min = int(s[9:11])
    end_hour = int(s[12:14])
    end_min = int(s[15:17])
    return start_hour, start_min, end_hour, end_min


def print_time(h, m):
    """Convert excess mins (>60) to hours to print current hr + min total."""
    add_hours, remaining_mins = divmod(m, 60)
    new_hours = h + add_hours
    print(f'Current total: {new_hours}h {remaining_mins}m')


print("Please enter a string for processing "
      "in the format 'dd/mm hh:mm-hh:mm', "
      "or R to reset the total, "
      "or X to exit the program.")

while input_string != "X":
    input_string = input("Input:")
    if input_string.upper() == "R":
        total_hours, total_mins = reset_time()
    elif input_string.upper() == "X":
        break
    else:
        processing_string = check_string_input(input_string)
        if processing_string is None:
            print("Error: Invalid string")
        else:
            start_hour, start_min, end_hour, end_min = get_values(input_string)
            if end_hour < start_hour:
                end_hour = end_hour + 24
            if end_min < start_min:
                end_min = end_min + 60
                start_hour = start_hour + 1
            hour_duration = end_hour - start_hour
            min_duration = end_min - start_min
            total_hours = total_hours + hour_duration
            total_mins = total_mins + min_duration
            print_time(total_hours, total_mins)
