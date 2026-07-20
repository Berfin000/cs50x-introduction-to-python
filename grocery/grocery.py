groceries = {}

while True:
    try:
        item = input()
    except EOFError:
        print()
        break

    item = item.lower()
    groceries[item] = groceries.get(item, 0) + 1

for item in sorted(groceries):
    print(f"{groceries[item]} {item.upper()}")




