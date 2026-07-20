from numb3rs import validate


def test_valid_ips():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("192.168.1.1") is True


def test_invalid_ips():
    assert validate("275.3.6.28") is False
    assert validate("255.255.255.256") is False
    assert validate("512.512.512.512") is False
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("cat") is False
    assert validate("1.2.3.abc") is False
