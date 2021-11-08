from utils import grouping as grp
from utils import filtering as fil
from tapes import grabber

df = grabber.query_tape()

rf_buyer_geo_dist = grp.group_sort_divide(
    fil.filter_df(df, ['product_category', 'debtor_type'], ['RF', 'core'])
    , 'buyer_country'
    , 'outstanding_advance_balance_usd'
    , 5)
if_buyer_geo_dist = grp.group_sort_divide(
    fil.filter_df(df, ['product_category', 'debtor_type'], ['IF', 'core'])
    , 'buyer_country'
    , 'outstanding_advance_balance_usd'
    , 5)

rf_curr_dist = grp.group_sort_divide(
    fil.filter_df(df, ['product_category', 'debtor_type'], ['RF', 'core'])
    , 'currency'
    , 'outstanding_advance_balance_usd'
    , 5)
if_curr_dist = grp.group_sort_divide(
    fil.filter_df(df, ['product_category', 'debtor_type'], ['IF', 'core'])
    , 'currency'
    , 'outstanding_advance_balance_usd'
    , 5)

rf_industry_dist = grp.group_sort_divide(
    fil.filter_df(df, ['product_category', 'debtor_type'], ['RF', 'core'])
    , 'hs_industry'
    , 'outstanding_advance_balance_usd'
    , 5)
if_industry_dist = grp.group_sort_divide(
    fil.filter_df(df, ['product_category', 'debtor_type'], ['IF', 'core'])
    , 'hs_industry'
    , 'outstanding_advance_balance_usd'
    , 5)
