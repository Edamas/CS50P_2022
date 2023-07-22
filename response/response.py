from validator_collection import validators


def main():
    email = input("What's your email address? ")
    print(validate(email))

def validate(email):
    try:
        validators.email(email)
        return "Valid"
    except:
        return "Invalid"

if __name__ == '__main__':
    main()
