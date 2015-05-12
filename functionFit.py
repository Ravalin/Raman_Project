from __future__ import unicode_literals
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import rc #used to customize all kinds of properties(size,dpi,color,style,etc.)
import os
from scipy.optimize import curve_fit
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator #do formatowania osi

#rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator
NazwaPliku= "polySilowstress.txt"
Dane=[] #empty table
Dane=np.loadtxt(NazwaPliku)
Dane=Dane[np.argsort(Dane[:,2])]
print Dane
Xex=Dane[:, 2]

Yex=Dane[:, 3]

def fit_function1(x,loc_par,gamma,height,offset):
	return height*gamma**2/((x-loc_par)**2+gamma**2)+offset

def fit_function(x,amplitude,sigmaf,mi,offset):
	return amplitude*np.exp(-(x-mi)**2/2./sigmaf**2)+offset
	
print(len(Xex))
Xbool=(Xex<600)*(Xex>400)
Xfit=Xex[Xbool]
Yfit=Yex[Xbool]
print "to jest  len(Dane[Xbool])",len(Dane[Xbool])
n=len(Dane[Xbool])
print "N jest ", n

mean=sum(Xfit)/n
sigmal=math.sqrt(sum((Xfit-mean)**2)/n)
gammal=1/(math.pi*max(Yfit))
print "to jest mean,sigma,gammal",mean,sigmal,gammal
#print "to jest xfit", Xfit, Yfit
#popt,pcov=curve_fit(fit_function,Xfit,Yfit,p0=[max(Yfit),mean,sigmal,0])
popt,pcov=curve_fit(fit_function,Xfit,Yfit,p0=[max(Yfit),sigmal, mean, 0]) #może można coś z offsetem pokombinować, ale nie wiem, czy tutaj to potrzebne
popt1,pcov1=curve_fit(fit_function1,Xfit,Yfit,p0=[mean,sigmal,max(Yfit),0])
amplitude_fit,sigma_fit,mi_fit,offset_fit=popt
loc_par_fit,gamma_fit,height_fit,offset1_fit=popt1

print popt


plt.title(u"Lorenz function fit")
plt.plot(Xex,Yex,"o",label="dane z pliku",color="c")
plt.plot(Xfit,fit_function1(Xfit,loc_par_fit,gamma_fit,height_fit, offset1_fit),linewidth="3.0",color="m",label='fit')

gamma_abs=math.fabs(gamma_fit)
#plt.plot(Xfit,fit_function(Xfit,amplitude_fit,sigma_fit,mi_fit, offset_fit),label='fit')
plt.legend()
plt.text(100, 20200, r'$\ x_0= %.3f,\u0263 = %.3f$' %(loc_par_fit, gamma_abs))
#czy nie trzeba dac tutaj Xfit???
plt.savefig("Lorentz_fit.png", bbox_inches='tight')
plt.show()

