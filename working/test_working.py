from working import convert
import pytest

def main():
    test_valid()
    test_invalid()


def test_valid():
    assert convert('01:00 AM to 02:00 AM') == '01:00 to 02:00'
    assert convert('02:00 AM to 03:00 PM') == '02:00 to 15:00'
    assert convert('3:00 AM to 4:00 PM') == '03:00 to 16:00'
    assert convert('4 AM to 5 PM') == '04:00 to 17:00'
    assert convert('06 AM to 07:00 PM') == '06:00 to 19:00'
    assert convert('8 AM to 9 PM') == '08:00 to 21:00'
    assert convert('10:01 AM to 11:02 PM') == '10:01 to 23:02'
    assert convert('12:00 AM to 11:59 PM') == '00:00 to 23:59'


def test_invalid():
    with pytest.raises(ValueError):
            convert('01:00 AM to 02:60 AM')
    with pytest.raises(ValueError):
        convert('-2:00 AM to 03:00 PM')
    with pytest.raises(ValueError):
        convert('13:00 AM to 4:00 PM')
    with pytest.raises(ValueError):
        convert('40 AM to 5 PM')
    with pytest.raises(ValueError):
        convert('6 AM to 17:00 PM')
    with pytest.raises(ValueError):
        convert('8AM to 9PM')
    with pytest.raises(ValueError):
        convert('10:01 AM - 11:02 PM')
    with pytest.raises(ValueError):
        convert('12:00AM to 11:59PM')


if __name__ == "__main__":
    main()
