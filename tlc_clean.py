from pandas.io.gbq import read_gbq

project = "spheric-crow-161317"
sample_query = "SELECT count(*) FROM `bigquery-public-data.new_york.tlc_yellow_trips_2009`"

df = read_gbq(query=sample_query, project_id=project, dialect='standard')

print df
