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


def fit_function(x,loc_par,gamma,height,offset):
    return height*gamma**2/((x-loc_par)**2+gamma**2)+offset

def perform_fitting(RamanShift, Intensity, MaxRamanShift, MinRamanShift):
    Xbool=(RamanShift<MaxRamanShift)*(RamanShift>MinRamanShift)
    Xfit=RamanShift[Xbool]
    Yfit=Intensity[Xbool]
    n=len(Xfit)

    mean=sum(Xfit)/n #loc_par
    sigmal=math.sqrt(sum((Xfit-mean)**2)/n)

    popt,pcov=curve_fit(fit_function,Xfit,Yfit,p0=[mean,sigmal,max(Yfit),0])
        #NAJWAZNIEJSZA LINIJKA
    loc_par_fit,gamma_fit,height_fit,offset1_fit=popt

    #plt.title(u"Lorenz function fit")
    #plt.plot(RamanShift,Intensity,"o",label="dane z pliku",color="c")
    #plt.plot(Xfit,fit_function(Xfit,popt[0],popt[1],popt[2], popt[3]),linewidth="3.0",color="m",label='fit')
    #plt.legend()
    #plt.text(100, 20200, r'$\ x_0= %.3f,\u0263 = %.3f$' %(popt[0], math.fabs(popt[1])))
        #plt.savefig(name+".png", bbox_inches='tight')
    #plt.show()
    return popt
