#write python program to print calender of a given month
import calendar
#enter certain year and month
year= int(input("please enter the year: "))
month= int(input("please enter the month: "))
#python built in function to determine the calendar of each year and month
result= calendar.month(year,month)
print(result)