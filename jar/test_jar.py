import pytest
from jar import Jar


def test_init():
    # Varsayılan kapasite kontrolü
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Özel kapasite kontrolü
    custom_jar = Jar(15)
    assert custom_jar.capacity == 15

    # Geçersiz kapasite kontrolü
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("ten")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    # Kapasiteyi aşma testi
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

    # Olmayan kurabiyeyi çekme testi
    with pytest.raises(ValueError):
        jar.withdraw(6)
