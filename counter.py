import pafy
import sys
from datetime import datetime, timedelta
from nptime import nptime
from time import sleep
import progressbar
import os

all = ['YTCounter']

class YTCounter:

    def __init__(self, url_playlist):
        self.playlist = pafy.get_playlist2(url_playlist)
        self.playlist_len = len(self.playlist)
        self.filename = self.playlist.plid + '.log'
        if not(os.path.exists(self.filename)):
            self._makefile()

    def _makefile(self):
        print('Computing...')
        bar = progressbar.ProgressBar(maxval=self.playlist_len, \
                widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        file = open(self.filename,'w+')
        for i in range(self.playlist_len):
            bar.update(i+1)
            duration = datetime.strptime(self.playlist[i].duration, '%H:%M:%S').time()
            file.write(str(duration)+'\n')
        file.close()
        bar.finish()

    def progress(self, current):
        print('Current progress: {0:.2f}% Complete'.format((current-1)/self.playlist_len*100))

    def left(self, current):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                cummulative_duration = nptime(0,0)
                for i, line in enumerate(file.readlines()):
                    if i > current:
                        duration = datetime.strptime(line.strip('\n'), '%H:%M:%S').time()
                        duration = timedelta(minutes=duration.minute, seconds=duration.second)
                        cummulative_duration += duration
            print('Remaining Time: {}'.format(cummulative_duration))

