import numpy as np
import pandas as pd
from db_connector import db
from utils.formatting import fmt_cur
from utils.formatting import fmt_pct
from utils.formatting import datetime_to_str
from emailer import email_sender


def get_entity_sql(product):

    sql = open('./portfolio_monitor/sql/{}_entity_breakdown.sql'.format(product), 'r').read()

    return sql

def get_exp_sql(product):

    sql = open('./portfolio_monitor/sql/{}_exposure.sql'.format(product), 'r').read()

    return sql

rf_exp = db.get_data(get_exp_sql('rf'), 'prod')
if_exp = db.get_data(get_exp_sql('if'), 'prod')
df_exp = db.get_data(get_exp_sql('df'), 'prod')
brf_exp = db.get_data(get_exp_sql('brf'), 'prod')
gotrade_exp = db.get_data(get_exp_sql('gotrade'), 'gotrade')

total_exp = rf_exp.values[0][0] + if_exp.values[0][0] + df_exp.values[0][0] + \
            brf_exp.values[0][0] + gotrade_exp.values[0][0]
total_exp_formatted = 'USD {:,.2f}'.format(total_exp)

rf_funding = db.get_data(get_entity_sql('rf'), 'prod')
rf_funding.set_index('id', inplace=True)
if_funding = db.get_data(get_entity_sql('if'), 'prod')
if_funding.set_index('id', inplace=True)
for i in range(0, rf_funding.index.max() + 1):
    if i not in if_funding.index:
        if_funding.loc[i] = 0
df_funding = db.get_data(get_entity_sql('df'), 'prod')
df_funding.set_index('id', inplace=True)
for i in range(0, rf_funding.index.max() + 1):
    if i not in df_funding.index:
        df_funding.loc[i] = 0
brf_funding = db.get_data(get_entity_sql('brf'), 'prod')
brf_funding.set_index('id', inplace=True)
for i in range(0, rf_funding.index.max() + 1):
    if i not in brf_funding.index:
        brf_funding.loc[i] = 0

exp_dict = {
    'Seller Finance - Receivable Factoring (RF)':[
        (rf_exp.values[0][0])
        , (rf_funding.loc[rf_funding.index == 2, 'sum'].values[0])
        , (rf_funding.loc[rf_funding.index == 2, 'sum'].values[0] / rf_exp.values[0])[0]
        , (rf_funding.loc[rf_funding.index == 1, 'sum'].values[0])
        , ((rf_funding.loc[rf_funding.index == 1, 'sum'].values[0] / rf_exp.values[0])[0])
        , (rf_funding.loc[rf_funding.index == 3, 'sum'].values[0])
        , ((rf_funding.loc[rf_funding.index == 3, 'sum'].values[0] / rf_exp.values[0])[0])
        , (rf_funding.loc[rf_funding.index == 4, 'sum'].values[0])
        , ((rf_funding.loc[rf_funding.index == 4, 'sum'].values[0] / rf_exp.values[0])[0])
    ]
    ,'Seller Finance - In-Transit Factoring (IF)':[
        (if_exp.values[0][0])
        , (if_funding.loc[if_funding.index == 2, 'sum'].values[0])
        , ((if_funding.loc[if_funding.index == 2, 'sum'].values[0] / if_exp.values[0])[0])
        , (if_funding.loc[if_funding.index == 1, 'sum'].values[0])
        , ((if_funding.loc[if_funding.index == 1, 'sum'].values[0] / if_exp.values[0])[0])
        , (if_funding.loc[if_funding.index == 3, 'sum'].values[0])
        , ((if_funding.loc[if_funding.index == 3, 'sum'].values[0] / if_exp.values[0])[0])
        , (0) #fmt_cur(if_funding.loc[if_funding['id'] == 4, 'sum'].values[0])
        , (0) #fmt_pct((if_funding.loc[if_funding.index == 4, 'sum'].values[0] / if_exp.values[0])[0])
        ]
    ,'Seller Finance - Domestic Factoring (DF)':[
        (df_exp.values[0][0])
        , (df_funding.loc[df_funding.index == 2, 'sum'].values[0])
        , ((df_funding.loc[df_funding.index == 2, 'sum'].values[0] / df_exp.values[0])[0])
        , (df_funding.loc[df_funding.index == 1, 'sum'].values[0])
        , ((df_funding.loc[df_funding.index == 1, 'sum'].values[0] / df_exp.values[0])[0])
        , (df_funding.loc[df_funding.index == 3, 'sum'].values[0])
        , ((df_funding.loc[df_funding.index == 3, 'sum'].values[0] / df_exp.values[0])[0])
        , (0) #fmt_cur(df_funding.loc[df_funding['id'] == 4, 'sum'].values[0])
        , (0) #fmt_pct((df_funding.loc[df_funding.index == 4, 'sum'].values[0] / df_exp.values[0])[0])
        ]
    ,'Buyer Finance - Reverse Factoring  (SCF)':[
        (brf_exp.values[0][0])
        , (brf_funding.loc[brf_funding.index == 2, 'sum'].values[0])
        , ((brf_funding.loc[brf_funding.index == 2, 'sum'].values[0] / brf_exp.values[0])[0])
        , (brf_funding.loc[brf_funding.index == 1, 'sum'].values[0])
        , ((brf_funding.loc[brf_funding.index == 1, 'sum'].values[0] / brf_exp.values[0])[0])
        , (brf_funding.loc[brf_funding.index == 3, 'sum'].values[0])
        , ((brf_funding.loc[brf_funding.index == 3, 'sum'].values[0] / brf_exp.values[0])[0])
        , (0) #fmt_cur(brf_funding.loc[df_funding['id'] == 4, 'sum'].values[0])
        , (0) #fmt_pct((brf_funding.loc[brf_funding.index == 4, 'sum'].values[0] / brf_exp.values[0])[0])
        ]
    ,'Buyer Finance - Inventory Finance (GoTrade)':[
        (gotrade_exp.values[0][0])
        , (gotrade_exp.values[0][0])
        , ((gotrade_exp.values[0][0] / gotrade_exp.values[0])[0]) #fmt_pct((gotrade_funding.loc[gotrade_funding.index == 2, 'sum'].values[0] / gotrade_exp.values[0])[0])
        , (0) #fmt_cur(gotrade_funding.loc[gotrade_funding.index == 1, 'sum'].values[0])
        , ((0 / brf_exp.values[0])[0]) #fmt_pct((gotrade_funding.loc[gotrade_funding.index == 1, 'sum'].values[0] / gotrade_exp.values[0])[0])
        , (0) #fmt_cur(gotrade_funding.loc[gotrade_funding.index == 3, 'sum'].values[0])
        , ((0 / brf_exp.values[0])[0]) #fmt_pct((gotrade_funding.loc[gotrade_funding.index == 3, 'sum'].values[0] / gotrade_exp.values[0])[0])
        , (0) #fmt_cur(gotrade_funding.loc[gotrade_funding['id'] == 4, 'sum'].values[0])
        , ((0 / brf_exp.values[0])[0]) #fmt_pct((gotrade_funding.loc[gotrade_funding.index == 4, 'sum'].values[0] / gotrade_exp.values[0])[0])
        ]
    ,'':['', '', '', '', '']
    ,'Total Outstanding Exposure':['', '']
}

