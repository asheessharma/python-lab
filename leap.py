y=int(input('enter the year'))
if y%4==0 and y%400==0:
    print("its a leap year")
elif y%4==0 and y%100!=0:
    print('its a leap year')
else:
    print("not a leap year")
