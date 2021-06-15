from database_downloader import DatabaseDownloader

SEARCH_STRING = 'https://lassoprot.cent.uw.edu.pl/browse/?lassoType=L3&set=0&bridgeType=ssbridge%2Camide%2Cester%2Cthioester%2Cothers&array=0&raw=1'

URL_ALL_FILES = 'https://lassoprot.cent.uw.edu.pl/files/{0}_{1}_all.tar.bz2'


dd = DatabaseDownloader(SEARCH_STRING, [URL_ALL_FILES], 'out_dir', create_separate_dirs=False)
dd.get_all()
