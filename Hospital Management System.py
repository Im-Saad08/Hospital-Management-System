import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.NameofTablets=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.NoofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowtoUseMedication=StringVar()
        self.PatientID=StringVar()
        self.NHSNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


        #================================Data Frame===============================#
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=400,height=350)


        #=================================Buttons Frame==============================#
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)


        #=================================Details Frame================================#
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190)


        #==================================DataFrameLeft================================#
        lblNameTablet=Label(DataFrameLeft,text="Names of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameofTablets,state="readonly",font=("times new roman",12,"bold"),width=33)
        comNameTablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NoofTablets,width=35)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.IssueDate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.SideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblDrivingMachine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblHowtoUseMedication=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblHowtoUseMedication.grid(row=3,column=2,sticky=W)
        txtHowtoUseMedication=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.HowtoUseMedication,width=35)
        txtHowtoUseMedication.grid(row=3,column=3,sticky=W)

        lblPatientID=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientID,width=35)
        txtPatientID.grid(row=4,column=3)

        lblNHSnumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNHSnumber.grid(row=5,column=2,sticky=W)
        txtNHSnumber=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NHSNumber,width=35)
        txtNHSnumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DateofBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)



        #===================================DataFrame Right=================================#
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=35,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #===================================Buttons==========================================#
        btnPrescription=Button(ButtonFrame,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=1,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=5)


        #==================================Table================================================#
        #==================================ScrollBar================================================#
        # Scrollbars
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(DetailsFrame,columns=("nameoftablets", "ref", "dose", "nooftablets", "lot","issuedate", "expdate", "dailydose", "storage","nhsnumber", "pname", "dob", "address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Ref")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="#Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS No.")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Patient Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)


    #==================================Functionality Declaration==================================#
    def iPrescriptionData(self):
        if self.NameofTablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="test123",database="Mydata")
            my_cursor=conn.cursor()
            #youtube video
            #MySQL required











        


        






root=Tk()
ob=Hospital(root)
root.mainloop()