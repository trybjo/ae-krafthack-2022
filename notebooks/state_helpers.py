import pandas as pd
import numpy as np



def get_running_state(df,minutes_of_masking):

    steady_df = df.copy()
    
    start_idx = steady_df.operation_mode == 'start'
    steady_df = steady_df.drop(columns=['operation_mode'])

    start_times = steady_df.index[start_idx]
    minute_mask = pd.to_timedelta(minutes_of_masking,'m')

    for start_time in start_times:
        end_time = start_time+minute_mask
        steady_df.loc[start_time:end_time,:] = np.nan


    return steady_df