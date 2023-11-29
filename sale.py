from tkinter import *
from tkinter import ttk,messagebox
import os

class saleClass:
    def __init__(self,window):
        self.window = window
        self.window.title("Sales | Puriwat Koosuwan")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg = "white")
        self.window.focus_force()

        self.invoice_list = []
        self.var_invoice = StringVar()

        #*==========Title======================================================

        lbl_title = Label(self.window, text = "View Sales", font=("inter", 30),bg="#EBA6A6",bd=20,relief="flat").pack(side=TOP, fill=X)

        lbl_invoice = Label(self.window, text = "Invoices No.", font=("inter", 15, "bold"),bg="#803D3D",fg="white").place(x=60, y=100)
        lbl_invoice = Entry(self.window, textvariable=self.var_invoice, font=("inter", 18),bg="lightyellow").place(x=190, y=100, width=180, height=30)
        btn_search = Button(self.window, text= "Search",command=self.search, font=("inter",15,"bold"),bg="#4caf50",fg="white", relief=FLAT, cursor="hand2").place(x=380,y=100,width=120, height=30)
        btn_clear = Button(self.window, text= "Clear",command=self.clear, font=("inter",15,"bold"),bg="#607d8b",fg="white", relief=FLAT, cursor="hand2").place(x=510,y=100,width=120, height=30)

        #*==========Invoice List======================================================

        sales_Frame = Frame(self.window,bd="3",relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=410,height=330)

        scrolly = Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_list = Listbox(sales_Frame,font=("inter",15),bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)

        #*==========Invoice View======================================================

        invoice_Frame = Frame(self.window,bd="3",relief=RIDGE)
        invoice_Frame.place(x=590,y=140,width=410,height=330)

        lbl_title2 = Label(invoice_Frame, text = "Invoice Area", font=("inter", 30),bg="#EBA6A6",relief="flat").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(invoice_Frame,orient=VERTICAL)
        self.invoice_area = Text(invoice_Frame,bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.Sales_list.yview)
        self.invoice_area.pack(fill=BOTH,expand=1)

        self.show()

#* =========== Function ================================

    def show(self):
        del self.invoice_list[:]
        self.Sales_list.delete(0,END)
        #print(os.listdir('bill'))
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.Sales_list.insert(END,i)
                self.invoice_list.append(i.split('.')[0])
                

    def get_data(self,ev):
        index_ = self.Sales_list.curselection()
        file_name = self.Sales_list.get(index_)
        self.invoice_area.delete('1.0',END)
        fp = open(f'bill/{file_name}','r')
        for i in fp:
            self.invoice_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error", "Invoice No. Required", parent=self.window)
        else:
            if self.var_invoice.get() in self.invoice_list:
                fp = open(f"bill/{self.var_invoice.get()}.txt","r")
                self.invoice_area.delete('1.0',END)
                for i in fp:
                    self.invoice_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invoice No. Incorrect", parent=self.window)

    def clear(self):
        self.show()
        self.invoice_area.delete('1.0',END)



if __name__ == "__main__":
    window = Tk()
    obj = saleClass(window)
    window.resizable(False, False)
    window.mainloop()