import os
import json
import isodate
from nptime import nptime
from datetime import datetime, timedelta
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from terminaltables import AsciiTable


def get_youtube_client():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )
    return youtube


def get_playlist_data_from_api(youtube_client, playlist_url):
    request = youtube_client.playlists().list(
        part="snippet",
        id=playlist_url,
    )
    response = request.execute()
    return response


def get_playlist_items_data_from_api(youtube_client, max_results, playlist_url):
    request = youtube_client.playlistItems().list(
        part="contentDetails",
        maxResults=max_results,
        playlistId=playlist_url,
    )
    response = request.execute()
    return response


def get_video_data_from_api(youtube_client, video_id):
    request = youtube_client.videos().list(part="contentDetails, snippet", id=video_id)
    response = request.execute()
    return response


def main_func(playlist_url):

    filename = f"{playlist_url}"
    path = f"{os.getcwd()}/{filename}"

    # Create directory with playlist name
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print(f"Failed to create directory {path}")
        else:
            print(f"Created directory {path}")

    # Get playlist data
    try:
        filepath = f"{path}/playlist.json"
        with open(filepath, "r") as file:
            playlist_data = json.load(file)
    except:
        try:
            youtube_client
        except NameError:
            youtube_client = get_youtube_client()
        
        playlist_data = get_playlist_data_from_api(
            youtube_client=youtube_client, playlist_url=playlist_url
        )
        print(f"Obained playlist data")

        # Create file with playlist data
        try:
            filepath = f"{path}/playlist.json"
            playlist_data_as_json = json.dumps(playlist_data, indent=2)
            with open(filepath, "w") as file:
                file.write(playlist_data_as_json)
            print(f"Created playlist data file {filepath}")
        except:
            print(f"Failed to create playlist data file {filepath}")

    playlist_title = playlist_data["items"][0]["snippet"]["title"]

    # Get playlist items data
    try:
        filepath = f"{path}/{filename}.json"
        with open(filepath, "r") as file:
            playlist_items_data = json.load(file)
    except:
        try:
            youtube_client
        except NameError:
            youtube_client = get_youtube_client()

        playlist_items_data = get_playlist_items_data_from_api(
            youtube_client=youtube_client, max_results=30, playlist_url=playlist_url
        )
        print(
            f"Obtained playlist data with {playlist_items_data['pageInfo']['totalResults']} videos"
        )

        # Create file with playlist items data
        try:
            filepath = f"{path}/{filename}.json"
            playlist_items_data_as_json = json.dumps(playlist_items_data, indent=2)
            with open(filepath, "w") as file:
                file.write(playlist_items_data_as_json)
            print(f"Created playlist data file {filepath}")
        except:
            print(f"Failed to create playlist data file {filepath}")

    videos_id = [
        video["contentDetails"]["videoId"] for video in playlist_items_data["items"]
    ]

    # Get each video data
    try:
        videos_data = []
        for i in range(1, len(videos_id) + 1):
            filepath = f"{path}/video-{i}.json"
            with open(filepath, "r") as file:
                video_data = json.load(file)
                videos_data.append(video_data)
    except:
        try:
            youtube_client
        except NameError:
            youtube_client = get_youtube_client()
        
        videos_data = [
            get_video_data_from_api(youtube_client, video) for video in videos_id
        ]
        print(f"Obtained data of {len(videos_data)} videos")

        # Create file for each video data
        try:
            video_count = 1
            for video_data in videos_data:
                filepath = f"{path}/video-{video_count}.json"
                video_data_as_json = json.dumps(video_data, indent=2)
                with open(filepath, "w") as file:
                    file.write(video_data_as_json)
                video_count += 1
                print(f"Created video-{video_count} data file")
        except:
            print(f"Failed to create video-{video_count} data file")

    videos_duration = [
        isodate.parse_duration(video_data["items"][0]["contentDetails"]["duration"])
        for video_data in videos_data
    ]

    videos_title = [
        video_data["items"][0]["snippet"]["title"] for video_data in videos_data
    ]

    # Part 1:
    info = [
        [
            f"Playlist: {playlist_title}",
            "Durati.",
            "Cummull.",
            "Remaini.",
            "Progre.",
        ]
    ]
    cummulative_duration = nptime(0, 0)
    playlist_len = len(videos_duration)
    count_update = 0
    for video_duration in videos_duration:
        duration = datetime.strptime(str(video_duration), "%H:%M:%S").time()
        duration = timedelta(minutes=duration.minute, seconds=duration.second)
        cummulative_duration += video_duration
        info.append(
            (
                f"Video {count_update+1}: {videos_title[count_update][0:30]}",
                duration,
                cummulative_duration,
                0,
                "",
            )
        )
        count_update += 1

    remaining_duration = info[playlist_len][2]

    # Part 2:
    # Computing remaining durations
    total_duration = cummulative_duration.to_timedelta().total_seconds()
    count_update = 1
    for video_duration in videos_duration:
        temp_list = list(info[count_update])
        temp_list[3] = remaining_duration - info[count_update][1]
        remaining_duration = temp_list[3]
        progress = (
            100
            - (remaining_duration.to_timedelta().total_seconds() / total_duration) * 100
        )
        temp_list[4] = "%.2f%%" % progress
        info[count_update] = tuple(temp_list)
        count_update += 1

    # Make output file
    filepath = f"{path}/{filename}.out"
    with open(filepath, "w+") as file:
        file.write(AsciiTable(info).table)
