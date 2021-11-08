import pandas as pd
from utils import formatting


def group_sort_divide(df, group, denom, top_n=None):

    df1_grouped = pd.DataFrame(df.groupby([group])[denom].sum())

    if type(top_n) == int:
        df1_grouped = df1_grouped.sort_values(denom, ascending=False).head(top_n)
        df1_grouped['percent_of_total'] = df1_grouped[denom] / df[denom].sum()
        df1_grouped['percent_of_total'] = df1_grouped['percent_of_total'].apply(formatting.fmt_pct)
        df1_grouped[denom] = df1_grouped[denom].apply(formatting.fmt_cur)
        
        return df1_grouped

    elif top_n is None:
        df1_grouped = df1_grouped.sort_values(denom, ascending=False)
        df1_grouped['percent_of_total'] = df1_grouped[denom] / df[denom].sum()
        df1_grouped['percent_of_total'] = df1_grouped['percent_of_total'].apply(formatting.fmt_pct)
        df1_grouped[denom] = df1_grouped[denom].apply(formatting.fmt_cur)
        
        return df1_grouped
    
    else:
        return 'You passed an incorrect value for top_n'