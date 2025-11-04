import os
import pandas as pd

def dt(hour, minute, second=0):
    from datetime import datetime
    return datetime(2023, 1, 1, hour, minute, second)

def run_batch():
    # Run batch.py for January 2023
    exit_code = os.system("python batch.py 2023 1")
    assert exit_code == 0

def test_integration():
    # Prepare input path and output path
    input_file = os.getenv(
        'INPUT_FILE_PATTERN',
        's3://nyc-duration/in/{year:04d}-{month:02d}.parquet'
    ).format(year=2023, month=1)
    output_file = os.getenv(
        'OUTPUT_FILE_PATTERN',
        's3://nyc-duration/out/{year:04d}-{month:02d}.parquet'
    ).format(year=2023, month=1)
    print(input_file)
    print(output_file)
    s3_endpoint_url = os.getenv('S3_ENDPOINT_URL', 'http://localhost:4566')
    options = {
        'client_kwargs': {
            'endpoint_url': s3_endpoint_url
        }
    }
    # Read output file from S3
    df_result = pd.read_parquet(output_file, storage_options=options)
    print(df_result)
    # Check sum of predicted durations
    total_duration = df_result['predicted_duration'].sum()
    print(f"Sum of predicted durations: {total_duration:.2f}")


if __name__ == "__main__":
    run_batch()
    test_integration()
