def filter_df(df, filters=[], values=[]):
    for i in range(0, len(filters)):
        df = df[df[filters[i]] == values[i]]
        
    return df


def neg_filter_df(df, filters=[], values=[]):
    for i in range(0, len(filters)):
        df = df[df[filters[i]] != values[i]]
        
    return df