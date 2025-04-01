# 🚆 Israel Rail Delays Dashboard

This project is a dynamic interactive dashboard built with **Streamlit** that visualizes train status data from Israel Railways.

Link for the app 
https://israelrails-fbxdsxdueydiwamd9rxfdp.streamlit.app/

It allows users to:
- Filter train events by **year**, **month**, and **train status**
- View the **top 10 stations** by number of events
- Analyze **train status distribution** (e.g., On Time, Delay, Early Departure)
- Interact with **real data** in a clean and responsive web interface

---

## 📁 Dataset
The dataset used includes columns like:
- `year`: Year of the event
- `month`: Month of the event
- `train_station`: Name of the station (translated to English)
- `train_status`: Type of status (e.g., Delay, On Time)
- `count`: Number of events for that combination

Format: CSV (`train_data.csv`) — manually cleaned and translated.

---

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** (dashboard framework)
- **Pandas** (data handling)
- **Matplotlib + Seaborn** (visualizations)

---

## ▶️ Running Locally
1. Clone the repository:
```bash
git clone https://github.com/LitalBarak96/israel_rails.git
cd israel_rails
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
streamlit run dashboard.py
```

---

## 🌐 Deploy Online (Streamlit Cloud)
The app is deployed on Streamlit Cloud and accessible publicly at:
```
https://<your-app-link>.streamlit.app
```

---

## 📌 To Do / Next Features
- Add line charts for delays over time
- Add downloadable CSV filtered table
- Compare multiple stations side-by-side
- Integrate map view for station locations

---

## 👩‍💻 Created by
**Lital Barak**  
[GitHub Profile](https://github.com/LitalBarak96)


Feel free to fork, suggest improvements, or ask questions!
