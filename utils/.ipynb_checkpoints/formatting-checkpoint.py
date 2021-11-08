import datetime as dt

def datetime_to_str(date=dt.date.today()):
    
    clean_date_str = date.isoformat().replace('-', '')
    
    return clean_date_str


def fmt_cur(float):

    formatted_float = 'USD {:,.2f}'.format(float)

    return formatted_float


def fmt_pct(float):

    formatted_float = '{:,.2%}'.format(float)

    return formatted_float
