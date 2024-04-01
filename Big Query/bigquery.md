1) In the BigQuery Studio section of the Google Cloud I opened a new SQL query.

![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Big%20Query/bigquery_new_sql_query.jpeg?raw=true) 

2) Used this [query](https://github.com/antfneves/spotify_top_songs_project/blob/main/Big%20Query/external_to_partitoned_table.sql)  to create an external table referring to my GCS path and to create a partition and cluster table from the external table. To create the partition and cluster table I used the date from the the snapshot_date column for partitioning and the spotify_id for clustering.

![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Big%20Query/bigquery_tables.jpg?raw=true)     
