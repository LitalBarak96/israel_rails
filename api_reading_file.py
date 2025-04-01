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