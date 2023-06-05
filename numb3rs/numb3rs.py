import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    return bool(re.match(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$', ip))


if __name__ == "__main__":
    main()
