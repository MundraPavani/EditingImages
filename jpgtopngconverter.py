import sys
import os
from PIL import Image
#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new\ exists, if not create it  #using os
if not os.path.exists(output_folder)
 os.makedirs(output_folder)

for filename in os.listdir(image_folder) 
  img = Image.open(f'{image_folder}{filename}')          #bec file is outside of folder
  clean_name = os.path.splitext(filename)[0]
  img.save(f'{output_folder}{cleanname}.png', 'png')
  print('all donne')
#loop through pokedex , bec have 4 images in same folder
#convert images to png
#save to the new folder
