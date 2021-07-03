def testdrive():
    try:
        offer_frame.grid_forget()
        about_frame.grid_forget()
        service_frame.grid_forget()
        dealer_frame.grid_forget()
        our_product_frame.grid_forget()
        achivement_frame.grid_forget()
    finally:
        testdrive_frame.grid(row=2, column=0)
        import testdrive
        testdrive.testdrive(testdrive_frame)


def achievements():
    try:
        offer_frame.grid_forget()
        about_frame.grid_forget()
        service_frame.grid_forget()
        dealer_frame.grid_forget()
        our_product_frame.grid_forget()
        testdrive_frame.grid_forget()
    finally:
        achivement_frame.grid(row=2, column=0)
        import achievements
        achievements.achievements(achivement_frame)


def feedback():
    def save_feedback():
        feed_back = feedback_box.get(1.0, END)
        if not feed_back.isspace():
            messagebox.showinfo('THANKS', 'Thanks for giving your feedback')
            feedback_box.delete(1.0, END)
        else:
            messagebox.showerror('ERROR', 'Feedback is empty')

    try:
        offer_frame.grid_forget()
        about_frame.grid_forget()
        service_frame.grid_forget()
        dealer_frame.grid_forget()
        achivement_frame.grid_forget()
        our_product_frame.grid_forget()
        testdrive_frame.grid_forget()
    finally:
        feedback_frame.grid(row=2, column=0)

        lbl_feedback = Label(feedback_frame, text='Enter your feedback', font=('bold', 22))
        lbl_feedback.grid(row=0, column=0)
        feedback_box = Text(feedback_frame, height=2, width=57)
        feedback_box.config(font=('times new roman', 18, 'bold'))
        feedback_box.grid(row=0, column=1, padx=20)
        submit_feedback_button = Button(feedback_frame, text="Submit", font=('bold', 22), bg="black", fg="white",
                                        padx=40,
                                        relief='groove', command=save_feedback)
        submit_feedback_button.grid(row=0, column=2, padx=20)


def vechile():
    try:
        offer_frame.grid_forget()
        about_frame.grid_forget()
        service_frame.grid_forget()
        dealer_frame.grid_forget()
        feedback_frame.grid_forget()
        achivement_frame.grid_forget()
        testdrive_frame.grid_forget()
    finally:
        our_product_frame.grid(row=2, column=0)
        import our_product_or_vechile
        our_product_or_vechile.vechile(our_product_frame)


def option_menu_value(*args):
    v = menu.get()
    menu.set('MENU')
    if v == 'ABOUT US':
        try:
            service_frame.grid_forget()
            offer_frame.grid_forget()
            our_product_frame.grid_forget()
            dealer_frame.grid_forget()
            feedback_frame.grid_forget()
            achivement_frame.grid_forget()
            testdrive_frame.grid_forget()
        finally:
            about_frame.grid(row=2, column=0)
            import menu_about
            menu_about.about(about_frame)
    elif v == 'OFFERS':
        try:
            service_frame.grid_forget()
            about_frame.grid_forget()
            our_product_frame.grid_forget()
            dealer_frame.grid_forget()
            feedback_frame.grid_forget()
            achivement_frame.grid_forget()
            testdrive_frame.grid_forget()
        finally:
            offer_frame.grid(row=2, column=0)
            import menu_offers
            menu_offers.offers(offer_frame)
    elif v == 'OUR PRODUCTS':
        try:
            offer_frame.grid_forget()
            about_frame.grid_forget()
            service_frame.grid_forget()
            dealer_frame.grid_forget()
            feedback_frame.grid_forget()
            achivement_frame.grid_forget()
            testdrive_frame.grid_forget()
        finally:
            our_product_frame.grid(row=2, column=0)
            import our_product_or_vechile
            our_product_or_vechile.vechile(our_product_frame)
    elif v == 'DEALER LOCATOR':
        try:
            offer_frame.grid_forget()
            about_frame.grid_forget()
            our_product_frame.grid_forget()
            service_frame.grid_forget()
            feedback_frame.grid_forget()
            achivement_frame.grid_forget()
            testdrive_frame.grid_forget()
        finally:
            dealer_frame.grid(row=2, column=0)
            import menu_near_dealer
            menu_near_dealer.near_dealer(dealer_frame)
    elif v == 'SERVICE DETAILS':
        try:
            offer_frame.grid_forget()
            about_frame.grid_forget()
            our_product_frame.grid_forget()
            dealer_frame.grid_forget()
            feedback_frame.grid_forget()
            achivement_frame.grid_forget()
            testdrive_frame.grid_forget()
        finally:
            service_frame.grid(row=2, column=0)
            import menu_service_details
            menu_service_details.service_details(service_frame)
    else:
        print('wrong choice')


