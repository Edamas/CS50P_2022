from numb3rs import validate

def main():
    test_in_range()
    test_negative_range()
    test_above_range()

def test_in_range():
    sample = [0, 1, 10, 100, 128, 200, 255]
    for a in sample:
        for b in sample:
            for c in sample:
                for d in sample:
                    ip = f'{a}.{b}.{c}.{d}'
                    assert validate(ip) == True


def test_negative_range():
    sample = [-256, -255, -200, -100, -10, -1, 0, 128, 255]
    for a in sample:
        for b in sample:
            for c in sample:
                for d in sample:
                    ip = f'{a}.{b}.{c}.{d}'
                    if sum([num < 0 for num in [a, b, c, d]]):
                        assert validate(ip) == False
                    else:
                        assert validate(ip) == True


def test_above_range():
    sample = [0, 128, 255, 256, 300, 500]
    for a in sample:
        for b in sample:
            for c in sample:
                for d in sample:
                    ip = f'{a}.{b}.{c}.{d}'
                    if sum([num > 255 for num in [a, b, c, d]]):
                        assert validate(ip) == False
                    else:
                        assert validate(ip) == True

def test_not_int():
    sample = [0, 1, 128, 255, '', 0.0, 0.1, 0.12, 0.255, 'dog', 'cat', True, False, [0], [1], [0, 1, 128]]
    for a in sample:
        for b in sample:
            for c in sample:
                for d in sample:
                    ip = f'{a}.{b}.{c}.{d}'
                    if sum([type(num) != int for num in [a, b, c, d]]):
                        assert validate(ip) == False
                    else:
                        assert validate(ip) == True

if __name__ == '__main__':
    main()
