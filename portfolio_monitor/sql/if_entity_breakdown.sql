select 
    sum(dt.outstanding_advance_balance_usd) as sum
    ,ie.name
    ,ie.id
    from 
        drip_prod.data_tapes dt
    join 
        drip_prod.investment_entities ie
        on
        ie.id = dt.entity_id
    where 
        1=1
        and dt.product_category = 'IF'
        and dt.debtor_type = 'core'
        and dt.exporter_country <> dt.buyer_country
    group by ie.name