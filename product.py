from tkinter import *
from tkinter import ttk,messagebox


class productClass:
    def __init__(self,window):
        self.window = window
        self.window.title("Product | Puriwat Koosuwan")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg = "white")
        self.window.focus_force()
        #*================================================================

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        self.cat_list=[]
        self.fetch_cat()

        self.product_list = []
        self.fetch_product()

        product_Frame = Frame(self.window, bd = 3, bg = "white", relief=FLAT)
        product_Frame.place(x = 10, y = 10, width = 450, height =480)

        #*============Title============

        title = Label(product_Frame, bg = "#803D3D", text="Product Details", font=("inter", 18), fg="white").pack(side=TOP,fill=X)

        #*============Label============

        lbl_category = Label(product_Frame, bg = "white", text="Category", font=("inter", 18)).place(x=30,y=60)
        lbl_productName = Label(product_Frame, bg = "white", text="Name", font=("inter", 18)).place(x=30,y=120)
        lbl_price = Label(product_Frame, bg = "white", text="Price", font=("inter", 18)).place(x=30,y=180)
        lbl_quantity = Label(product_Frame, bg = "white", text="Quantity", font=("inter", 18)).place(x=30,y=240)
        lbl_status = Label(product_Frame, bg = "white", text="Status", font=("inter", 18)).place(x=30,y=300)

        #*============InputBox============

        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly',justify=CENTER,font=("inter", 18))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 18), bg='lightyellow').place(x=150,y=120,width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 18), bg='lightyellow').place(x=150,y=180,width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 18), bg='lightyellow').place(x=150,y=240,width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly',justify=CENTER,font=("inter", 18))
        cmb_status.place(x=150,y=300,width=200)
        cmb_status.current(0)

        #*============Buttons============

        btn_add = Button(product_Frame, text="Save", command=self.add, font=("inter", 18),bg="#2196f3",fg="white", cursor="hand2", relief=FLAT).place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("inter", 18),bg="#4caf50",fg="white", cursor="hand2", relief=FLAT).place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=("inter", 18),bg="#f44336",fg="white", cursor="hand2", relief=FLAT).place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=("inter", 18),bg="#607d8b",fg="white", cursor="hand2", relief=FLAT).place(x=340, y=400, width=100, height=40)

        #*============SearchFrame============

        plabelframe = LabelFrame(self.window,text="Product Table", font=("inter", 18, "bold"),bg='white',bd=2,relief=RIDGE)
        plabelframe.place(x=480,y=10,width=600,height=450)

        #*============Product detail============

        p_frame = Frame(plabelframe, bd=3, relief=RIDGE)
        p_frame.place(x=0,y=0,width=598,height=420)

        scrolly = Scrollbar(p_frame,orient=VERTICAL)
        scrollx = Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame,columns=("order", "Category", "name", "price", "qty", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill= Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("order", text="Order")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("status", text="Status")

        self.product_table["show"]="headings"

        self.product_table.column("order", width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
       
        self.show()
        

#* =========== Function ================================

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content["values"]
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_name.set(row[2])
        self.var_price.set(row[3])
        self.var_qty.set(row[4])
        self.var_status.set(row[5])

    def fetch_cat(self):
        self.cat_list.append("Empty")
        tempcat = []
        try:
            f = open("CategoryText\categorytext", "r+")
            read = f.readlines()
            for row in list(read):
                row = row.strip("\n")
                tempcat.append(row)
            if len(tempcat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in tempcat:
                    self.cat_list.append(i)
            f.close()
        except Exception as ex:
            messagebox.showerror("fetch_cat Error", f"Error due to : {str(ex)}",parent=self.window)

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
            self.product_table.delete(*self.product_table.get_children())
            count = 1
            for row in self.product_list:
                self.product_table.insert('', END, values=(count ,row[0], row[1], row[2], row[3], row[4]))
                count += 1
        except Exception as ex:
            messagebox.showerror("show Error", f"Error due to : {str(ex)}", parent=self.window)

    def table_update(self):
        self.fetch_product()
        self.show()

    def clear(self):
        self.var_cat.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")        
        self.show()

    def add(self):
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.window)
            else:
                lst = self.product_list
                name = self.var_name.get()
                if any(name in sublist for sublist in lst):
                    messagebox.showerror("Error", "Product Exist", parent=self.window)
                else:
                    cat = self.var_cat.get()
                    name = self.var_name.get()
                    price = self.var_price.get()
                    qty = self.var_qty.get()
                    status = self.var_status.get()
                    f = open("ProductText\producttext", "r+")
                    read = f.readlines()
                    f.write(f"{cat},{name},{price},{qty},{status}\n")
                    f.close()
                    messagebox.showinfo("SUCCESS", "Product Added",parent=self.window)
                    self.table_update()
        except Exception as ex:
            messagebox.showerror("add Error", f"Error due to : {str(ex)}",parent=self.window)

    def delete(self):
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Please select product from the list", parent=self.window)
            else:
                op = messagebox.askyesno("confirm", "Do you really want to delete?", parent=self.window)
                if op==TRUE:
                    count = self.var_pid.get()
                    count = int(count)
                    name = self.var_name.get()
                    f = open("ProductText\producttext" , "r")
                    read  = f.readlines()
                    f.close()
                    f = open("ProductText\producttext" , "w")
                    if any(name in sublist for sublist in self.product_list):
                        for i,line in enumerate(read,1):
                            if i != count:
                                f.writelines(line)
                    f.close()
                    messagebox.showinfo("Success", "Product deleted", parent=self.window)
                    self.clear()
                    self.table_update()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.window)

    def update(self):
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Please select product from the list", parent=self.window)
            else:
                count = self.var_pid.get()
                count = int(count)
                cat = self.var_cat.get()
                name = self.var_name.get()
                price = self.var_price.get()
                qty = self.var_qty.get()
                status = self.var_status.get()
                f = open("ProductText\producttext" , "r")
                read  = f.readlines()
                f.close()
                f = open("ProductText\producttext" , "w")
                if any(name in sublist for sublist in self.product_list):
                    for i,line in enumerate(read,1):
                        if i == count:
                            f.writelines(f"{cat},{name},{price},{qty},{status}\n")
                        else:
                            f.writelines(line)
                    messagebox.showinfo("Success", "Product updated", parent=self.window)
                else:
                    for i in list(read):
                        f.writelines(i)
                    messagebox.showinfo("Fail", "Product not updated", parent=self.window)
                f.close()
                
                self.table_update()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.window)

    def test(self):
        order = self.var_pid.get()
        print(order)

if __name__ == "__main__":
    window = Tk()
    obj = productClass(window)
    window.resizable(False, False)
    window.mainloop()