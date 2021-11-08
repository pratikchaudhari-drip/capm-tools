import pandas as pd

def get_dq_days(df):
    
    if (df['cutoff_date'] > df['latest_due_date']) & (df['repaid_flag'] == 'Open'):
        days_dq = (df['cutoff_date'] - df['latest_due_date']).days
        return days_dq
    else:
        return 0

def get_days_to_repay(df):
    
    if df['full_payment_date'] == 0:
        return ''
    else:
        days_to_repay = (df['full_payment_date'] - df['first_advance_date']).days
        return days_to_repay

def get_domestic_factoring(df):

    if df['exporter_country'] == df['buyer_country']:
        return 'DF'
    else:
        return df['product_category']
        

col_name_dict = {'ID':'invoice_id',
'Reference':'reference_id',
'In Vasco?':'vasco_flag',
'Exporter Name':'exporter',
'Buyer Name':'buyer',
'Exporter ID':'exporter_id',
'Buyer ID':'buyer_id',
'Exporter Country':'exporter_country',
'Buyer Country':'buyer_country',
'Buyer Insurance Grade':'buyer_insurance_grade',
'Product Exported Description/HS Code':'hs_code',
'Currency':'currency',
'Product Category':'product_cat',
'Insurable Flag':'insured_flag',
'Modified Due Date Flag':'modified_date_flag',
'Net Invoice Value USD':'invoice_value',
'Anchor Event for Step Up Date':'anchor_event',
'Expected Tenor from Anchor Event Date':'expected_tenor',
'Grace Period':'grace_period',
'Invoice Date':'invoice_date',
'Anchor Event Date':'anchor_event_date',
'First Advance Date':'adv_date',
'Due Date':'due_date',
'Modified Due Date':'modified_due_date',
'New Due Date':'new_due_date',
'Step Up Date':'step_up_date',
'Principal Payment Date':'prin_payment_date',
'Actual Outstanding Tenor':'actual_tenor',
'Step-up Interest Rate Tenor including Holiday Grace':'step_up_int_tenor',
'Max Advance Rate':'max_adv_rate',
'Factoring Commission':'factor_fee_pct',
'Interest Rate':'int_rate',
'Step-up Interest Rate':'step_up_int_rate',
'Advanced Value USD':'adv_value',
'Advance Rate':'adv_rate',
'Payment Received USD':'payment_received',
'Invoice Value Received USD':'invoice_value_received',
'Advanced Value Received USD':'adv_value_received',
'Dilution on Invoice Value USD':'invoice_value_dilution',
'Dilution on Advanced Value USD':'adv_value_dilution',
'Outstanding Invoice Balance USD':'invoice_bal',
'Outstanding Advance Balance USD':'adv_bal',
'Release Net Payment to Exporter USD':'net_pmt_released',
'Actual Factoring Fees USD':'actual_factor_fee',
'Actual Regular Interest Charges USD':'actual_reg_int',
'Actual Overdue Interest Charges USD':'actual_tot_int',
'Actual Setup Fee USD':'actual_setup_fee',
'Adjustments USD':'adjustments',
'Actual Total Fees + Interest USD (Including Setup Fee)':'actual_total_fees',
'Actual  Total Fees + Interest USD (Excluding Setup Fees)':'actual_total_fees_no_setup',
'Stage':'stage',
'Full Payment Date':'full_payment_date',
'BL Date':'bill_of_lading_date',
'HS Code Description':'hs_code_descrip',
'Exporter Aggregate LTM Revenue USD':'total_exporter_volume',
'Open or Repaid Flag':'repaid_flag',
'Invoice Yield':'invoice_yield',
'Expected Tenor From Invoice Date':'expected_tenor_from_invoice_date',
'Expected Tenor From First Advance Date':'expected_tenor_from_adv_date',
'Exporter':'exporter',
'Buyer':'buyer',
'Product Exported Description/  HS Code':'hs_code',
'Advanced Date':'adv_date',
'Step-Up Date ':'step_up_date',
'Days Outstanding (Open Only)':'days_outstanding',
'Days Delinquent (Open Only)':'days_dq',
'Actual Interest Charges USD':'actual_reg_int',
'Actual Step-up Interest Charges USD':'actual_step_up_int',
'Actual Setup Fee ':'actual_setup_fee',
'Actual Expected Total Fees + Interest USD (Excluding Setup Fees)':'actual_total_fees_no_setup',
'Actual Other Adjustments USD':'adjustments',
'Aging':'aging',
'DQAging':'dq_aging',
'InvoiceYield(Repaid Only)':'invoice_yield',
'ExporterAggregate LTMRevenue':'total_exporter_volume',
'Step-up Interest Rate Tenor Including Grace Period':'step_up_int_tenor',
'Actual Factoring Fee USD':'actual_factor_fee',
'Actual Total Fees + Interest USD (Excluding Setup Fees)':'actual_total_fees_no_setup',
'In VASCO?':'vasco_flag',
'Outstanding Balance USD':'invoice_balance',
'Actual  Total Fees + Interest USD (Excluding Setup Fee)':'actual_total_fees_no_setup',
'Invoice Yield (Repaid Invoices Only)':'invoice_yield',
'ExporterID':'exporter_id',
'BuyerID':'buyer_id',
'Total Fees + Interest USD (Including Setup Fee)':'actual_total_fees',
'Dilution USD':'invoice_value_dilution'
 }


