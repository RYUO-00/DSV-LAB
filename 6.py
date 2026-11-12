# Experiment 6: Draw dot plots and heatmaps using the geoplotlib library
#
# Install first (run in the terminal, not in this file):
#   pip uninstall pyglet -y
#   pip install pyglet==1.5.27
#   pip install geoplotlib pandas
#
# Needs 'bus.csv' in the same folder.
import pyglet
print(pyglet.version)

import geoplotlib
from geoplotlib.utils import DataAccessObject
print("geoplotlib imported successfully")

import pandas as pd

try:
    # ---------- Read the dataset ----------
    data = pd.read_csv('bus.csv')

    # ---------- Add dummy coordinates if lat/lon columns are missing ----------
    if 'lat' not in data.columns or 'lon' not in data.columns:
        print("Adding dummy geographical data ('lat' and 'lon') for testing...")

        # Bengaluru, Chennai, Delhi, Mumbai, Kolkata
        lat_values = [12.9716, 13.0827, 28.7041, 19.0760, 22.5726]
        lon_values = [77.5946, 80.2707, 77.1025, 72.8777, 88.3639]

        # repeat the 5 coordinates for all rows
        data['lat'] = [lat_values[i % 5] for i in range(len(data))]
        data['lon'] = [lon_values[i % 5] for i in range(len(data))]

        # save the modified dataset
        data.to_csv('bus_with_coords.csv', index=False)

    # ---------- Create data access object ----------
    geodata = DataAccessObject.from_dataframe(data)

    # ---------- Dot plot (close the window to see the heatmap) ----------
    geoplotlib.dot(geodata)
    geoplotlib.show()

    # ---------- KDE heatmap ----------
    geoplotlib.kde(geodata, bw=5, cut_below=1e-4, cmap='hot')
    geoplotlib.show()

except FileNotFoundError:
    print("Error: The file 'bus.csv' was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