df = pd.DataFrame.from_dict(exp_dict, orient='index')

# def highlight_column(s, col):
#     return ['background-color: #d42a2a' if s.name == col else '' for v in s.index]

# df.style.apply(highlight_column, col=['2','4','6','8'])

df.rename(columns={
    0:'Total Outstanding'
    , 1:'1 - Drip Balance Sheet', 2:'1 - Pct of Total'
    , 3:'2 - SPV Vasco - Drip', 4:'2 - Pct of Total'
    , 5:'3 - SPV Portola - EWB', 6:'3 - Pct of Total'
    , 7:'4 - SPV Dribar - Barclays', 8:'4 - Pct of Total'
    }
    , inplace=True)

df.replace('', np.nan, inplace=True)

df.loc['Total Outstanding Exposure', 'Total Outstanding'] = df['Total Outstanding'].sum()
df.loc['Total Outstanding Exposure', '1 - Drip Balance Sheet'] = df['1 - Drip Balance Sheet'].sum()
df.loc['Total Outstanding Exposure', '2 - SPV Vasco - Drip'] = df['2 - SPV Vasco - Drip'].sum()
df.loc['Total Outstanding Exposure', '3 - SPV Portola - EWB'] = df['3 - SPV Portola - EWB'].sum()
df.loc['Total Outstanding Exposure', '4 - SPV Dribar - Barclays'] = df['4 - SPV Dribar - Barclays'].sum()

df.loc['Total Outstanding Exposure', '1 - Pct of Total'] = df.loc['Total Outstanding Exposure', '1 - Drip Balance Sheet'] / df.loc['Total Outstanding Exposure', 'Total Outstanding']
df.loc['Total Outstanding Exposure', '2 - Pct of Total'] = df.loc['Total Outstanding Exposure', '2 - SPV Vasco - Drip'] / df.loc['Total Outstanding Exposure', 'Total Outstanding']
df.loc['Total Outstanding Exposure', '3 - Pct of Total'] = df.loc['Total Outstanding Exposure', '3 - SPV Portola - EWB'] / df.loc['Total Outstanding Exposure', 'Total Outstanding']
df.loc['Total Outstanding Exposure', '4 - Pct of Total'] = df.loc['Total Outstanding Exposure', '4 - SPV Dribar - Barclays'] / df.loc['Total Outstanding Exposure', 'Total Outstanding']

cur_cols = ['Total Outstanding', '1 - Drip Balance Sheet', '2 - SPV Vasco - Drip', '3 - SPV Portola - EWB', '4 - SPV Dribar - Barclays']
pct_cols = ['1 - Pct of Total', '2 - Pct of Total', '3 - Pct of Total', '4 - Pct of Total']

for c in cur_cols:
    df[c] = df[c][~df[c].isna()].apply(fmt_cur)
for c in pct_cols:
    df[c] = df[c][~df[c].isna()].apply(fmt_pct)

df.fillna('', inplace=True)

tbl = """
<table><tr><td>{}</td></tr></table>
""".format(df.to_html())
tbl = tbl.replace("\n", "")

email_body = """

This is an autogenerated funding monitor report. 

As of now, Drip Capital's credit exposure is being funded in the following ways:

{}

Please contact brian@dripcapital.com with any questions. 
""".format(tbl)

email_subj = 'Funding Monitor Report - {}'.format(datetime_to_str())

email_sender.send_email(
    to=['capitalmarkets@dripcapital.com', 'analytics@dripcapital.com', 'u6c6i1t9b5k9w8g9@dripinc.slack.com']
    , cc= ['brian@dripcapital.com', 'akshay.dua@dripcapital.com', 'edmundo@dripcapital.com']
    , subject=email_subj
    , body=email_body)
