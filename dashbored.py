import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display
import translation



# הגדרות כלליות
st.set_page_config(layout="wide")
#C:/Users/Lital/Downloads/

# טעינת הנתונים
@st.cache_data
def load_data():
    df = pd.read_csv("train_data.csv", encoding="cp1255")
    df_tmp=translation.translation_to_hebrew(df)
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