date_cols = ['new_due_date'
            , 'due_date'
            , 'modified_due_date'
            , 'step_up_date'
            , 'first_advance_date'
            , 'invoice_date'
            , 'cutoff_date'
            , 'full_payment_date']



# for f in tqdm.tqdm(sorted(glob.glob(data_dir + 'tapes\\*.xlsx'))):
#     df = pd.read_excel(f, sheet_name='All Invoices', skiprows=3, parse_dates=True)
#     df.columns = df.columns.str.replace('\n', '')
    
#     df.rename(columns=col_name_dict, inplace=True)
    
#     df['cutoff_date'] = pd.to_datetime(f[-13:-5]).date().isoformat()
#     df.reset_index(drop=True, inplace=True)

#     for col in date_cols:
#         if col not in df:
#             df[col] = ''
#         df[col] = pd.to_datetime(df[col], errors='coerce')
  
    
#     df['latest_due_date'] = df[['new_due_date', 'due_date']].max(axis=1)
#     df['days_dq'] = df.apply(get_dq_days, axis=1)
#     df['days_to_repay'] = df.apply(get_days_to_repay, axis=1)
#     df['vin_mnth'] = pd.to_datetime(df['adv_date']).dt.to_period('M')
#     df['vin_qtr'] = pd.to_datetime(df['adv_date']).dt.to_period('Q')
#     df['hs_code_descrip_short'] = df['hs_code_descrip'].str[0:25]
    
#     df.rename(columns=col_name_dict, inplace=True)
#     df = df.loc[:, ~df.columns.str.contains('\s')]
    
#     df.to_csv(f.replace('.xlsx', '.csv'))


def clean_tape_query(df):

    df = df[df['advanced_value_usd'] > 0]
    df['full_payment_date'].fillna(0, inplace=True)
    df['latest_due_date'] = df[['new_due_date', 'due_date']].max(axis=1)
    df['days_to_repay'] = df.apply(get_days_to_repay, axis=1)
    df['product_category'] = df.apply(get_domestic_factoring, axis=1)
    df['vin_mnth'] = pd.to_datetime(df['first_advance_date']).dt.to_period('M')
    df['vin_qtr'] = pd.to_datetime(df['first_advance_date']).dt.to_period('Q')
    df['currency'] = df['currency'].str.upper()
    df['currency'][df['currency'] == 'EURO'] = df['currency'][df['currency'] == 'EURO'].str.replace('EURO', 'EUR')
    df['currency'][df['currency'] == 'POUND'] = df['currency'][df['currency'] == 'POUND'].str.replace('POUND', 'GBP')
        
    return df
