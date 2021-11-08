select 
    sum(dt.outstanding_advance_balance_usd)
    from 
        drip_prod.data_tapes dt
    where 
        1=1
        and dt.product_category = 'IF'
        and dt.debtor_type = 'core'
        and dt.exporter_country <> dt.buyer_country