def model(dbt, session):

    # get upstream data
    orders = dbt.ref("orders").pandas_api()

    # describe the data
    described = orders.describe()

    # insert the index as the first
    described.insert(0, "metric", described.index)

    return described
