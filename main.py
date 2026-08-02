import csv
import io

header = input()
n = int(input())

data_list = [input() for _ in range(n)]
data = '\n'.join(data_list)

reader = csv.reader(io.StringIO(data))
total = 0
for row in reader:
    total += float(row[-1])

avg = total / n
print(f"{avg:.2f}")
