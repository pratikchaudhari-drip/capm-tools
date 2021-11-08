select 
    dt.*
    ,u1.company as exporter_company_name
    ,u2.company as importer_company_name
    from 
        drip_prod.data_tapes dt
    left join 
        drip_prod.users u1
        on 
        dt.exporter_user_id = u1.id
    left join 
        drip_prod.users u2
        on 
        dt.importer_user_id = u2.id
    where
        1=1 
        and dt.advanced_value_usd > 0
        -- and dt.debtor_type is null -- 'core'
        and dt.stage not in ('outdated', 'hold', 'collection', 'verified', 'uploaded', 'data_entry'
                            , 'first_invoice', 'info_pending', 'processing', 'draft', 'buyer_esign_pending'
                            , 'pd_received_pending', 'pending', 'pdc_pending', 'generated', 'cma_bl_pending'
                            , 'data_entry_verification', 'buyer_not_approved')