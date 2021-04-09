import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import json

class YTCounter:

    def __init__(self, playlist_url, max_results):
        self.playlist_url = playlist_url
        self.max_results = max_results
        self.filename = f"{self.playlist_url}.json"
        self.playlist_data = self.get_playlist_data_from_api()
        self.playlist_data_as_json = json.dumps(self.playlist_data, indent=2)

    def __str__(self):
        return self.playlist_data_as_json

    def get_playlist_data_from_api(self):
        youtube = self.get_youtube_client()        
        request = youtube.playlistItems().list(
            part="contentDetails",
            maxResults=self.max_results,
            playlistId=self.playlist_url
        )
        response = request.execute()

        return response
    
    def get_youtube_client(self):
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secrets.json"

        #Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes
        )
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials
        )
        return youtube

    def save_playlist_data(self):
        try:
            path = f"{os.getcwd()}/{self.filename}"
            os.mkdir(path)
        except OSError:
            print(f"Failed to create directory {path}")
        else:
            print(f"Created directory {path}")
        
        try:
            filename = f"{path}/{self.filename}"
            with open(filename, 'w') as file:
                file.write(self.playlist_data_as_json)
        except:
            print(f"Failed to create playlist data file {filename}")
        else:
            print(f"Created playlist data file {filename}")

        return True


playlist_url = "PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX"
ytc = YTCounter(playlist_url=playlist_url, max_results=30)
ytc.save_playlist_data()
print(ytc)