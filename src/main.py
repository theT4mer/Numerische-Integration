# you might have to install these three dependencies manually, just google them
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
dataframe = pd.read_csv('Daten_TV.txt', header=None) # just replace my path with yours

data_points = dataframe.values  # we want to access the values provided by Gerky

# for debugging purposes only, you can commt this out but it does not hurt
for i in range(0, len(data_points)):
    print(data_points[i]) 

plt.figure(figsize=(10, 6))
plt.plot(range(len(data_points)), data_points, 'ro') 
plt.xlabel('Index')
plt.ylabel('Beatiful Values')
plt.title("Gerky's great and wonderful data")
plt.grid()
plt.show()