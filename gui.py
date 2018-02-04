from Tkinter import *                         # Import tkinter
from PIL import ImageTk, Image
from threading import Timer


def change_photo(e):
    global status
    status = 1 - status
    show_image()
    pass

def show_image():
    # photo = ImageTk.PhotoImage(Image.open(image_path))
    # photo=PhotoImage(file="red_button.png")           # Give photo an image
    b.config(image=photos[status])  # Configure the earlier instance to use the photo
    b.pack()
    
def second():
    global var
    global open_time
    global t
    global label
    global status
    if open_time <= 0:
        status = 0
        show_image()
    if status == 0:
        var.set("OFF")
        open_time = 60*60
    else:

        seconds = open_time % 60
        minutes = open_time / 60
        hours = minutes / 60
        minutes = minutes - 60 * hours
        var.set("{h:02d}:{m:02d}:{s:02d}".format(h=hours, m=minutes, s=seconds))
        open_time -= 1
    root.update_idletasks()
    t = Timer(1, second)
    t.start()

def plus(e):
    global open_time
    open_time += 15 * 60

def minus(e):
    global open_time
    open_time -= 15 * 60

open_time = 60*60


root=Tk() 
root.geometry("320x240") 

var = StringVar(root)
var.set('00:00')
label = Label(textvariable=var)
label.pack(side=TOP)

photos = []
photos.append(ImageTk.PhotoImage(Image.open("button_grey.jpg")))
photos.append(ImageTk.PhotoImage(Image.open("button_red.jpeg")))
b=Button(root,justify = LEFT) 
b.bind('<Button-1>',change_photo)
status = 1
show_image()

labelframe = LabelFrame(root)
labelframe.pack()
b_plus=Button(labelframe,justify = LEFT) 
b_plus.bind('<Button-1>',plus)
photo_plus = ImageTk.PhotoImage(Image.open("plus.jpg"))
b_plus.config(image=photo_plus)  # Configure the earlier instance to use the photo
b_plus.pack(side=LEFT)

b_minus=Button(labelframe,justify = LEFT) 
b_minus.bind('<Button-1>',minus)
photo_minus = ImageTk.PhotoImage(Image.open("minus.jpg"))
b_minus.config(image=photo_minus)  # Configure the earlier instance to use the photo
b_minus.pack(side=LEFT)
root.wm_attributes('-fullscreen', 'true')



t = Timer(1, second)
t.start()

root.mainloop() 


                              # Create everything
