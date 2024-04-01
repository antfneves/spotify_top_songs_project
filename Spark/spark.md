
1) With [Jupyter Notebook](https://github.com/antfneves/spotify_top_songs_project/blob/main/Spark/spotify_top_songs.ipynb) I used Spark to convert the columns snapshot_date and album_release_date from datetime to date.
2) I noticed, in the information provided by the dataset, that all the songs that have the NULL value in the country column means that they belong to the Global Top 50 playlist, so I substituted all of the NULLs with 'Global'.
3) Wrote the transformed data back to BigQuery.
