def model(dbt, session):

    # get upstream data
    orders = dbt.ref("orders").pandas_api()
    products = dbt.ref("stg_products").pandas_api()
    order_items = dbt.ref("stg_order_items").pandas_api()

    # list of unique product ids
    product_ids = None  # TODO: fix this

    # get the subtotal for each product_id for each order_id
    order_item_product_subtotals = (
        # TODO: fix this
    )

    # rename the product_id columns to include "subtotal_"
    renames = {product_id: f"subtotal_{product_id}" for product_id in product_ids}
    order_item_product_subtotals = order_item_product_subtotals.rename(columns=renames)

    # fill NaNs with 0s
    order_item_product_subtotals = order_item_product_subtotals.fillna(0)

    # merge with the existing orders mart
    orders_with_subtotals = orders.merge(order_item_product_subtotals, on="order_id")

    return orders_with_subtotals
