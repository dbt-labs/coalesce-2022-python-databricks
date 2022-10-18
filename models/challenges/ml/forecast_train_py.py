import pyspark.pandas as ps

from datetime import datetime

from prophet import Prophet
from prophet.serialize import model_to_json


def model(dbt, session):

    # comment this out to enable the model
    dbt.config(enabled=False)

    # dbt configuration
    dbt.config(materialized="incremental")

    # use current time as index
    trained_at = datetime.now()

    # get upstream data
    revenue = dbt.ref("revenue_weekly_by_location").pandas_api()

    # rename to match prophet's expected column names
    renames = {
        "date_week": "ds",
        "location_name": "location",
        "revenue": "y",
    }
    revenue = revenue.rename(columns=renames)

    # get list of unique locations dynamically
    locations = sorted(list(revenue["location"].unique().to_numpy()))

    # train the ML models per location
    models = [
        # TODO: fix this
    ]

    # persist models
    df = None  # TODO: fix this

    return df
