# Analysis of Musical and Lyrical Trends at Intelligent Interactive Systems (MIIS)

#### Oktay Ozan Güner   -  ID : OZAN_ID
#### Juan Miguel Alfonso Habana   -  ID : MIGUEL_ID

# Introduction
"""
Since 1990, the way people interact with music has evolved significantly. This period marks a transition from the tangible, physical media of CDs and vinyl to the intangible, yet infinitely accessible world of digital music. 
* How digitalization and streaming have influenced listeners? 
* How the listening habits have changed over time?

We'll examine how our music listening habits have been affected from duration of the songs to the way sentiment of the lyrics.
"""



# Importing packages
import lyricsgenius as lg 
from dotenv import load_dotenv
import os
import pandas as pd
import time 
import random
import numpy as np


load_dotenv()       # Loading environment variables
access_token = os.getenv("GENIUS_ACCESS_TOKEN")       
genius = lg.Genius(access_token)        # Reaching genius API

# Getting the Billboard lists that we scraped from Billboard url.
file_path = "Billboard_Lists_1960-01-01_2024-02-23.csv"
df = pd.read_csv(file_path)
df2 = df[["Artist_Name","Song"]].drop_duplicates().reset_index(drop=True)       # Removing duplicates based on artists and songs


df2["Lyrics"] = np.nan          # Assigning a new column to write lyrics into it
for ind, data in enumerate(df2.values):
    print(ind)
    try:
        start_time = time.time()
        song = genius.search_song(title=data[1], artist=data[0])        # Getting song names
        song_lyrics = song.lyrics                                       # Getting song lyrics
        df3["Lyrics"][ind] = song_lyrics                                # Assigning lyrics to 'Lyrics' column of the dataframe.
        end_time = time.time()
        print(f"Process Time: {end_time-start_time} seconds..")         # Measuring the processing time
    except:
        print("Error")
        pass


df2.to_csv("Billboard_Lyrics_1960-01-01_2024-02-23_Part9.csv", index=False)       # Saving the dataframe with the lyrics