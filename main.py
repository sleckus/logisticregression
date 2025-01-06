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
             color='RainTomorrow')


