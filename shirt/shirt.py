import sys
from PIL import Image, ImageOps

def main():
    before, after = get_args()
    try:
        shirt = Image.open('shirt.png')
    except FileNotFoundError:
        sys.exit('Input does not exist')
    photo = Image.open(before)
    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, shirt)
    photo.save(after)

def get_args():
    args = sys.argv[1:]
    if len(args) == 2:
        input_file, output_file = args
        input_ext, output_ext = input_file.lower().split('.')[-1], output_file.lower().split('.')[-1]
        if input_ext in ['jpg', 'jpeg', 'png']:
            if output_ext in ['jpg', 'jpeg', 'png']:
                if input_ext == output_ext:
                    return args
                else:
                    sys.exit('Input and output have different extensions')
            else:
                sys.exit('Invalid output')
        else:
            sys.exit('Invalid input')
    else:
        if len(args) > 2:
            problem = 'many'
        else:
            problem = 'few'
        sys.exit(f'Too {problem} command-line arguments')

if __name__ == '__main__':
    main()
