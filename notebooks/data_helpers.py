import pandas as pd
import numpy as np


def get_tensile_sensor_names():

    tensile_sensor_names = [
        "Bolt_1_Tensile",
        "Bolt_2_Tensile",
        "Bolt_3_Tensile",
        "Bolt_4_Tensile",
        "Bolt_5_Tensile",
        "Bolt_6_Tensile",
    ]

    return tensile_sensor_names


def get_torsion_sensor_names():

    torsion_sensor_names = [
        "Bolt_1_Torsion",
        "Bolt_2_Torsion",
        "Bolt_3_Torsion",
        "Bolt_4_Torsion",
        "Bolt_5_Torsion",
        "Bolt_6_Torsion",
    ]

    return torsion_sensor_names


def get_operating_signal_names():

    operating_signal_names = [
        "Unit_4_Power",
        "Unit_4_Reactive Power",
        "Turbine_Guide Vane Opening",
        "Turbine_Pressure Drafttube",
        "Turbine_Pressure Spiral Casing",
        "Turbine_Rotational Speed",
    ]

    return operating_signal_names


def get_running_state(df, minutes_of_masking: int):

    steady_df = df.copy()

    start_idx = steady_df.operation_mode == "start"
    steady_df = steady_df.drop(columns=["operation_mode"])

    start_times = steady_df.index[start_idx]
    minute_mask = pd.to_timedelta(minutes_of_masking, 'm')

    for start_time in start_times:
        end_time = start_time + minute_mask
        steady_df.loc[start_time:end_time, :] = np.nan

    return steady_df


def get_transient_state(df, minutes_of_masking: int):

    transient_df = df.copy()
    start_idx = transient_df.operation_mode == "start"

    start_times = transient_df.index[start_idx]
    minute_mask = pd.to_timedelta(minutes_of_masking, "m")

    for start_time in start_times:
        end_time = start_time + minute_mask
        transient_df.loc[start_time:end_time, "operation_mode"] = "start"
    
    transient_df.loc[transient_df.operation_mode!="start",:] = np.nan
    transient_df = transient_df.drop(columns=['operation_mode'])

    return transient_df


def load_training_data(
    full: bool, steady: bool, minutes_of_masking: int
) -> pd.DataFrame:
    """Get training dataset

    Args:
        full (bool): include all data avialable
        steady (bool): remove every observation after a start operation_mode
        minutes_of_masking (int): number of minutes to mask
    Returns:
        pd.DataFrame: dataframe with training data, either steady or transient state
    """

    df = pd.read_parquet("../data/input_dataset-2.parquet")

    if full:
        df_1 = pd.read_parquet("../data/input_dataset-1.parquet")
        df = pd.concat([df_1, df])

    df = df.rename(columns={"mode": "operation_mode"})

    if steady:
        df = get_running_state(df, minutes_of_masking=minutes_of_masking)
    if not steady:
        df = get_transient_state(df, minutes_of_masking=minutes_of_masking)

    df = df.reindex()

    return df


def load_test_data():

    a = 1
