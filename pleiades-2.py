#the matplotlib package contains Python tools for plotting
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
#read the star file
stars = pd.read_csv("pleiades.csv")

#function to plot each point with paramenters star type wanted and color it should be set to 
def starType(type,color):
    #get a sublist of the startype we are looking for
    starsList = stars[stars["SpType"].str[0:1] == type]
    #for every star in that sublist
    for n in starsList:
        #plot it using the RA and DEC (x,y) and make the point size 1.4 exponential porportional to its visual magnitude, and set the color
        plt.scatter(starsList["RA (2000)"], starsList["Dec(2000)"], s= 1.4**starsList["Vmag"], c=color)

# using the function to plot all types of stars
starType("~","black")
starType("O","blue")
starType("B","cyan")
starType("A","green")
starType("F","yellow")
starType("G","gold")
starType("K","orange")
starType("M","red")

#create a legend for the plot
plt.scatter(stars["RA (2000)"][0], stars["Dec(2000)"][0], s= 1.4**stars["Vmag"][0], c='black', label="Not Specified")
# there are no O type stars plt.scatter(stars["RA (2000)"][54], stars["Dec(2000)"][54], s= 1.3**stars["Vmag"][54], c='green', label="O")
plt.scatter(stars["RA (2000)"][58], stars["Dec(2000)"][58], s= 1.4**stars["Vmag"][58], c='cyan', label="B")
plt.scatter(stars["RA (2000)"][55], stars["Dec(2000)"][55], s= 1.4**stars["Vmag"][55], c='green', label="A")
plt.scatter(stars["RA (2000)"][74], stars["Dec(2000)"][74], s= 1.4**stars["Vmag"][74], c='yellow', label="F")
plt.scatter(stars["RA (2000)"][91], stars["Dec(2000)"][91], s= 1.4**stars["Vmag"][91], c='gold', label="G")
plt.scatter(stars["RA (2000)"][107], stars["Dec(2000)"][107], s= 1.4**stars["Vmag"][107], c='orange', label="K")
plt.scatter(stars["RA (2000)"][138], stars["Dec(2000)"][138], s= 1.4**stars["Vmag"][138], c='red', label="M")

#labeling and showing the plot
plt.xlabel('right ascension')
plt.ylabel('declination ')
plt.title('Pleiades Finding Chart ')
plt.legend(loc="lower right", ncol = 1,framealpha=0.5)
plt.show()