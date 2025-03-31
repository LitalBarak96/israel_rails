import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

# פונקציה לתיקון טקסטים בעברית
def fix_hebrew(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# הגדרות כלליות
st.set_page_config(layout="wide")
plt.rcParams['font.family'] = 'David'
plt.rcParams['axes.unicode_minus'] = False

# טעינת הנתונים
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/Lital/Downloads/train_data.csv", encoding="cp1255")
    df['station_status_nm'] = df['station_status_nm'].apply(fix_hebrew)
    df['train_station_nm'] = df['train_station_nm'].apply(fix_hebrew)
    return df

df = load_data()

st.title("🚆 דשבורד ניתוח סטטוס רכבות בישראל")

# סיידבר לבחירות
st.sidebar.header("סינון נתונים")

selected_year = st.sidebar.selectbox("בחר שנה", sorted(df['shana'].unique(), reverse=True))
selected_month = st.sidebar.selectbox("בחר חודש", sorted(df['hodesh'].unique()))
selected_status = st.sidebar.multiselect("בחר סטטוס", options=df['station_status_nm'].unique(), default=df['station_status_nm'].unique())

filtered_df = df[(df['shana'] == selected_year) &
                 (df['hodesh'] == selected_month) &
                 (df['station_status_nm'].isin(selected_status))]

st.markdown(f"### סטטוס רכבות לחודש {selected_month} בשנת {selected_year}")

# גרף לפי תחנה
fig1, ax1 = plt.subplots(figsize=(12, 6))
top_stations = filtered_df.groupby('train_station_nm')['status_count'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_stations.values, y=top_stations.index, ax=ax1)
ax1.set_title(fix_hebrew("10 התחנות המובילות במספר אירועים"))
ax1.set_xlabel(fix_hebrew("כמות"))
ax1.set_ylabel(fix_hebrew("תחנה"))
st.pyplot(fig1)

# גרף התפלגות סטטוסים
fig2, ax2 = plt.subplots(figsize=(10, 5))
status_counts = filtered_df.groupby('station_status_nm')['status_count'].sum()
sns.barplot(x=status_counts.index, y=status_counts.values, ax=ax2)
ax2.set_title(fix_hebrew("התפלגות סטטוסים"))
ax2.set_ylabel(fix_hebrew("כמות"))
ax2.set_xlabel(fix_hebrew("סטטוס"))
ax2.tick_params(axis='x', rotation=30)
st.pyplot(fig2)

# טבלת נתונים
st.markdown("### טבלת נתונים מסוננים")
st.dataframe(filtered_df[['shana', 'hodesh', 'train_station_nm', 'station_status_nm', 'status_count']].rename(columns={
    'shana': 'שנה',
    'hodesh': 'חודש',
    'train_station_nm': 'תחנה',
    'station_status_nm': 'סטטוס',
    'status_count': 'כמות'
}))
