# Analysis of Musical and Lyrical Trends

## Project Overview
This project explores how music and lyrics have evolved from 1990 to 2024, reflecting cultural and technological shifts.

## Project Goals
- Analyze the impact of digitalization and streaming services on music consumption.
- Examine trends in song duration, tonal and lyrical sentiment, and thematic content.

## Some of Technological Tools and Techniques
### Data Collection:
- **BeautifulSoup** for web scraping.
- **LyricsGenius** for lyric extraction via the Genius API.
- **Spotipy** for audio features via the Spotify API.

### Data Cleaning:
- **langdetect** for language detection.
- **deep translator** for translations.
- Preprocessing steps included removing non-English lyrics, special characters, and stopwords.

### Sentiment Analysis:
- **Spotify's valence metric** for tonal sentiment.
- **TweetNLP** for lyrical sentiment analysis.

### Topic Modeling:
- **BERTopic** for clustering and topic representation.
- **UMAP** for dimensionality reduction.
- **HDBSCAN** for clustering.

### Prompt Engineering:
- Utilized **ChatGPT-4** to assign appropriate topic names for better interpretability.

## Key Findings
- **Sentiment Shift:** Music is becoming more somber, with a notable increase in songs with negative valence over time.
- **Lyrical Trends:** Decline in romantic themes and a rise in aggressive and explicit content.
- **Song Duration:** Tracks are getting shorter, aligning with changing listener preferences and consumption habits.
- **Seasonal Variations:** Happier songs tend to peak in popularity from late spring to mid-autumn.

## Future Work
- Expanding analysis to include genre-specific trends and external influences such as historical events and social media.
- Exploring alternatives to the Genius API to enhance the robustness of our analysis.
- Conducting topic modeling on entire songs for more comprehensive insights.

## Conclusion
This project underscores the dynamic nature of music and its reflection of societal changes. We are excited to continue exploring the rich tapestry of musical evolution!

## Authors
- Ozan Güner
- Miguel Habana

[You can reach the project presentation from here for more details.](<Analysis of Musical and Lyrical Trends.pdf>)