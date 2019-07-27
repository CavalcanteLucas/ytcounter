from counter import *

#url_playlist = 'https://www.youtube.com/playlist?list=PLAwxTw4SYaPnFKojVQrmyOGFCqHTxfdv2'
url_playlist = input('Please provide a valid youtube playlist: ')
ytc = YTCounter(url_playlist)

#current = int(sys.argv[1])
current = input('Please provide current progress: ')

ytc.progress(current)
ytc.left(current)
