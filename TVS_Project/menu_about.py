def about(result_frame):
    import os
    import tkinter
    from PIL import ImageTk, Image
    import docx2txt

    scroll = tkinter.Scrollbar(result_frame)
    scroll.grid(row=0, column=1, ipady=176)
    lbl_name = tkinter.Text(result_frame, wrap=tkinter.WORD, height=19, width=140, yscrollcommand=scroll.set)
    global tvs_logo
    tvs_image_location = os.path.abspath('../tvs_project/TVS_about.jpg')
    opened_image = Image.open(tvs_image_location)
    resize_image = opened_image.resize((650,300))
    tvs_logo = ImageTk.PhotoImage(resize_image)
    lbl_name.image_create("insert", image=tvs_logo, padx=280)
    about_word_file_location = os.path.abspath('../tvs_project/WORD_files/TVS_about.docx')
    word_file = docx2txt.process(about_word_file_location)
    lbl_name.insert("insert", '\n' * 2 + f"{word_file}")
    lbl_name.config(font=("times new roman", 14))
    lbl_name.configure(padx=28)
    lbl_name.config(state='disable')
    lbl_name.grid(row=0, column=0)
    scroll.config(command=lbl_name.yview)


if __name__ == '__main__':
    import layout

    frame = layout.output_frame
    about(frame)
