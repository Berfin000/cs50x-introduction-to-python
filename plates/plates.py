def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False

    if not s[0].isalpha():
        return False
    if not s[1].isalpha():
        return False

    number_started = False

    for char in s:

        if char.isalpha():
            if number_started:
                return False

        elif char.isdigit():
            if not number_started:
                if char == '0':
                    return False
                number_started = True

        else:
            return False

    return True


main()
