import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult-stretch.data"

df = pd.read_csv(url)

print(df)