if __name__ == "__main__":
    import os
    from tkinter import *
    from tkinter import messagebox
    from PIL import ImageTk, Image

    a = Tk()
    height = a.winfo_screenheight()
    width = a.winfo_screenwidth()+10
    a.geometry(f'{width}x{height}+0+0')

    tvs_image_location = os.path.abspath('../tvs_project/tvs_main.jpg')

    image_frame = Frame(a, bg='orange')
    image_frame.grid(row=0, column=0)

    widget_frame = Frame(a)
    widget_frame.grid(row=1, column=0)

    about_frame = Frame(a, width=500)
    about_frame.grid(row=2, column=0)

    offer_frame = Frame(a, width=500)
    about_frame.grid(row=2, column=0)

    our_product_frame = Frame(a, width=500)
    our_product_frame.grid(row=2, column=0)

    service_frame = Frame(a, width=500, pady=30)
    service_frame.grid(row=2, column=0)

    dealer_frame = Frame(a, width=500, pady=30)
    dealer_frame.grid(row=2, column=0)

    feedback_frame = Frame(a, width=500, pady=30)
    feedback_frame.grid(row=2, column=0)

    achivement_frame = Frame(a, width=500)
    achivement_frame.grid(row=2, column=0)

    testdrive_frame = Frame(a)
    testdrive_frame.grid(row=2, column=0)

    opened_image = Image.open(tvs_image_location)
    resize_image = opened_image.resize((700, 210))

    global tvs_logo
    tvs_logo = ImageTk.PhotoImage(resize_image)
    lbl_tvs_logo = Label(image_frame, image=tvs_logo, bg='orange')
    lbl_tvs_logo.pack(side=TOP, padx=333)

    menu_list = ['ABOUT US', 'OFFERS', 'OUR PRODUCTS', 'SERVICE DETAILS', 'DEALER LOCATOR']
    menu = StringVar()
    menu.set('MENU')
    menu_button = OptionMenu(widget_frame, menu, *menu_list, command=option_menu_value)
    menu_button.config(font=('bold', 22), bg="black", fg="white", padx=52, pady=10, relief='groove')
    menu_button["menu"].config(bg="white", font=32)
    menu_button.pack(side=LEFT, anchor='w')

    testdrive_button = Button(widget_frame, text="Test Drive", font=('bold', 22), bg="black", fg="white", padx=30,
                              relief='groove', command=testdrive)
    testdrive_button.pack(side=LEFT)

    vechile_button = Button(widget_frame, text="Vechile", font=('bold', 22), bg="black", fg="white", padx=30,
                            relief='groove', command=vechile)
    vechile_button.pack(side=LEFT)

    achievements_button = Button(widget_frame, text="Achievements", font=('bold', 22), bg="black", fg="white", padx=35,
                                 relief='groove', command=achievements)
    achievements_button.pack(side=LEFT)

    feedback_button = Button(widget_frame, text="Feedback", font=('bold', 22), bg="black", fg="white", padx=35,
                             relief='groove', command=feedback)
    feedback_button.pack(side=LEFT)

    exit_button = Button(widget_frame, text="Exit", font=('bold', 22), bg="black", fg="white", padx=39, relief='groove',
                         command=quit)
    exit_button.pack(side=RIGHT)

    a.mainloop()
