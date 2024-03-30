-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `dezoomcampproject.spotify.external_top_songs`
OPTIONS (
  format = 'parquet',
  uris = ['gs://dezoomcampproject-terra-bucket/spotify_songs_data.parquet']
);

-- Creating a partition and cluster table
CREATE OR REPLACE TABLE dezoomcampproject.spotify.top_songs_partitoned_clustered
PARTITION BY DATE(snapshot_date)
CLUSTER BY spotify_id AS
SELECT * FROM dezoomcampproject.spotify.external_top_songs;