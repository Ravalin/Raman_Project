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

def main():
    names=[]
    names.append("polySilowstress.txt")
    for name in names:
        a=fit_parameters(name)
        print(a.Xex)
        a.perform_fitting()
        a.plot()
class fit_parameters:

    def __init__(self,name):
        self.name=name
        self.Dane=[]
        self.Xex=[]
        self.Yex=[]
        self.popt=[]
        self.pcov=[]
        self.Xfit=[]
        self.Yfit=[]

        self.Dane=np.loadtxt(name)
        self.Dane=self.Dane[np.argsort(self.Dane[:,2])]
        self.Xex=self.Dane[:, 2]
        self.Yex=self.Dane[:, 3]

    def fit_function(self,x,loc_par,gamma,height,offset):
        return height*gamma**2/((x-loc_par)**2+gamma**2)+offset

    def perform_fitting(self):
        Xbool=(self.Xex<600)*(self.Xex>400)
        self.Xfit=self.Xex[Xbool]
        self.Yfit=self.Yex[Xbool]
        n=len(self.Dane[Xbool])

        mean=sum(self.Xfit)/n #loc_par
        sigmal=math.sqrt(sum((self.Xfit-mean)**2)/n)

        self.popt,self.pcov=curve_fit(self.fit_function,self.Xfit,self.Yfit,p0=[mean,sigmal,max(self.Yfit),0])
        #NAJWAZNIEJSZA LINIJKA
        loc_par_fit,gamma_fit,height_fit,offset1_fit=self.popt
    def plot(self):
        plt.title(u"Lorenz function fit")
        plt.plot(self.Xex,self.Yex,"o",label="dane z pliku",color="c")
        plt.plot(self.Xfit,self.fit_function(self.Xfit,self.popt[0],self.popt[1],self.popt[2], self.popt[3]),linewidth="3.0",color="m",label='fit')
        plt.legend()
        plt.text(100, 20200, r'$\ x_0= %.3f,\u0263 = %.3f$' %(self.popt[0], math.fabs(self.popt[1])))
        #plt.savefig(name+".png", bbox_inches='tight')
        plt.show()

main()