import Tkinter as tk
import tkMessageBox as mb

def DlaRafalaAkcja():
    okno=mb.showinfo(title='Czesc Rafalku', message='co slychac? fajny guziczek, nie? :P')

def DlaMonikiAkcja():
    if DlaMoniki.get()=='Monika':
        okno1=mb.showinfo(title='Czesc Monisiu', message='co slychac? fajne poletko tekstowe, nie? :P')
    else:
        okno2=mb.showinfo(title='Czesc', message='Nie jestes Monika!!!')

GUI=tk.Tk()
GUI.geometry('400x400')
GUI.title("Dla Rafala i Moniki")

DlaRafala = tk.Button(text='Dla Rafalka', command=DlaRafalaAkcja).place(x=190,y=190)

Podpis=tk.Label(text='Podaj swoje imie:').place(x=10, y=280)

DlaMoniki=tk.Entry()
DlaMoniki.place(x=10, y=300)

Sprawdz = tk.Button(text='Sprawdz', command=DlaMonikiAkcja).place(x=100, y=300)

GUI.mainloop()
