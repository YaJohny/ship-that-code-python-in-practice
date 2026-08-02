import csv
import io

header = input()
n = int(input())

data_list = [input() for _ in range(n)]
data = '\n'.join(data_list)
data_with_header = header + '\n' + data

reader = csv.DictReader(io.StringIO(data_with_header))
total = 0
for row in reader:
    total += int(row["age"])

avg = total / float(n)
print("{avg:.2f}")
