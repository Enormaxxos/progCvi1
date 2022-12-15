import tkinter as tk
import json

window = tk.Tk()
window.option_add('*Font', 'Arial 9')

window.columnconfigure([0, 1, 2, 3], minsize=100)

jmeno_label = tk.Label(window, text='Jméno:').grid(row=0)
jmeno_entry = tk.Entry(window)
jmeno_entry.grid(row=0, column=1)

prijmeni_label = tk.Label(window, text='Příjmení:').grid(row=0, column=2)
prijmeni_entry = tk.Entry(window)
prijmeni_entry.grid(row=0, column=3)

telefon_label = tk.Label(window, text='Telefon:').grid(row=1)
telefon_entry = tk.Entry(window)
telefon_entry.insert(0, '+420')
telefon_entry.grid(row=1, column=1)

def odesli():
    newDict = {
        "jmeno":jmeno_entry.get(),
        "prijmeni":prijmeni_entry.get(),
        "telefon":telefon_entry.get()
    }
    with open("output.json","w") as o:
        json.dump(newDict,o,ensure_ascii=False)        


tk.Button(window, text=u"Odešli", width=10, command=odesli).grid(row=3, column=3)

tk.mainloop()