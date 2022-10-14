/*
    A SQL test on a Python model!
*/

select
    *
from {{ ref('describe_py') }}
where (
    summary = 'mean' and
    count_drink_items < .8
) or 
(
    summary = 'stddev' and
    subtotal > 20
)