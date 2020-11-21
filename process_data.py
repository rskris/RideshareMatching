import pandas as pd


RELEVANT_COLUMNS = [
    'tpep_pickup_datetime', 
    'tpep_dropoff_datetime',
    'trip_distance',
    'pickup_longitude',
    'pickup_latitude',
    'dropoff_longitude',
    'dropoff_latitude',
    'fare_amount'
]


def process_data(
        f_name,
        nrows=10000,
        columns=RELEVANT_COLUMNS,
        min_distance=0.0,
        max_distance=100,
):
    df = pd.read_csv(f_name, nrows=nrows, usecols=columns)
    df = df[df.trip_distance > min_distance]
    df = df[df.trip_distance <= max_distance]
    df = df[df.pickup_longitude != 0]
    df = df[df.dropoff_longitude != 0]
    df = df.reset_index()
    return df

