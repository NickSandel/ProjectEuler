# You are given the following information, but you may prefer to do some research for yourself.
import math
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Dumb way I suppose is to set first day for each month then walk all forward accounting for leap years and count up the Sundays?
# Cheaty way might be to use a calendar library to get all 1sts of the Months and check which are Sundays?
# Smart way would be to do something far more clever with finding the recurring pattern and adding up instances of it in this range

# Let's try the counting way first
# 1 Jan 1900 was a Monday
# Week runs Monday (1) to Sunday (7)
month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_additions = [month%7 for month in month_length]
print(day_additions)
# [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

# Do this as one big bloody batch?
# How many leap years in this period?
# 2000 was a leap year
leap_years = 1
for i in range(1901, 2000):
    if i%4 == 0:
        leap_years += 1

print(f"Leap years: {leap_years}") # 25, so 75 non leap years

# Can I do something more clever than brute iteration like finding which days will match in a year 
# and adding that up over the total then accounting for leap years messing this up for 25 years?
#                    [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
days_matching_1900 = [1, 4, 4, 7, 2, 5, 7, 3, 6, 1, 4, 6]
sunday_count = 0
for i in range(1, 2000-1900 + 1):
    year_days = []
    for month in range(len(days_matching_1900)):
        # Check for leap year this year or last (spilling over for Jan and Feb)
        year_days.append((days_matching_1900[month] + (i + 1 if i % 4 == 0 and month > 1 else i) + math.floor((i-1)/4))% 7)
    # year_days = [(day+i)%7 for day in days_matching_1901]
    print(f"{1900 + i} : {year_days}")
    sunday_count += year_days.count(0)
print(sunday_count)