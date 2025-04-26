#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
from pathlib import Path

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} case_name")
    sys.exit()

case = Path(sys.argv[1])

paths = list(case.glob('**/force.dat'))

if len(paths) == 0:
    print(f"Could not find case: {case}")
    sys.exit(1)

dfs = []
for path in paths:
    df = pd.read_csv(path, sep=r'\s+', comment='#', names=["time","total_x","total_y","total_z","pressure_x","pressure_y","pressure_z","viscous_x","viscous_y","viscous_z"])
    dfs.append(df)

df = pd.concat(dfs)

t0 = np.min(df['time'])
tend = np.max(df['time'])

t = (tend - t0) * 0.95 + t0

df_tail = df[df['time'] > t]

print(f"Mean total force after t={t}: {df_tail['total_x'].mean():.2f}")
print(f"Mean pressure force after t={t}: {df_tail['pressure_x'].mean():.2f}")
print(f"Mean viscous force after t={t}: {df_tail['viscous_x'].mean():.2f}")

plt.figure()
plt.plot(df['time'], df['total_x'],label="total")
plt.plot(df['time'], df['pressure_x'],label="pressure")
plt.plot(df['time'], df['viscous_x'],label="viscous")
plt.title(f"{case}")
plt.xlabel('Timestep')
plt.ylabel('Fx')
plt.legend()
plt.show()
