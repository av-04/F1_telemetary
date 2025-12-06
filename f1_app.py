import pandas as pd
import matplotlib.pyplot as plt
import streamlit as sd
import fastf1
import fastf1.plotting 
import numpy as np
import os
sd.set_page_config(page_title="F1_telemetary_comparisions", layout="wide")

cache_dir='cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
fastf1.Cache.enable_cache(cache_dir)

@sd.cache_data
def load_session(year, gp, session_type):
    session=fastf1.get_session(year, gp, session_type)
    session.load()
    return session

sd.sidebar.title("telemetary settings")
grand_prix = sd.sidebar.text_input("Race Location", "Monaco")
year=sd.sidebar.selectbox("Year",[2020,2021,2022,2023,2024])
session_map = {
    "Race": "R",
    "Qualifying": "Q",
    "Sprint": "S",
    "FP1": "FP1",
    "FP2": "FP2",
    "FP3": "FP3"
}
session_name = sd.sidebar.selectbox("Session", list(session_map.keys()), index=1)
session_identifier = session_map[session_name]
d1 = sd.sidebar.text_input("Driver 1 (e.g., VER)", "VER")
d2 = sd.sidebar.text_input("Driver 2 (e.g., HAM)", "HAM")

sd.title(f"F1_telemetary_comparisions :{d1}vs{d2}")
sd.write(f"**Event:** {year}{grand_prix}-{session_name}")
if sd.sidebar.button("Load Telemetry"):
    
    # Loading
    with sd.spinner(f"Searching for '{grand_prix}' in {year}..."):
        session = load_session(year, grand_prix, session_identifier)

    # Validation
    if session:
        sd.success(f"Found Session: {session.event['EventName']}")
        
        with sd.spinner("Processing Telemetry..."):
            try:
               
                laps_d1 = session.laps.pick_driver(d1).pick_fastest()
                laps_d2 = session.laps.pick_driver(d2).pick_fastest()

                
                if laps_d1 is None:
                    sd.error(f"Driver {d1} not found or set no time.")
                    sd.stop()
                if laps_d2 is None:
                    sd.error(f"Driver {d2} not found or set no time.")
                    sd.stop()

                # Telemetry
                tel_d1 = laps_d1.get_car_data().add_distance()
                tel_d2 = laps_d2.get_car_data().add_distance()

                sd.subheader(f"Speed Trace: {d1} vs {d2}")
                fig1, ax1 = plt.subplots(figsize=(10, 5))
                
                
                color1 = fastf1.plotting.get_driver_color(d1, session=session)
                color2 = fastf1.plotting.get_driver_color(d2, session=session)
                
                ax1.plot(tel_d1['Distance'], tel_d1['Speed'], color=color1, label=d1)
                ax1.plot(tel_d2['Distance'], tel_d2['Speed'], color=color2, label=d2)
                ax1.set_xlabel("Distance (m)")
                ax1.set_ylabel("Speed (km/h)")
                ax1.legend()
                ax1.grid(True, linestyle='--', alpha=0.5)
                
                sd.pyplot(fig1)

                # Delta 
                sd.subheader("Time Delta (Gap)")
                sd.caption(f"Negative (Color 1) = {d1} is Ahead | Positive (Color 2) = {d2} is Ahead")

                max_dist = max(tel_d1['Distance'].max(), tel_d2['Distance'].max())
                dist_grid = np.linspace(0, max_dist, int(max_dist))
                
                time_d1 = np.interp(dist_grid, tel_d1['Distance'], tel_d1['Time'].dt.total_seconds())
                time_d2 = np.interp(dist_grid, tel_d2['Distance'], tel_d2['Time'].dt.total_seconds())
                
                delta = time_d2 - time_d1 
                
                fig2, ax2 = plt.subplots(figsize=(10, 4))
                ax2.plot(dist_grid, delta, color='white', linewidth=1)
                ax2.axhline(0, color='gray', linestyle='--')
                
                ax2.fill_between(dist_grid, 0, delta, where=delta<0, color=color1, alpha=0.3)
                ax2.fill_between(dist_grid, 0, delta, where=delta>0, color=color2, alpha=0.3)
                
                ax2.set_facecolor('black') 
                ax2.set_ylabel("Gap (seconds)")
                ax2.set_xlabel("Distance (m)")
                
                sd.pyplot(fig2)
            
            except Exception as e:
                sd.error(f"An error occurred during plotting: {e}")

    else:
        sd.warning(f"Could not find a race named '{grand_prix}' in {year}. Please check your spelling.")

else:
    sd.info("Enter the Race Location in the sidebar and click 'Load Telemetry'")
