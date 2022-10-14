/*
    A SQL test on a Python model!
*/

select
    *
from {{ ref('describe_py') }}
where (
    metric = 'mean' and
    count_drink_items < .8
) or 
(
    metric = 'std' and
    subtotal > 20
)