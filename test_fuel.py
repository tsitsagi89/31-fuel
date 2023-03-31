import fuel

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("2/2") == 100
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/100") == 1
    assert fuel.convert("1/0") == "division by zero"
    assert fuel.convert("1/0") == "division by zero"
    assert fuel.convert("Cat/0") == "fraction should be integer"
    assert fuel.convert("2/1") == "ValueError"


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(65) == "65%"

if __name__ == "__main__":
    main()