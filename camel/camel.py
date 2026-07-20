def convert(camel):
    snake = ""
    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return snake


def main():
    camel = input("camelCase: ")
    print(convert(camel))


if __name__ == "__main__":
    main()
