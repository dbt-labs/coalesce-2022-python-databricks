def model(dbt, session):

    # get upstream data
    orders = dbt.ref("orders").pandas_api()

    # describe the data
    described = None  # TODO: fix this

    # insert the index as the first column
    described.insert(0, "metric", described.index)

    return described
