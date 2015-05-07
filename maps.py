from pylab import *
import matplotlib.colors
#GLOWNA FUNKCJA, PEWNIE DA RADE TO ROZWIAZAC W BARDZIEJ ELEGANCKI SPOSOB
def main():
    #PRZYKLADOWE DANE DLA JEDNEGO PARAMETRU
    #W KAZDEJ LISCIE SA DANE Z JEDNEGO "WIERSZA" PROBKI
    data=([10.0,3.9,3.0,6.8,7.5],
          [1.8,5.9,3.4,7.5,5.0])
    #TE DWIE (TRZY?) WARTOSCI POWINIEN PODAWAC UZYTKOWNIK
    umin=0
    umax=10
    av_norm=0.5
    try:
        #av_norm=middle_point(data)
        make_map(data,umin,umax,av_norm)
    except ValueError:
        print("ValueError!")
        exit(1)
#FUNKCJA ZNAJDUJACA SREDNIA/DLUGOSC TABLICY
#WARTOSC TA DAJE NAM SRODEK NA PASKU KOLORU
def middle_point(data):
        av_norm=0.5
        av_data=average(data)
        length=0
        for i in data:
            for j in i:
                length+=1
        if length !=0:
            av_norm=av_data/length
            return av_norm
        else:
            return None
def make_map(data,vmin=0.0,vmax=1.0,av=0.5):
    data_array=np.array(data)
    #USTAWIENIE KOLOROWANIA
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
    pcolor(data_array,cmap=my_cmap,vmin=vmin,vmax=vmax)
    colorbar()
#URUCHOMIENIE PROGRAMU
main()