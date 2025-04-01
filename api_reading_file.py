import urllib.request
import json

# כתובת ה-API
url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=1ebbbb91-1d44-4f41-a85c-4a93a35e32d6&limit=5'

# פתיחת הקישור
with urllib.request.urlopen(url) as response:
    data = json.load(response)

# הדפסת התוצאה
print(data)

import pandas as pd

records = data['result']['records']
df = pd.DataFrame(records)

print(df.head())





import urllib.request
import json
import pandas as pd

resource_id = '1ebbbb91-1d44-4f41-a85c-4a93a35e32d6'
limit = 1000
offset = 0
all_records = []

while True:
    url = f"https://data.gov.il/api/3/action/datastore_search?resource_id={resource_id}&limit={limit}&offset={offset}"

    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        records = data['result']['records']

        if not records:
            break  # אם נגמרו הנתונים, יוצאים מהלולאה

        all_records.extend(records)
        offset += limit  # ממשיכים לעמוד הבא

# הפיכת הכל ל-DataFrame
df = pd.DataFrame(all_records)
print(f"הורדו {len(df)} שורות")
print(df.head())