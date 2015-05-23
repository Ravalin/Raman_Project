import numpy as np
import maps1
import functionFit1


def createMap(name, minimum, maximum):
    Dane=np.loadtxt(name)
    X=Dane[:,0]
    Y=Dane[:,1]
    RamanShift=Dane[:,2]
    Intensity=Dane[:,3]
    xactual=X[0]
    yactual=Y[0]

    paramerty=[] #do przechowywania parametrow dopasowania
    mean = []
    mean.append([]) #puste tablice (wartosci na x-ach) tablic (wartosci na y-ach)
    sigma =[]
    sigma.append([])
    nx=0    #do numerowania wspolrzednych na mapowanej probce
    ny=0
    npocz=0; #npocz i nkoncowe wyznaczaja zakresy poszczegolnych punktow pomiarowych podczas mapowania
    nkoncowe=0;

    while(nkoncowe<len(X)):#iteruje po tablicy wspolrzednych x-owych i sprawdzam czy x i y sie zmienia, dzielac na poszczegolne pliki
        if X[nkoncowe]==xactual and Y[nkoncowe]==yactual:
            nkoncowe+=1
        elif Y[nkoncowe]!=yactual: #patrze tylko czy y sie zmienia, zmiane x-a sprawdzam pozniej
            yactual=Y[nkoncowe]
            parametry=functionFit1.perform_fitting(RamanShift[npocz:nkoncowe-1], Intensity[npocz:nkoncowe-1], maximum, minimum)
            f = open((str(nx)+"."+str(ny)+".txt"),"w")
            while(npocz<nkoncowe): #zapisywanie do pliku
                f.write(str(X[npocz])+"\t"+str(Y[npocz])+"\t"+str(RamanShift[npocz])+"\t"+str(Intensity[npocz])+"\n")
                npocz+=1
            f.close()
            mean[nx].append(parametry[0])
            if X[nkoncowe]!=xactual: #jesli x tez sie zmienil to zmieniam wspolrzedna x-owa i zeruje y-owa
                nx+=1
                ny=0
                xactual=X[nkoncowe]
                yactual=Y[nkoncowe]
                mean.append([])
            else:   #jesli x sie nie zmienil - zmieniam tylko wspolrzedna y-owa
                ny+=1
                yactual=Y[nkoncowe]
            npocz+=1    #npocz staje sie dawnym n koncowym - poczatek nastepnego zakresu
            nkoncowe+=1

    f = open((str(nx)+"."+str(ny)+".txt"),"w") #ostatni zakres trzeba rozpatrzyc osobno
    parametry=functionFit1.perform_fitting(RamanShift[npocz:nkoncowe-1], Intensity[npocz:nkoncowe-1], maximum, minimum)
    mean[nx].append(parametry[0])
    while(npocz<nkoncowe):
        f.write(str(X[npocz])+"\t"+str(Y[npocz])+"\t"+str(RamanShift[npocz])+"\t"+str(Intensity[npocz])+"\n")
        npocz+=1
    f.close()

    #print(mean)
    try:
        av_norm=maps1.middle_point(mean)
        maps1.make_map(mean,maps1.minimum(mean),maps1.maximum(mean),0.5) #rysowanie mapy
    except ValueError:
        print("ValueError!")
        exit(1)

createMap("polySilowstress.txt", 400, 600)
