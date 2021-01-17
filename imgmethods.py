from PIL import Image
img = Image.open('./pokedex/charmander.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))
