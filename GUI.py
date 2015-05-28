import Tkinter as tk
import tkMessageBox as mb
import numpy as np
from Tkinter import *
import createMap as cM
from pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import maps1

def map():
    f=Figure()
    a=f.add_subplot(1,1,1)
    data=cM.createMap(NazwaPlikutxt.get(), int (wartpocztxt.get()), int (wartkonctxt.get()))
    data_array=np.array(data)
    av=0.5
    cdict = {'red': ((0.0, 0.0, 0.0),
                     (av, 1.0, 1.0),
                      (1.0, 0.0, 0.0)),
              'green': ((0.0, 0.0, av),
                          (av, 1.0, 1.0),
                          (1.0, av, 0.0)),
               'blue': ((0.0, 0.0, 0.0),
                         (av, 1.0, 1.0),
                        (1.0, 0.0, 0.0))}
    #UTWORZENIE MAPY I PLIKU GRAFICZNEGO
    my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    b=a.pcolor(data_array,cmap=my_cmap,vmin=maps1.minimum(data),vmax=maps1.maximum(data))
    f.colorbar(b)
    canvas = FigureCanvasTkAgg(f, master=GUI)
    canvas.get_tk_widget().place(x=0, y=0)


GUI=tk.Tk()

GUI.geometry('900x500')
GUI.title("RamanMaps")

NazwaPliku=tk.Label(text='File name:')
NazwaPliku.place(x=680, y=10)
NazwaPlikutxt=tk.Entry()
NazwaPlikutxt.place(x=680, y=30)
NazwaPlikutxt.insert(0,"polySilowstress.txt")

wartpocz=tk.Label(text='Initial Raman Shift [cm^-1]:')
wartpocz.place(x=680, y=60)
wartpocztxt=tk.Entry()
wartpocztxt.place(x=680, y=80)
wartpocztxt.insert(0, "400")

wartkonc=tk.Label(text='Final Raman Shift [cm^-1]:')
wartkonc.place(x=680, y=110)
wartkonctxt=tk.Entry()
wartkonctxt.place(x=680, y=130)
wartkonctxt.insert(0, "600")

mapuj = tk.Button(text='Create map', command=map).place(x=680, y=300)

GUI.mainloop()


