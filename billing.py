from tkinter import *
from tkinter import ttk,messagebox
import time

class billClass:
    def __init__(self,window):
        self.window = window
        self.window.title("Billing System | Puriwat Koosuwan")
        self.window.geometry("1350x700+0+0")
        self.window.config(bg='white')
        
        #*==========customerVariable============

        self.var_cname = StringVar()
        self.var_contact = StringVar()

        #*==========CalculatorVariable============

        self.var_cal_input = StringVar()

        #*==========CartVariable============

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        self.var_cat=StringVar()
        self.var_status=StringVar()

        self.cart_list = []

        self.product_list = []
        self.fetch_product()

        #*==========Title======================================================

        lbl_title = Label(self.window, text = "BILL SYSTEM", font=("inter", 30),bg="#EBA6A6",bd=25,relief="flat").pack(side=TOP, fill=X)

        #*==========ProductFrame======================================================

        ProductFrame1 =  Frame(self.window,bd=4,relief=RIDGE,bg='white')
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle = Label(ProductFrame1, text = "All Products", font=("inter", 20,"bold"),bg="#803D3D",fg='white',relief="flat").pack(side=TOP, fill=X)

        #*==========ProductDetails======================================================

        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2,y=40,width=398,height=470)

        scrolly = Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3,columns=("order","category" ,"name", "price", "qty", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill= Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("order", text="N.")
        self.product_Table.heading("category", text="Cat")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Qty")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"]="headings"

        self.product_Table.column("order", width=20)
        self.product_Table.column("category", width=50)
        self.product_Table.column("name", width=90)
        self.product_Table.column("price", width=60)
        self.product_Table.column("qty", width=40)
        self.product_Table.column("status", width=50)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note = Label(ProductFrame1,text='"Note: Enter 0 Qty To Remove Product From The Cart"',font=("inter",11,'bold'),anchor='w',bg='white',fg='red').pack(side=BOTTOM,fill=X)

        #*==========CustomerDetails======================================================     

        CustomerFrame = Frame(self.window,bd=4,relief=RIDGE,bg='white')
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle = Label(CustomerFrame, text = "Customer Details", font=("inter", 13,'bold'),bg="#FFDADA",relief="flat").pack(side=TOP, fill=X)
        lbl_name = Label(CustomerFrame,text = "Name", font=("inter",14,'bold'), bg='white').place(x=5,y=30)
        txt_name = Entry(CustomerFrame,textvariable=self.var_cname, font=("inter",13), bg='lightyellow').place(x=70,y=35,width=180)
        
        lbl_contact = Label(CustomerFrame,text = "Contact No.", font=("inter",14,'bold'), bg='white').place(x=255,y=30)
        txt_contact = Entry(CustomerFrame,textvariable=self.var_contact, font=("inter",13), bg='lightyellow').place(x=375,y=35,width=140)
        
        #*==========Cart/CalculatorFrame======================================================     

        CalCartFrame = Frame(self.window,bd=2,relief=RIDGE,bg='white')
        CalCartFrame.place(x=420,y=190,width=530,height=360)

        #*==========CalculatorFrame======================================================     

        CalFrame = Frame(CalCartFrame,bd=9,relief=RIDGE,bg='white')
        CalFrame.place(x=5,y=10,width=268,height=340)

        txt_Calinput =  Entry(CalFrame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_Calinput.grid(row=0,columnspan=4)

        btn_7 = Button(CalFrame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),width=4,bd=5,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8 = Button(CalFrame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),width=4,bd=5,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9 = Button(CalFrame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),width=4,bd=5,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_plus = Button(CalFrame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),width=4,bd=5,pady=10,cursor='hand2').grid(row=1,column=3)

        btn_4 = Button(CalFrame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),width=4,bd=5,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5 = Button(CalFrame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),width=4,bd=5,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6 = Button(CalFrame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),width=4,bd=5,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_minus = Button(CalFrame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),width=4,bd=5,pady=10,cursor='hand2').grid(row=2,column=3)

        btn_1 = Button(CalFrame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),width=4,bd=5,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2 = Button(CalFrame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),width=4,bd=5,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3 = Button(CalFrame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),width=4,bd=5,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mul = Button(CalFrame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),width=4,bd=5,pady=10,cursor='hand2').grid(row=3,column=3)

        btn_0 = Button(CalFrame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),width=4,bd=5,pady=15,cursor='hand2').grid(row=4,column=0)
        btn_c = Button(CalFrame,text='C',font=('arial',15,'bold'),command=self.clear_cal,width=4,bd=5,pady=15,cursor='hand2').grid(row=4,column=1)
        btn_equ = Button(CalFrame,text='=',font=('arial',15,'bold'),command=self.calculate,width=4,bd=5,pady=15,cursor='hand2').grid(row=4,column=2)
        btn_div = Button(CalFrame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),width=4,bd=5,pady=15,cursor='hand2').grid(row=4,column=3)

        #*==========CartFrame======================================================     

        CartFrame = Frame(CalCartFrame, bd=3, relief=RIDGE)
        CartFrame.place(x=280,y=8,width=245,height=342)
        self.cartTitle = Label(CartFrame, text = "Cart \t Total Products: [0]", font=("inter", 12,'bold'),bg="#FFDADA",relief="flat")
        self.cartTitle.pack(side=TOP, fill=X)


        scrolly = Scrollbar(CartFrame,orient=VERTICAL)
        scrollx = Scrollbar(CartFrame,orient=HORIZONTAL)

        self.cart_Table = ttk.Treeview(CartFrame,columns=("order", "name", "price", "qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill= Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)

        self.cart_Table.heading("order", text="Order")
        self.cart_Table.heading("name", text="Name")
        self.cart_Table.heading("price", text="Price")
        self.cart_Table.heading("qty", text="Qty")

        self.cart_Table["show"]="headings"

        self.cart_Table.column("order", width=40)
        self.cart_Table.column("name", width=90)
        self.cart_Table.column("price", width=90)
        self.cart_Table.column("qty", width=40)
        self.cart_Table.pack(fill=BOTH, expand=1)
        self.cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)

        #*==========AddToCartFrame======================================================     

        CartButtonFrame = Frame(self.window,bd=2,relief=RIDGE,bg='white')
        CartButtonFrame.place(x=420,y=550,width=530,height=110)

        lbl_P_name = Label(CartButtonFrame,text = "Product Name", font=("inter",15,'bold'), bg='white').place(x=5,y=5)
        txt_P_name = Entry(CartButtonFrame,textvariable=self.var_pname, font=("inter",13), bg='lightyellow', state='readonly').place(x=5,y=35,width=190, height=22)

        lbl_P_price = Label(CartButtonFrame,text = "Price", font=("inter",15,'bold'), bg='white').place(x=230,y=5)
        txt_P_price = Entry(CartButtonFrame,textvariable=self.var_price, font=("inter",13), bg='lightyellow', state='readonly').place(x=230,y=35,width=150, height=22)

        lbl_P_qty = Label(CartButtonFrame,text = "Quantity", font=("inter",15,'bold'), bg='white').place(x=390,y=5)
        txt_P_qty = Entry(CartButtonFrame,textvariable=self.var_qty, font=("inter",13), bg='lightyellow',).place(x=390,y=35,width=100, height=22)

        self.lbl_instock = Label(CartButtonFrame,text = "In Stock", font=("inter",14,'bold'), bg='white')
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart = Button(CartButtonFrame,text='Clear',command=self.clear_cart, font=("inter",15,"bold"),bg="#607d8b",fg="white", cursor="hand2", relief=FLAT).place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(CartButtonFrame,text='Add | Update Cart',command=self.add_update_cart, font=("inter",15,"bold"),bg="#4caf50",fg="white", cursor="hand2", relief=FLAT).place(x=340,y=70,width=180,height=30)

        #*==========BillingDetails======================================================   

        billFrame = Frame(self.window,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=395,height=410)

        bTitle = Label(billFrame, text = "Customer Bill", font=("inter", 20,"bold"),bg="#803D3D",fg='white',relief="flat").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill = Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill.yview)

        #*==========BillingFrame======================================================   

        billMenuFrame = Frame(self.window,bd=2,relief='flat',bg='white')
        billMenuFrame.place(x=953,y=520,width=395,height=140)

        self.lbl_amount = Label(billMenuFrame, text="Bill Amount\n[0]", font=("inter",15,'bold'), bg='#CBAAAA', fg='white')
        self.lbl_amount.place(x=2,y=5,width=120,height=70)

        self.lbl_discount = Label(billMenuFrame, text="Discount\n[3%]", font=("inter",15,'bold'), bg='#CBAAAA', fg='white')
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_netPay = Label(billMenuFrame, text="Net Pay\n[0]", font=("inter",15,'bold'), bg='#CBAAAA', fg='white')
        self.lbl_netPay.place(x=246,y=5,width=144,height=70)
 
        btn_clearAll = Button(billMenuFrame, text="Clear All", command=self.clear_all,font=("inter",15,'bold'), bg='#607d8b', fg='white',cursor="hand2", relief=FLAT)
        btn_clearAll.place(x=2,y=80,width=120,height=50)

        btn_generate = Button(billMenuFrame, text="Generate/Save", command=self.generate_bill, font=("inter",15,'bold'), bg='#4caf50', fg='white',cursor="hand2", relief=FLAT)
        btn_generate.place(x=124,y=80,width=265,height=50)

        footer = Label(self.window, text=("Stock Management System | Puriwat Koosuwan"),font=("inter",15,'bold'),bg='#D9D9D9',fg='white').pack(side=BOTTOM,fill=X)

        self.show()
