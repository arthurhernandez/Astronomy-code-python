#Arthur Hernandez
# python excersise 6
# Mon dec 2nd 

from os import name
import numpy as np

#the matplotlib package contains Python tools for plotting
import matplotlib.pyplot as plt
import pandas as pd
import math

#opening and reading the file
starlist = pd.read_csv("51peg.csv")

#Determining the standard deviation of the risiduals

phase = np.arange(4.1, 4.4, 0.3)

arr = np.array(phase,starlist["RV (m/s)"])
deviation = np.std(arr)
RV = 63 * np.sin(2 * np.pi * deviation) + 9
print(RV)

plt.plot(starlist["Day"], starlist["RV (m/s)"],'b-') 
plt.plot(starlist["Day"], 63 * np.sin(2 * np.pi * starlist["RV (m/s)"] +9 ),'g-') 
plt.plot(starlist["Day"], 63 * np.sin(2 * np.pi * starlist["RV (m/s)"] +9 ),'g-') 

#plt.plot(deviation, starlist["Day"],'g-') 
plt.xlim([0, 33])

plt.xlabel('standard deviation residuals')
plt.ylabel('Period')
plt.title('Standard Deviation Residuals Vs. Period')

plt.show()
