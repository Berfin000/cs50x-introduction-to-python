from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
if len(sys.argv) == 1:
    all_fonts = figlet.getFonts()
    random_font = random.choice(all_fonts)
    figlet.setFont(font=random_font)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

user_input= input("Input: ")
render_text= figlet.renderText(user_input)
print(render_text)


