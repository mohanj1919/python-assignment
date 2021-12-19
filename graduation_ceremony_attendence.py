import itertools

"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773

"""

def get_attendance_possibilities(n):
    for i in itertools.product("01", repeat=n):
        yield ",".join(i)


def find_attendence_possibilities(n):
    valid_attendence = 0
    graduation_missed_scenarios = 0
    for scenario in get_attendance_possibilities(n):
        if '0,0,0,0' not in scenario:
            valid_attendence += 1
            if scenario[-1] == '0':
                # last day is the graduation ceremony.
                graduation_missed_scenarios += 1
    print(f"{graduation_missed_scenarios}/{valid_attendence}")

find_attendence_possibilities(5)
find_attendence_possibilities(10)
