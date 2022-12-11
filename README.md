This is a repository that shows the progress that I made in using Python to create a mood-based song recommender. This project was done over the course of a college semester. I started the project by trying to learn more about music recommendations. This was done through requesting data from Spotify and
looking at the Spotify songs' energy and valence as a means to identify the mood of them. Then, I would recommend Spotify songs for a Spotify song input
based on whether these songs had a close energy and valence value to the inputted song. Based on my classmates' feedback of creating a recommender system
distinct from Spotify, I focused on grouping the songs on my computer into playlists based on the extracted tempo and loudness from the mp3 files. The
description of each of the files in the repository is listed below in the order in which I started working on them in the semester:

authorization.py: Python script where I requested a token from Spotify that would allow me to access the website's data.

recommendation.pdf: Python journal where I created the dataset of songs from each genre in Spotify that would be returned as recommendations for an inputted Spotify song.

music.csv: Returned dataset generated from recommendation.ipynb.

application.pdf: Python journal where I defined how recommendations would be returned for an inputted Spotify song in which songs that were closest to the inputted song in energy and valence would be recommended.

Songs.pdf: Journal where I generated playlist recommendation for the songs in song_data

