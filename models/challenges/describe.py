
def model(dbt, session):

    orders = dbt.ref("orders")

    described = orders.describe()
    return described