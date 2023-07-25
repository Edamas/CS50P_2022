from datetime import date
import inflect
import sys

def main():
    birth = input('Date of Birth: ')
    try:
        y, m, d = [int(i) for i in birth.split('-')]
    except ValueError:
        sys.exit('Invalid date')
    print(get_minutes(y, m, d))

def get_minutes(y, m, d):
    try:
        start = date(y, m, d)
    except:
        sys.exit('Invalid date')
    minutes = (date.today() - start).days * 24 * 60
    inf = inflect.engine()
    return inf.number_to_words(minutes, andword='').capitalize() + ' minutes'

if __name__ == "__main__":
    main()
