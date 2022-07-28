import numpy as np
#the matplotlib package contains Python tools for plotting
import matplotlib.pyplot as plt
import pandas as pd
import math
#read in the Ex1.csv file.
#column headings = Name, LHS, Parallax, SpType, Bmag, Vmag
#"pd.read.csv" tells Python to execute the read.csv tool in the pandas library
starlist = pd.read_csv("Ex1.csv")

#compute the B-V color of each star.
color = starlist['Bmag'] - starlist['Vmag']
#compute the color correction
bc = -2.1 * color ** 4 + 6.1 * color ** 3 - 6.3 * color ** 2 + 2.1 * color - .15

#compute the absolute V magnitude of each star.
#remember:  m-M=5log10(distance/10)
#"np.log10" tells Python to execute the log10 function in numpy
absmag = starlist['Vmag'] - 5.0*np.log10(1.0/(starlist['Parallax']*10.))

##Temperature = -1700*(B-V)3 + 6300*(B-V)2 -9100*(B-V) + 9500
temp = -1700 * color ** 3 + 6300 * color ** 2 - 9100 * color + 9500

# the mbol equals the abs magnitude - the bolemetric correction
mbol = absmag + bc 

#tell python to make a plot
#`plt.ion()
#calculate the luminosity 
lum = 10**(-.4*(mbol - 4.74))
#plot the B-V color on the x-axis and absolute V magnitude on the y-axis.
#the 'bo' indicates that the points should be plotted with blue circles.
#the "plt" tells Python the commands are in matplotlib
##plt.plot(color, absmag, 'bo')
plt.plot(temp, lum, 'bo')
# scale the axis
plt.xscale("log")
plt.yscale("log")

#set the limits on the x- and y-axes.
#note that the y-axis is plotted with larger magnitudes on the bottom.
#plt.axis([min(bc),max(bc),min(temp),max(temp)])

#invert x-axis making sure to add some padding for the min and the max temperatures. 
plt.xlim(max(temp+ 10**3), min(temp - 10**2))

#make sure the tick marks on both axes point inside the plot.
plt.tick_params(which='both', direction='in') 


#label the x and y axes
plt.xlabel('Temperature')
plt.ylabel('Log (Luminosity)')
#produce the plot
#save the plot as a pdf file.  Other options include png, ps, eps, and jpg.
plt.savefig('CMD.pdf')

plt.show()
