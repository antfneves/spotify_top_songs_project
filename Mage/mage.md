1) Added the GOOGLE_SERVICE_ACC_KEY_FILEPATH and the GOOGLE_LOCATION to the io_config.yaml file.

2) Created a pipeline with three blocks: load_spotify, transform_spotify_data and spotify_to_gcs.

3) In the [first block](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/load_spotify.py) I declared the filepath and the data types for the columns.

4) In the [second block](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/transform_spotify_data.py) I decided to drop all the rows that have the columns name and artists with NULL values.

5) In the [last block](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/spotify_to_gcs.py) I declared the bucket name of my GCS and the name of the parquet file that I wanted to create and send to the bucket.

6)   
