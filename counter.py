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
        self.url_playlist = url_playlist
        self.filename = ''.join((self.url_playlist.split('playlist?list=')[1],'.log'))
        if os.path.exists(self.filename):
            if os.stat(self.filename).st_size == 0:
                os.remove(self.filename)
                self._makefile()
        else:
            self._makefile()
            
    def _makefile(self):
        print('Computing ...')
        print('Logfile: ')
        print(self.filename)
        self.playlist = pafy.get_playlist2(self.url_playlist)
        self.playlist_len = len(self.playlist)
        bar = progressbar.ProgressBar(maxval=self.playlist_len, \
                widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        file = open(self.filename,'w+')
        info = []
        cummulative_duration = nptime(0,0)
        
        # part 1: 
        # computing individual and cummulative durations
        for i in range(self.playlist_len):
            duration = datetime.strptime(self.playlist[i].duration, '%H:%M:%S').time()
            duration = timedelta(minutes=duration.minute, seconds=duration.second)
            cummulative_duration += duration
            info.append((duration,cummulative_duration,0))
            bar.update(int(i/2)+1)
            
        remaining_duration = info[self.playlist_len-1][1]

        # part 2: 
        # computing remaining durations and file writing 
        for i in range(self.playlist_len):
            temp_list = list(info[i])
            temp_list[2] = remaining_duration - info[i][0]
            remaining_duration = temp_list[2]
            info[i] = tuple(temp_list)
            write_line = ' '.join(tuple(list(map(str,(info[i])))))
            file.write(write_line+'\n')
            bar.update(int(self.playlist_len/2)+int(i/2)+1)

        file.close()
        bar.finish()

    # obsolete
    # def progress(self, current):
    #     print('Current progress: {0:.2f}% Complete'.format((current-1)/self.playlist_len*100))

    # obsolete
    # def left(self, current):
    #     if os.path.exists(self.filename):
    #         with open(self.filename,'r') as file:
    #             cummulative_duration = nptime(0,0)
    #             for i, line in enumerate(file.readlines()):
    #                 if i > current:
    #                     duration = datetime.strptime(line.strip('\n'), '%H:%M:%S').time()
    #                     duration = timedelta(minutes=duration.minute, seconds=duration.second)
    #         print('Remaining Time: {}'.format(cummulative_duration))