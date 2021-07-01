import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

telem = pd.read_csv('test_telem.csv') # TEST TELEMETRY FROM KAGGLE: https://www.kaggle.com/kunalkarnik95/drone-flight-video-with-telemetry-gps-esc
cols = []
for col in telem.columns:
    cols.append(col)
print(list(enumerate(cols)))

latitude = np.array(telem[cols[3]])
longitude = np.array(telem[cols[4]])
altitude = np.array(telem[cols[7]])
speed = np.array(telem[cols[13]])

plt.subplot(2, 2, 1)
plt.title('Latitude', y=1.04)
plt.plot(latitude)

plt.subplot(2, 2, 2)
plt.title('Longitude', y=1.04)
plt.plot(longitude)

plt.subplot(2, 2, 3)
plt.title('Altitude', y=1.04)
plt.plot(altitude)

plt.subplot(2, 2, 4)
plt.title('Speed', y=1.04)
plt.plot(speed)

plt.show()
