import pandas
import json

with open('data.json') as f:
    data = json.load(f)

biggestLen = 0
for i in data:
    biggestLen = len(data[i]) if len(data[i]) > biggestLen else biggestLen

for i in data:
    for j in range(biggestLen - len(data[i])):
        data[i].append('N/A')

df = pandas.DataFrame(data)
df.to_csv('results.csv', index=False)
