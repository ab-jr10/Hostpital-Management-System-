import random
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from datetime import datetime





class Registration:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "black")



        # Taking live date time using datetime module ####

        Date_of_registration = StringVar()
        current_date = datetime.now()
        Date_of_registration.set(current_date.strftime("%d/%m/%Y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pin_code = StringVar()
        Address = StringVar()
        First_name = StringVar()
        Middle_name = StringVar()
        Last_name = StringVar()

        #### var1, 2, 3, 4, 5 for combobox ####
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()         # to keep numerical value


        Membership = StringVar()
        Membership.set("0")     # or when membership checkbox is unclicked or reset has been done it will automatically set as 0





        ###############  TITLE  #################

        title = Label(self.root, text="Member Registration Form", font=("Lucida Sans Unicode", 30, "bold"), bd=5, relief=GROOVE, bg="#FF8B33", fg="#000000")
        title.pack(side= TOP, fill = X)


        ###########  member frame  ###############

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#CCCCFF")
        Manage_Frame.place(x= 20, y= 100, width= 450, height= 630)




        ################ text, label, comboboxes in manage frame  ############

        Cus_title = Label(Manage_Frame, text="Customer Detail", font=("arial", 20, "bold"), bg="#CCCCFF", fg="black")
        Cus_title.grid(row= 0, columnspan= 2, pady= 5)



        member_datelbl = Label(Manage_Frame, text= "Date", font= ("arial",15, "bold"), bg= "#CCCCFF", fg= "black")
        member_datelbl.grid(row= 1, column= 0, pady= 5, padx= 10, sticky= "w")

        member_datetxt = Entry(Manage_Frame, font= ("arial", 15, "bold"), textvariable= Date_of_registration)
        member_datetxt.grid(row= 1, column= 1, pady= 5, padx= 10, sticky= "w")

        

        member_reflbl = Label(Manage_Frame, text= "Reference ID", font= ("arial",15,"bold"), bg= "#CCCCFF", fg= "black")
        member_reflbl.grid(row= 2, column= 0, pady= 5, padx= 10, sticky="w")

        member_reftxt = Entry(Manage_Frame, font=("arial", 15, "bold"), text= Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")



        member_fname_lbl = Label(Manage_Frame, text="First Name", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_fname_lbl.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fname_txt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=First_name)
        member_fname_txt.grid(row=3, column=1, pady=5, padx=10, sticky="w")



        member_lname_lbl = Label(Manage_Frame, text="Last Name", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_lname_lbl.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lname_txt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable= Last_name)
        member_lname_txt.grid(row=4, column=1, pady=5, padx=10, sticky="w")



        member_mobile_lbl = Label(Manage_Frame, text="Mobile No.", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_mobile_lbl.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobile_txt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable= Mobile_no)
        member_mobile_txt.grid(row=5, column=1, pady=5, padx=10, sticky="w")



        member_address_lbl = Label(Manage_Frame, text="Address", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_address_lbl.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_address_txt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable= Address)
        member_address_txt.grid(row=6, column=1, pady=5, padx=10, sticky="w")



        member_Pincode_lbl = Label(Manage_Frame, text="Pin Code", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_Pincode_lbl.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_Pincode_txt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable= Pin_code)
        member_Pincode_txt.grid(row=7, column=1, pady=5, padx=10, sticky="w")



        member_gender_lbl = Label(Manage_Frame, text="Gender", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_gender_lbl.grid(row=8, column=0, pady=5, padx=10, sticky="w")

        member_gender_cmb = ttk.Combobox(Manage_Frame, text = var4, state= "randomly", font= ("arial", 15, "bold"), width= 19)
        member_gender_cmb['values'] = ("","Male","Female","Other")
        member_gender_cmb.current(0)        # when nothing it will be set as empty which we have given at index 0
        member_gender_cmb.grid(row= 8, column= 1, pady= 5, padx= 10, sticky= "w")



        member_id_proof_lbl = Label(Manage_Frame, text="Id Proof", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_id_proof_lbl.grid(row=9, column=0, pady=5, padx=10, sticky="w")

        member_id_proof_cmb = ttk.Combobox(Manage_Frame, text = var3, state= "randomly", font= ("arial", 15, "bold"), width= 19)
        member_id_proof_cmb['values'] = ("","Adhaar Card","Passport","Driving license", "Pan Card", "Student Id")
        member_id_proof_cmb.current(0)               # when nothing it will be set as empty which we have given at index 0
        member_id_proof_cmb.grid(row= 9, column= 1, pady= 5, padx= 10, sticky= "w")



        member_mem_type_lbl = Label(Manage_Frame, text="Member Type", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_mem_type_lbl.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        member_mem_type_cmb = ttk.Combobox(Manage_Frame, text = var2, state= "randomly", font= ("arial", 15, "bold"), width= 19)
        member_mem_type_cmb['values'] = ("","Ayushman Card", "Insurance", "Pay Immediately", "Pay when leaving")
        member_mem_type_cmb.current(0)              # when nothing it will be set as empty which we have given at index 0
        member_mem_type_cmb.grid(row= 10, column= 1, pady= 5, padx= 10, sticky= "w")



        member_payment_with_lbl = Label(Manage_Frame, text="Gender", font=("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_payment_with_lbl.grid(row=11, column=0, pady=5, padx=10, sticky="w")

        member_payment_with_cmb = ttk.Combobox(Manage_Frame, text=var1, state="randomly", font=("arial", 15, "bold"), width=19)
        member_payment_with_cmb['values'] = ("", "Cash", "Debit Card", "Credit Card", "Phonepe", "Paytm", "GooglePay")
        member_payment_with_cmb.current(0)           # when nothing it will be set as empty which we have given at index 0
        member_payment_with_cmb.grid(row=11, column=1, pady=5, padx=10, sticky="w")


        member_membership = Checkbutton(Manage_Frame, text="Membership Fees", variable= var5, onvalue= 1, offvalue= 0, font= ("arial", 15, "bold"), bg="#CCCCFF", fg="black")
        member_membership.grid(row= 12, column= 0, sticky= "w")
        member_membership_txt = Entry(Manage_Frame, font= ("arial", 15, "bold"), state= DISABLED, justify= RIGHT, textvariable= Membership)
        member_membership_txt.grid(row= 12, column= 1, pady= 5, padx= 10, sticky= "w")


        #################  detail frame  ############

        Detail_Frame = Frame(self.root, relief= RIDGE, bg="#CCCCFF")
        Detail_Frame.place(x= 500, y= 100, width= 820, height= 630)
        
        Detail_label = Label(Detail_Frame, font=("arial", 11, "bold"), pady=10, padx=2, width=95, text="Date\t Ref Id\t Firstname    Lastname    Mobile No.    Address    Pincode    Gender    Membership")
        Detail_label.grid(row= 0, column= 0, columnspan= 4, sticky= "w")
        Detail_label_text = Text(Detail_Frame, width= 123, height= 34, font= ("arial", 12))
        Detail_label_text.grid(row= 1, column= 0, columnspan= 4)



        ####### adding button in detail frame #######

        receipt_btn = Button(Detail_Frame, padx= 15, bd= 5, font=("arial", 12, "bold"), bg= "#ff9966", width= 20, text= "Receipt")
        receipt_btn.grid(row= 2, column= 0)
        
        
        reset_btn = Button(Detail_Frame, padx= 15, bd= 5, font=("arial", 12, "bold"), bg= "#ff9966", width= 20, text= "Reset")
        reset_btn.grid(row= 2, column= 1)
        
        
        exit_btn = Button(Detail_Frame, padx= 15, bd= 5, font=("arial", 12, "bold"), bg= "#ff9966", width= 20, text= "Exit")
        exit_btn.grid(row= 2, column= 2)










if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
