1) Added the GOOGLE_SERVICE_ACC_KEY_FILEPATH and the GOOGLE_LOCATION to the [io_config.yaml](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/io_config.yaml) file.

2) Created a pipeline with three blocks: [load_spotify ](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/load_spotify.py), [transform_spotify_data](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/transform_spotify_data.py) and  [spotify_to_gcs](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/spotify_to_gcs.py).

3) In the [first block](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/load_spotify.py) I declared the file path and the data types for the columns.

4) In the [second block](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/transform_spotify_data.py) I decided to drop all the rows that have the columns name and artists with NULL values.

5) In the [last block](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/spotify_to_gcs.py) I declared the bucket name of my GCS and the name of the parquet file that I wanted to create and send to the bucket.

![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/mage_tree.jpg?raw=true) 

6) Created a trigger to run the pipeline on a daily basis.

![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Mage/mage_trigger.jpg?raw=true)    
    
