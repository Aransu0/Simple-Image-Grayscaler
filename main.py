from PIL import Image

with Image.open("gojo.jpg") as img:
    img.load()

img.show()
