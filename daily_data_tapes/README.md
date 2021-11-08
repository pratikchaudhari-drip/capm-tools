# daily_data_tapes

to be deployed on server for receiving daily emails of final tapes


Features to discuss:
1. For invoices in “Pending Settlement” and 'autosettled' stage, change NAs in Fees and Interest (using metabase query)
2. Few IF invoices have 'insurable flag' tagged 'insured'
3. Query for SCF
4. Finalise on the tapes' date nomenclature
5. Add facility-wise eligiblity columns
6. Not sure how the server will handle db_connector - or if we even need to include it as part of the script
