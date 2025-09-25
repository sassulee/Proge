import tkinter as tk

# Funktsioon, mis avaneb, kui "Alusta!" nuppu vajutada
def avane_järgmine_leht():
    # Peamine aken (sulgeb esimesed lehe komponendid)
    for widget in root.winfo_children():
        widget.destroy()

    # Järgmine leht: küsimus ja nupud
    label_kyssa = tk.Label(root, text="Vasta küsimusele:", font=("Arial", 18), bg="white")
    label_kyssa.pack(pady=10, anchor="w", padx=20)

    label_question = tk.Label(root, text="Milline söögikord on?", font=("Arial", 24), bg="white")
    label_question.pack(pady=20, anchor="w", padx=20)

    # Nupud teisel lehel, türkiissinised
    button_hommikusook = tk.Button(root, text="Hommikusöök", font=("Arial", 16), bg="turquoise", command=lambda: valitud_soogikord("Hommikusöök"))
    button_hommikusook.pack(pady=10, anchor="w", padx=20)

    button_lounasook = tk.Button(root, text="Lõunasöök", font=("Arial", 16), bg="turquoise", command=lambda: valitud_soogikord("Lõunasöök"))
    button_lounasook.pack(pady=10, anchor="w", padx=20)

    button_ohtusook = tk.Button(root, text="Õhtusöök", font=("Arial", 16), bg="turquoise", command=lambda: valitud_soogikord("Õhtusöök"))
    button_ohtusook.pack(pady=10, anchor="w", padx=20)

# Funktsioon, et tagastada valitud söögikord ja kuvada teade
def valitud_soogikord(soogikord):
    for widget in root.winfo_children():
        widget.destroy()

    label_soogikord = tk.Label(root, text=f"Valisid: {soogikord}", font=("Arial", 24), bg="white")
    label_soogikord.pack(pady=50)

    nupp_tagasi = tk.Button(root, text="Tagasi", font=("Arial", 16), bg="turquoise", command=tagasi_esmaselehele)
    nupp_tagasi.pack(pady=20)
    nupp_edasi = tk.Button(root, text="Edasi", font=("Arial", 16), bg="turquoise", command=edasi_järgmiselehele)
    nupp_tagasi.pack(pady=20)

# Funktsioon, et tagasi minna esmasele lehele
def tagasi_esmaselehele():
    for widget in root.winfo_children():
        widget.destroy()

    # Esimene leht: SööX türkiissinises kastis
    frame_esmane = tk.Frame(root, bg="turquoise")
    frame_esmane.pack(fill="both", expand=True)

    label = tk.Label(frame_esmane, text="SööX", font=("Arial", 40), bg="turquoise", fg="white")
    label.pack(pady=100)

    nupp = tk.Button(frame_esmane, text="Alusta!", font=("Arial", 16), bg="turquoise", command=avane_järgmine_leht)
    nupp.pack(pady=20)

# Funktsioon, et edasi minna järgmisele lehele


# Põhiaken
root = tk.Tk()
root.title("Leht 1")
root.geometry("800x400")
root.configure(bg="white")

# Esimene leht: SööX türkiissinises kastis
frame_esmane = tk.Frame(root, bg="turquoise")
frame_esmane.pack(fill="both", expand=True)

label = tk.Label(frame_esmane, text="SööX", font=("Arial", 40), bg="turquoise", fg="white")
label.pack(pady=100)

# Nupp, mis liigutab järgmisele lehele
nupp = tk.Button(frame_esmane, text="Alusta!", font=("Arial", 16), bg="white", command=avane_järgmine_leht)
nupp.pack(pady=20)

# Käivitame Tkinteri põhitsükkel
root.mainloop()
