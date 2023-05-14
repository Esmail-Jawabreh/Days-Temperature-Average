numDays = int(input("How many day's temperature? "))
total = 0 
temp = []

for i in range(1, numDays + 1):
    nextDay = int(input("Day " + str(i) + "'s high temperature: "))
    temp.append(nextDay)
    total += temp[i - 1]


avg = round(total/numDays,2)
print("\nAverage = " + str(avg))


above = []
for i in range(numDays):
    if temp[i] > avg:
        above.append(i + 1)

print(str(len(above)) + " day(s) above average.")
print("Day(s) above the average: " + ', '.join(str(day) for day in above))