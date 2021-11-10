select
    i.id,
    i.customer_notes as AT_identifier,
    i.importer_user_id as buyer_id,
    i.exporter_user_id as exporter_id,
    u.country as exporter_country,
    u1.country as buyer_country, upper(i.currency) as currency,
    (case when i. term_from=1 then "Invoice Date"
          when i. term_from=2 then "BL Date"
          when i. term_from=3 then "FDA Clearance Date"
          when i. term_from=5 then "Discharge Date"
          when i. term_from=6 then "Goods Usage Date"
          when i. term_from=7 then "Advance Date"
          else null end) as anchor_event,
    (case when i. term_from=7 then disbursed_date
          when i. term_from=5 then discharge_date
          when i. term_from=2 then bl_date
          when i. term_from in (3,6) then fda_date
          else null end) as anchor_event_date,
    i.credit_term as expected_tenor_from_anchor_event_date,
    i.invoice_date,
    i.disbursed_date as first_advance_date,
    i.repayment as due_date,
    i.received as full_payment_date,
    (case when i.duration>0 then duration else null end) as actual_outstanding_tenor,
    (i.advance_total_usd) as net_invoice_value_usd,
    (i.deposit_total_usd) as margin_received,
    (i.advance_total_usd-i.deposit_total_usd) as principal_amount_USD,
    (i.payment_total_usd) as payment_total_usd,
    i.status,
    p.interest_rate/100 as interest_rate,
    p.flat_discounting_fee/100 as Reverse_factoring_fee,
    p.overdue_rate/100 as step_up_interest_rate,
    (i.total_fees*i.settle_conversion) as actual_total_fee,
    (i.total_interest_paid*i.settle_conversion) as actual_interest_paid,
    (i.total_disc_fees_paid*i.settle_conversion) as actual_reverse_factoring_fee_paid,
    (i.total_overdue_paid*i.settle_conversion) as actual_overdue_interest_charges_paid

    from
      drip_prod.invoices i
    left join
      drip_prod.users u
      on
      i.exporter_user_id=u.id
    left join
      drip_prod.users u1
      on
      i.importer_user_id=u1.id
    left join
      drip_prod.plans p
      on
      i.plan_id=p.id
    where
      1=1
      and i.debtor_type like "%scf%"
      and i.importer_user_id!=167338
