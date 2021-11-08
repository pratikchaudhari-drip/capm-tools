import pandas as pd
from db_connector import db
from utils import formatting as fmt
from emailer import email_sender

def get_sql(product):

    sql = open('./portfolio_monitor/sql/{}_exposure.sql'.format(product), 'r').read()

    return sql

rf_exp = db.get_data(get_sql('rf'), 'prod')
if_exp = db.get_data(get_sql('if'), 'prod')
df_exp = db.get_data(get_sql('df'), 'prod')
brf_exp = db.get_data(get_sql('brf'), 'prod')
gotrade_exp = db.get_data(get_sql('gotrade'), 'gotrade')

total_exp = rf_exp.values[0][0] + if_exp.values[0][0] + df_exp.values[0][0] + \
            brf_exp.values[0][0] + gotrade_exp.values[0][0]
total_exp_formatted = 'USD {:,.2f}'.format(total_exp)

exp_dict = {
    'Seller Finance - Receivable Factoring (RF)':[fmt.fmt_cur(rf_exp.values[0][0]), fmt.fmt_pct(rf_exp.values[0][0] / total_exp)]
    ,'Seller Finance - In-Transit Factoring (IF)':[fmt.fmt_cur(if_exp.values[0][0]), fmt.fmt_pct(if_exp.values[0][0] / total_exp)]
    ,'Seller Finance - Domestic Factoring (DF)':[fmt.fmt_cur(df_exp.values[0][0]), fmt.fmt_pct(df_exp.values[0][0] / total_exp)]
    ,'Buyer Finance - Reverse Factoring  (SCF)':[fmt.fmt_cur(brf_exp.values[0][0]), fmt.fmt_pct(brf_exp.values[0][0] / total_exp)]
    ,'Buyer Finance - Inventory Finance (GoTrade)':[fmt.fmt_cur(gotrade_exp.values[0][0]), fmt.fmt_pct(gotrade_exp.values[0][0] / total_exp)]
    ,'':['', '']
    ,'Total Outstanding Exposure':[fmt.fmt_cur(total_exp), '100%']
}

df = pd.DataFrame.from_dict(exp_dict, orient='index')

df.rename(columns={0:'Total Exposure', 1:'Pct of Total Outstanding Exposure'}, inplace=True)

tbl = """
<table><tr><td>{}</td></tr></table>
""".format(df.to_html())
tbl = tbl.replace("\n", "")

email_body = """

This is an autogenerated credit exposure report. 

As of now, Drip Capital has the following credit exposure:

{}

Please contact brian@dripcapital.com with any questions. 
""".format(tbl)

email_subj = 'Credit Exposure Report - {}'.format(fmt.datetime_to_str())

email_sender.send_email(
    to=['capitalmarkets@dripcapital.com', 'analytics@dripcapital.com', 'u6c6i1t9b5k9w8g9@dripinc.slack.com']
    , cc= ['brian@dripcapital.com', 'akshay.dua@dripcapital.com', 'edmundo@dripcapital.com']
    , subject=email_subj
    , body=email_body)