
with 

source as (

    select * from {{ source('ecommerce', 'customers') }}

),

renamed as (

    select

        ----------  ids
        customer_id,

        ---------- properties
        customer_name

    from source

)

select * from renamed