#* =========== Function ================================

#*===========Calculator==============

    def get_input(self,num):
        xnum=self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def calculate(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

#*==========show, getdata==========

    def table_update(self):
        self.fetch_product()
        self.show()

    def fetch_product(self):
        try:
            self.product_list = []
            f = open("ProductText\producttext", "r+")
            read = f.readlines()
            for row in list(read):
                row = row.strip("\n")
                row = row.split(",")
                self.product_list.append(row)
            f.close()
        except Exception as ex:
            messagebox.showerror("fetch_product Error", f"Error due to : {str(ex)}",parent=self.window)        

    def show(self):
        try:
            self.product_Table.delete(*self.product_Table.get_children())
            count = 1
            for row in self.product_list:
                self.product_Table.insert('', END, values=(count, row[0], row[1], row[2], row[3], row[4]))
                count += 1

        except Exception as ex:
            messagebox.showerror("show Error", f"Error due to : {str(ex)}", parent=self.window)

    def get_data(self, ev):
        f = self.product_Table.focus()
        content = (self.product_Table.item(f))
        row = content["values"]
        if row[5] == "Inactive":
            messagebox.showerror("Error", "Product is Inactive", parent=self.window)
        else:
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_pname.set(row[2])
            self.var_price.set(row[3])
            self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
            self.var_stock.set(row[4])
            self.var_qty.set('1')

#*==========Cart============

    def get_data_cart(self, ev):
        f = self.cart_Table.focus()
        content = (self.cart_Table.item(f))
        row = content["values"]
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_pname.set(row[2])
        self.var_price.set(row[3])
        self.var_qty.set(row[4])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])

    def  add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror("Error", "Please Select Product", parent=self.window)
        elif self.var_qty.get() == '':
            messagebox.showerror("Error", "Please Enter Quantity", parent=self.window)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror("Error", "Out Of Stock", parent=self.window)
        else:
            # priceCal = int(self.var_qty.get())*float(self.var_price.get())
            # priceCal = float(priceCal)
            priceCal = self.var_price.get()
            cart_data = [self.var_pid.get(),self.var_pname.get(),priceCal,self.var_qty.get(),self.var_stock.get(),self.var_cat.get(),self.var_price.get()]
            print(cart_data)
            #*==========
            present = 'no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ +=1
            
            if present == 'yes':
                op = messagebox.askyesno('CONFIRM',"The Product Is Already In The Cart\nDo You Want To Update | Remove?", parent=self.window)
                if op == True:
                    if  self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2] = priceCal
                        self.cart_list[index_][3] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()

    def show_cart(self):
        try:
            self.cart_Table.delete(*self.cart_Table.get_children())
            for row in self.cart_list:
                self.cart_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.window)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock")
        self.var_stock.set('')

