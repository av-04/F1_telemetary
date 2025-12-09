import fastf1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def plot_racing_line(session, driver):
    try:
        lap = session.laps.pick_driver(driver).pick_fastest()
        telemetry = lap.get_telemetry()
    
        x = telemetry['X'].values
        y = telemetry['Y'].values
        speed = telemetry['Speed'].values

        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Plot the colorful line
        norm = plt.Normalize(speed.min(), speed.max())
        lc = LineCollection(segments, cmap='YlGn', norm=norm, linewidth=5)
        lc.set_array(speed)
        line = ax.add_collection(lc)
        
        # Colorbar
        cbar = fig.colorbar(line, ax=ax)
        cbar.set_label('Speed (km/h)', color='white')
        cbar.ax.yaxis.set_tick_params(color='white')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

        # 1. Label Start/Finish Line
        ax.scatter(x[0], y[0], color='white', s=100, marker='x', zorder=10)
        ax.text(x[0], y[0], '  Start/Finish', color='white', fontsize=9, va='center')

        # 2. Add Descriptive Text Box
        text_str = f"Driver: {driver}\n\nColor Guide:\n💚 Green = High Speed\n💛 Yellow = Low Speed"
        ax.text(0.02, 0.95, text_str, transform=ax.transAxes, 
                color='white', fontsize=10, va='top',
                bbox=dict(boxstyle='round', facecolor='black', alpha=0.7, edgecolor='gray'))
    
        # Styling
        ax.set_aspect('equal') 
        ax.set_facecolor('black')
        fig.patch.set_facecolor('black')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"Fastest Lap Analysis: {driver}", color='white', fontsize=14)

        ax.autoscale_view()

        return fig
        
    except Exception as e:
        print(f"Error plotting racing line: {e}")
        return None
