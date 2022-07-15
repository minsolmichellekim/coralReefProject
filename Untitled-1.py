from PIL import Image
import cv2

picture = Image.open("IMG_3158.png")
picture = picture.convert("RGB")

width, height = picture.size
blue = (35, 94, 134)
white = (255, 255, 255)

# Process every pixel and convert other colors to white
for x in range(width):
   for y in range(height):
       current_color = picture.getpixel( (x,y) )
       if current_color == (35, 94, 134) or current_color == (224, 224, 192):
            picture.putpixel( (x,y), white)

picture.save("altered.png")

#Convert to binary
img = cv2.imread("altered.png", 2)
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
