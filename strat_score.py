import fastf1
import pandas as pd
import numpy as np

def calc_strat_score(session, driver):
    try:
        laps=session.laps.pick_driver(driver)
        if laps.empty:
            return 1000
        result = session.results.loc[session.results['Abbreviation']==driver].iloc[0]

        #finsihing position
        finish_pos = result['ClassifiedPosition']
        try:
            finish_pos = float(finish_pos)
        except:
            finish_pos = 20.0 # Penalty for DNF
            
        points_finish = (21 - finish_pos) * 25
        
        #grid position and overtakes being done 
        grid_pos=result['GridPosition']
        if grid_pos==0:
            grid_pos=20
        positions_gained=grid_pos-finish_pos
        points_overtake=positions_gained*20
        
        #Stability and consistency in laps
        clean_laps = laps.pick_quicklaps()
        if len(clean_laps) > 1:
        
            consistency = clean_laps['LapTime'].std().total_seconds()
            points_consistency = max(0, (3.0 - consistency) * 100)
        else:
            points_consistency = 0

        #Final Calculation
        strat_score = 1000 + points_finish + points_overtake + points_consistency
        
        return round(strat_score)

    except Exception as e:
        print(f"Error calculating Strat_Score for {driver}: {e}")
        return 1000 # Safety fallback

