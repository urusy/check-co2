from google.cloud import bigquery
import datetime
import json
import mh_z19
import slackweb

project = "urusy-1"
dataset = "co2"
table = "mh_z19"

CO2_THRESHOLD = 900

sensor_data = mh_z19.read_all()

bigquery_client = bigquery.Client()

query = "INSERT INTO `{0}.{1}.{2}` VALUES (TIMESTAMP('{3}'), {4}, {5}, {6}, {7}, {8})".format(project, dataset, table, datetime.datetime.now(datetime.timezone.utc), sensor_data["co2"], sensor_data["temperature"], sensor_data["TT"], sensor_data["SS"], sensor_data["UhUl"])

rows = bigquery_client.query(query).result()

# if over threshold co2 notification to slack
co2 = sensor_data["co2"]

with open('config.json', 'r') as config:
    json_dict = json.load(config)
    latest_file_name = json_dict['files']['latest']
    slack_url = json_dict['slack']['url']

with open(latest_file_name) as latest_file_r:
    co2_latest = int(latest_file_r.read())

if co2 >= CO2_THRESHOLD and co2_latest < CO2_THRESHOLD:
    # fire
    slack = slackweb.Slack(url=slack_url)
    slack.notify(text='Carbon dioxide concentration has exceeded the standard value. : ' + str(co2) + ' ppm\nhttps://datastudio.google.com/u/0/reporting/64e830d0-97f4-43c2-b239-ded45d657b12/page/98meB')

with open(latest_file_name, mode='w') as latest_file_w:
    latest_file_w.write(str(co2))
