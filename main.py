from google.cloud import bigquery
import datetime
import json

project = "urusy-1"
dataset = "co2"
table = "mh_z19"

sensor_json = '{"co2": 611, "temperature": 25, "TT": 65, "SS": 0, "UhUl": 34816}'

sensor_data = json.loads(sensor_json)

bigquery_client = bigquery.Client()
query = "INSERT INTO `{0}.{1}.{2}` VALUES (TIMESTAMP('{3}'), {4}, {5}, {6}, {7}, {8})".format(project, dataset, table, datetime.datetime.now(), sensor_data["co2"], sensor_data["temperature"], sensor_data["TT"], sensor_data["SS"], sensor_data["UhUl"])

rows = bigquery_client.query(query).result()
