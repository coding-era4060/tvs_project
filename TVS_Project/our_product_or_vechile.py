def vechile(result_frame):
    def form(required_list):
        # required_list = detail_list
        # detail_list = [NAME, mobile_no, state, Address, City, ID, offers,
        #                pay_mode, insurance_comp, accessories, logistics,
        #                vat, vechile_prize, grandtotal, final_amount, insurance_name,
        #                insurance_amount]

        final_bill = tkinter.Toplevel(bg="peach puff")

        create_company_phone_no = (random.randint(1000000000, 9999999999))

        lbl_tvs_motor = tkinter.Label(final_bill, text="TVS MOTORS COMPANY PVT. LTD. ", bg="peach puff",
                                      font=('andalus', 24, 'bold', 'underline'))
        lbl_tvs_motor.grid(row=0, columnspan=5, ipady=10)
        lbl_authorised_dealer = tkinter.Label(final_bill, text="Authorised Dealer : ", bg="peach puff",
                                              font=('andalus', 16, 'bold'))
        lbl_authorised_dealer.grid(row=1, column=0)
        lbl_dealer_name = tkinter.Label(final_bill, text="HARSH MOTORS", bg="peach puff",
                                        font=('andalus', 16, 'bold'))
        lbl_dealer_name.grid(row=1, column=1)
        lbl_dealer_address = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                           text="TVS Chouraha" + "," + required_list[4] + "," + required_list[2])
        lbl_dealer_address.grid(row=2, columnspan=3, ipady=10)
        lbl_dealer_address.config(wraplength=300)
        lbl_owner_tag = tkinter.Label(final_bill, text="OWNNER NAME : ", bg="peach puff", font=('andalus', 16, 'bold'))
        lbl_owner_tag.grid(row=1, column=2)
        lbl_owner_name = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                       text=required_list[0].capitalize())
        lbl_owner_name.grid(row=1, column=3)
        lbl_address_tag = tkinter.Label(final_bill, text="Address : ", bg="peach puff", font=('andalus', 16, 'bold'))
        lbl_address_tag.grid(row=2, column=2, ipady=10)
        lbl_owner_address = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                          text=required_list[3] + "," + required_list[4] + "," + required_list[2])
        lbl_owner_address.grid(row=2, column=3, ipady=10)
        lbl_owner_address.config(wraplength=300)
        lbl_Phone_no_tag = tkinter.Label(final_bill, text="Phone : ", bg="peach puff", font=('andalus', 16, 'bold'))
        lbl_Phone_no_tag.grid(row=3, column=0)
        lbl_dealer_Phone_no = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                            text=str(create_company_phone_no))
        lbl_dealer_Phone_no.grid(row=3, column=1)
        lbl_contact_no_tag = tkinter.Label(final_bill, text="Contact No. : ", bg="peach puff",
                                           font=('andalus', 16, 'bold'))
        lbl_contact_no_tag.grid(row=3, column=2)
        lbl_owner_contact_no = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                             text=required_list[1])
        lbl_owner_contact_no.grid(row=3, column=3)
        create_separator = tkinter.Label(final_bill, text=(
            "_______________________________________________________________________________________"),
                                         bg="peach puff", font=('andalus', 16, 'bold'))
        create_separator.grid(row=4, columnspan=5)
        lbl_vechile_tag = tkinter.Label(final_bill, text="Vechile : ", bg="peach puff", font=('andalus', 16, 'bold'))
        lbl_vechile_tag.grid(row=5, column=0, ipady=10)
        lbl_owner_vechile_name = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                               text=required_list[13])
        lbl_owner_vechile_name.grid(row=5, column=1, ipady=10)
        lbl_VAT_tag = tkinter.Label(final_bill, text=('VAT 0.15% on ' + str(required_list[12]) + ' : '),
                                    bg="peach puff",
                                    font=('andalus', 16, 'bold'))
        lbl_VAT_tag.grid(row=5, column=2, ipady=10)
        lbl_owner_vechile_VAT = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                              text=required_list[11])
        lbl_owner_vechile_VAT.grid(row=5, column=3, ipady=10)
        lbl_logistic_tag = tkinter.Label(final_bill, text="Logistics Charge : ", bg="peach puff",
                                         font=('andalus', 16, 'bold'))
        lbl_logistic_tag.grid(row=6, column=0)
        lbl_owner_vechile_logistic = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                                   text=required_list[10])
        lbl_owner_vechile_logistic.grid(row=6, column=1)
        lbl_accessories_tag = tkinter.Label(final_bill, text="Accessories Charge : ", bg="peach puff",
                                            font=('andalus', 16, 'bold'))
        lbl_accessories_tag.grid(row=6, column=2)
        lbl_owner_vechile_accessories = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                                      text=required_list[9])
        lbl_owner_vechile_accessories.grid(row=6, column=3)
        lbl_insurance_tag = tkinter.Label(final_bill, text="INSURANCE :  ", bg="peach puff",
                                          font=('andalus', 16, 'bold'))
        lbl_insurance_tag.grid(row=7, column=0, ipady=10)
        lbl_owner_vechile_insurance = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                                    text=str(required_list[16]) + str(
                                                        required_list[17]) + " for 1 year")
        lbl_owner_vechile_insurance.grid(row=7, column=1, ipady=10)
        lbl_totalamount_tag = tkinter.Label(final_bill, text="Total Amount : ", bg="peach puff",
                                            font=('andalus', 16, 'bold'))
        lbl_totalamount_tag.grid(row=7, column=2, ipady=10)
        lbl_owner_vechile_totalamount = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                                      text=required_list[14])
        lbl_owner_vechile_totalamount.grid(row=7, column=3, ipady=10)
        lbl_finalamount_tag = tkinter.Label(final_bill, text="After Select offer your total amount is : ",
                                            bg="peach puff",
                                            font=('andalus', 16, 'bold'))
        lbl_finalamount_tag.grid(row=8, columnspan=2)
        lbl_owner_vechile_finalamount = tkinter.Label(final_bill, font=('andalus', 16, 'bold'), bg="peach puff",
                                                      text=str(required_list[15]))
        lbl_owner_vechile_finalamount.grid(row=8, column=2)

    def calculation(item_list):
        # item_list = detail_list
        # detail_list = [NAME, mobile_no, state, Address, City, ID, offers,
        #                pay_mode, insurance_comp, accessories, logistics,
        #                vat, vechile_prize, vechile__name, grandtotal]
        if item_list[6] == 1:
            after_offer = item_list[14] - (item_list[14] / 10)
        elif item_list[6] == 2:
            after_offer = item_list[14] - ((item_list[14] / 100) * 7)
        elif item_list[6] == 3:
            after_offer = item_list[14] - ((item_list[14] / 100) * 30)
        else:
            after_offer = item_list[14]

        if item_list[7] == 1:
            after_paymode = after_offer - (after_offer / 20)
        elif item_list[7] == 2:
            after_paymode = after_offer
        elif item_list[7] == 3:
            after_paymode = after_offer
        else:
            after_paymode = after_offer

        if item_list[8] == 1:
            insurance_amount = 3500
            final_amount = after_paymode + insurance_amount
            insurance_name = "IFFCO-TOKYO"
        elif item_list[8] == 2:
            insurance_amount = 2600
            final_amount = after_paymode + insurance_amount
            insurance_name = "ORIENTAL"
        elif item_list[8] == 3:
            insurance_amount = 2100
            final_amount = after_paymode + insurance_amount
            insurance_name = "BAJAJ Finance"
        else:
            insurance_amount = 1500
            final_amount = after_paymode + insurance_amount
            insurance_name = "L&T FINANCE"

        item_list.append(final_amount)
        item_list.append(insurance_name)
        item_list.append(insurance_amount)
        form(item_list)

    def buy_vechile_form(vechile_img, vechile_prize, vechile__name):
        def check_entries():
            NAME = name.get()
            mobile_no = contact_no.get()
            State = state_name.get()
            Address = address.get()
            City = city.get()
            ID = id_proof.get()
            offers = selected_offer.get()
            pay_mode = selected_paymode.get()
            insurance_comp = selected_insurance.get()
            _name_ = NAME.split(' ')
            if len(State) != 0:
                if mobile_no.isdigit() and len(mobile_no) == 10:
                    if City.isalpha():
                        if len(ID) != 0:
                            if offers != 0:
                                if pay_mode != 0:
                                    if insurance_comp != 0:
                                        if not Address.isspace():
                                            no = 1
                                            for i in _name_:
                                                if i.isalpha():
                                                    bk = no
                                                    no += 1
                                            if len(_name_) >= 2:
                                                if bk == len(_name_):
                                                    if pay_mode != 4:
                                                        accessories = (random.randint(400, 800))
                                                        logistics = (random.randint(500, 1500))
                                                        vat = vechile_prize * 0.15
                                                        grandtotal = accessories + logistics + vat + vechile_prize
                                                        detail_list = [NAME, mobile_no, State, Address,
                                                                       City, ID,
                                                                       offers,
                                                                       pay_mode, insurance_comp,
                                                                       accessories, logistics,
                                                                       vat, vechile_prize, vechile__name,
                                                                       grandtotal]
                                                        calculation(detail_list)
                                                    else:
                                                        messagebox.showinfo('MESSAGE',
                                                                            'Installment Mode Is Under Construction')
                                                else:
                                                    messagebox.showerror('ERROR', 'Enter Correct Name')
                                            else:
                                                messagebox.showerror('ERROR', 'Enter Full Name')
                                        else:
                                            messagebox.showerror('ERROR', 'All Field Is Required')
                                    else:
                                        messagebox.showerror('ERROR', 'Insurance Company Not Selected')
                                else:
                                    messagebox.showerror('ERROR', 'Pay Mode Not Selected')
                            else:
                                messagebox.showerror('ERROR', 'OFFER Not Selected')
                        else:
                            messagebox.showerror('ERROR', 'All Field Is Required')
                    else:
                        messagebox.showerror('ERROR', 'Enter Correct City Name')
                else:
                    messagebox.showerror('ERROR', 'Enter Correct Contact Number')
            else:
                messagebox.showerror('ERROR', 'All Field Is Required')

        def my_function(event):
            buy_canvas.configure(scrollregion=buy_canvas.bbox("all"), width=1315, height=700)

        # name, total, initial_amount, vat, accessories, logistics

        buy_form = tkinter.Toplevel(height=710, width=1130)

        buy_canvas = tkinter.Canvas(buy_form)
        buy_frame = tkinter.Frame(buy_canvas)

        buyed_vechile_img_frame = tkinter.Frame(buy_frame, bg='khaki1')
        buyed_vechile_img_frame.grid(row=0, column=0)

        buyer_details_frame = tkinter.Frame(buy_frame, bg='olivedrab1')
        buyer_details_frame.grid(row=1, column=0, pady=20)

        buy_scrollbar = tkinter.Scrollbar(buy_form, orient="vertical", command=buy_canvas.yview)
        canvas.configure(yscrollcommand=buy_scrollbar.set)

        buy_scrollbar.grid(row=0, column=1, ipady=336)
        buy_canvas.grid(row=0, column=0)
        buy_canvas.create_window((0, 0), window=buy_frame, anchor='nw')

        buy_frame.bind("<Configure>", my_function)

        name = tkinter.StringVar()
        contact_no = tkinter.StringVar()
        address = tkinter.StringVar()
        city = tkinter.StringVar()
        state_name = tkinter.StringVar()
        id_proof = tkinter.StringVar()

        selected_offer = tkinter.IntVar()
        selected_paymode = tkinter.IntVar()
        selected_insurance = tkinter.IntVar()

        global buyed_img
        buyed_img = ImageTk.PhotoImage(vechile_img)

        lbl_buyed_img = tkinter.Label(buyed_vechile_img_frame, image=buyed_img)
        lbl_buyed_img.grid(row=0, column=0, padx=410)

        lbl_option_tag = tkinter.Label(buyer_details_frame, text=" CREATE BILL  ", bg="blue", width=101, fg="white",
                                       font=("andalus", 16, 'bold'),
                                       bd=5)
        lbl_option_tag.grid(row=1, columnspan=4)

        lbl_name = tkinter.Label(buyer_details_frame, bg='olivedrab1', text="Enter Your Name  ",
                                 font=('andalus', 16, 'bold'))
        lbl_name.grid(row=2, column=0)
        entry_name = tkinter.Entry(buyer_details_frame, font=('andalus', 20, 'bold'), width=20, bd=5, textvariable=name)
        entry_name.grid(row=2, column=1)
        lbl_contact_no = tkinter.Label(buyer_details_frame, bg='olivedrab1', text="Enter Contact Number",
                                       font=('andalus', 16, 'bold'))
        lbl_contact_no.grid(row=2, column=2)
        entry_contact_no = tkinter.Entry(buyer_details_frame, font=('andalus', 20, 'bold'), width=20, bd=5,
                                         textvariable=contact_no)
        entry_contact_no.grid(row=2, column=3)
        lbl_id = tkinter.Label(buyer_details_frame, bg='olivedrab1', text="Select ID", font=('andalus', 16, 'bold'))
        lbl_id.grid(row=3, column=0)
        ids = ["Aadhar Card", "PAN Card", "Passport", "Driving License", "Voter ID"]
        select_id = ttk.Combobox(buyer_details_frame, textvariable=id_proof, font=('andalus', 20, 'bold'),
                                 state='readonly', width=20,
                                 values=ids)
        select_id.grid(row=3, column=1)
        lbl_address = tkinter.Label(buyer_details_frame, bg='olivedrab1', text="Enter Address",
                                    font=('andalus', 16, 'bold'))
        lbl_address.grid(row=3, column=2)
        entry_address = tkinter.Entry(buyer_details_frame, font=('andalus', 20, 'bold'), width=20, bd=5,
                                      textvariable=address)
        entry_address.grid(row=3, column=3)
        lbl_state = tkinter.Label(buyer_details_frame, bg='olivedrab1', text="Select state",
                                  font=('andalus', 16, 'bold'))
        lbl_state.grid(row=4, column=0)
        statename = ['Rajasthan', 'Gujarat', 'Madhya Pradesh', "Uttar Pradesh-East", "Uttar Pradesh-Central",
                     "Uttar Pradesh-west", "Tamilnadu", "Kerala", "Andhra Pradesh", 'Goa', "Pondicherry", "Assam",
                     "West Bengal", "Odisha", "Jharkhand", "Bihar", "Jammu & Kashmir", "Himachal Pradesh", "Punjab",
                     "Delhi", "Haryana", "Uttarakhand", "Chattisgarh", "Maharashtra", "Karnataka"]
        state = ttk.Combobox(buyer_details_frame, textvariable=state_name, values=statename,
                             font=('andalus', 20, 'bold'), state='readonly', height=5, width=20)
        state.grid(row=4, column=1)
        lbl_city = tkinter.Label(buyer_details_frame, bg='olivedrab1', text="Enter city ", font=("andalus", 16, 'bold'),
                                 bd=5)
        lbl_city.grid(row=4, column=2)
        entry_city = tkinter.Entry(buyer_details_frame, font=('andalus', 20, 'bold'), width=20, bd=5, textvariable=city)
        entry_city.grid(row=4, column=3)
        lbl_option_tag = tkinter.Label(buyer_details_frame, text=" Select an option ", bg="blue", width=101, fg="white",
                                       font=("andalus", 16, 'bold'),
                                       bd=5)
        lbl_option_tag.grid(row=5, columnspan=4)
        lbl_offer_1 = tkinter.Radiobutton(buyer_details_frame,
                                          text="If you are government servants given 10% off on your total amount",
                                          bg='olivedrab1', font=('andalus', 14, 'bold'), value=1,
                                          variable=selected_offer)
        lbl_offer_1.grid(row=6, column=0)
        lbl_offer_1.config(wraplength=300)
        lbl_offer_2 = tkinter.Radiobutton(buyer_details_frame,
                                          text="If you have any older vechile of TVS company then you get 7% off on your total amount",
                                          font=('andalus', 14, 'bold'), bg='olivedrab1', value=2,
                                          variable=selected_offer)
        lbl_offer_2.grid(row=6, column=1)
        lbl_offer_2.config(wraplength=300)
        lbl_offer_3 = tkinter.Radiobutton(buyer_details_frame,
                                          text="If you exchange your TVS vechile then you pay only 30% from total amount",
                                          font=('andalus', 14, 'bold'), bg='olivedrab1', value=3,
                                          variable=selected_offer)
        lbl_offer_3.grid(row=6, column=2)
        lbl_offer_3.config(wraplength=200)
        lbl_offer_4 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="None of These",
                                          font=('andalus', 14, 'bold'), value=4,
                                          variable=selected_offer)
        lbl_offer_4.grid(row=6, column=3)
        lbl_offer_4.config(wraplength=300)
        lbl_pyamode_tag = tkinter.Label(buyer_details_frame, text=" Select an Paymode Option", bg="blue", width=101,
                                        fg="white",
                                        font=("andalus", 16, 'bold'),
                                        bd=5)
        lbl_pyamode_tag.grid(row=7, columnspan=4)
        lbl_mode_1 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="Cash",
                                         font=('andalus', 16, 'bold'), value=1, variable=selected_paymode)
        lbl_mode_1.grid(row=8, column=0)
        lbl_mode_2 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="Credit card",
                                         font=('andalus', 16, 'bold'), value=2,
                                         variable=selected_paymode)
        lbl_mode_2.grid(row=8, column=1)
        lbl_mode_3 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="E-Wallet",
                                         font=('andalus', 16, 'bold'), value=3,
                                         variable=selected_paymode)
        lbl_mode_3.grid(row=8, column=2)
        lbl_mode_4 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="On Installment",
                                         font=('andalus', 16, 'bold'), value=4,
                                         variable=selected_paymode)
        lbl_mode_4.grid(row=8, column=3)
        lbl_insurance_tag = tkinter.Label(buyer_details_frame, text=" Select an Insurance ", bg="blue", width=101,
                                          fg="white",
                                          font=("andalus", 16, 'bold'),
                                          bd=5)
        lbl_insurance_tag.grid(row=10, columnspan=4)
        lbl_insurance_1 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="IFFCO-TOKYO",
                                              font=('andalus', 16, 'bold'), value=1,
                                              variable=selected_insurance)
        lbl_insurance_1.grid(row=11, column=0)
        lbl_insurance_2 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="ORIENTAL ",
                                              font=('andalus', 16, 'bold'), value=2,
                                              variable=selected_insurance)
        lbl_insurance_2.grid(row=11, column=1)
        lbl_insurance_3 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="BAJAJ FINANCE",
                                              font=('andalus', 16, 'bold'),
                                              value=3, variable=selected_insurance)
        lbl_insurance_3.grid(row=11, column=2)
        lbl_insurance_4 = tkinter.Radiobutton(buyer_details_frame, bg='olivedrab1', text="L&T FINANCE",
                                              font=('andalus', 16, 'bold'), value=4,
                                              variable=selected_insurance)
        lbl_insurance_4.grid(row=11, column=3)
        create_bill_btn = tkinter.Button(buyer_details_frame, relief='groove', bg='black', fg='white',
                                         text="Create Bill", font=("andalus", 16, 'bold'),
                                         command=check_entries)
        create_bill_btn.grid(row=12, column=2)

    def check_value():
        def scooters(scooter_frame):
            scooter_tag_lbl = tkinter.Label(scooter_frame, anchor='w', text="SCOOTERS",
                                            font=('bold', 22, 'underline'))
            scooter_tag_lbl.grid(row=0, column=0, pady=40)

            global jupiter_img
            jupiter_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Jupiter_2020.jpg')
            jupiter_opened_image = Image.open(jupiter_image_location)
            jupiter_resize_image = jupiter_opened_image.resize((500, 250))
            jupiter_img = ImageTk.PhotoImage(jupiter_resize_image)
            jupiter_text = '110 cc | 7.8 bhp | 108 Kgs\n\n' \
                           'TVS JUPITER            \n' \
                           'Ex-showroom             \n' \
                           '₹ 61,971 onwards        '
            jupiter_price = 49000
            jupiter_name = 'TVS JUPITER'
            lbl_jupiter_img = tkinter.Button(scooter_frame, image=jupiter_img, text=jupiter_text, compound='top',
                                             font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                             relief='flat', padx=20, bg='white',
                                             command=lambda: buy_vechile_form(jupiter_resize_image, jupiter_price,
                                                                              jupiter_name))
            lbl_jupiter_img.grid(row=1, column=0, padx=50)

            global ntorq_img
            Ntorq_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Ntorq_125.jpg')
            Ntorq_opened_image = Image.open(Ntorq_image_location)
            Ntorq_resize_image = Ntorq_opened_image.resize((500, 250))
            ntorq_img = ImageTk.PhotoImage(Ntorq_resize_image)
            ntorq_text = '125 cc | 9.25 bhp | 116.1 Kgs\n\n' \
                         'TVS NTORQ            \n' \
                         'Ex-showroom             \n' \
                         '₹ 73,042 onwards        '
            ntorq_price = 73042
            ntorq_name = 'TVS NTORQ'
            lbl_ntorq_img = tkinter.Button(scooter_frame, image=ntorq_img, text=ntorq_text, compound='top',
                                           font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                           relief='flat',
                                           padx=20, bg='white',
                                           command=lambda: buy_vechile_form(Ntorq_resize_image, ntorq_price,
                                                                            ntorq_name))
            lbl_ntorq_img.grid(row=1, column=1, padx=80)

            global zest_img
            zest_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Zest.jpg')
            zest_opened_image = Image.open(zest_image_location)
            zest_resize_image = zest_opened_image.resize((500, 250))
            zest_img = ImageTk.PhotoImage(zest_resize_image)
            zest_text = '110 cc | 7.9 bhp | 97 Kgs\n\n' \
                        'Zest 110            \n' \
                        'Ex-showroom             \n' \
                        '₹ 50,344 onwards        '
            zest_price = 50344
            zest_name = 'Zest 110'
            lbl_zest_img = tkinter.Button(scooter_frame, image=zest_img, text=zest_text, compound='top',
                                          font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                          relief='flat',
                                          padx=20, bg='white',
                                          command=lambda: buy_vechile_form(zest_resize_image, zest_price,
                                                                           zest_name))
            lbl_zest_img.grid(row=2, column=0)

            global pept_img
            pept_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Scooty_Pep_Plus.jpg')
            pept_opened_image = Image.open(pept_image_location)
            pept_resize_image = pept_opened_image.resize((500, 250))
            pept_img = ImageTk.PhotoImage(pept_resize_image)
            pept_text = '87.5 cc | 5.36 bhp | 93 Kgs\n\n' \
                        'Scooty Pep+            \n' \
                        'Ex-showroom             \n' \
                        '₹ 52,954 onwards        '
            pept_price = 52954
            pept_name = 'Scooty Pep+'
            lbl_pept_img = tkinter.Button(scooter_frame, image=pept_img, text=pept_text, compound='top',
                                          font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                          relief='flat',
                                          padx=20, bg='white',
                                          command=lambda: buy_vechile_form(pept_resize_image, pept_price,
                                                                           pept_name))
            lbl_pept_img.grid(row=2, column=1)

        def bikee(vechile_frame):
            bike_tag_lbl = tkinter.Label(vechile_frame, text="MOTERCYCLES", font=('bold', 22, 'underline'))
            bike_tag_lbl.grid(row=3, column=0, pady=40)

            global apache310_img
            apache310_img_image_location = os.path.abspath(
                '../tvs_project/vechile_images/TVS_Apache_RR310_2020.png')
            apache310_imgr_opened_image = Image.open(apache310_img_image_location)
            apache310_imgr_resize_image = apache310_imgr_opened_image.resize((500, 250))
            apache310_img = ImageTk.PhotoImage(apache310_imgr_resize_image)
            apache310_img_text = '312.5 cc | 33.5 bhp | 174 Kgs\n\n' \
                                 'Apache RR 310            \n' \
                                 'Ex-showroom             \n' \
                                 '₹ 2,45,000 onwards        '
            apache310_price = 245000
            apache310_name = 'Apache RR 310'
            lbl_jupiter_img = tkinter.Button(vechile_frame, image=apache310_img, text=apache310_img_text,
                                             compound='top',
                                             font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                             relief='flat', padx=20, bg='white',
                                             command=lambda: buy_vechile_form(apache310_imgr_resize_image,
                                                                              apache310_price,
                                                                              apache310_name))
            lbl_jupiter_img.grid(row=4, column=0, pady=40, padx=50)

            global apache_rtr_series_img
            apache_rtr_series_image_location = os.path.abspath(
                '../tvs_project/vechile_images/TVS_RTR_Series_2020.jpg')
            apache_rtr_series_opened_image = Image.open(apache_rtr_series_image_location)
            apache_rtr_series_resize_image = apache_rtr_series_opened_image.resize((500, 250))
            apache_rtr_series_img = ImageTk.PhotoImage(apache_rtr_series_resize_image)
            apache_rtr_series_text = '160 cc | 15 bhp | 137 Kgs\n\n' \
                                     'Apache RTR Series            \n' \
                                     'Ex-showroom             \n' \
                                     '₹ 97,000 onwards        '
            apache_rtr_series_price = 97000
            apache_rtr_name = 'Apache RTR Series'
            lbl_ntorq_img = tkinter.Button(vechile_frame, image=apache_rtr_series_img, text=apache_rtr_series_text,
                                           compound='top',
                                           font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                           relief='flat',
                                           padx=20, bg='white',
                                           command=lambda: buy_vechile_form(apache_rtr_series_resize_image,
                                                                            apache_rtr_series_price,
                                                                            apache_rtr_name))
            lbl_ntorq_img.grid(row=4, column=1, padx=80)

            global radeon_img
            radeon_img_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Radeon_2020.png')
            radeon_img_opened_image = Image.open(radeon_img_image_location)
            radeon_img_resize_image = radeon_img_opened_image.resize((500, 250))
            radeon_img = ImageTk.PhotoImage(radeon_img_resize_image)
            radeon_img_text = '110 cc | 8.08 bhp | 116 Kgs\n\n' \
                              'TVS Raedon            \n' \
                              'Ex-showroom             \n' \
                              '₹ 59,742 onwards        '
            radeon_price = 59742
            radeon_name = 'TVS Raedon'
            lbl_zest_img = tkinter.Button(vechile_frame, image=radeon_img, text=radeon_img_text, compound='top',
                                          font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                          relief='flat',
                                          padx=20, bg='white',
                                          command=lambda: buy_vechile_form(radeon_img_resize_image,
                                                                           radeon_price,
                                                                           radeon_name))
            lbl_zest_img.grid(row=5, column=0)

            global sport_img
            sport_img_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Sport_2020.jpg')
            sport_img_opened_image = Image.open(sport_img_image_location)
            sport_img_resize_image = sport_img_opened_image.resize((500, 250))
            sport_img = ImageTk.PhotoImage(sport_img_resize_image)
            sport_text = '109.7 cc | 8.18 bhp | 110 Kgs\n\n' \
                         'TVS Sport            \n' \
                         'Ex-showroom             \n' \
                         '₹ 44,425 onwards        '
            sport_price = 44425
            sport_name = 'TVS Sport'
            lbl_pept_img = tkinter.Button(vechile_frame, image=sport_img, text=sport_text, compound='top',
                                          font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                          relief='flat',
                                          padx=20, bg='white',
                                          command=lambda: buy_vechile_form(sport_img_resize_image,
                                                                           sport_price,
                                                                           sport_name))
            lbl_pept_img.grid(row=5, column=1)

            global victor_img
            victor_img_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_Victor.jpg')
            victor_img_opened_image = Image.open(victor_img_image_location)
            victor_img_resize_image = victor_img_opened_image.resize((500, 250))
            victor_img = ImageTk.PhotoImage(victor_img_resize_image)
            victor_text = '110 cc | 9.46 bhp | 112 Kgs\n\n' \
                          'TVS Victor            \n' \
                          'Ex-showroom             \n' \
                          '₹ 55,757 onwards        '
            victor_price = 55757
            victor_name = 'TVS Victor'
            lbl_zest_img = tkinter.Button(vechile_frame, image=victor_img, text=victor_text, compound='top',
                                          font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                          relief='flat',
                                          padx=20, bg='white',
                                          command=lambda: buy_vechile_form(victor_img_resize_image,
                                                                           victor_price,
                                                                           victor_name))
            lbl_zest_img.grid(row=6, column=0)

            global starcity_img
            starcity_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_StarCity_2020.jpg')
            starcity_opened_image = Image.open(starcity_image_location)
            starcity_resize_image = starcity_opened_image.resize((500, 250))
            starcity_img = ImageTk.PhotoImage(starcity_resize_image)
            starcity_text = '110 cc | 8.08 bhp | 116 Kgs\n\n' \
                            'TVS Star City +            \n' \
                            'Ex-showroom             \n' \
                            '₹ 61,988 onwards        '
            starcity_price = 61988
            starcity_name = 'TVS Star City +'
            lbl_starcity_img = tkinter.Button(vechile_frame, image=starcity_img, text=starcity_text, compound='top',
                                              font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                              relief='flat',
                                              padx=20, bg='white',
                                              command=lambda: buy_vechile_form(starcity_resize_image,
                                                                               starcity_price,
                                                                               starcity_name))
            lbl_starcity_img.grid(row=6, column=1)

        def mopeed(vechile_frame):
            moped_tag_lbl = tkinter.Label(vechile_frame, text="MOPEDS", font=('bold', 22, 'underline'))
            moped_tag_lbl.grid(row=7, column=0, pady=40)
            global xl_img
            xl_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_XL_2020.png')
            xl_img_opened_image = Image.open(xl_image_location)
            xl_img_resize_image = xl_img_opened_image.resize((500, 250))
            xl_img = ImageTk.PhotoImage(xl_img_resize_image)
            xl_text = '99.7 cc | 4.3 bhp | 89 Kgs\n\n' \
                      'TVS XL100            \n' \
                      'Ex-showroom             \n' \
                      '₹ 29,990 onwards        '
            xl_price = 29990
            xl_name = 'TVS XL100'
            lbl_xl_img = tkinter.Button(vechile_frame, image=xl_img, text=xl_text,
                                        compound='top',
                                        font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                        relief='flat', padx=20, bg='white',
                                        command=lambda: buy_vechile_form(xl_img_resize_image,
                                                                         xl_price,
                                                                         xl_name))
            lbl_xl_img.grid(row=8, column=0, pady=40, padx=50)

        def electriic(electriic_frame):
            electric_tag_lbl = tkinter.Label(electriic_frame, text="ELECTRIC", font=('bold', 22, 'underline'))
            electric_tag_lbl.grid(row=9, column=0, pady=40)

            global iqube_img
            iqube_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_IQUBE.jpg')
            iqube_opened_image = Image.open(iqube_image_location)
            iqube_resize_image = iqube_opened_image.resize((500, 250))
            iqube_img = ImageTk.PhotoImage(iqube_resize_image)
            iqube_text = '75 km | 2.25 KWH | 78 km/h \n\n' \
                         'TVS iQube            \n' \
                         'Ex-showroom             \n' \
                         '₹ 1,15,000 onwards        '
            iqube_price = 115000
            iqube_name = 'TVS iQube'
            lbl_iqube_img = tkinter.Button(electriic_frame, image=iqube_img, text=iqube_text,
                                           compound='top',
                                           font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                           relief='flat',
                                           padx=20, bg='white',
                                           command=lambda: buy_vechile_form(iqube_resize_image,
                                                                            iqube_price,
                                                                            iqube_name))
            lbl_iqube_img.grid(row=10, column=0, padx=80)

        def three_wheelerr(vechile_frame):
            three_wheeler_tag_lbl = tkinter.Label(vechile_frame, text="Three Wheelers",
                                                  font=('bold', 22, 'underline'))
            three_wheeler_tag_lbl.grid(row=11, column=0, pady=40)
            global king_img
            king_image_location = os.path.abspath('../tvs_project/vechile_images/TVS_King.jpg')
            king_opened_image = Image.open(king_image_location)
            king_resize_image = king_opened_image.resize((500, 250))
            king_img = ImageTk.PhotoImage(king_resize_image)
            king_text = '199 cc | 6 bhp | 360 Kgs\n\n' \
                        'TVS King            \n' \
                        'Ex-showroom             \n' \
                        '₹ 1,35,150 onwards        '
            king_price = 135150
            king_name = 'TVS King'
            lbl_king_img = tkinter.Button(vechile_frame, image=king_img, text=king_text, compound='top',
                                          font=('andalus', 18, 'bold'), bd=0, activebackground='white',
                                          relief='flat',
                                          padx=20, bg='white',
                                          command=lambda: buy_vechile_form(king_resize_image,
                                                                           king_price,
                                                                           king_name))
            lbl_king_img.grid(row=12, column=0)

        all_vechile_val = all_vechile.get()
        scooter_val = scooter.get()
        bike_val = bike.get()
        moped_val = moped.get()
        electric_val = electric.get()
        three_wheeler_val = three_wheeler.get()

        if all_vechile_val == 'on':
            scooter.set('on')
            bike.set('on')
            moped.set('on')
            electric.set('on')
            three_wheeler.set('on')

            scooter_val = 'on'
            bike_val = 'on'
            moped_val = 'on'
            electric_val = 'on'
            three_wheeler_val = 'on'

            if scooter_val == 'on':
                scooter.set('on')
                scoot_frame.grid(row=0, column=0)
                scooters(scoot_frame)
            elif scooter_val == 'off':
                scooter.set('off')
                scoot_frame.grid_forget()
            if bike_val == 'on':
                bike.set('on')
                bik_frame.grid(row=1, column=0)
                bikee(bik_frame)
            elif bike_val == 'off':
                bike.set('off')
                bik_frame.grid_forget()
            if moped_val == 'on':
                moped.set('on')
                moped_frame.grid(row=2, column=0)
                mopeed(moped_frame)
            elif moped_val == 'off':
                moped.set('off')
                moped_frame.grid_forget()
            if electric_val == 'on':
                electric.set('on')
                electric_frame.grid(row=3, column=0)
                electriic(electric_frame)
            elif electric_val == 'off':
                electric.set('off')
                electric_frame.grid_forget()
            if three_wheeler_val == 'on':
                three_wheeler.set('on')
                three_wheeler_frame.grid(row=4, column=0)
                three_wheelerr(three_wheeler_frame)
            elif three_wheeler_val == 'off':
                three_wheeler.set('off')
                three_wheeler_frame.grid_forget()

        elif all_vechile_val == 'off':
            scooter.set('off')
            bike.set('off')
            moped.set('off')
            electric.set('off')
            three_wheeler.set('off')

        if scooter_val == 'on':
            scooter.set('on')
            scoot_frame.grid(row=0, column=0)
            scooters(scoot_frame)
        elif scooter_val == 'off':
            scooter.set('off')
            scoot_frame.grid_forget()
        if bike_val == 'on':
            bike.set('on')
            bik_frame.grid(row=1, column=0)
            bikee(bik_frame)
        elif bike_val == 'off':
            bike.set('off')
            bik_frame.grid_forget()
        if moped_val == 'on':
            moped.set('on')
            moped_frame.grid(row=2, column=0)
            mopeed(moped_frame)
        elif moped_val == 'off':
            moped.set('off')
            moped_frame.grid_forget()
        if electric_val == 'on':
            electric.set('on')
            electric_frame.grid(row=3, column=0)
            electriic(electric_frame)
        elif electric_val == 'off':
            electric.set('off')
            electric_frame.grid_forget()
        if three_wheeler_val == 'on':
            three_wheeler.set('on')
            three_wheeler_frame.grid(row=4, column=0)
            three_wheelerr(three_wheeler_frame)
        elif three_wheeler_val == 'off':
            three_wheeler.set('off')
            three_wheeler_frame.grid_forget()

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=1320, height=400)

    import os
    import tkinter
    from tkinter import ttk
    from tkinter import messagebox
    from PIL import ImageTk, Image
    import random

    canvas = tkinter.Canvas(result_frame, bg='white')
    frame = tkinter.Frame(canvas, bg='white')

    check_box_frame = tkinter.Frame(frame, bg='white')
    check_box_frame.grid(row=0, column=0)
    picture_frame = tkinter.Frame(frame)
    picture_frame.grid(row=1, column=0)

    scoot_frame = tkinter.Frame(picture_frame)
    scoot_frame.grid(row=0, column=0)

    bik_frame = tkinter.Frame(picture_frame)
    bik_frame.grid(row=1, column=0)

    moped_frame = tkinter.Frame(picture_frame)
    moped_frame.grid(row=2, column=0)

    electric_frame = tkinter.Frame(picture_frame)
    electric_frame.grid(row=3, column=0)

    three_wheeler_frame = tkinter.Frame(picture_frame)
    three_wheeler_frame.grid(row=4, column=0)

    myscrollbar = tkinter.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.grid(row=0, column=1, ipady=176)
    canvas.grid(row=0, column=0)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    frame.bind("<Configure>", myfunction)

    all_vechile = tkinter.StringVar()
    scooter = tkinter.StringVar()
    bike = tkinter.StringVar()
    moped = tkinter.StringVar()
    electric = tkinter.StringVar()
    three_wheeler = tkinter.StringVar()

    all_vechile.set('off')
    scooter.set('off')
    bike.set('off')
    moped.set('off')
    electric.set('off')
    three_wheeler.set('off')

    check_1 = tkinter.Checkbutton(check_box_frame, text='ALL VECHILE', bg='white', font=("calibri", 14, 'bold'),
                                  variable=all_vechile, onvalue='on', offvalue='off', command=check_value)
    check_1.grid(row=0, column=0, padx=40)
    check_2 = tkinter.Checkbutton(check_box_frame, text='SCOOTERS', bg='white', font=("calibri", 14, 'bold'),
                                  variable=scooter, onvalue='on', offvalue='off', command=check_value)
    check_2.grid(row=0, column=1, padx=40)
    check_3 = tkinter.Checkbutton(check_box_frame, text='MOTERCYCLES', bg='white', font=("calibri", 14, 'bold'),
                                  variable=bike, onvalue='on', offvalue='off', command=check_value)
    check_3.grid(row=0, column=2, padx=40)
    check_4 = tkinter.Checkbutton(check_box_frame, text='MOPEDS', bg='white', font=("calibri", 14, 'bold'),
                                  variable=moped, onvalue='on', offvalue='off', command=check_value)
    check_4.grid(row=0, column=3, padx=40)
    check_5 = tkinter.Checkbutton(check_box_frame, text='ELECTRIC', bg='white', font=("calibri", 14, 'bold'),
                                  variable=electric, onvalue='on', offvalue='off', command=check_value)
    check_5.grid(row=0, column=4, padx=40)
    check_6 = tkinter.Checkbutton(check_box_frame, text='THREE WHEELERS', bg='white', font=("calibri", 14, 'bold'),
                                  variable=three_wheeler, onvalue='on', offvalue='off', command=check_value)
    check_6.grid(row=0, column=5, padx=40)


if __name__ == '__main__':
    import layout

    frame1 = layout.output_frame
    vechile(frame1)
