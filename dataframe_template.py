import pandas as pd

# Create a dictionary representing the typical number of days in a month.
days = {1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31}

# Create an empty list to contain the month number for each row in the final DataFrame.
Month = []

# Iterate through each 'month' in the days dictionary to populate the Month list with the correct Month IDs.
for i in days:
    for j in range(0, days[i]):
        for x in range(0, 24):
            Month.append(i)
# Create an empty list to contain the day-of-the-month for each row in the final DataFrame.
Day = []

# Iterate through each 'day' in the days dictionary to populate the Day list with the correct Day IDs.
for i in days:
    for x in range(1, days[i] + 1):
        for hour in range(0, 24):
            Day.append(x)

# Create an empty list to contain the hour for each row in the final DataFrame.
Hour = []

# Iterate through each day-of-the-year and each hour-of-the-day to populate the Hour list with the correct Hour IDs.
for i in range(0, 365):
    for x in range(0, 24):
        Hour.append(x)

# Create the final DataFrame to be used as a template by the process_output module.
template = pd.DataFrame({"Month": Month,
                         "Day": Day,
                         "Hour": Hour})

