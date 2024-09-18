import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
aqi_reading = abs(np.random.randint(50,500,1440) + np.random.normal(0,1,1440))
print(aqi_reading)
smoothAqi = signal.savgol_filter(aqi_reading,51,5)
print(smoothAqi)
def hourly_avg(sig):
    sum=0
    c=1
    avgArray = []
    for n in len(sig):
        if((len(sig) % 60) != 0):
            sum = sum + sig[n]
        else:
            avgArray[c-1] = sum/60
            sum=0
            c=c+1
    return avgArray
def excessAqi(sig):
    c=0
    excess_time_stamp = []
    for n in sig:
        if(n>200):
            if(c>15):
                excess_time_stamp.append[n]
            else:
                c=c+1
        else:
            c=0
    return excess_time_stamp
plt.figure()
plt.plot(aqi_reading,color = "blue")
plt.plot(smoothAqi,color ="green")
plt.plot()
