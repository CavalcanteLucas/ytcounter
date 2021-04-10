Hello user,

This programs tells you how long it will take for you to 
finish your favorite YouTube playlist. Have fun.

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

- Input:
    - Valid YouTube playlist ID;
- Output:
    - Progress table


Please have a great day!

## References:

- Basic reference for getting `PlaylistItems` data from **YouTubeAPIv3**: https://developers.google.com/youtube/v3/docs/playlistItems/list
- Further instructions for running these codes locally: https://developers.google.com/explorer-help/guides/code_samples#python
- Add external users:
    - https://console.cloud.google.com/
    - API e serviços
    - Credenciais
    - Editar cliente OAuth
    - Tela de consentimento OAuth
    - Add users

## TODO:
- Add header to logfile
- Add tests
    - Second column must be increasing
    - Third column must be decreasing
    - Last element of third column must be 00:00:00