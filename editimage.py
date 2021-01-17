from PIL import Image, ImageFilter
img = Image.open('./pokedex/squirtle.jpg')
filtered_img = img.filter(ImageFilter.BLUR)  #SMOOTH, 
filtered_img.save("blur.png", 'png')
print(img)
