from google.cloud import bigquery
import datetime

project = "urusy-1"
dataset = "co2"
table = "MH_Z19"

bigquery_client = bigquery.Client()
query = "INSERT INTO `{0}.{1}.{2}` VALUES (TIMESTAMP('{3}'), {4}, {5}, {6}, {7}, {8})".format(project, dataset, table, datetime.datetime.now(), 1.1, 2.2, 3, 4, 5)

rows = bigquery_client.query(query).result()
