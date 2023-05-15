from typing import Optional

from pyspark.sql import SparkSession


def start_spark(app_name: Optional[str], bucket: str) -> SparkSession:
    """
    :param app_name: Name of the Spark App
    :param bucket: the name of the bucket to be used by the Spark BigQuery connector
    :return: SparkSession
    """
    if app_name:
        builder = SparkSession.builder.appName(f'{app_name}')
    else:
        builder = SparkSession.builder

    spark = builder.getOrCreate()
    spark.conf.set('temporaryGcsBucket', bucket)

    return spark
