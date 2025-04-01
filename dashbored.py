import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

import urllib.request
import json




def translation_to_hebrew(df):
    translate_status = {
        'איחור': 'Delay',
        'בזמן': 'On Time',
        'הקדמה ביציאה': 'Early Departure'
    }
    df['station_status_nm'] = df['station_status_nm'].replace(translate_status)

    # station_translation = {
    #     "תל אביב - השלום": "Tel Aviv - HaShalom",
    #     "חיפה מרכז": "Haifa Center",
    #     "ירושלים יצחק נבון": "Jerusalem Yitzhak Navon",
    # 'אשדוד עד הלום': 'Ashdod Ad Halom', 'אשקלון':'Ashkelon',
    #     # הוסיפי עוד לפי הצורך
    # }
    # print(df['train_station_nm'].unique())

    stations_hebrew = ['אשדוד עד הלום', 'אשקלון', 'באר יעקב', 'באר שבע מרכז', 'באר שבע צפון', 'בית יהושע', 'בית שמש',
                       'בני ברק', 'בנימינה', 'בת גלים', 'בת ים יוספטל', 'בת ים קוממיות', 'דימונה', 'הוד השרון',
                       'הרצליה', 'השלום', 'חדרה מערב', 'חולון וולפסון', 'חוף הכרמל', 'חוצות מפרץ', 'חיפה מרכז',
                       'יבנה מזרח', 'יבנה מערב', 'כפר חבד', 'כפר סבא', 'לא ידוע קוד 6500', 'לא ידוע קוד 6700',
                       'לא ידוע קוד 800', 'להבים רהט', 'לוד', 'לוד גני אביב', 'מודיעין מרכז', 'מרכזית המפרץ/קו החוף',
                       'נהריה', 'נתבג"', 'נתניה', 'סגולה', 'עכו', 'עתלית', 'פאתי מודיעין', 'צומת חולון',
                       'קיסריה פרדס חנה', 'קרית אריה', 'קרית גת', 'קרית חיים', 'ראש העין צפון', 'ראשונים', 'רחובות',
                       'רמלה', 'רשלצ משה דיין"', 'שדרות', 'תא אוניברסיטה', 'תל אביב ההגנה', 'תל אביב מרכז', 'נתיבות',
                       'אופקים', 'בית שאן', 'כפר ברוך', 'כפר יהושע', 'עפולה', 'נתניה קריית ספיר', 'קרית מוצקין',
                       'אחיהוד', 'כרמיאל', 'מרכזית המפרץ', 'רעננה דרום', 'רעננה מערב', 'ירושלים/יצחק נבון',
                       'קרית מלאכי', 'מזכרת בתיה']
    stations_english = ['Ashdod Ad Halom', 'Ashkelon', 'Beer Yaakov', 'Beer Sheva Central', 'Beer Sheva North',
                        'Beit Yehoshua', 'Beit Shemesh', 'Bnei Brak', 'Binyamina', 'Bat Galim', 'Bat Yam Yoseftal',
                        'Bat Yam Kommiyot', 'Dimona', 'Hod Hasharon', 'Herzliya', 'Hashalom', 'Hadera West',
                        'Holon Wolfson', 'Hof Carmel', 'Hotozat Mifratz', 'Haifa Central', 'Yavne East', 'Yavne West',
                        'Kfar Chabad', 'Kfar Saba', 'Unknown Code 6500', 'Unknown Code 6700', 'Unknown Code 800',
                        'Lahavim Rahat', 'Lod', 'Lod Ganei Aviv', 'Modiin Central', 'Central Hamifratz/Coastline',
                        'Nahariya', 'Natbeg', 'Netanya', 'Segula', 'Akko', 'Atlit', 'Pati Modiin', 'Tzomet Holon',
                        'Caesarea Pardes Hanna', 'Kiryat Aryeh', 'Kiryat Gat', 'Kiryat Haim', 'Rosh Haayin North',
                        'Rishonim', 'Rehovot', 'Ramla', 'Rashaltz Moshe Dayan', 'Sderot', 'Tel Aviv University',
                        'Tel Aviv HaHagana', 'Tel Aviv Center', 'Netivot', 'Ofakim', 'Beit Shean', 'Kfar Baruch',
                        'Kfar Yehoshua', 'Afula', 'Netanya Kiryat Sapir', 'Kiryat Motzkin', 'Achihud', 'Carmiel',
                        'Mercazit Hamifratz', 'Raanana South', 'Raanana West', 'Jerusalem/Yitzhak Navon',
                        'Kiryat Malachi', 'Maskeret Batya']

    station_translation = {hebrew: english for hebrew, english in zip(stations_hebrew, stations_english)}

    df['train_station_nm'] = df['train_station_nm'].replace(station_translation)

    df.rename(columns={
        'shana': 'year',
        'hodesh': 'month',
        'train_station_nm': 'train_station',
        'station_status_nm': 'train_status',
        'status_count': 'count'
    }, inplace=True)

    return df

# הגדרות כלליות
st.set_page_config(layout="wide")
#C:/Users/Lital/Downloads/

# טעינת הנתונים
@st.cache_data
def load_data():
    # כתובת ה-API
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=1ebbbb91-1d44-4f41-a85c-4a93a35e32d6&limit=5'

    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    records = data['result']['records']
    df = pd.DataFrame(records)

    df_tmp=translation_to_hebrew(df)
    return df_tmp

df = load_data()
print(df.head())



st.title(" Israel Rail Dashboard")

# Sidebar filters
st.sidebar.title("Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(df['year'].unique(), reverse=True))
selected_month = st.sidebar.selectbox("Select Month", sorted(df['month'].unique()))
selected_status = st.sidebar.multiselect("Select Train Status", options=df['train_status'].unique(), default=df['train_status'].unique())

# Filter data
filtered_df = df[(df['year'] == selected_year) &
                 (df['month'] == selected_month) &
                 (df['train_status'].isin(selected_status))]

st.subheader(f"Train data for {selected_month}/{selected_year}")

# Top 10 stations with most events
top_stations = filtered_df.groupby('train_station')['count'].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_stations.values, y=top_stations.index, ax=ax1)
ax1.set_title("Top 10 Stations by Event Count")
ax1.set_xlabel("Count")
ax1.set_ylabel("Station")
st.pyplot(fig1)

# Status distribution
status_counts = filtered_df.groupby('train_status')['count'].sum()
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=status_counts.index, y=status_counts.values, ax=ax2)
ax2.set_title("Train Status Distribution")
ax2.set_xlabel("Status")
ax2.set_ylabel("Count")
ax2.tick_params(axis='x', rotation=30)
st.pyplot(fig2)

# Show filtered data
st.subheader("Filtered Data Table")
st.dataframe(filtered_df[['year', 'month', 'train_station', 'train_status', 'count']])
