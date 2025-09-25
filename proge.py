import tkinter as tk
from PIL import Image, ImageTk

# Loome akna
aken = tk.Tk()
aken.title("SööX")
aken.configure(bg="white")
aken.geometry("900x800")  # Piisavalt ruumi pildile ja tekstile

# --- Vasak pool (tekst + nupud) ---

vasak_frame = tk.Frame(aken, bg="white")
vasak_frame.pack(side="left", padx=40, pady=40, anchor="n")

# Pealkiri
pealkiri = tk.Label(vasak_frame, text="Vasta küsimustele", font=("Arial", 40, "bold"), bg="white")
pealkiri.pack(anchor="w")

# Küsimus
kuul = tk.Label(vasak_frame, text="Millist sorti sööki soovid?", font=("Arial", 20), bg="white")
kuul.pack(anchor="w", pady=(10, 20))

# Funktsioonid nuppudele
def vali_magus():
    print("Valisid: Magus")

def vali_soolane():
    print("Valisid: Soolane")

# Nupu loomise abifunktsioon
def loo_nupp(text, command):
    raam = tk.Frame(vasak_frame, bg="black", padx=2, pady=2)
    nupp = tk.Button(raam, text=text, font=("Arial", 20, "bold"), bg="#add8e6", fg="black",
                     bd=0, width=20, command=command)
    nupp.pack()
    raam.pack(pady=5)
    return raam

# Nupud
loo_nupp("Magus", vali_magus)
loo_nupp("Soolane", vali_soolane)

# --- Parem pool (pilt) ---

parem_frame = tk.Frame(aken, bg="white")
parem_frame.pack(side="right", padx=20, pady=20)

# Laeme ja kuvame pildi
from PIL import Image, ImageTk

try:
    orig_img = Image.open("burx.png")
    suurus = (400, 400)
    img = orig_img.resize(suurus, Image.Resampling.LANCZOS)  # uus viis Pillow'ga
    tk_img = ImageTk.PhotoImage(img)

    pildi_label = tk.Label(parem_frame, image=tk_img, bg="white")
    pildi_label.image = tk_img  # HOIAB VIITE ALLES!
    pildi_label.pack()

except Exception as e:
    print("Viga pildi laadimisel:", e)
    error_label = tk.Label(parem_frame, text="Pildi laadimine ebaõnnestus", fg="red", bg="white")
    error_label.pack()


# Käivitame akna
aken.mainloop()
