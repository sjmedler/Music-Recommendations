import tekore as tk

def authorize():
    CLIENT_ID = "hidden"
    CLIENT_SECRET = "hidden"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)
