from rembg import remove
import easygui
from PIL import Image, ImageOps
import random

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

inputpath = easygui.fileopenbox(title="Select Your Image")
outputpath = easygui.filesavebox(title="Save File To")

input = Image.open(inputpath)
output = remove(input)

background = Image.new("RGBA", output.size, get_random_color())

background.paste(output, (0, 0), output)

background.save(outputpath)
