import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def option_menu_value(*args):
    v = menu.get()
    menu.set('MENU')
    print(v)


a = Tk()
a.geometry('1350x720')
tvs_image_location = os.path.abspath('../tvs_project/tvs logo.png')

image_frame = Frame(a, bg='orange')
image_frame.grid(row=0, column=0)

widget_frame = Frame(a)
widget_frame.grid(row=1, column=0)

output_frame = Frame(a, bg='white', width=50)
output_frame.grid(row=2, column=0)

opened_image = Image.open(tvs_image_location)

global tvs_logo
tvs_logo = ImageTk.PhotoImage(opened_image)
lbl_tvs_logo = Label(image_frame, image=tvs_logo, bg='orange')
lbl_tvs_logo.pack(side=TOP, padx=274)

menu_list = ['ABOUT US', 'OFFERS', 'OUR PRODUCTS', 'SERVICE DETAILS', 'DEALER LOCATOR']
menu = StringVar()
menu.set('MENU')
menu_button = OptionMenu(widget_frame, menu, *menu_list, command=option_menu_value)
menu_button.config(font=('bold', 22), bg="black", fg="white", padx=50, pady=10, relief='groove')
menu_button["menu"].config(bg="white", font=32)
menu_button.pack(side=LEFT, anchor='w')

about_button = Button(widget_frame, text="Test Drive", font=('bold', 22), bg="black", fg="white", padx=40,
                      relief='groove')
about_button.pack(side=LEFT)

vechile_button = Button(widget_frame, text="Vechile", font=('bold', 22), bg="black", fg="white", padx=50,
                        relief='groove')
vechile_button.pack(side=LEFT)

award_button = Button(widget_frame, text="Awards", font=('bold', 22), bg="black", fg="white", padx=40,
                      relief='groove')
award_button.pack(side=LEFT)

feedback_button = Button(widget_frame, text="Feedback", font=('bold', 22), bg="black", fg="white", padx=40,
                         relief='groove')
feedback_button.pack(side=LEFT)

exit_button = Button(widget_frame, text="Exit", font=('bold', 22), bg="black", fg="white", padx=40, relief='groove')
exit_button.pack(side=RIGHT)

a.mainloop()