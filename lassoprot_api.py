from database_downloader import DatabaseDownloader

SEARCH_STRING = 'https://lassoprot.cent.uw.edu.pl/browse/?lassoType=L3&set=0&bridgeType=ssbridge%2Camide%2Cester%2Cthioester%2Cothers&array=0&raw=1'


'https://lassoprot.cent.uw.edu.pl/static/lasso_data/6S24/A/surface_6S24_A_399_480.tcl'


dd = DatabaseDownloader(SEARCH_STRING, [URL_KNOT_MATRIX,
                                        URL_KNOT_MATRIX_SVG,
                                        URL_KNOT_MATRIX_ARROWS_SVG,
                                        URL_KNOTMAP,
                                        URL_TRIMMED_PDB,
                                        URL_CHAIN_XYZ], 'out_dir', create_separate_dirs=False)