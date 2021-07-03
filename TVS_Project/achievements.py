def achievements(result_frame):
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=1320, height=400)

    import os
    import tkinter
    from PIL import ImageTk, Image
    canvas = tkinter.Canvas(result_frame)
    frame = tkinter.Frame(canvas)

    achievement_frame = tkinter.Frame(frame)
    achievement_frame.grid(row=0, column=0)

    awards_frame = tkinter.Frame(frame)
    awards_frame.grid(row=1, column=0)

    myscrollbar = tkinter.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.grid(row=0, column=1, ipady=186)
    canvas.grid(row=0, column=0)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    frame.bind("<Configure>", myfunction)

    #   ###################       ACHIEVEMENTS        #######################
    award_label = tkinter.Label(achievement_frame, text='ACHIEVEMENTS', font=('andalus', 18, 'bold'))
    award_label.grid(row=0, column=0, pady=10)

    apache_award = os.path.abspath('../tvs_project/tvs_award/achievements-1.jpg')
    opened_image = Image.open(apache_award)
    resize_image = opened_image.resize((348, 161))
    global apache_img
    apache_img = ImageTk.PhotoImage(resize_image)
    apache_text = 'Highest In Customer Satisfaction'
    lbl_iqube_img = tkinter.Label(achievement_frame, image=apache_img, text=apache_text,
                                  compound='top',
                                  font=('andalus', 18, 'bold'), bg='white')
    lbl_iqube_img.grid(rowspan=3, column=0, padx=50, pady=20, ipadx=15, ipady=15)

    apacheRR_award = os.path.abspath('../tvs_project/tvs_award/achievements-2.jpg')
    opened_image = Image.open(apacheRR_award)
    resize_image = opened_image.resize((248, 140))
    global apacheRR_img
    apacheRR_img = ImageTk.PhotoImage(resize_image)
    apacheRR_text = ' Most Appealing\n      Premeium Motorcycle      '
    lbl_iqube_img = tkinter.Label(achievement_frame, image=apacheRR_img, text=apacheRR_text,
                                  compound='left',
                                  font=('andalus', 18, 'bold'), bg='white')
    lbl_iqube_img.grid(row=1, column=1, padx=110, pady=20, ipadx=15, ipady=15)

    Raedon_award = os.path.abspath('../tvs_project/tvs_award/achievements-3.jpg')
    opened_image = Image.open(Raedon_award)
    resize_image = opened_image.resize((248, 140))
    global raedon_img
    raedon_img = ImageTk.PhotoImage(resize_image)
    raedon_text = 'Highest Ranked Economy \n  Motorcycle In Initial Quality'
    lbl_iqube_img = tkinter.Label(achievement_frame, image=raedon_img, text=raedon_text,
                                  compound='left',
                                  font=('andalus', 18, 'bold'), bg='white')
    lbl_iqube_img.grid(row=2, column=1, padx=17, ipadx=15, ipady=15)

    #    ######################       LABEL AWARDS TAG         ######################

    tvs_motor_label = tkinter.Label(awards_frame, text='TVS Motor', font=('andalus', 18, 'bold'))
    tvs_motor_label.grid(row=0, column=0, pady=10)

    #    ######################        AWARDS          ######################

    tvs_award = os.path.abspath('../tvs_project/tvs_award/tvs_award_3.jpg')
    opened_image = Image.open(tvs_award)
    resize_image = opened_image.resize((230, 210))
    global tvs_award_img
    tvs_award_img = ImageTk.PhotoImage(resize_image)

    #   ######################        Award_1          ######################

    tvs_award_1 = os.path.abspath('../tvs_project/tvs_award/tvs_award_1.jpg')
    opened_image = Image.open(tvs_award_1)
    resize_image = opened_image.resize((230, 210))
    global tvs_award_1_img
    tvs_award_1_img = ImageTk.PhotoImage(resize_image)
    tvs_award_1_text = 'Bike Awards - 2019\n\n Two wheeler manufacturer of the year'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_1_img, text=tvs_award_1_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=1, column=0, ipadx=40, padx=30)

    #   ######################        Award_2          ######################

    tvs_award_2 = os.path.abspath('../tvs_project/tvs_award/tvs_award_2.jpg')
    opened_image = Image.open(tvs_award_2)
    resize_image = opened_image.resize((230, 210))
    global tvs_award_2_img
    tvs_award_2_img = ImageTk.PhotoImage(resize_image)
    tvs_award_2_text = 'Indian Motorcycle Of The Year - 2017'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_2_img, text=tvs_award_2_text,
                                  compound='top',
                                  font=('andalus', 14, 'bold'), bg='white')
    lbl_iqube_img.grid(row=1, column=1, ipady=19, ipadx=10, padx=30)

    #    ######################        Award_3          ######################

    tvs_award_3_text = 'Indian Motorcycle Of The Year - 2017'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_3_text,
                                  compound='top',
                                  font=('andalus', 14, 'bold'), bg='white')
    lbl_iqube_img.grid(row=1, column=2, ipady=19, ipadx=10, padx=30)

    #    ######################        Award_4          ######################

    tvs_award_4_text = 'Most Appealing Executive Scooter\n\nTVS Scooty Zest 110 is awarded the Most\n' \
                       'Appealing Executive Scooter by J.D. Power \n Asia Pacific Awards for 2016'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_4_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=2, column=0, ipady=10, ipadx=18, padx=30)

    #    ######################        Award_5          ######################

    tvs_award_5_text = 'Two Wheeler manufacturer Of The Year\n \nTVS Motor Company was named the Two\nWheeler' \
                       ' Manufacturer of the Year by NDTV\n Car and Bike Awards 2015'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_5_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=2, column=1, ipady=10, ipadx=18, padx=30)

    #    ######################        Award_6          ######################

    tvs_award_6_text = '''Most Trusted Brand\n\n TVS is India's Most Trusted Brand in the two\n Wheeler Category'''
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_6_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=2, column=2, ipady=17, ipadx=10, padx=30, pady=30)

    #   ######################        Award_7          ######################

    tvs_award_7_text = 'Most Appealing Premium Motorcycle\n\nTVS Apache RTR 180 is the Most Appealing\n' \
                       'Premium Motorcycle as awarded by J.D. Power \n Asia Pacific Awards for 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_7_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=3, column=0, ipady=20, ipadx=5, padx=30)

    #    ######################        Award_8          ######################

    tvs_award_8_text = 'Highest Ranked Economy Motorcycle in\n Initial Quality\n\n' \
                       ' TVS Starcity+ is Awarded the Highest Ranked\n Economy Motorcycle' \
                       'by J.D. power\n Asia Pacific Awards for 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_8_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=3, column=1, ipady=10, ipadx=5, padx=30)

    #    ######################        Award_9          ######################

    tvs_award_9_text = 'Most Appealing Economy Motorcycle \n\n' \
                       'TVS Starcity+ is Awarded the Most\nAppealing Economy Motorcycle' \
                       'by J.D. power\n Asia Pacific Awards for 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_9_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=3, column=2, ipady=20, ipadx=10, padx=30, pady=30)

    #  ######################        Award_10          ######################

    tvs_award_10_text = 'Most Appealing Executive Scooter\n\n' \
                        'TVS Jupiter is Awarded theMost Appealing \nExecutive Scooter' \
                        ' by J.D. power\n Asia Pacific Awards for 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_10_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=4, column=0, ipady=10, ipadx=23, padx=30)

    #    ######################        Award_11          ######################

    tvs_award_11_text = 'Highest in customer satisfaction\n\n' \
                        'TVS Motor has been awarded higest in\n customer satisfaction' \
                        'by J.D. power Asia\n Pacific Awards for 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_11_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=4, column=1, ipady=10, ipadx=27, padx=30)

    #    ######################        Award_12          ######################

    tvs_award_12_text = 'Most Appealing Premium Motorcycle\n\n' \
                        'TVS Apache RTR 180 is the Most Appealing\n Premium Motorcycle' \
                        ' as Awarded by\n J.D. power Asia Pacific Awards for 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_12_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=4, column=2, ipady=10, ipadx=15, padx=30, pady=30)
    #
    #    ######################        Award_13          ######################

    tvs_award_13_text = 'Best Executive Executive Scooter\n\n' \
                        'TVS Wego is Awarded the Best Executive \nScooter' \
                        ' by J.D. power Asia Pacific\n Awards for 2016'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_13_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=5, column=0, ipady=10, ipadx=27, padx=30)

    #    ######################        Award_14          ######################

    tvs_award_14_text = 'Most Appealing Economy Motorcycle\n\n' \
                        'TVS Starcity+ is Awarded the Most\n Appealing Economy Motorcycle' \
                        ' by \n J.D. power Asia Pacific Awards for 2016 '
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_img, text=tvs_award_14_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=5, column=1, ipady=10, ipadx=27, padx=30)

    #    ######################        Award_15          ######################

    tvs_award_15 = os.path.abspath('../tvs_project/tvs_award/mb_.jpg')
    opened_image = Image.open(tvs_award_15)
    resize_image = opened_image.resize((250, 210))
    global tvs_award_15_img
    tvs_award_15_img = ImageTk.PhotoImage(resize_image)
    tvs_award_15_text = 'Motorbeam - Bike Manufacturer Of The\n' \
                        'Year - 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_15_img, text=tvs_award_15_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=5, column=2, ipady=38, ipadx=33, padx=30, pady=30)

    #      #####################        Award_16          ######################

    tvs_award_16 = os.path.abspath('../tvs_project/tvs_award/NDTV_CAR.jpg')
    opened_image = Image.open(tvs_award_16)
    resize_image = opened_image.resize((250, 210))
    global tvs_award_16_img
    tvs_award_16_img = ImageTk.PhotoImage(resize_image)
    tvs_award_16_text = 'NDTV Car & Bike 2018'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_award_16_img, text=tvs_award_16_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=6, column=0, ipady=30, ipadx=59, padx=30, pady=30)

    #    ######################       LABEL BRAND AWARDS TAG         ######################

    tvs_motor_label = tkinter.Label(awards_frame, text='Brand Awards', font=('andalus', 18, 'bold'))
    tvs_motor_label.grid(row=7, column=0, pady=10)

    #    ######################        BRAND AWARDS          ######################

    tvs_brand_award_1 = os.path.abspath('../tvs_project/tvs_award/brand_award_1.jpg')
    opened_image = Image.open(tvs_brand_award_1)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_1_img
    tvs_brand_award_1_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_1_text = 'Autocar Awards 2018 - Readers Choice\n\n Brand - Apache RR 310'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_1_img, text=tvs_brand_award_1_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=8, column=0, ipadx=37, padx=30)

    tvs_brand_award_2 = os.path.abspath('../tvs_project/tvs_award/brand_award_2.jpg')
    opened_image = Image.open(tvs_brand_award_2)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_2_img
    tvs_brand_award_2_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_2_text = 'Autocar Awards 2018 - Readers Choice\n\n Brand - TVS Apache RTR 160 4V'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_2_img, text=tvs_brand_award_2_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=8, column=1, ipadx=32, padx=30)

    tvs_brand_award_3 = os.path.abspath('../tvs_project/tvs_award/brand_award_3.jpg')
    opened_image = Image.open(tvs_brand_award_3)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_3_img
    tvs_brand_award_3_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_3_text = 'Autocar Awards 2018 - Readers Choice\n\n Brand - TVS Raedon'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_3_img, text=tvs_brand_award_3_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=8, column=2, ipadx=32, padx=30)

    tvs_brand_award_4 = os.path.abspath('../tvs_project/tvs_award/brand_award_4.jpg')
    opened_image = Image.open(tvs_brand_award_4)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_4_img
    tvs_brand_award_4_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_4_text = 'CNBC TV18 - Viewers Choice\nMotorcycle Of The Year\n\nBrand - Apache RTR 200 4V'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_4_img, text=tvs_brand_award_4_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=9, column=0, ipady=20, ipadx=70, padx=30, pady=50)

    tvs_brand_award_5 = os.path.abspath('../tvs_project/tvs_award/brand_award_5.jpg')
    opened_image = Image.open(tvs_brand_award_5)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_5_img
    tvs_brand_award_5_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_5_text = 'The Deming Prize\n\n' \
                             'TVS Motor Company is the only two-wheeler\n' \
                             'company in the world to be awrded the\n ' \
                             'worlds most prestigious and coveted\n ' \
                             'recognition in TQM'

    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_5_img, text=tvs_brand_award_5_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=9, column=1, ipady=1, ipadx=12, padx=30, pady=50)

    tvs_brand_award_6 = os.path.abspath('../tvs_project/tvs_award/brand_award_6.jpg')
    opened_image = Image.open(tvs_brand_award_6)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_6_img
    tvs_brand_award_6_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_6_text = 'Progressive Manufacturer 100 Award\n\n' \
                             'TVS wins coveted 2009 Progressive\n' \
                             'Manufacturer 100 Award for end-to-end\n' \
                             'automation of the entire business process of\n' \
                             'its lubricant brand, TVS TRU4'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_6_img, text=tvs_brand_award_6_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=9, column=2, ipady=1, ipadx=10, padx=30, pady=50)

    tvs_brand_award_7 = os.path.abspath('../tvs_project/tvs_award/brand_award_7.jpg')
    opened_image = Image.open(tvs_brand_award_7)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_7_img
    tvs_brand_award_7_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_7_text = 'Motor Vikatan - 2019 (Computer\nMotorcycle Of The Year)\n\n' \
                             'Brand - TVS Raedon'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_7_img, text=tvs_brand_award_7_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=10, column=0, ipadx=65, padx=30, pady=20)

    tvs_brand_award_8 = os.path.abspath('../tvs_project/tvs_award/brand_award_8.jpg')
    opened_image = Image.open(tvs_brand_award_8)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_8_img
    tvs_brand_award_8_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_8_text = 'Motoring Awards - 2017 (Premium\nMotorcycle Of The Year)\n\n' \
                             'Brand - TVS Apache RTR 200 4V'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_8_img, text=tvs_brand_award_8_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=10, column=1, ipadx=53, padx=20)

    tvs_brand_award_10 = os.path.abspath('../tvs_project/tvs_award/brand_award_9.jpg')
    opened_image = Image.open(tvs_brand_award_10)
    resize_image = opened_image.resize((230, 210))
    global tvs_brand_award_10_img
    tvs_brand_award_10_img = ImageTk.PhotoImage(resize_image)
    tvs_brand_award_10_text = 'Motoroctane 2W Awards - 2018(Best\n' \
                              'Affordable Enthusiast Bike)\n\n' \
                              'Brand - Apache RR 310'
    lbl_iqube_img = tkinter.Label(awards_frame, image=tvs_brand_award_10_img, text=tvs_brand_award_10_text,
                                  compound='top',
                                  font=('andalus', 12, 'bold'), bg='white')
    lbl_iqube_img.grid(row=10, column=2, ipadx=44, padx=20)


if __name__ == '__main__':
    import layout

    frame_2 = layout.output_frame
    achievements(frame_2)
