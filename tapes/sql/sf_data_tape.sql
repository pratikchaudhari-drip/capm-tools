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
        and dt.debtor_type = 'core'
