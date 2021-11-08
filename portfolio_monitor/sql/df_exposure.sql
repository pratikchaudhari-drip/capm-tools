select 
    sum(dt.outstanding_advance_balance_usd)
    from 
        drip_prod.data_tapes dt
    where 
        1=1
        and dt.exporter_country = dt.buyer_country