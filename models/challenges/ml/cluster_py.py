# imports
import pyspark.pandas as ps

from sklearn.cluster import KMeans


def model(dbt, session):

    # get variables
    n_clusters = dbt.config.get("suspected_personas")

    # get upstream data
    orders_with_subtotals = dbt.ref("pivot_py").pandas_api()

    # drop non-numeric columns
    X = None  # TODO: fix this

    # train model
    kmeans = KMeans(n_clusters=n_clusters)
    model = None  # TODO: fix this

    # score model
    cluster_labels = None  # TODO: fix this

    # add cluster labels to orders_with_subtotals
    temp = ps.DataFrame(data=cluster_labels, columns=["cluster_label"])
    orders_with_subtotals_and_clusters = orders_with_subtotals.merge(
        temp, left_index=True, right_index=True
    )

    return orders_with_subtotals_and_clusters
