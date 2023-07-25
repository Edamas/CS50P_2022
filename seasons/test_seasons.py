from seasons import get_minutes
import pytest

def main():
    test_get_minutes()


def test_get_minutes():
    assert get_minutes(2022, 7, 25) == 'Five hundred twenty-five thousand, six hundred minutes'
    assert get_minutes(2021, 7, 25) == 'One million, fifty-one thousand, two hundred minutes'
    with pytest.raises(SystemExit) as pytest_exit:
        get_minutes(2020, 2, 30)
    assert pytest_exit.type == SystemExit


if __name__ == '__main__':
    main()
