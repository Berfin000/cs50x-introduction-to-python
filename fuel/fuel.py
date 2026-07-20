while True:
    fraction = input("Fraction: ")

    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)

        # Geçersiz durumlar
        if y == 0 or x > y or x < 0:
            raise ValueError

        # Geçerli kesir olduğunda döngüden çık
        break
    except (ValueError, ZeroDivisionError):
        continue

# Yüzde hesapla
percentage = round(x / y * 100)

# Çıktıyı yazdır
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
