import math


daysOfWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saterday"]

month = input("Enter the month (1-Jan to 12-Dec): ")
k = input("Enter the day: ")
year = input("Enter the year: ")


month = int(month)
year = int(year)
k = int(k)

daysOfWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saterday"]


def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)
 
# Driver Code
day = dayofweek(k, month, year)
print(daysOfWeek[day])