#*==========Bill===========

    def generate_bill(self):
        if self.var_cname.get() =='' or self.var_contact.get() =='': 
            messagebox.showerror("Error", "Customer Details Required", parent=self.window)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", "The Cart Is Empty", parent=self.window)
        else:
            #*==========
            self.billTop()
            #*==========
            self.billMiddle()
            #*==========
            self.billBottom()
            fp = open(f"bill/{str(self.invoice)}.txt","w")
            fp.write(self.txt_bill.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill Have Been Generated/Saved",parent=self.window)

    def billTop(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\t   "StoreName"
\n\t Phone No. 081*******,  Saraburi 18000
{str("=" * 52)}
 Customer Name: {self.var_cname.get()}
 Phone No.: {self.var_contact.get()}
 Bill No.: {str(self.invoice)}\t\t\t  Date: {str(time.strftime("%d/%m/%Y"))}
{str("=" * 52)}
 Product Name\t\t\tQTY\tPrice
{str("=" * 52)}
        ''' 
        self.txt_bill.delete('1.0',END)
        self.txt_bill.insert('1.0', bill_top_temp)

    def billMiddle(self):
        try:
            for row in self.cart_list:
                
                pid = int(row[0])
                name = row[1]
                qty = int(row[4]) - int(row[3])
                pro_price = row[6]
                cat = row[5]

                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'

                #[self.var_pid.get(),self.var_pname.get(),priceCal,self.var_qty.get(),self.var_stock.get(),self.var_cat.get(),self.var_price.get()]

                price = float(row[2]) * int(row[3])
                price = str(price)
                self.txt_bill.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tTHB "+price)
                #*========Update QTY===========
                f = open("ProductText\producttext" , "r")
                read  = f.readlines()
                f.close()
                f = open("ProductText\producttext" , "w")
                for i,line in enumerate(read,1):
                    print(pid)
                    print(type(pid))
                    print(i)
                    print(type(i))
                    if i == pid:
                        f.writelines(f"{cat},{name},{pro_price},{qty},{status}\n")
                    else:
                        f.writelines(line)
                f.close()
            self.table_update()
            del self.cart_list[:]
            self.show_cart()
            self.clear_cart()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.window)

    def billBottom(self):
        bill_bottom_temp = f'''
{str("=" * 52)}
 Bill Amount\t\t\t\tTHB {self.billAmount}
 Discount\t\t\t\tTHB {self.discount}
 Net Pay\t\t\t\tTHB {self.net_pay}
{str("="* 52)}
        '''
        self.txt_bill.insert(END, bill_bottom_temp)

    def  bill_update(self):
        self.billAmount = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.billAmount = self.billAmount + (float(row[2]) * int(row[3]))
            #*========Discount============
        self.discount = (self.billAmount * 3)/100
        self.net_pay  = self.billAmount - self.discount
        #*==========LabelConfig==============
        self.lbl_amount.config(text = f'Bill Amount\n{str(self.billAmount)}')
        self.lbl_netPay.config(text = f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text = f"Cart \t Total Products: [{str(len(self.cart_list))}]")

#*=========clearButton=========

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill.delete('1.0',END)
        self.cartTitle.config(text = "Cart \t Total Products: [0]")
        self.clear_cart()
        self.show()
        self.show_cart()



if __name__ == "__main__":
    window = Tk()
    obj = billClass(window)
    window.resizable(False, False)
    window.mainloop()