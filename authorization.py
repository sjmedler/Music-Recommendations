import tekore as tk

def authorize():
    CLIENT_ID = "8b6f1243968d4e4cada4c1f45763409a"
    CLIENT_SECRET = "afbe6d6090ea47d3829fc015e7fadc1b"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)
