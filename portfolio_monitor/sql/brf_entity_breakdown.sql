select 
    sum(dt.outstanding_advance_balance_usd) - sum(dt.margin_received_usd) as sum
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
        -- and dt.product_category = 'IF'
        and dt.debtor_type = 'scf'
        and dt.outstanding_advance_balance_usd > 0
        -- and dt.exporter_country <> dt.buyer_country
    group by ie.name