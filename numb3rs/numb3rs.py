import re
import sys

def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for i in range(1, 5):
            part = matches.group(i)

            if len(part) > 1 and part.startswith("0"):
                return False

            num = int(part)
            if num < 0 or num > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
