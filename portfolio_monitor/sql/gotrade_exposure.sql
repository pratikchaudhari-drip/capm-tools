select
    sum(b.inventory_limit_utilisation + b.total_ar_limit_utilisation) as `total_gotrade_exposure`
    from
        got_prod.buyers b
    where
        1=1