import io
import requests
import pandas as pd
from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    filepath = 'universal_top_spotify_songs.csv'

    spotify_dtypes ={
        'spotify_id': str,
        'name': str,
        'artists': str,
        'name': str,
        'daily_rank': pd.Int64Dtype(),
        'daily_movement': pd.Int64Dtype(),
        'weekly_movement': pd.Int64Dtype(),
        'weekly_movement': pd.Int64Dtype(),
        'country': str,
        'popularity': pd.Int64Dtype(),
        'is_explicit': bool,
        'duration_ms': pd.Int64Dtype(),
        'album_name': str,
        'danceability': float,
        'energy': float,
        'key': pd.Int64Dtype(),
        'loudness': float,
        'mode': pd.Int64Dtype(),
        'speechiness': float,
        'acousticness': float,
        'liveness': float,
        'valence': float,
        'tempo': float,
        'time_signature': pd.Int64Dtype()       

        }

    parse_dates = ['snapshot_date', 'album_release_date']

    return pd.read_csv(filepath, sep=",", dtype=spotify_dtypes, parse_dates=parse_dates)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
