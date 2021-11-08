import pandas as pd
import datetime as dt

def strip_date(date=dt.date.today()):
    
    clean_date_str = date.isoformat().replace('-', '')
    
    return clean_date_str

def write_dataframe(df, csv_filename):

    df.to_csv(csv_filename + '{}.csv'.format(strip_date()))