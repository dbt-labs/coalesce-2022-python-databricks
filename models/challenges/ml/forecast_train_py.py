# TODO: use mlflow?
import pyspark.pandas as ps

from datetime import datetime

from prophet import Prophet
from prophet.serialize import model_to_json


def model(dbt, session):

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
        Prophet().fit(revenue[revenue["location"] == location].to_pandas())
        for location in locations
    ]

    # persist models
    df = ps.DataFrame(
        {
            "trained_at": [trained_at] * len(locations),
            "location": locations,
            "model": [model_to_json(model) for model in models],
        }
    )

    return df
