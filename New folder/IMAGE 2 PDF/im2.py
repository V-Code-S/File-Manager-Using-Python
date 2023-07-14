from PIL import Image

image_1 = Image.open(r'C:\Users\viruk\OneDrive\Documents\images\viru.png')
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\viruk\OneDrive\Documents\pdf123.pdf')
