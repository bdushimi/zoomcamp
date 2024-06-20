import pickle
import pandas as pd
import uuid
import sys

year = 2023
month = 3
taxi_type = 'yellow'
categorical = ['PULocationID', 'DOLocationID']


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


def run():
    year = int(sys.argv[1])
    month = int(sys.argv[2])

    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/{taxi_type}_{year:04d}-{month:02d}.parquet'
    apply_model(input_file, output_file)


def read_data(filename: str):
    categorical = ['PULocationID', 'DOLocationID']

    df = pd.read_parquet(filename)

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    return df


def apply_model(input_file, output_file):
    df = read_data(input_file)

    # #Make Prediction
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    # Q1 The standard deviation of the predicted duration for this dataset.
    sd = y_pred.std()
    print('sd of y_pred : ', sd)

    mean_predicted = y_pred.mean()
    print(f"The mean predicted value is: {mean_predicted}")

    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    # Q2 Wrtting the ride_id and predicitons in a new data frame
    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )


if __name__ == '__main__':
    run()
