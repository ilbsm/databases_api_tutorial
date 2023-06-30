from spyprot.ilbsm_database_downloader import ILBSMDatabaseDownloader
import pandas as pd

SEARCH_STRING = 'https://alphaknot.cent.uw.edu.pl/browse/?field=Organism&val=HUMAN&conj=NOT&field=Knot+Type&val=Unknown&conj=AND&field=Title&val=Mucin%25&array=0&raw=1'
#SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=False&bridgeType=probab&slipknotTypes=%2B31&array=0&raw=1'

# AlphaFold v1 - Knot Map, detailed data etc.
URL_KNOT_MODEL = 'https://alphaknot.cent.uw.edu.pl/model_file/{0}/{1}-F{2}-v1.cif'
URL_KNOT_MATRIX_SVG = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{0}/{1}/{2}/{1}-F{2}_48.svg'
URL_KNOT_MATRIX_ARROWS_SVG = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{0}/{1}/{2}/{1}-F{2}_48_AR.svg'
URL_RAW_DATA = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{0}/{1}/{2}/{1}-F{2}.txt'

dd = ILBSMDatabaseDownloader(SEARCH_STRING, [URL_KNOT_MODEL,
                                             URL_KNOT_MATRIX_SVG,
                                             URL_KNOT_MATRIX_ARROWS_SVG], 'out_dir', create_separate_dirs=False)
#dd.get_all()


def get_chain_details(uniid, model, version):
    url = 'https://alphaknot.cent.uw.edu.pl/view/{0}/{1}/{2}'.format(uniid, model, version)
    data = pd.read_html(url, flavor='bs4', header=0, encoding='UTF8')
    return data[6]

get_chain_details('Q8WXI7', '60', '1')

# Get list of all models in the database
data = pd.read_csv('https://alphaknot.cent.uw.edu.pl/_all.txt.gz', delimiter=' ')
print(data)

