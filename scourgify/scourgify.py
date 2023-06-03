import sys, csv

def check_args(args):
    if len(args) > 2:
        problem = 'few'
    elif len(args) < 2:
        problem = 'many'
    else:
        return True
    sys.exit(f"Too {problem} command-line arguments")


def nomalize_data(before):
    person = []
    reader = csv.DictReader(before)

    for ind in reader:
        temp = {}
        temp["last"], temp["first"] = [i.strip() for i in ind["name"].split(",")]

        temp["house"] = ind["house"]
        person.append(temp)
    return person


def save(data, filename):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)

def main():
    args = sys.argv[1:]
    if check_args(args):
        before, after = args
        try:
            with open(before, "r", encoding="utf-8") as file:
                save(nomalize_data(file), after)
        except FileNotFoundError:
            sys.exit(f"{before} not found")


if __name__ == "__main__":
    main()
