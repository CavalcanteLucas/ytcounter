from counter import *

# dummy playlist
# url_playlist = 'https://www.youtube.com/playlist?list=PLOeTgPBs_o-GCUZceNPyaKoh7isj2MaFa'


url_playlist = 'https://www.youtube.com/playlist?list=PLAwxTw4SYaPnFKojVQrmyOGFCqHTxfdv2'
#url_playlist = input('Please provide valid youtube playlist: ')

ytc = YTCounter(url_playlist)

# current = int(sys.argv[1])
# current = int(input('Please provide current progress: '))

# ytc.progress(current)
# ytc.left(current)
