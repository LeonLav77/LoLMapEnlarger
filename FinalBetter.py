from tkinter import *  
from PIL import ImageTk,Image
import d3dshot
import time
import cv2
import keyboard
d = d3dshot.create()
 
root = Tk()  
canvas = Canvas(root, width = 1500, height = 1080)  
canvas.pack()
global scale_percent
scale_percent = 250     #percent by which the image is resized
global img
l = True
x = 0

GENERALPATH = 'C:/Users/Leon/Desktop/screenshotovi'
def staviSliku(imeSlike):
    img = ImageTk.PhotoImage(Image.open(f'{GENERALPATH}/slika'+str(imeSlike)+'.png'))  
    canvas.create_image(20, 20, anchor=NW, image=img)
    root.update_idletasks()
    root.update()
while l:
    d.screenshot_to_disk(f'{GENERALPATH}','slika'+str(x)+'.png',region=(1540,690,1918,1080))
    src = cv2.imread(f'{GENERALPATH}/slika'+str(x)+'.png', cv2.IMREAD_UNCHANGED) 
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    dsize = (width, height)
    output = cv2.resize(src, dsize)
    cv2.imwrite(f'{GENERALPATH}/slika'+str(x)+'.png',output) 
    staviSliku(x)
    x += 1
    if x < 2:
        x = 0
    if keyboard.is_pressed('m') and keyboard.is_pressed('n'):
            print('You Pressed A Key!')
            break