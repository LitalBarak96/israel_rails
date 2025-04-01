import os
import json
import urllib.request
import pandas as pd

def load_data():
    cache_file = "train_data_cache.csv"

    # אם הקובץ כבר שמור - נטען ממנו
    if os.path.exists(cache_file):
        print("📂 Loading data from local cache...")
        return pd.read_csv(cache_file)

    print("📡 Downloading data from API...")
    resource_id = '1ebbbb91-1d44-4f41-a85c-4a93a35e32d6'
    limit = 32000
    offset = 0
    all_records = []

    while True:
        url = f"https://data.gov.il/api/3/action/datastore_search?resource_id={resource_id}&limit={limit}&offset={offset}"

        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            records = data['result']['records']

            if not records:
                break

            all_records.extend(records)
            offset += limit

    df = pd.DataFrame(all_records)
    df.to_csv(cache_file, index=False)
    print("✅ Data saved to cache.")
    return df
