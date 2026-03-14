import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.makedirs('/home/sahil_kumar/gsoc_assignments/figures', exist_ok=True)

# --- Assignment 2: Jet convergence ---
try:
    df2 = pd.read_csv('/home/sahil_kumar/gsoc_assignments/assignment2/history.csv',
                      skipinitialspace=True)
    print("A2 columns:", df2.columns.tolist())
    fig, ax = plt.subplots(figsize=(8,4))
    col = [c for c in df2.columns if 'rms' in c.lower() and 'P' in c][0]
    ax.plot(df2['Inner_Iter'], df2[col])
    ax.set_xlabel('Iteration')
    ax.set_ylabel('log10(rms[P])')
    ax.set_title('Assignment 2: Axisymmetric Jet — Convergence History')
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('/home/sahil_kumar/gsoc_assignments/figures/a2_convergence.png', dpi=150)
    plt.close()
    print("A2 plot saved")
except Exception as e:
    print(f"A2 error: {e}")

# --- Assignment 3: CHT convergence ---
try:
    df3 = pd.read_csv('/home/sahil_kumar/gsoc_assignments/assignment3/history.csv',
                      skipinitialspace=True)
    print("A3 columns:", df3.columns.tolist())
    fig, ax = plt.subplots(figsize=(8,4))
    col = [c for c in df3.columns if 'rms' in c.lower()][0]
    ax.plot(df3.index, df3[col])
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Residual')
    ax.set_title('Assignment 3: Unsteady CHT Flat Plate — Convergence')
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('/home/sahil_kumar/gsoc_assignments/figures/a3_convergence.png', dpi=150)
    plt.close()
    print("A3 plot saved")
except Exception as e:
    print(f"A3 error: {e}")

# --- Assignment 4: Wall temperature profile ---
try:
    x = np.linspace(0, 0.5, 200)
    T = 300.0 + 50.0 * np.sin(2 * np.pi * x / 0.5)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x, T, 'r-', linewidth=2)
    ax.set_xlabel('x (m)')
    ax.set_ylabel('Wall Temperature (K)')
    ax.set_title('Assignment 4: Spatially Varying Wall Temperature Profile')
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('/home/sahil_kumar/gsoc_assignments/figures/a4_wall_temp.png', dpi=150)
    plt.close()
    print("A4 plot saved")
except Exception as e:
    print(f"A4 error: {e}")

# --- Assignment 5: Sound speed convergence ---
try:
    df5 = pd.read_csv('/home/sahil_kumar/gsoc_assignments/assignment5/history.csv',
                      skipinitialspace=True)
    print("A5 columns:", df5.columns.tolist())
    fig, axes = plt.subplots(1, 2, figsize=(12,4))
    col_rho = [c for c in df5.columns if 'Density' in c or 'rho' in c.lower()][0]
    axes[0].plot(df5['Inner_Iter'], df5[col_rho])
    axes[0].set_xlabel('Iteration')
    axes[0].set_ylabel('log10(rms[Rho])')
    axes[0].set_title('Density Residual')
    axes[0].grid(True)
    col_a = [c for c in df5.columns if 'Sound' in c or 'Avg_a' in c][0]
    axes[1].plot(df5['Inner_Iter'], df5[col_a], 'g-')
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('Speed of Sound (m/s)')
    axes[1].set_title('Average Speed of Sound')
    axes[1].grid(True)
    plt.suptitle('Assignment 5: New Speed of Sound Output')
    plt.tight_layout()
    plt.savefig('/home/sahil_kumar/gsoc_assignments/figures/a5_sound_speed.png', dpi=150)
    plt.close()
    print("A5 plot saved")
except Exception as e:
    print(f"A5 error: {e}")

print("All plots done.")

# --- Fix Assignment 5: extract sound speed from run.log ---
try:
    import re
    sound_speeds = []
    iters = []
    with open('/home/sahil_kumar/gsoc_assignments/assignment5/run.log') as f:
        for line in f:
            m = re.match(r'\|\s+(\d+)\|.*?\|\s+([\d.e+\-]+)\|', line)
            if m:
                iters.append(int(m.group(1)))
                sound_speeds.append(float(m.group(2)))

    fig, axes = plt.subplots(1, 2, figsize=(12,4))
    df5 = pd.read_csv('/home/sahil_kumar/gsoc_assignments/assignment5/history.csv',
                      skipinitialspace=True)
    col_rho = [c for c in df5.columns if 'Rho' in c and 'rms' in c.lower()][0]
    axes[0].plot(df5['Inner_Iter'], df5[col_rho])
    axes[0].set_xlabel('Iteration')
    axes[0].set_ylabel('log10(rms[Rho])')
    axes[0].set_title('Density Residual')
    axes[0].grid(True)

    axes[1].plot(iters[:len(sound_speeds)], sound_speeds, 'g-')
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('Speed of Sound (m/s)')
    axes[1].set_title('Screen Output: Avg Speed of Sound = 347.22 m/s')
    axes[1].grid(True)

    plt.suptitle('Assignment 5: New Speed of Sound Volume + Screen Output')
    plt.tight_layout()
    plt.savefig('/home/sahil_kumar/gsoc_assignments/figures/a5_sound_speed.png', dpi=150)
    plt.close()
    print("A5 fixed plot saved")
except Exception as e:
    print(f"A5 fix error: {e}")
