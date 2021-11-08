select 
    sum(dt.outstanding_advance_balance_usd) - sum(dt.margin_received_usd) as sum
    -- ,ie.name
    -- ,ie.id
    from 
        drip_prod.data_tapes dt
    where 
        1=1
        -- and dt.product_category = 'IF'
        and dt.debtor_type = 'scf'
        and dt.stage not in ('hold', 'uploaded')
        and dt.outstanding_advance_balance_usd > 0
        -- and dt.exporter_country <> dt.buyer_country
    -- group by ie.name