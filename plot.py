#!/usr/bin/env python3

import sys
import json
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

print("\n\n")

with open('/media/DATA/MEGA/Calendar.json', 'r') as f:
    dataArray = json.load(f)
    lastDate = datetime.strptime(dataArray[-1]['fecha'], "%Y-%m-%d").date()

    if len(sys.argv) == 1:
        print("Introduce start date (yyyy-mm-dd) and optionally end date")
        startIndex = -100
        endIndex = -1
    else:
        startDate = datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
        startIndex = (startDate - lastDate).days - 1
        if len(sys.argv) > 2:
            endDate = datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
        else:
            endDate = lastDate
        endIndex = (endDate - lastDate).days - 1

    fechas = []
    notas = []
    notas_pain = []
    for dayIndex in range(startIndex, endIndex + 1):
        fechas.append(dataArray[dayIndex]['fecha'])
        notas.append(dataArray[dayIndex]['nota'])
        if dataArray[dayIndex]['pain']:
            notas_pain.append(dataArray[dayIndex]['nota'])
        else:
            notas_pain.append(-1)

fig, ax = plt.subplots()

ax.plot(fechas, notas, '*-')
ax.plot(fechas, notas_pain, 'r*')

ticks = np.linspace(0, len(fechas)-1, 5)
ticks = [int(tick) for tick in ticks]
labels = [fechas[tick] for tick in ticks]
plt.xticks(ticks, labels)

ax.set_ylim([0, 10])
ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.yaxis.grid()
plt.tight_layout()
plt.show()

print("\n\n")