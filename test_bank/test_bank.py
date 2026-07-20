from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h_start():
    assert value("hey") == 20
    assert value ("hi") == 20

def test_others():
    assert value("whats up") == 100
    assert value("good morning") == 100
