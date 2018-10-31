from tkinter import *
from PIL import Image, ImageTk
import os
import imageSel
from PIL import Image
from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert


window = Tk()

window.title("MediLink.com")

window.geometry('500x500')

col = Image.open(imageSel.im) #read image
print (col)
gray = col.convert('L')  #conversion to gray scale
bw = gray.point(lambda x: 0 if x<128 else 255, '1')  #binarization
#bw.save("bw.jpg") #save it
#Image.open('bw.jpg').show()
im1 = Image.open(bw)
im1 = im1.resize((250, 250), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(im1)
myvar=Label(window,image = tkimage)
myvar.image = tkimage
myvar.grid(column=1,row=6)

window.mainloop()
