#Arhur Hernandez Exercise 3 AST - 451
from os import name
import numpy as np

#the matplotlib package contains Python tools for plotting
import matplotlib.pyplot as plt
import pandas as pd
import math

# debs.csv has header:   name,logm1,logm2,lograd1,lograd2
starlist = pd.read_csv("debs.csv")
#instantiate and set beta values
b1 = 4
b2 = 17 

# r = m**(b1 - 1) / (b1 + 3)
#plot through the different ranges specific to solar mass and radii 
#since range method doesnt allow for float values I created a list to pass from .1 to 1

lowMassStars = [.1,.2,.3,.4,.5,.6,.7,.8,.9]
#to 101 to include 100
for m in range(0,101):
    #if mass is less than 1 use the low mass star list and b = 4 
    if m < 1:
        for l in lowMassStars:
            plt.plot(l,l**((b1 - 1) / (b1 + 3)),'ro') 
    #else if mass is less than or equal to 20 and b = 17      
    elif m <= 20:
        plt.plot(m,m**((b2 - 1) / (b2 + 3)),'ro') 
    #else if mass is divisible by 10 (increment by 10) to 100 and b = 4  
    elif m % 10 == 0:
        plt.plot(m,m**((b2 - 1) / (b2 + 3)),'ro') 

#I am not sure if this is the "correct" implementation suggested in the rubric
#in case it isn't I decided to write another implementation located at the bottom of this assignment

#plot the star points
#since this data is already in logarithmic i will inverse log it (assuming its in log base 10)

for x in starlist["name"]:
    plt.plot(10**starlist["logm1"],10**starlist["lograd1"], 'go') 
    plt.plot(10**starlist["logm2"],10**starlist["lograd2"], 'bo') 

#no need  to set x and y limits the regular ones seem fine
#logarithmic scales 
plt.yscale("log")
plt.xscale("log")

#set plot labels, title, and legend 
plt.xlabel('Log(Solar Masses)')
plt.ylabel('Log(Solar Radii)')
plt.title('Mass-Radius Relation for Stars')

#in order to create a legend, I have to map a color to the lists outside of for loop, I duplicated one of each
plt.plot(10**starlist["logm1"][1],10**starlist["lograd1"][2], 'go',label="Binary Star set1")
plt.plot(10**starlist["logm2"][1],10**starlist["lograd2"][2], 'bo',label="Binary Star set2")
plt.plot(.1,.1**((b1 - 1) / (b1 + 3)),'ro',label="Mass Radius Relation") 
plt.legend(loc="lower right",)
#show the plot
plt.show()
#save as pdf
plt.savefig('MassRadiusRelation.pdf')


#second implementation
#lowMassStars = [.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
#for i in lowMassStars:
#    print("h")
#for loop for masses/radii 2-19 increment by 1
#for j in range(2,19,1):
#    print("h")
#for loop for masses/radii 20-100 increment by 10
#for k in range(20,110,10):
#    print("h")
