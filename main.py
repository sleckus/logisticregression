from pathlib import Path
import pandas as pd
import plotly.express as px


FILES_PATH = Path("2_logistic_regression_files/")
FILES_PATH.mkdir(parents=True, exist_ok=True)


csv_path = "weatherAUS.csv"
try:
    raw_df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"File {csv_path} not found. Please ensure it exists in the working directory.")
    exit()


raw_df.info(max_cols=len(raw_df))


raw_df.dropna(subset=['RainToday', 'RainTomorrow'], inplace=True)


fig = px.histogram(raw_df, x="Location", title="Location vs. Rainy Days", color="RainToday",
                   labels={"RainToday": "Rain Today?", "Location": "Location"})
fig.show()

px.histogram(raw_df,
             x='Temp3pm',
             title='Temperature at 3 pm vs. Rain Tomorrow',
             color='RainTomorrow').show()

px.scatter(raw_df.sample(2000),
           title='Temp (3 pm) vs. Humidity (3 pm)',
           x='Temp3pm',
           y='Humidity3pm',
           color='RainTomorrow').show()

px.scatter(raw_df.sample(2000),
           title='Min Temp. vs Max Temp.',
           x='MinTemp',
           y='MaxTemp',
           color='RainToday').show()

px.scatter(raw_df.sample(2000),
           x="WindSpeed9am",
           y="WindSpeed3pm",
           color="RainToday",
           title="Wind Speed (9am) vs. Wind Speed (3pm)",
           labels={"WindSpeed9am": "Wind Speed at 9am", "WindSpeed3pm": "Wind Speed at 3pm", "RainToday": "Rain Today?"}).show()

px.box(raw_df,
       x="RainTomorrow",
       y="Cloud3pm",
       title="Cloud Cover (3pm) vs. Rain Tomorrow",
       color="RainTomorrow",
       labels={"RainTomorrow": "Rain Tomorrow?", "Cloud3pm": "Cloud Cover at 3pm"}).show()

px.histogram(raw_df,
             x="WindGustDir",
             title="Wind Gust Direction vs. Rain Today",
             color="RainToday",
             labels={"RainToday": "Rain Today?", "WindGustDir": "Wind Gust Direction"}).show()


px.box(raw_df,
       x="RainToday",
       y="Sunshine",
       title="Sunshine vs. Rain Today",
       color="RainToday",
       labels={"RainToday": "Rain Today?", "Sunshine": "Sunshine (hours)"}).show()



