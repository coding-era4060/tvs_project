def service_details(result_frame):
    def show_service_details():
        service = service_no.get()
        if service == 1:
            text = 'Your vechile need first service in 3rd month or 1000km from date of purchasing'
        elif service == 2:
            text = 'Your vechile need second service in 6th month or 2500km from date of purchasing'
        elif service == 3:
            text = 'Your vechile need Third service in 8th month or 6000km from date of purchasing'
        elif service == 4:
            text = 'Your vechile need Fourth service in 10th month or 9000km from date of purchasing'
        elif service == 5:
            text = 'Your vechile need Fifth service in 12th month or 12000km from date of purchasing'

        messagebox.showinfo('SERVICE DETAIL', text)


    import tkinter
    from tkinter import messagebox
    service_no = tkinter.IntVar()
    service_1 = tkinter.Radiobutton(result_frame, text="First service", font=("andalus", 16, 'bold'), value=1,
                                    variable=service_no, padx=40)
    service_1.grid(row=0, column=0)
    service_2 = tkinter.Radiobutton(result_frame, text="Second service", font=('andalus', 16, 'bold'), value=2,
                                    variable=service_no, padx=40)
    service_2.grid(row=0, column=1)
    service_3 = tkinter.Radiobutton(result_frame, text="Third service", font=("andalus", 16, 'bold'), value=3,
                                    variable=service_no, padx=40)
    service_3.grid(row=0, column=2)
    service_4 = tkinter.Radiobutton(result_frame, text="Fourth service", font=('andalus', 16, 'bold'), value=4,
                                    variable=service_no, padx=40)
    service_4.grid(row=0, column=3)
    service_5 = tkinter.Radiobutton(result_frame, text="Fifth service", font=("andalus", 16, 'bold'), value=5,
                                    variable=service_no, padx=40)
    service_5.grid(row=0, column=4)
    but = tkinter.Button(result_frame, relief='groove', text="Search", font=("andalus", 16, 'bold'),
                         command=show_service_details, bg='black', fg='white')
    but.grid(row=1, column=2, pady=20)


if __name__ == '__main__':
    import layout

    frame = layout.output_frame
    service_details(frame)
