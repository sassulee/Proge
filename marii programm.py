import tkinter as tk

# Loome peamise akna
aken = tk.Tk()
aken.title("SööX")
aken.configure(bg="#add8e6")  # helesinine värv (light blue)

# Määrame akna suuruse
aken.geometry("900x800")

pealkiri = tk.Label(aken, text="SööX", font=("Arial", 60, "bold"), bg="#add8e6", fg="white")
pealkiri.pack(pady=(70, 100))

nupu_raam = tk.Frame(aken, bg="black", padx=2, pady=2)  # "padx" ja "pady" määravad äärise paksuse
nupu_raam.pack()
alusta_nupp = tk.Button(
    nupu_raam,
    text="Alusta!",
    font=("Arial", 50, "bold"),
    bg="white",
    fg="black",
    bd=0,        # ilma 3D-efektita
    activebackground="lightgray",  # kui soovid klõpsul taustavärvi
)
alusta_nupp.pack()

# Käivitame rakenduse
aken.mainloop()
