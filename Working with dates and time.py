import datetime # for dates and time

# DATE
# currentDate = datetime.date.today() #currentDate is not a variable
# # print(currentDate)
# # print(currentDate.year)
# # print(currentDate.month)
# # print(currentDate.day)

# # #strftime allows you to specify the date format
# # print(currentDate.strftime('%d %b, %Y')) #%d - day %b - month %Y - year
# # print(currentDate.strftime('%d %b, %y'))

# # print(currentDate.strftime
# #       ('Please attend our event %A %B %d     in the year %Y'))


# userInput = input("Please enter your birthday ")
# birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
# print(birthday) 

# days = birthday - currentDate # must be the current year of last birthday
# print(days.days) # or print(days)

# TIME
# currentTime = datetime.datetime.now()
# print(currentTime)
# print(currentTime.hour)
# print(currentTime.minute)
# print(currentTime.second)
# print(datetime.datetime.strftime(currentTime, '%H:%M'))

currentDate = datetime.datetime.now()
print(currentDate.minute)