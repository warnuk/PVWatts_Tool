import pandas as pd
import numpy as np

def populate_df(data, template=None):
    '''put data into pandas DataFrame using template if provided'''
    if template:
        df = pd.read_csv(template, header=0)
    else:
        df = pd.DataFrame()
    ac_kw = []
    for value in data['ac']:
        ac_kw.append(value/1000)
    df['AC (kW)'] = ac_kw
    return(df)

def kW_per_day(df):
    '''sum hourly data by day'''
    pass

def peak_days(df):
    '''select max, min, and med days)'''
    kW_per_day(df)
    pass
