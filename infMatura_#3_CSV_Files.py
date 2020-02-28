# file  = open("Resources\Google Stock Market Data - google_stock_data.csv")
# for line in file:
#     print(line)

path = "Resources\Google Stock Market Data - google_stock_data.csv"
lines = [line for line in open(path)]
print(lines[0])
#The strip() returns a copy of the string with both leading and trailing characters stripped
print(lines[0].strip().split(','))
dataset = [line.strip().split(',') for line in open(path)]
print(dataset[1])

#CSV MODULES ARE EFFICIENT TO USE IN CASES WHEN A COMMA IS FOR EXAMPLE IN A MOVIE'S TITLE (SINCE SPLIT() METHOD
#WON'T DISTINGUISH THE "RECORDS" ON ITS OWN
print("\n")
import csv
from datetime import datetime
print(dir(datetime))
# print(dir(csv))
file = open(path, newline='')
# newline keyword argument makes sure the csv module will work correctly across all platforms
reader = csv.reader(file)
header = next(reader) # The first line is the header
data = []
for row in reader:
    #row = [Dare, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])
print(data[0])

# Computing and storing daily stock returns
returns_path = "Resources\google_returns.csv"
file = open(returns_path, "w")
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y') #StringFormatTime
    writer.writerow([formatted_date, daily_return])