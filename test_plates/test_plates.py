from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA") == True
    assert is_valid("AAAAAAA") ==False

def test_beginning():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("11") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_number_placement():
    assert is_valid("AAA22") == True
    assert is_valid("AAA22A") == False
    assert is_valid("PI3.14") == False
