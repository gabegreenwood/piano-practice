#!/usr/bin/env python3

from datetime import datetime, timedelta
import random
import sys
import time

letters = ['A','B','C','D','E','F','G']

prompt = "Enter the interval time for which to display each note:"
print(prompt)
while True:
    try:
        interval = int(input())
        break
    except ValueError:
        print("Please enter an integer:")
    except KeyboardInterrupt:
        exit()

prompt = "For how many minutes would you like to practice?"
print(prompt)
while True:
    try:
        timeout = timedelta(minutes=float(input()))
        break
    except ValueError:
        print("Please enter a number:")
    except KeyboardInterrupt:
        exit()

previous = None
start_time = datetime.now()
while datetime.now() - start_time < timeout:
    try:
        i = random.randint(0, len(letters)-1)
        if i == previous:
            continue
        else:
            previous = i
        sys.stdout.write(f"  {letters[i]}\r")
        sys.stdout.flush()
        time.sleep(interval)

    except KeyboardInterrupt:
        exit()
print("Good job, you're done!")
