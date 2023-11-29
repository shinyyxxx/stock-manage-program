from tkinter import *
from category import categoryClass
from product import productClass
from sale import saleClass
from billing import billClass

class SMP(Canvas):
    def __init__(self, window):
        super().__init__()
        self["height"] = 1024
        self["width"] = 1440
        self["relief"] = RIDGE
        self["bd"] = 0
        self["bg"] = "#ffffff"
        self["highlightthickness"] = 0

        self.window = window
        self.window.title("Stock Management System | Puriwat Koosuwan")

        self.window.geometry("1440x1024")
        self.window.configure(bg = "#ffffff")

        #*==========Button======================================================

        self.img0 = PhotoImage(file = f"image\exitbt.png")
        exitB = Button(image = self.img0,borderwidth = 0,highlightthickness = 0,command = self.window.destroy,cursor="hand2",relief = "flat")
        exitB.place( x = 802, y = 716, width = 341, height = 136)

        self.img1 = PhotoImage(file = f"image\salebt.png")
        saleB = Button(image = self.img1,borderwidth = 0,highlightthickness = 0,command = self.sale,cursor="hand2",relief = "flat")
        saleB.place( x = 1030, y = 433, width = 341, height = 136)

        self.img2 = PhotoImage(file = f"image\productbt.png")
        productB = Button(image = self.img2,borderwidth = 0,highlightthickness = 0,command = self.product,cursor="hand2",relief = "flat")
        productB.place( x = 549, y = 433, width = 341, height = 136)

        self.img3 = PhotoImage(file = f"image\categorybt.png")
        categoryB = Button(image = self.img3,borderwidth = 0,highlightthickness = 0,command = self.category,cursor="hand2",relief = "flat")
        categoryB.place( x = 68, y = 433, width = 341, height = 136)

        self.img4 = PhotoImage(file = f"image\_billingbt.png")
        billingB = Button(image = self.img4,borderwidth = 0,highlightthickness = 0,command = self.billing,cursor="hand2",relief = "flat")
        billingB.place( x = 312, y = 716, width = 341, height = 136)

        #*==========Background======================================================

        self.background_img = PhotoImage(name="background" ,file = f"image\dashboard.png")
        background = Label(image = self.background_img)
        background.pack(padx=10, pady=10)

#* ================================================================

    def category(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=productClass(self.new_win)

    def sale(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=saleClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=billClass(self.new_win)

window = Tk()
obj = SMP(window)
obj.place(x = 0, y = 0)
window.resizable(False, False)
window.mainloop()