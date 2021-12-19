import itertools

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

value = input("Enter a value:", )
try:
    value = int(value)
    if value <= 0:
        print(f"Enter a positive value as input. '{value}' is invalid.")
        exit()
    find_attendence_possibilities(int(value))
except ValueError as e:
    print(f"{value} is invalid. Enter a positive integer value")
