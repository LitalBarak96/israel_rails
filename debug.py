import api_reading_file
import translation
df_tmp =api_reading_file.load_data()
df = translation.translation_to_hebrew(df_tmp)

print(df['train_station'].unique())

# # נניח שהדאטהפריים שלך הוא df
# station_to_find = "Tel Aviv HaShalom"
#
# # סינון לפי שם התחנה
# result = df[df['train_station'] == station_to_find]
# print(result)