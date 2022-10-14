def model(dbt, session):

    # get upstream data
    orders = dbt.ref("orders").pandas_api()
    products = dbt.ref("stg_products").pandas_api()
    order_items = dbt.ref("stg_order_items").pandas_api()

    # list of unique product ids
    product_ids = sorted(list(set(products["product_id"].unique().to_numpy())))

    # get the subtotal for each product_id for each order_id
    order_item_product_subtotals = (
        order_items.merge(products, on="product_id")
        .groupby(["order_id", "product_id"])
        .agg(subtotal=("product_price", "sum"))
        .reset_index()
        .pivot(index="order_id", columns="product_id", values="subtotal")
        .reset_index()
    )

    # rename the product_id columns to include "subtotal_"
    renames = {product_id: f"subtotal_{product_id}" for product_id in product_ids}
    order_item_product_subtotals = order_item_product_subtotals.rename(columns=renames)

    # fill NaNs with 0s
    order_item_product_subtotals = order_item_product_subtotals.fillna(0)

    # merge with the existing orders mart
    orders_with_subtotals = orders.merge(order_item_product_subtotals, on="order_id")

    return orders_with_subtotals
