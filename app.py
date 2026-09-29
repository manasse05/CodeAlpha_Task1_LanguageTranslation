import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Langues proposées : nom affiché -> code utilisé par le service de traduction
LANGUES = {
    "Français": "fr",
    "Anglais": "en",
    "Espagnol": "es",
    "Allemand": "de",
    "Italien": "it",
    "Portugais": "pt",
    "Arabe": "ar",
    "Chinois": "zh-CN",
}


def traduire():
    # Récupère le texte saisi (de la première ligne jusqu'à la fin) et enlève les espaces inutiles
    texte = zone_entree.get("1.0", tk.END).strip()

    # Si l'utilisateur n'a rien écrit, on l'avertit et on s'arrête
    if not texte:
        messagebox.showwarning("Attention", "Écris un texte à traduire.")
        return

    # Transforme les noms choisis (ex: "Français") en codes (ex: "fr")
    source = LANGUES[langue_source.get()]
    cible = LANGUES[langue_cible.get()]

    try:
        # Envoie le texte au service de traduction et récupère la réponse
        resultat = GoogleTranslator(source=source, target=cible).translate(texte)
    except Exception:
        # En cas de problème (pas de wifi, service indisponible...), on affiche un message clair
        messagebox.showerror("Erreur", "La traduction a échoué. Vérifie ta connexion internet.")
        return

    # Affiche le résultat : on débloque la zone, on efface l'ancien texte, on écrit, on la reverrouille
    zone_sortie.config(state="normal")
    zone_sortie.delete("1.0", tk.END)
    zone_sortie.insert(tk.END, resultat)
    zone_sortie.config(state="disabled")


def copier():
    # Récupère le texte traduit et le place dans le presse-papiers
    resultat = zone_sortie.get("1.0", tk.END).strip()
    if resultat:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(resultat)
        messagebox.showinfo("Copié", "Traduction copiée dans le presse-papiers.")


def inverser():
    # Échange la langue source et la langue cible
    ancienne_source = langue_source.get()
    langue_source.set(langue_cible.get())
    langue_cible.set(ancienne_source)


# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Outil de traduction - CodeAlpha")
fenetre.geometry("600x520")
fenetre.configure(padx=15, pady=15)

# Choix des langues
langue_source = tk.StringVar(value="Français")
langue_cible = tk.StringVar(value="Anglais")

cadre_langues = tk.Frame(fenetre)
cadre_langues.pack(fill="x")

ttk.Label(cadre_langues, text="De :").pack(side="left")
ttk.Combobox(
    cadre_langues, textvariable=langue_source,
    values=list(LANGUES.keys()), state="readonly", width=12
).pack(side="left", padx=5)

ttk.Button(cadre_langues, text="⇄", width=4, command=inverser).pack(side="left", padx=5)

ttk.Label(cadre_langues, text="Vers :").pack(side="left")
ttk.Combobox(
    cadre_langues, textvariable=langue_cible,
    values=list(LANGUES.keys()), state="readonly", width=12
).pack(side="left", padx=5)

# Zone où l'utilisateur écrit son texte
ttk.Label(fenetre, text="Texte à traduire :").pack(anchor="w", pady=(15, 0))
zone_entree = tk.Text(fenetre, height=8, wrap="word")
zone_entree.pack(fill="x")

# Bouton de traduction
ttk.Button(fenetre, text="Traduire", command=traduire).pack(pady=10)

# Zone où s'affiche la traduction (verrouillée pour éviter les modifications)
ttk.Label(fenetre, text="Traduction :").pack(anchor="w")
zone_sortie = tk.Text(fenetre, height=8, wrap="word", state="disabled")
zone_sortie.pack(fill="x")

# Bouton pour copier la traduction
ttk.Button(fenetre, text="Copier la traduction", command=copier).pack(pady=10)

# Lance l'application
fenetre.mainloop()