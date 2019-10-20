# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def time():
    a = str(a)
    year = a[:2]
    month = int(a[2:5])
    list1 = [31, 59, 90, 120, 151, 180, 211, 242, 272, 303, 333, 364]
    position = 0
    for i in list1:
        position = position + 1
        if month - i < 0: 
            month = month -i
            monthf = position
            break
    day = abs(month)
    b = float(a[:5])
    a = float(a)
    hours = (a-b)*24
    hours2 = float(str(hours)[:2])
    mins = (hours-hours2)*60
    mins2 = float(str(mins)[:2])
    sec = str(int((mins-mins2)*60))
    print("\n the year is: " +year+
          "\n the month is: " +str(monthf)+
          "\n the day is: " +str(day)+
          "\n the minutes are: " +str(int(mins2))+
          "\n the seconds are: " + sec)
    
            
    
