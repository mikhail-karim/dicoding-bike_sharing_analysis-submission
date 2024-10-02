# ✨ Bike Sharing Data Analytics Dashboard ✨

![This is how the dashboard looks like](dashboard/streamlit_dashboard_showcase.jpg)

## Description
This is the github repository of my dicoding final project course "Belajar Data Analisis dengan Python".

## Prerequisite
Required libraries:
- numpy
- pandas
- matplotlib
- seaborn
- streamlit

## Setup Environment
```
git clone https://github.com/mikhail-karim/dicoding-bike_sharing_analysis-submission.git
pip install -r requirements.txt
```
or
```
pip insall numpy pandas matplotlib seaborn streamlit
```

## Run steamlit app
```
cd dashboard
streamlit run dashboard.py
```

## Notes
for a smooth experience using streamlit, it is recommended to change the followings in the notebook.ipynb file:
```
line 52: main_day_df = pd.read_csv("https://raw.githubusercontent.com/mikhail-karim/dicoding-bike_sharing_analysis-submission/refs/heads/main/dashboard/main_day.csv")
line 53: main_hour_df = pd.read_csv("https://raw.githubusercontent.com/mikhail-karim/dicoding-bike_sharing_analysis-submission/refs/heads/main/dashboard/main_hour.csv")
line 57:     st.image("./dashboard/Bicycle.png")
```

## Enjoy!