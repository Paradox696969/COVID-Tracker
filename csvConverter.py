import pandas
import json

with open('data.json') as f:
    data = json.load(f)

df = pandas.DataFrame(data)
df.to_csv('results.csv', index=False)