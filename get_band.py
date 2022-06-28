from PIL import Image

colorImage = Image.open("photos/IMG_3158.JPG")
rotated = colorImage.rotate(50)

width, height = rotated.size
left = 2.54 * width / 5
right = 3.06 * width / 5
top = 2.2 * height / 5
bottom = 3.08 * height / 5

rotated = rotated.crop((left, top, right, bottom))

rotated.save("band.jpg")
