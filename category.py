from tkinter import *
from tkinter import ttk,messagebox

class categoryClass:
    def __init__(self,window):
        self.window = window
        self.window.title("Category | Puriwat Koosuwan")

        window.geometry("715x437")
        window.configure(bg = "#ffffff")
        canvas = Canvas(window,bg = "#ffffff",height = 437,width = 715,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)
        self.window.focus_force()

        self.background_img = PhotoImage(file = f"image\ground.png")
        background = canvas.create_image(357.5, 101.5,image=self.background_img)

        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        self.product_list = []
        self.fetch_product()

        #* =========== Category details ================================

        Cat_frame = Frame(self.window,bd = 2,bg = "#fcd9d9",highlightthickness = 0,relief=RIDGE)
        Cat_frame.place(x = 472, y = 95,width = 202,height = 316)
        scrolly = Scrollbar(Cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(Cat_frame,orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(Cat_frame,columns=("order", "name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill= Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("order", text="Order")
        self.categoryTable.heading("name", text="Name")
        self.categoryTable["show"]="headings"
        self.categoryTable.column("order", width=40)
        self.categoryTable.column("name", width=100)
        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        #* =========== Buttons ================================

        self.img0 = PhotoImage(file = f"image\categoryadd.png")
        bt_add = Button(self.window, image = self.img0,borderwidth = 0,highlightthickness = 0,command = self.add,relief = "flat", cursor="hand2")
        bt_add.place(x = 62, y = 313,width = 137,height = 46)

        self.img1 = PhotoImage(file = f"image\categorydelete.png")
        bt_delete = Button(self.window, image = self.img1,borderwidth = 0,highlightthickness = 0,command = self.delete,relief = "flat", cursor="hand2")
        bt_delete.place(x = 245, y = 313,width = 137,height = 46)

        txt_name = Entry(self.window, textvariable=self.var_name,font=("goudy old style", 15),bd = 0,bg = "#d9d9d9",highlightthickness = 0)
        txt_name.place(x = 62, y = 237,width = 320,height = 40)

        
#* =========== Function ================================

    def add(self):
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name required", parent=self.window)
            else:
                name = self.var_name.get()
                f = open("CategoryText\categorytext", "r+")
                read = f.readlines()
                for i in list(read):
                    i = i.strip("\n")
                    i = i.casefold()
                    compare_name = name.casefold()
                    if compare_name == i:
                        return messagebox.showerror("Error", "Category name exists", parent=self.window)
                f.write(f"{name}\n")
                f.close()
                messagebox.showinfo("SUCCESS", "Category Added",parent=self.window)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent=self.window)

    def show(self):
        try:
            count = 1
            f = open("CategoryText\categorytext", "r+")
            read = f.readlines()
            for records in self.categoryTable.get_children():
                self.categoryTable.delete(records)
            for row in read:
                self.categoryTable.insert('', END, values=(count ,row))
                count += 1
            f.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.window)

    def get_data(self, ev):
        f = self.categoryTable.focus()
        content = (self.categoryTable.item(f))
        row = content["values"]

        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def fetch_product(self):
        try:
            self.product_list = []
            f = open("ProductText\producttext", "r")
            read = f.readlines()
            for row in list(read):
                row = row.strip("\n")
                row = row.split(",")
                self.product_list.append(row)
            f.close()
        except Exception as ex:
            messagebox.showerror("fetch_product Error", f"Error due to : {str(ex)}",parent=self.window)       

    def delete(self):
        try:
            f = open("CategoryText\categorytext", "r")
            read = f.readlines()
            f.close()
            name = self.var_name.get()
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Please select category from the list", parent=self.window)
            else:
                op = messagebox.askyesno("confirm", "Do you really want to delete?", parent=self.window)
                if op==TRUE:
                    f = open("CategoryText\categorytext", "w")
                    for line in read:
                        if line != name:
                            f.write(line)
                    f.close()
                    f  = open("ProductText\producttext", "w")
                    name = name.strip("\n")
                    for line in self.product_list:
                        print(line[0])
                        print(type(line[0]))
                        print(name)
                        print(type(name))
                        if line[0] != name:
                            newline = ','.join(line) + '\n'
                            print(newline)
                            f.write(newline)
                    f.close()
                    messagebox.showinfo("Success", "Category deleted", parent=self.window)
                    self.show()
                    self.var_cat_id.set("")
                    self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.window)



if __name__ == "__main__":
    window = Tk()
    obj = categoryClass(window)
    window.resizable(False, False)
    window.mainloop()