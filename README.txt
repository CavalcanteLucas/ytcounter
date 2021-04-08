Hello user, 
This programs tells you how long it will take for you to 
finish your favorite YouTube playlist. Have fun.

Input:
    - Valid YouTube playlist URL;
    - Current progress on the playlist, as a number.
Output:
    - Current progress in %;
    - Remaining time.

Instructions of use:

1) Create and activate a new virtual environment:
```
$virtualenv venv
$source venv/bin/activate
```

2) Install requirements:
```
$pip install -r requirements.txt --user
```

3) Edit `example.py` with a valid URL and run:
python example.py

Please have a great day!

TODO:
> add header to logfile
> add tests
    - second column must be increasing
    - third column must be decreasing
    - last element of third column must be 00:00:00