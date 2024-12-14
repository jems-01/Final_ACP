from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import dataB
import mysql.connector

class main:
    motor_parking_rate_perHour = 15.0
    car_parking_rate_perHour = 30.0
    entry_time = datetime.now()
    exit_time = datetime.now()

    def __init__(self, master):
        self.master = master
        self.master.title('SPMS')
        self.master.geometry('1280x650+35+10')
        self.master.resizable(0,0)

        self.title = Label(self.master, text="Smart Parking Management System", font = "Times 20 bold", fg="#f55442", bg="black")
        self.title.pack(side="top")

        self.frame1 = LabelFrame(self.master, bg="black")
        self.frame1.place(relheight=0.2, relwidth=0.59, relx=0.01, rely=0.16, anchor='w')
        
        self.frame2 = LabelFrame(self.master, bg='blue')
        self.frame2.place(relheight=0.2, relwidth=0.35, relx=0.6, rely=0.16, anchor='w')

        self.frame3 = LabelFrame(self.master, bg='white', text='List', bd=8, font='Times 12 bold')
        self.frame3.place(relheight=0.7, relwidth=0.80, relx=0.09, rely=0.26)

        self.spaceNo = Label(self.frame1, text="Parking space ID:", font='Courier 12 bold')
        self.spaceNo.place(x=1, y=10)
        self.spaceNo_entry = Entry(self.frame1, width=25, font='Courier 10', bd=2)
        self.spaceNo_entry.place(x=1, y=30)

        self.customerName = Label(self.frame1, text="Customer Name:", font='Courier 12 bold')
        self.customerName.place(x=240, y=10)
        self.customerName_entry = Entry(self.frame1, width=25, font='Courier 10', bd=2)
        self.customerName_entry.place(x=240, y=30)

        self.vehicleType = Label(self.frame1, text='Vehicle Type(motor/car):', font='Courier 10 bold')
        self.vehicleType.place(x=1, y=63)
        self.vehicleType_entry = Entry(self.frame1, width=25, font='Courier 10', bd=2)
        self.vehicleType_entry.place(x=1, y=83)

        self.plateNo = Label(self.frame1, text='Plate No:', font='Courier 12 bold')
        self.plateNo.place(x=240, y=63)
        self.plateNo_entry = Entry(self.frame1, width=25, font='Courier 10', bd=2)
        self.plateNo_entry.place(x=240, y=83)

        self.timeInBtn = Button(self.frame1, text='Check in', height=2, width=11, fg="black", bg="white", command=self.checkIn)
        self.timeInBtn.place(x=460, y=10)

        self.timeOutBtn = Button(self.frame1, text='Check out', height=2, width=11, fg="black", bg="white", command=self.checkOut)
        self.timeOutBtn.place(x=555, y=10)

        self.PaidBtn = Button(self.frame1, text='Paid', height=2, width=12, fg="black", bg="white", command=self.paid)
        self.PaidBtn.place(x=650, y=10)

        self.DisplayBtn = Button(self.frame1, text='Display Info', height=2, width=11, fg="black", bg="white", command=self.display)
        self.DisplayBtn.place(x=460, y=63)
        
        self.HistoryBtn = Button(self.frame1, text="History", width=11, height=2, fg='black', bg='white', command= self.showHistory)
        self.HistoryBtn.place(x=555, y=63)

        self.space_no1 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no1.place(relheight=0.80, relwidth=0.1, x=3, y=1)
        self.space_no1_Lbl = Label(self.space_no1, text="A1", font='Ariel 9 bold', bg='lightgreen')
        self.space_no1_Lbl.place(relx=0.5, rely=0.5, anchor="center")

        self.space_no2 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no2.place(relheight=0.80, relwidth=0.1, x=59, y=1)
        self.space_no2_Lbl = Label(self.space_no2, text="A2", font='Ariel 9 bold', bg='lightgreen')
        self.space_no2_Lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        self.space_no3 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no3.place(relheight=0.80, relwidth=0.1, x=115, y=1)
        self.space_no3_Lbl = Label(self.space_no3, text="A3", font='Ariel 9 bold', bg='lightgreen')
        self.space_no3_Lbl.place(relx=0.5, rely=0.5, anchor="center")   
                
        self.space_no4 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no4.place(relheight=0.80, relwidth=0.1, x=171, y=1)
        self.space_no4_Lbl = Label(self.space_no4, text="A4", font='Ariel 9 bold', bg='lightgreen')
        self.space_no4_Lbl.place(relx=0.5, rely=0.5, anchor="center")
                
        self.space_no5 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no5.place(relheight=0.80, relwidth=0.1, x=227, y=1)
        self.space_no5_Lbl = Label(self.space_no5, text="A5", font='Ariel 9 bold', bg='lightgreen')
        self.space_no5_Lbl.place(relx=0.5, rely=0.5, anchor="center")
                
        self.space_no6 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no6.place(relheight=0.80, relwidth=0.1, x=283, y=1)
        self.space_no6_Lbl = Label(self.space_no6, text="A6", font='Ariel 9 bold', bg='lightgreen')
        self.space_no6_Lbl.place(relx=0.5, rely=0.5, anchor="center")
                
        self.space_no7 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no7.place(relheight=0.80, relwidth=0.1, x=339, y=1)
        self.space_no7_Lbl = Label(self.space_no7, text="A7", font='Ariel 9 bold', bg='lightgreen')
        self.space_no7_Lbl.place(relx=0.5, rely=0.5, anchor="center")
                
        self.space_no8 = LabelFrame(self.frame2, bg='lightgreen')
        self.space_no8.place(relheight=0.80, relwidth=0.1, x=395, y=1)
        self.space_no8_Lbl = Label(self.space_no8, text="A8", font='Ariel 9 bold', bg='lightgreen')
        self.space_no8_Lbl.place(relx=0.5, rely=0.5, anchor="center")

        self.availability()

        self.customerList = Listbox(self.frame3, font='Times 12 bold')
        self.customerList.bind('<<ListboxSelect>>', self.customerRec)
        self.customerList.place(x=1, relheight=1, relwidth=1)

    def customerRec(self, event=None):
        try:
            selected_index = self.studentsList.curselection()

            selected_data = self.studentsList.get(selected_index[0])

            self.spaceNo_entry.delete(0, END)
            self.spaceNo_entry.insert(0, selected_data[1])  
            self.customerName_entry.delete(0, END)
            self.customerName_entry.insert(0, selected_data[2])  
            self.vehicleType_entry.delete(0, END)
            self.vehicleType_entry.insert(0, selected_data[3])  
            self.plateNo_entry.delete(0, END)
            self.plateNo_entry.insert(0, selected_data[4])  
            
        except IndexError:
            messagebox.showerror("Error", "Failed to retrieve the customer record. Please try again.")

    def clearEntries(self):
        self.spaceNo_entry.delete(0, END)
        self.customerName_entry.delete(0, END)
        self.vehicleType_entry.delete(0, END)
        self.plateNo_entry.delete(0, END)

    def checkIn(self):
        try:
            if len(self.spaceNo_entry.get()) != 0:
                for rows in dataB.checkDuplicate():
                    if self.spaceNo_entry.get().upper() in rows:
                        messagebox.showerror('Error', 'Space already occupied.')
                        return

                spaceNo = self.spaceNo_entry.get().upper()
                customerName = self.customerName_entry.get()
                vehicleType = self.vehicleType_entry.get()
                plateNo = self.plateNo_entry.get()
                entry_time = self.entry_time

                if not all([customerName, vehicleType, plateNo]):
                    messagebox.showerror('Error', 'Please fill all the field.')
                    return
                if vehicleType.lower() != "motor" and vehicleType.lower() != "car":
                    messagebox.showerror('Error', 'Please enter the right vehicle type.')
                    return
                    
                dataB.addRec(spaceNo, customerName, vehicleType, plateNo, entry_time)
                self.clearEntries()
                dataB.checkAvailability()

                
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to add record: {e}")

    def checkOut(self):
        if(len(self.spaceNo_entry.get()) != 0):
            spaceNo = self.spaceNo_entry.get().upper()
            dataB.updateExitTIme(self.exit_time, spaceNo)
            try:
                entry_time = dataB.entryTime(spaceNo)
                exit_time = dataB.exitTime(spaceNo)
                duration = exit_time - entry_time
                total_seconds = duration.total_seconds()
                hours_parked = total_seconds / 3600
                if dataB.vhType(spaceNo) == "motor":
                    total_fee = round(hours_parked * self.motor_parking_rate_perHour, 2)
                else:
                    total_fee = round(hours_parked * self.car_parking_rate_perHour, 2)

                if(len(self.spaceNo_entry.get())) != 0:
                    self.customerList.delete(0, END)
                    dataB.dataUpdate(total_fee, spaceNo)
                    data =  dataB.searchData(spaceNo)

                for row in data:
                    spaceId = row[0]
                    customerName = row[1]
                    vehicleType = row[2]
                    plateNo = row[3]
                    entryTime = row[4]
                    exitTime = row[5]
                    parkingFee = row[6]
                    self.customerList.insert(END, row)
                    dataB.addToHistory(spaceId, customerName, vehicleType, plateNo, entryTime, exitTime, parkingFee)


            except mysql.connector.Error as e:
                messagebox.showerror('Error', f"failed to retieve data: {e}")
        else:
            messagebox.showerror('Error', 'Please enter space number: ')

    def paid(self):
        dataB.deleteRec(spaceNo = self.spaceNo_entry.get().upper())
        self.customerList.delete(0, END)

        self.clearEntries()
            
        
    def display(self):
        self.customerList.delete(0, END)
        for No in dataB.getSpaceNo():
            dataB.updateExitTIme(self.exit_time, No)
            entry_time = dataB.entryTime(No)
            exit_time = dataB.exitTime(No)
            duration = exit_time - entry_time
            total_seconds = duration.total_seconds()
            hours_parked = total_seconds / 3600
            if dataB.vhType(No) == "motor":
                total_fee = round(hours_parked * self.motor_parking_rate_perHour, 2)
            else:
                total_fee = round(hours_parked * self.car_parking_rate_perHour, 2)

            dataB.dataUpdate(total_fee, No)

        header = f"{"SpaceNo":<15}{"CustomerName":<30}{"VehicleType":<20}{"PlateNo":<20}{"EntryTime":<20}{"ExitTime":<20}{"Fee":<10}"
        self.customerList.insert(END, header)   
        self.customerList.insert(END, "-" * 100)
        for rows in dataB.showData():
            formatRow = f"{rows[0]:<20}{rows[1]:<30}{rows[2]:<20}{rows[3]:<20}{rows[4]}{"":<20}{rows[5]}{"":<20}{rows[6]:<10}"
            self.customerList.insert(END, formatRow)

        self.clearEntries()

    def showHistory(self):
        self.customerList.delete(0, END)
        for rows in dataB.showHistory():
            self.customerList.insert(END, rows)

    def availability(self):
        spaces = [
            'A1', 'A2', 'A3', 'A4',
            'A5', 'A6', 'A7', 'A8'
        ]
        for index, rows in enumerate(dataB.checkAvailability()):
            if spaces[index] in rows:
                if spaces[index] == spaces[0]:
                    self.space_no1.config(bg='red')
                    self.space_no1_Lbl.config(bg='red')
                elif spaces[index] == spaces[1]:
                    self.space_no2.config(bg='red')
                    self.space_no2_Lbl.config(bg='red')
                elif spaces[index] == spaces[2]:
                    self.space_no3.config(bg='red')
                    self.space_no3_Lbl.config(bg='red')
                elif spaces[index] == spaces[3]:
                    self.space_no4.config(bg='red')
                    self.space_no4_Lbl.config(bg='red')
                elif spaces[index] == spaces[4]:
                    self.space_no5.config(bg='red')
                    self.space_no5_Lbl.config(bg='red')
                elif spaces[index] == spaces[5]:
                    self.space_no6.config(bg='red')
                    self.space_no6_Lbl.config(bg='red')
                elif spaces[index] == spaces[6]:
                    self.space_no7.config(bg='red')
                    self.space_no7_Lbl.config(bg='red')
                elif spaces[index] == spaces[7]:
                    self.space_no8_Lbl.config(bg='red')
                    self.space_no8.config(bg='red')
            


                
        
root = Tk()
app = main(root)
root.mainloop()