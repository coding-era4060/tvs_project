def near_dealer(result_frame):
    def show_rto():
        def crash():
            try:
                up_frame.grid_forget()
            finally:
                button.grid_forget()
                show_address.grid_forget()
                show_rto()

        show_address = tkinter.Frame(result_frame)
        state_code = rto_code.get()
        show_address.grid(row=1, columnspan=4, pady=30)
        if state_code == 'rajasthan' or state_code == "RAJASTHAN" or state_code == 'Rajasthan' or state_code == 'rj' or state_code == 'RJ' or state_code == "Rj":
            rajasthan_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'), text=(
                "Plot No. 16-17,\n  Top floor of National Motors,\n  Jhotwara industrial Area,\n  Jaipur-302 012.\n  Phone: 0141-5150900/5150901\n  Email:AO.Jaipur@tvsmotor.com"))
            rajasthan_add_1.grid(row=0, column=0)

            rajasthan_add_2 = tkinter.Label(show_address,
                                            text="204,2nd floor,\n  Daulet Chamber,4-D,\n  Sardarpura,Udaipur-313 004.\n  Phone:9001897485\n  E-mail:AO.Udaipur@tvsmotor.com",
                                            font=('andalus', 16, 'bold'))
            rajasthan_add_2.grid(row=0, column=1)

        elif state_code == 'Gujarat' or state_code == 'GUJARAT' or state_code == 'Gj' or state_code == 'gujarat' or state_code == 'GJ' or state_code == 'gj':
            gujarat_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                          text="\n109,Ayana Complex,\nOpp.Suvarna Villa Bungalows,\n100ft Thaltej Hebatpur,Thatlej,\nAhemdabad-380 054.\nPhone: 079-65443748 \nEmail:AO.Ahemdabad@tvsmotor.com")
            gujarat_add_1.grid(row=0, column=1)

        elif state_code == 'Madhya Pradesh' or state_code == 'MADHYA PRADESH' or state_code == 'Mp' or state_code == 'madhya pradesh' or state_code == 'mp' or state_code == 'MP':
            mp_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                     text="\n301,3rd floor,\nShagun Arcade,Vijay Nagar,\nIndore-452 010.\nPhone: 9826388896\nEmail:AO.Indore@tvsmotor.com")
            mp_add_1.grid(row=0, column=1)

        elif state_code == 'Uttar Pradesh' or state_code == 'UTTAR PRADESH' or state_code == 'Up' or state_code == 'uttar pradesh' or state_code == 'up' or state_code == 'UP':
            def up():
                def up_crush():
                    radio_button_crash.grid_forget()
                    up_frame.grid_forget()
                    up()

                region = state_region.get()
                global up_frame
                up_frame = tkinter.Frame(result_frame)
                up_frame.grid(row=2, columnspan=4, pady=30)
                show_address.grid(row=1, columnspan=4, pady=30)
                if region == 'east':
                    up_east_add_1 = tkinter.Label(up_frame, font=("andalus", 16, 'bold'), text=(
                        "\n1st floor,Cyber Tower,TC-34/V-2,\nVibhuti Khand,Gomti Nagar,\nLucknow-226 010.\nPhone: 0522-4918300\nEmail:AO.Upe@tvsmotor.com"))
                    up_east_add_1.grid(row=1, column=1)
                elif region == 'central':
                    up_central_add_1 = tkinter.Label(up_frame, font=("andalus", 16, 'bold'), text=(
                        "\n1st floor,Cyber Tower,TC-34/V-2,\nVibhuti Khand,Gomti Nagar,\nLucknow-226 010.\nPhone: 0522-4918300\nAO.Upc@tvsmotor.com"))
                    up_central_add_1.grid(row=1, column=1)
                else:
                    up_west_add_1 = tkinter.Label(up_frame, font=("andalus", 16, 'bold'), text=(
                        "\nK-23,1st floor,Lajpat Nagar,Part|| ,\nNew Delhi-110 024.\nPhone:011-29834773/29834640\nAO.Upw@tvsmotor.com"))
                    up_west_add_1.grid(row=1, column=1)
                radio_button_crash = tkinter.Button(show_address, text='click me', relief='groove',
                                                    font=('andalus', 16, 'bold'),
                                                    command=up_crush)
                radio_button_crash.grid(row=0, column=3, padx=30)

            state_region = tkinter.StringVar()
            lb_up_east = tkinter.Radiobutton(show_address, text="Uttar Pradesh-East", font=("andalus", 16, 'bold'),
                                             value='east', variable=state_region)
            lb_up_east.grid(row=0, column=0)
            lb_up_central = tkinter.Radiobutton(show_address, text="Uttar Pradesh-Central",
                                                font=('andalus', 16, 'bold'), value='central', variable=state_region)
            lb_up_central.grid(row=0, column=1)
            lb_up_west = tkinter.Radiobutton(show_address, text="Uttar Pradesh-west", font=("andalus", 16, 'bold'),
                                             value='west', variable=state_region)
            lb_up_west.grid(row=0, column=2)
            radio_button = tkinter.Button(show_address, text='click me', relief='groove', font=('andalus', 16, 'bold'),
                                          command=up)
            radio_button.grid(row=0, column=3, padx=30)

        elif state_code == "Tamilnadu" or state_code == 'TAMILNADU' or state_code == 'Tn' or state_code == 'tamilnadu' or state_code == 'TN' or state_code == 'tn':
            tamilnadu_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                            text="\nSPL-sriram nivas,1st floor,\nNo.38,venkatakrishna road,\nMandaveli,chennai-600 028.\nphone:044-24951652/24950018\nE-mail:AO.Chennai@tvsmotor.com")
            tamilnadu_add_1.grid(row=0, column=1)

        elif state_code == "Kerala" or state_code == 'KERELA' or state_code == 'Kr' or state_code == 'kerela' or state_code == 'KR' or state_code == 'kr':
            kerela_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                         text="\nAmbady tower,second floor,\ndoor no.27/631,A6,\nedappally-pookkattupady road,\nedappally PO.,Cochin-682 024.\nPhone:0484-2544578/2556938\nEmail:AO.Cochin@tvsmotor.com")
            kerela_add_1.grid(row=0, column=1)

        elif state_code == "Andhra Aradesh" or state_code == 'ANDHRA PRADESH' or state_code == 'Ap' or state_code == 'andhra pradesh' or state_code == 'AP' or state_code == 'ap':
            ap_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                     text="\nD-19,302-3rd floor,gayanthri arcade,\nvikrampuri,secunderabad-500 003.\nPhone:040-27840590/27844419\nEmail:AO.Hyerabad@tvsmotor.com")
            ap_add_1.grid(row=0, column=1)

        elif state_code == "Karnataka" or state_code == 'KARNATAKA' or state_code == 'Ka' or state_code == 'karnataka' or state_code == 'KA' or state_code == 'ka':
            karnataka_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                            text="\nBDP PLaza,3rd floor,new cotton market,\nkarnataka bank road,Hubli-580 029.\nPhone:0836-4250617\4250618\nE-mail:AO.Hubli@tvsmotor.com")
            karnataka_add_1.grid(row=0, column=1)

        elif state_code == "Maharashtra" or state_code == 'MAHARASHTRA' or state_code == 'Mh' or state_code == 'maharashtra' or state_code == 'MH' or state_code == 'mh':
            maharashtra_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                              text="\nJiwani Mansion,GATNo:2347/B/2/3,\nOpp.Talera warehouse,\nPune Nagar Road,\nWagoli-Taluka Haveli,Pune-412 207.\nPhone:020-66204375/66204377\nE-mail:Service.Pune@tvsmotor.com")
            maharashtra_add_1.grid(row=0, column=1)

        elif state_code == "Chattisgarh" or state_code == 'CHATTISGARH' or state_code == 'Cg' or state_code == 'chattisgarh' or state_code == 'CG' or state_code == 'cg':
            chattisgarh_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                              text="\nMagneto the Mall,Offizo 6th floor,\noffice No.627-628,Labhandi,\nGE Road,Raipur-492 010.\nPhone:0771-4260006\nE-mail:AO.Raipur@tvsmotor.com")
            chattisgarh_add_1.grid(row=0, column=1)

        elif state_code == "Uttarakhand" or state_code == 'UTTARAKHAND' or state_code == 'Uk' or state_code == 'uttarakhand' or state_code == 'uk' or state_code == 'UK':
            uttarakhand_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                              text="\nK-23,1st floor,Lajpat Nagar,Part|| ,\nNew Delhi-110 024.\nPhone:011-29834773/29834640\nE-mail:AO.Upw@tvsmotor.com")
            uttarakhand_add_1.grid(row=0, column=1)

        elif state_code == "Haryana" or state_code == 'HARYANA' or state_code == 'Hr' or state_code == 'haryana' or state_code == 'hr' or state_code == 'HR':
            haryana_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                          text="\nK-23,1st floor,Lajpat Nagar,Part|| ,\nNew Delhi-110 024.\nPhone:011-29834773/29834640\nAO.Haryana@tvsmotor.com")
            haryana_add_1.grid(row=0, column=1)

        elif state_code == "Delhi" or state_code == 'DELHI' or state_code == 'Dl' or state_code == 'delhi' or state_code == 'dl' or state_code == 'DL':
            delhi_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                        text="\nK-23,1st floor,Lajpat Nagar,Part|| ,\nNew Delhi-110 024.\nPhone:011-29834773/29834640\nE-mail:AO.Delhi@tvsmotor.com\n")
            delhi_add_1.grid(row=0, column=1)

        elif state_code == "Punjab" or state_code == 'PUNJAB' or state_code == 'Pb' or state_code == 'punjab' or state_code == 'pb' or state_code == 'PB':
            punjab_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                         text="\nSCF-10-11,Kalghaidhar Enclave,\nBaltana Road,Zirakpur,\nDistrict Mohali-140 603.\nPhone:07162-653477/653480\nE-mail:AO.Chandigarh@tvsmotor.com")
            punjab_add_1.grid(row=0, column=1)

        elif state_code == "Himachal Pradesh" or state_code == 'HIMACHAL PRADESH' or state_code == 'Hp' or state_code == 'himachal pradesh' or state_code == 'HP' or state_code == 'hp':
            hp_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                     text="\nSCF-10-11,Kalghaidhar Enclave,\nBaltana Road,Zirakpur,\nDistrict Mohali-140 603.\nPhone:07162-653477/653480\nE-mail:AO.Chandigarh@tvsmotor.com")
            hp_add_1.grid(row=0, column=1)

        elif (
                state_code == "Jammu & Kashmir" or state_code == 'JAMMU & KASHMIR' or state_code == 'jammu & kashmir' or state_code == 'Jk' or state_code == 'jk' or state_code == 'JK'
                or state_code == "kashmir" or state_code == "Kashmir" or state_code == "KASHMIR" or state_code == "JAMMU" or state_code == "jammu" or state_code == "Jammu"):
            jk_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                     text="\nSCF-10-11,Kalghaidhar Enclave,\nBaltana Road,Zirakpur,\nDistrict Mohali-140 603.\nPhone:07162-653477/653480\nE-mail:AO.Chandigarh@tvsmotor.com")
            jk_add_1.grid(row=0, column=1)

        elif state_code == "Bihar" or state_code == 'BIHAR' or state_code == 'Br' or state_code == 'bihar' or state_code == 'BR' or state_code == 'br':
            bihar_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                        text="\nN-Plaza,Jamal Road,\nP.S. Kotwali,Patna-800 001.\nPhone:0612-2200068/2200069\nE-mail:AO.BNJ@tvsmotor.com")
            bihar_add_1.grid(row=0, column=1)

        elif state_code == "Jharkhand" or state_code == 'JHARKHAND' or state_code == 'Jh' or state_code == 'jharkhand' or state_code == 'JH' or state_code == 'jh':
            jharkhand_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                            text="\n2nd floor,Lucas Building,\nArgora BypassRoad,\nRanchi-834 002.\nPhone:0651-2244715\nE-mail:AO.Ranchi@tvsmotor.com")
            jharkhand_add_1.grid(row=0, column=1)

        elif state_code == "Odisha" or state_code == 'ODISHA' or state_code == 'Od' or state_code == 'odisha' or state_code == 'od' or state_code == 'OD':
            odisha_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                         text="\n#303,3rd floor,\nCreative Plaza,Rasulgarh,\nBhubaneshwar-751 010.\nPhone:0674-2580018/2580019\nE-mail:AO.Bhubaneshwar@tvsmotor.com")
            odisha_add_1.grid(row=0, column=1)

        elif state_code == "West Bengal" or state_code == 'WEST BENGAL' or state_code == 'Wb' or state_code == 'west bengal' or state_code == 'WB' or state_code == 'wb' or state_code == "Kolkata" or state_code == "kolkata":
            wb_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                     text="\n9/2,Dover lane,Ground floor,\nGariahat,kolkata-700 029.\nPhone:033-24617092/24617096\nE-mail:AO.kolkata@tvsmotor.com")
            wb_add_1.grid(row=0, column=1)

        elif state_code == "Assam" or state_code == 'ASSAM' or state_code == 'As' or state_code == 'assam' or state_code == 'AS' or state_code == 'as':
            assam_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                        text="\n147,Udayan,Ganesh Guri,\nOpp.Punjab National Bank,\nR G B.Road,\nGuwahati-781 005.\nPhone:0361-2202030/2202031\nE-mail:AO.Guwahati@tvsmotor.com")
            assam_add_1.grid(row=0, column=1)

        elif state_code == "Pondicherry" or state_code == 'PONDICHERRY' or state_code == 'Py' or state_code == 'pondicherry' or state_code == 'PY' or state_code == 'py':
            pondicherry_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                              text="\nSPL-sriram nivas,1st floor,\nNo.38,venkatakrishna road,\nMandaveli,chennai-600 028.\nphone:044-24951652/24950018\nE-mail:AO.Chennai@tvsmotor.com")
            pondicherry_add_1.grid(row=0, column=1)

        elif state_code == "goa" or state_code == 'GOA' or state_code == 'Ga' or state_code == 'Goa' or state_code == 'GA' or state_code == 'ga':
            goa_add_1 = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                      text="\nBDP PLaza,3rd floor,new cotton market,\nkarnataka bank road,Hubli-580 029.\nPhone:0836-4250617\4250618\nE-mail:AO.Hubli@tvsmotor.com")
            goa_add_1.grid(row=0, column=1)
        elif (
                state_code == "Lakshadweep" or state_code == "LAKSHADWEEP" or state_code == "Ld" or state_code == "lakshadweep" or state_code == "LD" or state_code == "ld" or state_code == "Daman & Diu" or state_code == "daman & diu"
                or state_code == "DAMAN & DIU" or state_code == "Dd " or state_code == "DD" or state_code == "dd" or state_code == "Andman & Nicobar" or state_code == "andman & nicobar" or state_code == "AN" or state_code == "an"
                or state_code == "ANDMAN & NICOBAR" or state_code == "An" or state_code == "Telangana" or state_code == "telangana" or state_code == "TELANGANA" or state_code == "Ts" or state_code == "TS" or state_code == "ts"
                or state_code == "Tripura" or state_code == "tripura" or state_code == "TRIPURA" or state_code == "Tr" or state_code == "TR" or state_code == "tr" or state_code == "Sikkim" or state_code == "sikkim" or state_code == "SK"
                or state_code == "SIKKIM" or state_code == "Sk" or state_code == "sk" or state_code == "Nagaland" or state_code == "NAGALAND" or state_code == "Nl" or state_code == "nagaland" or state_code == "NL" or state_code == "nl"
                or state_code == "Mizoram" or state_code == "mizoram" or state_code == "MIZORAM" or state_code == "Mz" or state_code == "MZ" or state_code == "mz" or state_code == "Meghalaya" or state_code == "meghalaya"
                or state_code == "MEGHALAYA" or state_code == "Ml" or state_code == "ML" or state_code == "ml" or state_code == "Manipur" or state_code == "manipur" or state_code == "MN" or state_code == "MANIPUR" or state_code == "Mn"
                or state_code == "mn" or state_code == "Arunachal Pradesh" or state_code == "arunachal pradesh" or state_code == "AR" or state_code == "ARUNACHAL PRADESH" or state_code == "Ar" or state_code == "ar"):
            not_available = tkinter.Label(show_address, font=("andalus", 16, 'bold'),
                                          text="\nSorry!!!There is no Area office in this region")
            not_available.grid(row=0, column=1)

        button = tkinter.Button(result_frame, text='Search', relief='groove', font=('andalus', 16, 'bold'),
                                command=crash)
        button.grid(row=0, column=2, padx=30)

    import tkinter

    rto_code = tkinter.StringVar()
    rto_code.set('Enter State name or rto code')

    search_state = tkinter.Label(result_frame, text='Search State', font=('andalus', 16, 'bold'))
    search_state.grid(row=0, column=0)

    search_state_box = tkinter.Entry(result_frame, textvariable=rto_code, width=30, font=('andalus', 16, 'bold'))
    search_state_box.grid(row=0, column=1, padx=30)

    search_Button = tkinter.Button(result_frame, text='Search', relief='groove', font=('andalus', 16, 'bold'),
                                   command=show_rto)
    search_Button.grid(row=0, column=2, padx=30)


if __name__ == '__main__':
    import layout

    frame = layout.output_frame
    near_dealer(frame)
