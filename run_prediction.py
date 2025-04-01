from predictor import DelayPredictor  # ודאי שהשם תואם לקובץ שלך
import api_reading_file as readingfile
import translation
# טען את הדאטה (כמובן תחליפי לנתיב המתאים אצלך)
df_tmp = readingfile.load_data()
df=translation.translation_to_hebrew(df_tmp)
#print(df.head())
# יצירת המודל
predictor = DelayPredictor(df)

# אימון
predictor.train()

# שמירה (לא חובה כל פעם)
predictor.save_model()

# חיזוי לדוגמה
station = "Sderot"
year = 2023
month = 3

prediction = predictor.predict(station, year, month)
print(f"Predicted delay count: {int(prediction)}")