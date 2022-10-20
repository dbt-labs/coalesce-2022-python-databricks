
with 

source as (

    select * from {{ source('ecommerce', 'orders') }}

    --- data runs to 2026, truncate timespan to desired range, current time as default
    where ordered_at <= {{ var('truncate_timespan_to') }}

),

renamed as (

    select

        ----------  ids
        order_id,
        location_id,
        customer_id,

        ---------- properties
        cast(order_total / 100.0 as float) as order_total,
        cast(tax_paid / 100.0 as float) as tax_paid,

        ---------- timestamps
        ordered_at

    from source

)

select * from renamed
