from tkinter import *
from tkinter import ttk

class SooxApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("SööX")
        self.geometry("800x800")
        self.configure(bg="#d0edf7")

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        
        self.frames = {}

        for F in (StartPage, FoodListPage, RecipePage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        
        Label(self, text="SööX", font=("Arial", 40), bg="#d0edf7").place(relx=0.5, rely=0.3, anchor=CENTER)
        Button(self, text="Start", command=lambda: controller.show_frame("FoodListPage"),
               width=20, height=2).place(relx=0.5, rely=0.5, anchor=CENTER)

class FoodListPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        Label(self, text="Vali söök", font=("Arial", 30), bg="#d0edf7").place(relx=0.5, rely=0.1, anchor=CENTER)

        foods = {
            "Spaghetti Bolognese": "Keeda spagettid. Seejärel prae hakkliha ja lisa hakklihamaitseaine, kui praetud lisa tomatikaste, maitseained ja ongi valmis.",
            "Kanapasta": "Keeda makaronid ja tükelda kana. Seejärel prae kana, lisa maitseained ning kui kana on kuldpruun, lisa köögikoor, riivjuust, maitseained ning keeda seda, kuni valmis.",
            "Kartulid hakkliha kastmega": "Keeda kartulid, prae hakkliha ja lisa hakkliha maitseaine. Kui hakkliha on praetud lisa pannile jahu ning sega hakkliha läbi. Lisa piim, maitseained ja ongi valmis."
        }

        y = 0.25
        for food, recipe in foods.items():
            Button(self, text=food, command=lambda f=food, r=recipe: self.open_recipe(f, r),
                   width=25, height=2).place(relx=0.5, rely=y, anchor=CENTER)
            y += 0.15

        Button(self, text="Tagasi", command=lambda: controller.show_frame("StartPage"),
               width=15, height=2).place(relx=0.5, rely=0.8, anchor=CENTER)

    def open_recipe(self, food, recipe):
        recipe_page = self.controller.frames["RecipePage"]
        recipe_page.set_recipe(food, recipe)
        self.controller.show_frame("RecipePage")

class RecipePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        self.food_label = Label(self, text="", font=("Arial", 30), bg="#d0edf7")
        self.food_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.recipe_label = Label(self, text="", wraplength=700, justify="center", bg="#d0edf7")
        self.recipe_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(self, text="Tagasi", command=lambda: controller.show_frame("FoodListPage"),
               width=15, height=2).place(relx=0.5, rely=0.85, anchor=CENTER)

    def set_recipe(self, food, recipe):
        self.food_label.config(text=food)
        self.recipe_label.config(text=recipe)

if __name__ == "__main__":
    app = SooxApp()
    app.mainloop()
