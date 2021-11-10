import pandas as pd
from db_connector import db
from tapes import cleaner
from utils.formatting import datetime_to_str

def read_tape(cutoff_date):

    filepath = '.\\__data__\\tapes\\tape_drip-{}.csv'.format(datetime_to_str())

    df = pd.read_csv(filepath)

    # df = clean_tape(df)

    return df


def query_tape(type = 'sf'):
    if (type == 'sf'):
        tape_query = open('.\\tapes\\sql\\data_tape.sql', 'r').read()
        df = db.get_data(tape_query)
        return df
    else:
        tape_query = open('.\\tapes\\sql\\scf_data_tape.sql', 'r').read()
        df = db.get_data(tape_query)
        return df


def read_alm(cutoff_date):

    filepath = '.\\__data__\\asset_level_monthly-{}.csv'.format(datetime_to_str())

    df = pd.read_csv(filepath)

    # df = clean_tape(df)

    return df

