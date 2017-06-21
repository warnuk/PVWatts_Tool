import pandas as pd

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

col1 = []
for i in days:
    for j in range(0, days[i]):
        for x in range(0, 24):
            col1.append(i)

col2 = []
for i in days:
    for x in range(1, days[i] + 1):
        for hour in range(0, 24):
            col2.append(x)

col3 = []
for i in range(0, 365):
    for x in range(0, 24):
        col3.append(x)

template = pd.DataFrame({"Month": col1,
                         "Day": col2,
                         "Hour": col3})
