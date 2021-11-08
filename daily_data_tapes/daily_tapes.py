import pandas as pd
import numpy as np
from db_connector import db

sql = open(".\\sql\\sf_tape.sql", 'r').read()
sf_raw = db.get_data(sql)


def sf_clean_tape_query(df):

    df = df[df['advanced_value_usd'] > 0]
    df['full_payment_date'].fillna(0, inplace=True)
    df['payment_received_usd'].fillna(0, inplace=True)
    df['latest_due_date'] = df[['new_due_date', 'due_date']].max(axis=1)
    df['vin_mnth'] = pd.to_datetime(df['first_advance_date']).dt.to_period('M')
    df['vin_qtr'] = pd.to_datetime(df['first_advance_date']).dt.to_period('Q')

    return df

sf_tape = sf_clean_tape_query(sf_raw)
sf_tape.to_pickle("sf_tape.pkl")


