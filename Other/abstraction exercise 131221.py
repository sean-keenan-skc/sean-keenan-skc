from datetime import date

print('Please fill in the below details relating to when the dog was got: ')
year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
startdate = date(year,month,day)

print("Please fill in the below details relating to when the item was lost: ")
year=int(input('Year: '))
month=int(input('Month: '))
day=int(input('Day: '))
enddate = date(year,month,day)

numstudydays = enddate - startdate

print ("The item has been missing for", numstudydays)
