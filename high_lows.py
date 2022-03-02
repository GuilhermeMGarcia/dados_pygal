import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtem as datas e as temperaturas maximas do arquivo
file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# Faz a plotagem dos dados
fig = plt.figure(dpi=115, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Formata o grafico
plt.title("Daily high temperatures, - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()