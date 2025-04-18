import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import arabic_reshaper
from bidi.algorithm import get_display
#
# df = pd.read_csv("C:/Users/Lital/Downloads/train_data.csv",encoding="cp1255")
# print(df.head())

#
# for col in df.columns:
#     print(f"{col}: {df[col].nunique()} ערכים ייחודיים")





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
                       'נהריה', 'נתב"ג', 'נתניה', 'סגולה', 'עכו', 'עתלית', 'פאתי מודיעין', 'צומת חולון',
                       'קיסריה פרדס חנה', 'קרית אריה', 'קרית גת', 'קרית חיים', 'ראש העין צפון', 'ראשונים', 'רחובות',
                       'רמלה', 'רשל"צ משה דיין', 'שדרות', 'תא אוניברסיטה', 'תל אביב ההגנה', 'תל אביב מרכז',
                       'נתיבות',
                       'אופקים', 'בית שאן', 'כפר ברוך', 'כפר יהושע', 'עפולה', 'נתניה קריית ספיר', 'קרית מוצקין',
                       'אחיהוד', 'כרמיאל', 'מרכזית המפרץ', 'רעננה דרום', 'רעננה מערב', 'ירושלים/יצחק נבון',
                       'קרית מלאכי', 'מזכרת בתיה']

    stations_english = ['Ashdod Ad Halom', 'Ashkelon', 'Beer Yaakov', 'Beer Sheva Central', 'Beer Sheva North',
                        'Beit Yehoshua', 'Beit Shemesh', 'Bnei Brak', 'Binyamina', 'Bat Galim', 'Bat Yam Yoseftal',
                        'Bat Yam Komemiyut', 'Dimona', 'Hod Hasharon', 'Herzliya', 'Hashalom', 'Hadera West',
                        'Holon Wolfson', 'Hof HaCarmel', 'Hutzot Hamifratz', 'Haifa Merkaz', 'Yavne Mizrah',
                        'Yavne Maarav', 'Kfar Chabad', 'Kfar Saba', 'Unknown Code 6500', 'Unknown Code 6700',
                        'Unknown Code 800', 'Lehavim Rahat', 'Lod', 'Lod Ganei Aviv', 'Modiin Merkaz',
                        'Merkazit Hamifratz Coastline', 'Nahariya', 'Ben Gurion Airport', 'Netanya', 'Segula', 'Akko',
                        'Atlit', 'Patei Modiin', 'Tzomet Holon', 'Caesarea Pardes Hanna', 'Kiryat Aryeh', 'Kiryat Gat',
                        'Kiryat Haim', 'Rosh HaAyin North', 'Rishonim', 'Rehovot', 'Ramla', 'Rishon Lezion Moshe Dayan',
                        'Sderot', 'Tel Aviv University', 'Tel Aviv HaHagana', 'Tel Aviv Center', 'Netivot', 'Ofakim',
                        'Beit Shean', 'Kfar Baruch', 'Kfar Yehoshua', 'Afula', 'Netanya Kiryat Sapir', 'Kiryat Motzkin',
                        'Ahihud', 'Carmiel', 'Merkazit Hamifratz', 'Raanana South', 'Raanana West',
                        'Jerusalem Yitzhak Navon', 'Kiryat Malachi', 'Mazkeret Batya']

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


#translation_to_hebrew(df)
#print(df.head())