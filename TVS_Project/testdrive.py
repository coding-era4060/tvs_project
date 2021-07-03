def testdrive(result_frame):
    def submit():
        NAME = name.get()
        contact_no = phone.get()
        state_name = state.get()
        vechile_name = vechile.get()
        _name_ = NAME.split(' ')

        if contact_no.isnumeric() and len(contact_no) == 10:
            if len(state_name) != 0:
                if len(vechile_name) != 0:
                    no = 1
                    for i in _name_:
                        if i.isalpha():
                            bk = no
                            no += 1
                    if len(_name_) >= 2:
                        if bk == len(_name_):
                            pass
                        else:
                            messagebox.showerror('ERROR', 'Enter Correct Name')
                    else:
                        messagebox.showerror('ERROR', 'Enter Full Name')
                else:
                    messagebox.showerror('ERROR', 'All Field Are Required ')
            else:
                messagebox.showerror('ERROR', 'All Field Are Required ')
        else:
            messagebox.showerror('ERROR', 'Invalid Number')

    def reset():
        name.set('')
        phone.set('')
        email.set('')
        state.set('')
        vechile.set('')

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=1320, height=400)

    import os
    import tkinter
    from tkinter import ttk
    from PIL import ImageTk, Image
    from tkinter import messagebox

    canvas = tkinter.Canvas(result_frame)
    frame = tkinter.Frame(canvas)

    image_frame = tkinter.Frame(frame)
    image_frame.grid(row=0, column=0)

    details_frame = tkinter.Frame(frame, bg='white')
    details_frame.grid(row=0, column=1, pady=60, padx=30)

    myscrollbar = tkinter.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.grid(row=0, column=1, ipady=186)
    canvas.grid(row=0, column=0)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    frame.bind("<Configure>", myfunction)

    test_drive_img_location = os.path.abspath('../tvs_project/test_ride.jpg')
    opened_image = Image.open(test_drive_img_location)
    resize_image = opened_image.resize((550, 328))
    global test_drive_img
    test_drive_img = ImageTk.PhotoImage(resize_image)
    lbl_iqube_img = tkinter.Label(image_frame, image=test_drive_img)
    lbl_iqube_img.grid(row=0, column=0, padx=50, pady=50)

    book_lbl = tkinter.Label(details_frame, text='Book Your Test Ride', bg='white', font=('andalus', 20, 'bold'))
    book_lbl.grid(row=0, columnspan=2, pady=20)

    book_detail_lbl = tkinter.Label(details_frame, text='To Book Your Test Ride Now, Kindly Fill Your Information',
                                    bg='white', font=('andalus', 14, 'bold'))
    book_detail_lbl.grid(row=1, columnspan=2, pady=20, padx=20)

    name = tkinter.StringVar()
    phone = tkinter.StringVar()
    email = tkinter.StringVar()
    state = tkinter.StringVar()
    vechile = tkinter.StringVar()

    name_lbl = tkinter.Label(details_frame, text='Name', bg='white', font=('andalus', 14, 'bold'))
    name_lbl.grid(row=2, column=0, pady=10)

    entry_name_lbl = tkinter.Entry(details_frame, bg='white', width=21, textvariable=name, font=('andalus', 14, 'bold'))
    entry_name_lbl.grid(row=2, column=1, pady=10)

    phone_lbl = tkinter.Label(details_frame, text='Phone', bg='white', font=('andalus', 14, 'bold'))
    phone_lbl.grid(row=3, column=0, pady=10)

    entry_phone_lbl = tkinter.Entry(details_frame, bg='white', width=21, textvariable=phone,
                                    font=('andalus', 14, 'bold'))
    entry_phone_lbl.grid(row=3, column=1, pady=10)

    email_lbl = tkinter.Label(details_frame, text='E-MAIL', bg='white', font=('andalus', 14, 'bold'))
    email_lbl.grid(row=4, column=0, pady=10)

    entry_email_lbl = tkinter.Entry(details_frame, bg='white', textvariable=email, width=21,
                                    font=('andalus', 14, 'bold'))
    entry_email_lbl.grid(row=4, column=1, pady=10)

    state_lbl = tkinter.Label(details_frame, text='State', bg='white', font=('andalus', 14, 'bold'))
    state_lbl.grid(row=5, column=0, pady=10)

    state_list = ["RAJASTHAN", 'GUJARAT', 'MADHYA PRADESH', 'UTTAR PRADESH', 'TAMILNADU',
                  'KERELA', 'MAHARASHTRA', 'CHATTISGARH', 'UTTARAKHAND', 'HARYANA', 'DELHI',
                  'PUNJAB', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'BIHAR', 'JHARKHAND',
                  'ODISHA', 'WEST BENGAL', 'ASSAM', 'PONDICHERRY', 'GOA']

    vechile_list = ['Apache RR 310', 'Apache RTR Series', 'TVS Raedon', 'Star City +', 'TVS Sport',
                    'TVS Ntorq', 'TVS Jupiter', 'Zest 110', 'Scooty Pep+', 'TVS XL 100']

    entry_state_lbl = ttk.Combobox(details_frame, font=('andalus', 14, 'bold'), textvariable=state, state='readonly',
                                   height=5,
                                   value=state_list)
    entry_state_lbl.grid(row=5, column=1, pady=10)

    vechile_lbl = tkinter.Label(details_frame, text='Vechile', bg='white', font=('andalus', 14, 'bold'))
    vechile_lbl.grid(row=6, column=0, pady=10)

    entry_vechile_lbl = ttk.Combobox(details_frame, textvariable=vechile, font=('andalus', 14, 'bold'),
                                     state='readonly',
                                     height=5,
                                     value=vechile_list)
    entry_vechile_lbl.grid(row=6, column=1, pady=10)

    submit_btn = tkinter.Button(details_frame, width=10, text='Submit', bg='deep sky blue', relief='groove',
                                font=('andalus', 14, 'bold'), command=submit)
    submit_btn.grid(row=7, column=0, pady=20, padx=30)

    submit_btn = tkinter.Button(details_frame, width=10, text='Reset', bg='deep sky blue', relief='groove',
                                font=('andalus', 14, 'bold'), command=reset)
    submit_btn.grid(row=7, column=1, pady=20, padx=30)


if __name__ == '__main__':
    import layout

    frame_1 = layout.output_frame
    testdrive(frame_1)
