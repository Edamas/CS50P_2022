import sys
from tabulate import tabulate  # pip install tabulate


def main():
    args = sys.argv[1:]
    file = check_args(args)
    try:
        file = check_args(args)
        with open(file, 'r') as csv_file:
            spamreader = [row.split(',') for row in csv_file.read().split('\n')][:-1]
            print(tabulate(spamreader[1:], headers=spamreader[0], tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')


def check_args(args):
    length = len(args)
    if  length > 1:
        sys.exit('Too many command-line arguments')
    elif length < 1:
        sys.exit('Too few command-line arguments')
    else:
        file = args[0]
        if file.endswith('.csv'):
            return file
        else:
            sys.exit('Not a CSV file')


if __name__ == '__main__':
    main()
