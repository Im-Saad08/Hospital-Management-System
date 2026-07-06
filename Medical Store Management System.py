#Patient Management System
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.state("zoomed")

        # Variables
        self.data = []
        self.selected_item = None

        self.NameofTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NoofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.StorageAdvice = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()

        # Heading
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Frames
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        self.DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Patient Information")
        self.DataFrameLeft.place(x=0, y=5, width=980, height=350)

        self.DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Prescription")
        self.DataFrameRight.place(x=990, y=5, width=460, height=350)

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1530, height=190)

        # Text widget
        self.txtPrescription = Text(self.DataFrameRight, font=("arial", 12, "bold"), width=35, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Input fields
        self.build_form()

        # Buttons
        Button(ButtonFrame, text="Prescription", command=self.generate_prescription, bg="green", fg="white", font=("arial", 12, "bold"), width=21).grid(row=0, column=0)
        Button(ButtonFrame, text="Prescription Data", command=self.add_data, bg="green", fg="white", font=("arial", 12, "bold"), width=21).grid(row=0, column=1)
        Button(ButtonFrame, text="Update", command=self.update_data, bg="green", fg="white", font=("arial", 12, "bold"), width=21).grid(row=0, column=2)
        Button(ButtonFrame, text="Delete", command=self.delete_data, bg="green", fg="white", font=("arial", 12, "bold"), width=21).grid(row=0, column=3)
        Button(ButtonFrame, text="Clear", command=self.clear_form, bg="green", fg="white", font=("arial", 12, "bold"), width=21).grid(row=0, column=4)
        Button(ButtonFrame, text="Exit", command=root.quit, bg="green", fg="white", font=("arial", 12, "bold"), width=21).grid(row=0, column=5)

        # Table
        scroll_x = Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(DetailsFrame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(DetailsFrame, columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.pack(fill=BOTH, expand=1)

        for col in self.hospital_table["columns"]:
            self.hospital_table.heading(col, text=col.title())
            self.hospital_table.column(col, width=100)

        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.hospital_table["show"] = "headings"

    def build_form(self):
        # Form inputs on the left (same format as yours)
        labels = ["Name of Tablets", "Reference No.", "Dose", "No of Tablets", "Lot", "Issue Date", "Expiry Date", "Daily Dose", "Storage Advice", "NHS Number", "Patient Name", "Date of Birth", "Patient Address"]
        vars = [self.NameofTablets, self.Ref, self.Dose, self.NoofTablets, self.Lot, self.IssueDate, self.ExpDate, self.DailyDose, self.StorageAdvice, self.NHSNumber, self.PatientName, self.DateofBirth, self.PatientAddress]

        for i in range(13):
            Label(self.DataFrameLeft, text=labels[i], font=("arial", 12, "bold"), padx=2, pady=6).grid(row=i % 9, column=(0 if i < 9 else 2), sticky=W)
            Entry(self.DataFrameLeft, font=("arial", 12, "bold"), textvariable=vars[i], width=35).grid(row=i % 9, column=(1 if i < 9 else 3))

        self.comNameTablet = ttk.Combobox(self.DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.NameofTablets, width=33, state="readonly")
        self.comNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        self.comNameTablet.grid(row=0, column=1)

    def add_data(self):
        record = [
            self.NameofTablets.get(), self.Ref.get(), self.Dose.get(), self.NoofTablets.get(),
            self.Lot.get(), self.IssueDate.get(), self.ExpDate.get(), self.DailyDose.get(),
            self.StorageAdvice.get(), self.NHSNumber.get(), self.PatientName.get(),
            self.DateofBirth.get(), self.PatientAddress.get()
        ]

        if any(not field for field in record):
            messagebox.showwarning("Warning", "All fields must be filled.")
            return

        self.hospital_table.insert("", END, values=record)
        self.clear_form()

    def clear_form(self):
        for var in [self.NameofTablets, self.Ref, self.Dose, self.NoofTablets, self.Lot,
                    self.IssueDate, self.ExpDate, self.DailyDose, self.StorageAdvice,
                    self.NHSNumber, self.PatientName, self.DateofBirth, self.PatientAddress]:
            var.set("")
        self.txtPrescription.delete("1.0", END)

    def get_cursor(self, event=""):
        selected = self.hospital_table.focus()
        values = self.hospital_table.item(selected, "values")
        if values:
            self.NameofTablets.set(values[0])
            self.Ref.set(values[1])
            self.Dose.set(values[2])
            self.NoofTablets.set(values[3])
            self.Lot.set(values[4])
            self.IssueDate.set(values[5])
            self.ExpDate.set(values[6])
            self.DailyDose.set(values[7])
            self.StorageAdvice.set(values[8])
            self.NHSNumber.set(values[9])
            self.PatientName.set(values[10])
            self.DateofBirth.set(values[11])
            self.PatientAddress.set(values[12])
            self.selected_item = selected

    def update_data(self):
        if self.selected_item:
            new_record = [self.NameofTablets.get(), self.Ref.get(), self.Dose.get(), self.NoofTablets.get(),
                          self.Lot.get(), self.IssueDate.get(), self.ExpDate.get(), self.DailyDose.get(),
                          self.StorageAdvice.get(), self.NHSNumber.get(), self.PatientName.get(),
                          self.DateofBirth.get(), self.PatientAddress.get()]
            self.hospital_table.item(self.selected_item, values=new_record)
            self.clear_form()

    def delete_data(self):
        selected = self.hospital_table.focus()
        if selected:
            self.hospital_table.delete(selected)
            self.clear_form()

    def generate_prescription(self):
        self.txtPrescription.delete("1.0", END)
        lines = [
            f"Tablet: {self.NameofTablets.get()}",
            f"Ref: {self.Ref.get()}",
            f"Dose: {self.Dose.get()}",
            f"#Tablets: {self.NoofTablets.get()}",
            f"Lot: {self.Lot.get()}",
            f"Issued: {self.IssueDate.get()} / Exp: {self.ExpDate.get()}",
            f"Daily Dose: {self.DailyDose.get()}",
            f"Storage: {self.StorageAdvice.get()}",
            f"NHS No: {self.NHSNumber.get()}",
            f"Name: {self.PatientName.get()}",
            f"DOB: {self.DateofBirth.get()}",
            f"Address: {self.PatientAddress.get()}"
        ]
        self.txtPrescription.insert(END, "\n".join(lines))


if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
