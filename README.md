Hello user,

This programs tells you how long it will take for you to 
finish your favorite YouTube playlist.

Please have a great day!

## Important

Ask for access to <lucas@labcodes.com.br>

## Instructions of use

1) Create and activate a new virtual environment:
```
$virtualenv venv
$source venv/bin/activate
```

2) Install requirements:
```
$pip install -r requirements.txt
```

3) Edit `example.py` with a valid URL and run:
```
python example.py
```

### Input:
- Valid YouTube playlist ID

Example:

The valid ID from the playlist: https://www.youtube.com/watch?v=xpDnVSmNFX0&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&ab_channel=GauravSen is `PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX`

### Output:
- Progress table

Example:
```
+------------------------------------------+---------+----------+----------+---------+
| Playlist: System Design                  | Durati. | Cummull. | Remaini. | Progre. |
+------------------------------------------+---------+----------+----------+---------+
| Video 1: System Design Basics: Horizont  | 0:07:56 | 00:07:56 | 06:26:26 | 2.01%   |
| Video 2: How to start with distributed   | 0:10:03 | 00:17:59 | 06:16:23 | 4.56%   |
| Video 3: What is Load Balancing?         | 0:13:50 | 00:31:49 | 06:02:33 | 8.07%   |
| Video 4: What is Consistent Hashing and  | 0:10:50 | 00:42:39 | 05:51:43 | 10.81%  |
| Video 5: What is a Message Queue and Wh  | 0:09:59 | 00:52:38 | 05:41:44 | 13.35%  |
| Video 6: What is a microservice archite  | 0:08:19 | 01:00:57 | 05:33:25 | 15.46%  |
| Video 7: What is Database Sharding?      | 0:08:56 | 01:09:53 | 05:24:29 | 17.72%  |
| Video 8: How Netflix onboards new conte  | 0:10:56 | 01:20:49 | 05:13:33 | 20.49%  |
| Video 9: System Design: Tinder as a mic  | 0:36:41 | 01:57:30 | 04:36:52 | 29.79%  |
| Video 10: Whatsapp System Design: Chat M | 0:27:00 | 02:24:30 | 04:09:52 | 36.64%  |
| Video 11: What is Distributed Caching? E | 0:14:04 | 02:38:34 | 03:55:48 | 40.21%  |
| Video 12: What is an API and how do you  | 0:15:26 | 02:54:00 | 03:40:22 | 44.12%  |
| Video 13: Capacity Estimation: How much  | 0:13:12 | 03:07:12 | 03:27:10 | 47.47%  |
| Video 14: How to avoid a single point of | 0:06:34 | 03:13:46 | 03:20:36 | 49.13%  |
| Video 15: Introduction to NoSQL database | 0:27:01 | 03:40:47 | 02:53:35 | 55.98%  |
| Video 16: How databases scale writes: Th | 0:17:22 | 03:58:09 | 02:36:13 | 60.39%  |
| Video 17: Distributed Consensus and Data | 0:15:48 | 04:13:57 | 02:20:25 | 64.39%  |
| Video 18: What is the Publisher Subscrib | 0:11:25 | 04:25:22 | 02:09:00 | 67.29%  |
| Video 19: Why do Databases fail? AntiPat | 0:08:27 | 04:33:49 | 02:00:33 | 69.43%  |
| Video 20: What's an Event Driven System? | 0:14:59 | 04:48:48 | 01:45:34 | 73.23%  |
| Video 21: Designing Instagram: System De | 0:24:29 | 05:13:17 | 01:21:05 | 79.44%  |
| Video 22: Service discovery and heartbea | 0:06:45 | 05:20:02 | 01:14:20 | 81.15%  |
| Video 23: Avoid cascading failures in a  | 0:18:06 | 05:38:08 | 00:56:14 | 85.74%  |
| Video 24: Detecting anomalies using Isol | 0:07:37 | 05:45:45 | 00:48:37 | 87.67%  |
| Video 25: Google Maps Algorithm: Designi | 0:22:22 | 06:08:07 | 00:26:15 | 93.34%  |
| Video 26: Containers and Virtualisation  | 0:08:00 | 06:16:07 | 00:18:15 | 95.37%  |
| Video 27: 5 Tips for System Design Inter | 0:08:19 | 06:24:26 | 00:09:56 | 97.48%  |
| Video 28: System Design Course Overview  | 0:05:51 | 06:30:17 | 00:04:05 | 98.96%  |
| Video 29: Low Level Design: A Video Cour | 0:04:05 | 06:34:22 | 00:00:00 | 100.00% |
+------------------------------------------+---------+----------+----------+---------+
```

## References:

- Basic reference for getting `PlaylistItems` data from **YouTubeAPIv3**
  - https://developers.google.com/youtube/v3/docs/playlistItems/list
- Further instructions for running these codes locally
  - https://developers.google.com/explorer-help/guides/code_samples#python
- Add external users:
  - https://console.cloud.google.com/
    - API e serviços
    - Credenciais
    - Editar cliente OAuth
    - Tela de consentimento OAuth
    - Add users

## TODO:

- Integrate with Django and YouTube API
  - https://www.toptal.com/django/youtube-api-integration-uploading-videos
  - https://www.toptal.com/django/integrate-oauth-2-into-django-drf-back-end
- Gerar politica de privacidade para publicar aplicacao:
  - https://www.nuvemshop.com.br/ferramentas/gerador-politica-de-privacidade
- Add to "Instructions of use"
  - Tell user to clone the project
  - Tell user to create `client_secrets.json`
  - Show authentication cycle illustration
    - Link generation
    - OAuth screenshots
- Add header to logfile (??)
- Add tests
  - Second column must be increasing
  - Third column must be decreasing
  - Last element of third column must be 00:00:00
- Work for playlists with more than 50 videos
- Make download of missing videos metadata in a partially downloaded playlist
- Create 'metadata' directory to include all downloaded data
  - Add 'metadata' dir to .gitignore file