

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    mins = s[3:5]
    secs = s[6:8]
    if s[8:10] == "PM":
        if int(hour) < 12:
            hour = 12 + int(hour)
            hour = str(hour)
    elif s[8:10] == "AM":
        if hour == "12":
            hour = "00"
    return f"{hour}:{mins}:{secs}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
