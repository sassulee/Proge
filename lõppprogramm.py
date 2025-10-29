from tkinter import *

class SooxApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("SööX")
        self.geometry("800x800")
        self.configure(bg="#d0edf7")

        container = Frame(self, bg="#d0edf7")
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.user_choices = {"meal": None, "goal": None, "type": None}
        self.frames = {}

        for F in (StartPage, SecondPage, ThirdPage, FourthPage, FoodListPage, RecipePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# --- Ühtne nupu ja fondi stiil ---
BTN_STYLE = {
    "font": ("Segoe UI Semibold", 14),
    "bg": "#b7e3f5",
    "activebackground": "#9fd9f0",
    "relief": "ridge",
    "bd": 2,
    "cursor": "hand2"
}

LABEL_FONT_LARGE = ("Segoe UI Semibold", 32)
LABEL_FONT_MED = ("Segoe UI Semibold", 22)


class StartPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        Label(self, text="SööX", font=("Segoe UI Black", 48), bg="#d0edf7").place(relx=0.5, rely=0.3, anchor=CENTER)
        Button(self, text="Start", command=lambda: controller.show_frame("SecondPage"),
               width=20, height=2, **BTN_STYLE).place(relx=0.5, rely=0.5, anchor=CENTER)


class SecondPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        Label(self, text="Milline söögikord on?", font=LABEL_FONT_LARGE, bg="#d0edf7").place(relx=0.5, rely=0.2, anchor=CENTER)
        y = 0.4
        for meal in ["Hommikusöök", "Lõunasöök", "Õhtusöök"]:
            Button(self, text=meal,
                   command=lambda m=meal: self.select_meal(m),
                   width=30, height=2, **BTN_STYLE).place(relx=0.5, rely=y, anchor=CENTER)
            y += 0.15

    def select_meal(self, meal):
        self.controller.user_choices["meal"] = meal
        self.controller.show_frame("ThirdPage")


class ThirdPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        Label(self, text="Mis on sinu eesmärk?", font=LABEL_FONT_LARGE, bg="#d0edf7").place(relx=0.5, rely=0.2, anchor=CENTER)
        y = 0.4
        for goal in ["Võtta kaalust alla", "Võtta kaalust juurde", "Säilitada kaalu"]:
            Button(self, text=goal,
                   command=lambda g=goal: self.select_goal(g),
                   width=30, height=2, **BTN_STYLE).place(relx=0.5, rely=y, anchor=CENTER)
            y += 0.15

    def select_goal(self, goal):
        self.controller.user_choices["goal"] = goal
        self.controller.show_frame("FourthPage")


class FourthPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        Label(self, text="Mis sorti sööki soovid?", font=LABEL_FONT_LARGE, bg="#d0edf7").place(relx=0.5, rely=0.2, anchor=CENTER)
        y = 0.4
        for food_type in ["Magus", "Soolane"]:
            Button(self, text=food_type,
                   command=lambda f=food_type: self.select_type(f),
                   width=30, height=2, **BTN_STYLE).place(relx=0.5, rely=y, anchor=CENTER)
            y += 0.15

    def select_type(self, food_type):
        self.controller.user_choices["type"] = food_type
        food_list_page = self.controller.frames["FoodListPage"]
        food_list_page.update_foods()
        self.controller.show_frame("FoodListPage")


class FoodListPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        Label(self, text="Vali söök", font=LABEL_FONT_MED, bg="#d0edf7").place(relx=0.5, rely=0.1, anchor=CENTER)

        self.buttons = []

        Button(self, text="Tagasi algusesse", command=lambda: controller.show_frame("StartPage"),
               width=25, height=2, **BTN_STYLE).place(relx=0.5, rely=0.9, anchor=CENTER)

        # --- KÕIK sinu originaalsed toidud ja retseptid ---
        self.food_data = {
            ("Hommikusöök", "Võtta kaalust juurde", "Magus"): {
                "Pannkoogid meega": "Sega jahu, piim ja muna. Prae ja serveeri meega.",
                "Kaerahelbepuder moosiga": "Keeda 150g kaerahelbed piima ja veega ning lisa moos.",
                "Šokolaadine maapähkli-smuuti": "Banaan, 2sl maapähklivõi, 250ml piima, 1sl kakaopulbrit, 1sl kaerahelbeid ning blenderda."
            },
            ("Hommikusöök", "Võtta kaalust juurde", "Soolane"): {
                "Pannkoogid meega": "Sega jahu, piim ja muna. Prae ja serveeri meega.",
                "Kaerahelbepuder moosiga": "Keeda kaerahelbed piima ja veega ning lisa moos.",
                "Röstsai avokaado, munapraad ja juustuga": "Rösti 2 viilu täisteraleiba, määri peale avokaado, pane peale praemuna ja veidi juustu. Soovi korral lisa ka peekonit."
            },
            ("Hommikusöök", "Võtta kaalust alla", "Magus"): {
                "Kreemine jogurtikauss chiaga": "Maitsestamata kreeka jogurtit, mesi, mustikad ja chia seemned.",
                "Kaerahelbepuder õuna ja kaneeliga": "Keeda kaerahelbed veega, lisa õunad ja kaneel.",
                "Marja-proteiinismuuti": "Blenderda kokku 150 ml mandlipiima, peotäis mustikaid, pool banaani, 1 mõõt vaniljeproteiinipulbrit ja jääd. Väga kerge ja täitev, ideaalne enne tööle minekut.."    
            },
            ("Hommikusöök", "Võtta kaalust alla", "Soolane"): {
                "Omlett köögiviljadega": "Klopi munad ja lisa paprika, sibul, tomat.",
                "Kodujuust salatiga": "Serveeri kodujuustu koos salatilehtede ja kurkidega.",
                "Avokaado ja muna rukkileival": "Rösti 1 viil täisterarukkileiba, määri peale pool avokaadot ja pane üks keedumuna viilutatult. Lisa musta pipart ja veidi sidrunimahla."
            },
            ("Hommikusöök", "Säilitada kaalu", "Soolane"): {
                "Täistera wrap kanaga": "Soojenda täisteratortilja, lisa 80 g kanafileed, natuke hummust, salatilehti ja kurki. Keera kokku ja lõika pooleks.",
                "Munapuder kodujuustu ja tomatiga": "Prae 2 muna väheses õlis, sega sisse 2 sl kodujuustu ja tükeldatud tomat. Serveeri täisteraleival.",
                "Kodujuustusalat köögiviljadega": "Sega 150 g kodujuustu kurgi, tomati ja keedumuna tükikestega, maitsesta ürdisoola ja tilga oliiviõliga."
            },
            ("Hommikusöök", "Säilitada kaalu", "Magus"): {
                "Šokolaadine chia-puding": "Sega kokku 200 ml mandlipiima, 2 sl chia seemneid, 1 tl mett ja 1 tl kakaopulbrit. Lase seista üleöö külmkapis. Hommikul sega läbi ja lisa banaaniviilud.",
                "Kohupiim banaani ja meega": "Sega 150 g kohupiima poole banaaniga, lisa 1 tl mett ja paar hakitud pähklit. Lihtne, valgurikas ja mõnusalt magus."
            },
            ("Lõunasöök", "Võtta kaalust juurde", "Magus"): {
                "Šokolaadine kaera-banaaniroog": "Keeda 70 g kaerahelbeid täispiimas, lisa 1 banaan, 1 sl kakaopulbrit, 1 sl maapähklivõid ja veidi mett.",
                "Juustune magus-pasta": "Keeda 80 g täisterapastat, lisa 50 g ricottat, 1 tl mett ja kaneeli. Sega sisse rosinaid või hakitud datleid.",
                "Kookose-riisipallid": "Sega 100 g keedetud riisi, 2 sl kookospiima, 1 sl mett ja 1 sl kookoshelbeid. Vormi pallid ja jahuta külmikus."
            },
            ("Lõunasöök", "Võtta kaalust juurde", "Soolane"): {
                "Pasta lõhe ja avokaadoga": "Keeda 80 g täisterapastat, sega 100 g suitsulõhe ja pool avokaadot. Lisa oliiviõli ja sidrunimahla.",
                "Riis kana, pähklite ja köögiviljadega": "Keeda 80 g pruunriisi, lisa 100 g kanafileed, köögivilju ja 1 sl hakitud pähkleid. Maitsesta sojakastme ja vürtsidega.",
                "Burrito kauss": "Kaussi 70 g pruuni riisi, 100 g hakkliha või kalkunihakkliha, ubasid, maisi, avokaadot ja veidi juustu. Maitsesta tšilli ja koriandriga."
            },
            ("Lõunasöök", "Võtta kaalust alla", "Magus"): {
                "Kohupiimavorm marjadega": "Sega 200 g kohupiima, 1 muna, 1 tl mett ja peotäis marju. Küpseta 180 °C juures 20 minutit, kuni pind on kuldne.",
                "Smuutikauss banaani ja kakaoga": "Blenderda 1 banaan, ½ avokaadot, 100 ml mandlipiima ja 1 tl kakaopulbrit. Serveeri kausis koos chia seemnete ja mustikatega."
            },
            ("Lõunasöök", "Võtta kaalust alla", "Soolane"): {
                "Kana-köögiviljapann": "Prae 100 g kanafileed väheses õlis, lisa brokkoli, paprika ja suvikõrvits. Maitsesta soola, pipra ja ürtidega. Serveeri ilma lisakaloriteta.",
                "Salat kikerherneste ja tomatiga": "Sega 100 g keedetud kikerherneid, tomat, kurk, punane sibul ja spinatilehed. Lisa veidi sidrunimahla ja tilk oliiviõli.",
                "Täistera wrap kalkuni ja salatiga": "Täistera tortilja, 80 g kalkuniliha, salatilehed, kurk, tomat ja veidi jogurtikastet. Keera kokku."
            },
            ("Lõunasöök", "Säilitada kaalu", "Soolane"): {
                "Maguskartuli-läätsesalat": "Küpseta 150 g maguskartulit, sega 100 g keedetud läätsi, spinati, punase sibula ja tilga oliiviõliga. Maitsesta ürtidega.",
                "Täisterapasta köögiviljade ja kanaga": "Keeda 70 g täisterapastat, sega 100 g kanafilee ja köögiviljadega (brokkoli, paprika). Lisa veidi oliiviõli ja ürte.",
                "Täidetud paprikad kalkunihakklihaga": "Täida paprikad 100 g kalkunihakklihaga, lisa köögivilju ja veidi tomatipastat. Küpseta ahjus 20 minutit."
            },
            ("Lõunaöök", "Säilitada kaalu", "Magus"): {
                "Magus kinoa jogurti ja puuviljadega": "Keeda 70 g kinoad piimaga, lisa 1 tl mett ja kaneeli. Serveeri koos 2 sl kreeka jogurti ja viilutatud puuviljadega.",
                "Riisipuding kookospiimaga": "Keeda 60 g jasmiiniriisi 150 ml kookospiimas ja 100 ml vees, lisa 1 tl mett ja näpuotsatäis vanilli. Serveeri marjade või mangoga.",
                "Banaanipannkoogid maapähklivõiga": "Püreeri 1 banaan ja 2 muna, küpseta väikesed pannkoogid. Peale määri 1 tl maapähklivõid ja mõned banaaniviilud."
            },
            ("Õhtusöök", "Võtta kaalust juurde", "Magus"): {
                "Maapähklivõi-banaan kaerahelbekauss": "70 g kaerahelbeid piimas, 1 banaan, 1 sl maapähklivõid, 1 tl mett, veidi šokolaaditükke.",
                "Ricotta-datli puder": "100 g ricottat, 3 hakitud datlit, 1 tl mett, veidi vaniljet, peotäis pähkleid.",
                "Kakao-chiapuding marjadega": "3 sl chia seemneid, 200 ml mandlipiima, 1 tl kakaopulbrit, 1 tl mee, marjad peale."
            },
            ("Õhtusöök", "Võtta kaalust juurde", "Soolane"): {
                "Pasta kanaga tomatikastmes": "80 g täisterapastat, 100 g kanafileed, purustatud tomat, küüslauk, veidi parmesani.",
                "Kartuli-läätsesalat avokaadoga": "150 g keedetud kartulit, 50 g keedetud läätsi, pool avokaadot, veidi oliiviõli ja sidrunimahla.",
                "Täidetud paprika kala ja riisiga": "100 g valget kala, 50 g pruuni riisi, ürdid, küpsetatud paprikas ahjus."
            },
            ("Õhtusöök", "Võtta kaalust alla", "Magus"): {
                "Kohupiima-puuviljakrõmps": "150 g kohupiima, hakitud kirsid, mustikad, peale paar hakitud mandlit.",
                "Õuna-kaerakrõps puding": "40 g kaerahelbeid keedetud mandlipiimas, riivitud pool õuna, kaneel, paar pähklit peale.",
                "Marja-keefir smuuti kauss": "150 ml keefiri blenderdatud koos ½ tassi marjade ja veidi chia seemnetega, serveeri jahtunult."
            },
            ("Õhtusöök", "Võtta kaalust alla", "Soolane"): {
                "Ahjuköögiviljade ja halloumi kauss": "röstitud suvikõrvits, paprika, punane sibul, 50 g halloumit, tilgake oliiviõli.",
                "Munavorm spinati ja seentega": "2 muna, spinat, seened, väike lusikatäis parmesani, küpseta ahjus.",
                "Kikerherneste-tomatisupp": "Kikerherned, purustatud tomatid, sibul, küüslauk, pipar, veidi ürte."
            },
            ("Õhtusöök", "Säilitada kaalu", "Soolane"): {
                "Küpsetatud lõhe ja köögiviljad": "100 g lõhefileed, brokkoli, porgand, paprika, veidi sidrunimahla ja oliiviõli.",
                "Quinoa-bataadi kauss": "70 g kinoad, röstitud bataat, spinat, veidi fetajuustu, oliiviõli.",
                "Täidetud suvikõrvitsad kanaga": "100 g kanafileed, hakitud tomatid, basiilik, küpsetatud ahjus suvikõrvitsa sees."
            },
            ("Õhtusöök", "Säilitada", "Magus"): {
                "Banaan-riisi puding": "60 g keedetud riisi, 1 banaan, 100 ml mandlipiima, veidi mett ja kaneeli.",
                "Jogurti-marja trifle": "kihita klaasis 100 g kreeka jogurtit, marju ja 1 sl granolat.",
                "Kakao-kaerakauss": "40 g kaerahelbeid, 150 ml piima, 1 tl kakaopulbrit, lusikatäis kodujuustu, peotäis marju."
            },
            
        }
        
    def update_foods(self):
        for b in self.buttons:
            b.destroy()
        self.buttons.clear()

        choices = self.controller.user_choices
        key = (choices["meal"], choices["goal"], choices["type"])
        foods = self.food_data.get(key, {"Pole retsepte": "Selle kategooria jaoks retsepte pole veel lisatud."})

        y = 0.3
        for food, recipe in foods.items():
            btn = Button(self, text=food, width=30, height=2,
                         command=lambda f=food, r=recipe: self.open_recipe(f, r), **BTN_STYLE)
            btn.place(relx=0.5, rely=y, anchor=CENTER)
            self.buttons.append(btn)
            y += 0.15

    def open_recipe(self, food, recipe):
        recipe_page = self.controller.frames["RecipePage"]
        recipe_page.set_recipe(food, recipe)
        self.controller.show_frame("RecipePage")


class RecipePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d0edf7")
        self.controller = controller

        self.food_label = Label(self, text="", font=LABEL_FONT_MED, bg="#d0edf7")
        self.food_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.recipe_label = Label(self, text="", wraplength=700, justify="center",
                                  font=("Segoe UI", 13), bg="#d0edf7")
        self.recipe_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(self, text="Tagasi toitude juurde",
               command=lambda: controller.show_frame("FoodListPage"),
               width=25, height=2, **BTN_STYLE).place(relx=0.5, rely=0.85, anchor=CENTER)

    def set_recipe(self, food, recipe):
        self.food_label.config(text=food)
        self.recipe_label.config(text=recipe)


if __name__ == "__main__":
    app = SooxApp()
    app.mainloop()
