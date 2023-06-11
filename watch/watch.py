import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if '<iframe' in s:
        parsed = re.search(pattern=r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', string=s)
        parsed = parsed.group(0).replace('/embed/', '/').replace('www.youtube.com', 'www.youtu.be').replace('youtube.com', 'youtu.be').replace('http://', 'https://')

        if 'title' not in s:
            parsed = parsed.replace('www.', '')
        if 'youtu.be' in parsed:
            return parsed

          
if __name__ == "__main__":
    main()
