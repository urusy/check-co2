from google.cloud import bigquery
import datetime
import json
import mh_z19

project = "urusy-1"
dataset = "co2"
table = "mh_z19"

print("start process")

sensor_data = mh_z19.read_all()
print("get sensor value")

print(sensor_data)
print(type(sensor_data))

#sensor_data = json.loads(json_str)

print("loads json")

bigquery_client = bigquery.Client()

print("connect bigquery")

query = "INSERT INTO `{0}.{1}.{2}` VALUES (TIMESTAMP('{3}'), {4}, {5}, {6}, {7}, {8})".format(project, dataset, table, datetime.datetime.now(datetime.timezone.utc), sensor_data["co2"], sensor_data["temperature"], sensor_data["TT"], sensor_data["SS"], sensor_data["UhUl"])

rows = bigquery_client.query(query).result()

print("finish process")
