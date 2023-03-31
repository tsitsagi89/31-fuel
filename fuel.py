def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        fraction = float(eval(fraction))
        if fraction*100 > 100:
            return "ValueError"
        else:
            return fraction*100
    except ValueError:
        return("fraction should be <= 1")
    except NameError:
        return("fraction should be integer")
    except ZeroDivisionError:
        return("division by zero")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        percentage = "{:.0%}".format(percentage/100)
        return percentage


if __name__ == "__main__":
    main()