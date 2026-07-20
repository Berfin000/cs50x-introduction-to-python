from datetime import date
import pytest
from seasons import calculate_minutes, minutes_to_words, get_date


def test_get_date_valid():
    assert get_date("1999-01-01") == date(1999, 1, 1)


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("January 1, 1999")
    with pytest.raises(ValueError):
        get_date("1999-13-01")


def test_calculate_minutes():
    # 1 yıl tam olarak 525600 dakika (artık yıl değilse)
    assert calculate_minutes(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    # 2 yıl 1051200 dakika
    assert calculate_minutes(date(1998, 1, 1), date(2000, 1, 1)) == 1051200


def test_minutes_to_words():
    assert (
        minutes_to_words(525600)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        minutes_to_words(1051200)
        == "One million, fifty-one thousand, two hundred minutes"
    )
