This is a repository that shows the progress that I made in using Python to create a mood-based song recommender. This project was done over the course of a college semester. I started the project by trying to learn more about music recommendations. This was done through requesting data from Spotify and
looking at the Spotify songs' energy and valence as a means to identify the mood of them. Then, I would recommend Spotify songs for a Spotify song input
based on whether these songs had a close energy and valence value to the inputted song. Based on my classmates' feedback of creating a recommender system
distinct from Spotify, I focused on grouping the songs on my computer into playlists based on the extracted tempo and loudness from the mp3 files. The
description of each of the files in the repository is listed below in the order in which I started working on them in the semester:

authorization.py: Python script where I requested a token from Spotify that would allow me to access the website's data.

recommendation.ipynb: Python journal where I created the dataset of songs from each genre in Spotify that would be returned as recommendations for an inputted Spotify song.

music.csv: Returned dataset generated from recommendation.ipynb.

application.ipynb: Python journal where I defined how recommendations would be returned for an inputted Spotify song in which songs that were closest to the inputted song in energy and valence would be recommended.

song_data: Folder which contains all of the mp3 files for the songs that I tried to get playlist recommendations for.

wav: The wav files generated from converting the mp3 files from song_data. These files were used to extract the tempo and loudness feature for each song.

Songs.ipynb: Journal where I generated playlist recommendation for the songs in song_data

