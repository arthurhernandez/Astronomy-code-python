#plot the spectrum of a star and fit it with a Planck function
# we want the plank function to cross all 3 at one wavelength, 
#I do not know what I am doing wrong. I think it has to do with 
# the way I am plotting the wavelengths. For now this will have to be my submission. 
# Please let me know how I could have fixed this program 
# normalizing plank functions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
#defining constants
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
#read in the Ex1.csv file.
#column headings = Wavelength,Flux
star = pd.read_csv("star-1.csv")
# get the temperature 
teff=float(input('EnterTemperature:'))
wavelength = star['Wavelength']
def planck(wavelengths, teff):
    #intensity = (2*h*wavelength**3/c**2)*1/(np.exp(h*wavelength/(k*teff)) - 1)
    intensity = (2.0*h*c**2)/((wavelengths**5) * (np.exp(h*c/(wavelengths*k*teff)) - 1.0) )
    return intensity

intensity1 = planck(wavelength, teff-2000)
intensity2 = planck(wavelength, teff+2000)
intensity3 = planck(wavelength, teff)

#plt.ylim(0,5)

plt.plot(wavelength, intensity1, 'g-') 
plt.plot(wavelength, intensity2, 'b-') 
plt.plot(wavelength, intensity3, 'r-')

#plt.xlim(10**10-13, 10**10-19)
#make sure the tick marks on both axes point inside the plot.
plt.tick_params(which='both', direction='in') 
#plt.yscale("log")
#label the x and y axes
plt.xlabel('Wavelength')
plt.ylabel('Log(B(T.I))')
#produce the plot
#save the plot as a pdf file.  Other options include png, ps, eps, and jpg.
plt.savefig('CMD.pdf')

plt.show()
