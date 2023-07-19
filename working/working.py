import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid = re.search(r'^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$', s)
    if valid:
        _, start_h, start_m, start_ampm, _, end_h, end_m, end_ampm = valid.groups()
        return f'{usa_to_int(start_h, start_m, start_ampm)} to {usa_to_int(end_h, end_m, end_ampm)}'
    else:
        raise ValueError


def usa_to_int(hour, minute, ampm):
    invalid = False
    if 1 <= int(hour) <= 12:
        hour = int(hour)
        if ampm == 'AM':
            if hour == 12:
                hour = 0
        else:
            if 1 <= hour <= 11:
                hour += 12
    else:
        invalid = True

    if minute == None:
        minute = 0
    else:
        if 0 <= int(minute) <= 59:
            minute = int(minute)
        else:
            invalid = True

    if invalid:
        raise ValueError
    else:
        return f'{str(hour).rjust(2, "0")}:{str(minute).rjust(2, "0")}'

if __name__ == "__main__":
    main()
