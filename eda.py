import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import arabic_reshaper
from bidi.algorithm import get_display

df = pd.read_csv("C:/Users/Lital/Downloads/train_data.csv",encoding="cp1255")
print(df.head())

print(df.shape)        # כמה שורות ועמודות
print(df.columns)      # שמות עמודות
print(df.head())       # 5 שורות ראשונות
print(df.dtypes)       # סוגי העמודות
print(df.isna().sum()) # ערכים חסרים


for col in df.columns:
    print(f"{col}: {df[col].nunique()} ערכים ייחודיים")




def fix_hebrew(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

# מיישם את זה על העמודה שלך:
df["station_status_fixed"] = df["station_status_nm"].apply(fix_hebrew)

# גרף
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="station_status_fixed", order=df["station_status_fixed"].value_counts().index)

plt.title(fix_hebrew("התפלגות סטטוסי רכבת"))
plt.xlabel(fix_hebrew("סטטוס רכבת"))
plt.ylabel(fix_hebrew("כמות"))
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()



