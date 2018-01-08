from PIL import ImageGrab

img = ImageGrab.grab((0, 100, 540, 1020))

img.save('wegoing.png')
