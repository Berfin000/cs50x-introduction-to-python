import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

gecerli_uzantilar= [".jpg", ".jpeg", ".png"]
uzanti1= os.path.splitext(sys.argv[1])[1].lower()
uzanti2= os.path.splitext(sys.argv[2])[1].lower()

if uzanti1 not in gecerli_uzantilar:
    sys.exit("Invalid output")
if uzanti2 not in gecerli_uzantilar:
    sys.exit("Invalid output")
if uzanti1 != uzanti2:
    sys.exit("Input and output have different extensions")

try:
    girdi_resmi= Image.open(sys.argv[1])
    tisort= Image.open("shirt.png")
    boyut=tisort.size
    sablon_resim= ImageOps.fit(girdi_resmi, boyut)
    sablon_resim.paste(tisort, tisort)
    sablon_resim.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")

