#In this python file, I request to get data from the Spotify API. This is done through the Spotify developers website where I set
# up an account to get my client id and sectet. These credentials are then what I use to send a request to Spotify to gain a token
# that allows me to access the data on Spotify. This token was used in the recommendation journal where I gathered songs from Spotify.
import tekore as tk

def authorize():
    CLIENT_ID = "hidden"
    CLIENT_SECRET = "hidden"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)
