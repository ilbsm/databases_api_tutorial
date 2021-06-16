from ilbsm_database_downloader import ILBSMDatabaseDownloader
import pandas as pd

SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=True&bridgeType=probab&knotTypes=-31&array=0&raw=1'
#SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=False&bridgeType=probab&slipknotTypes=%2B31&array=0&raw=1'

# Knots
URL_KNOT_MATRIX = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.png'
URL_KNOT_MATRIX_SVG = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}_vec.svg'
URL_KNOT_MATRIX_ARROWS_SVG = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.svg'
URL_KNOTMAP = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/knotmap_{0}_{1}.txt'
URL_TRIMMED_PDB = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.pdb.gz'
URL_CHAIN_XYZ = 'https://knotprot.cent.uw.edu.pl/chains/{0}/{1}/chain.xyz.txt'
# Knotoids
URL_KNOTOID_WHOLE_MAP = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}_projection_map.png'
URL_KNOTOID_WHOLE_RAW = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}_diagrams.txt'
URL_KNOTOID_SUB_MATRIX = 'https://knotprot.cent.uw.edu.pl/static/knot_data//{0}/{1}/{0}_{1}_projection_map.png'
URL_KNOTOID_SUB_RAW = 'https://knotprot.cent.uw.edu.pl/static/knot_data//{0}/{1}/{0}_{1}_data.txt'
URL_KNOTOID_SUB_CIRCULAR = 'https://knotprot.cent.uw.edu.pl/static/knot_data//{0}/{1}/{0}_{1}_disk_matrix.png'
URL_KNOTOID_SUB_FINGERPRINT_MATRIX = 'https://knotprot.cent.uw.edu.pl/static/knot_data//{0}/{1}/{0}_{1}_fingerprint_matrix.png'
URL_KNOTOID_SUB_KNOTTED_CORE = 'https://knotprot.cent.uw.edu.pl/static/knot_data//{0}/{1}/{0}_{1}_knotted-core.txt'
URL_KNOTOID_SUB_SEARCH_RAW = 'https://knotprot.cent.uw.edu.pl/static/knot_data//{0}/{1}/search100.txt'

dd = ILBSMDatabaseDownloader(SEARCH_STRING, [URL_KNOT_MATRIX,
                                             URL_KNOT_MATRIX_SVG,
                                             URL_KNOT_MATRIX_ARROWS_SVG,
                                             URL_KNOTMAP,
                                             URL_TRIMMED_PDB,
                                             URL_CHAIN_XYZ], 'out_dir', create_separate_dirs=False)
#dd.get_all()

dd = ILBSMDatabaseDownloader(SEARCH_STRING, [URL_KNOTOID_WHOLE_MAP,
                                             URL_KNOTOID_WHOLE_RAW,
                                             URL_KNOTOID_SUB_MATRIX,
                                             URL_KNOTOID_SUB_RAW,
                                             URL_KNOTOID_SUB_CIRCULAR,
                                             URL_KNOTOID_SUB_FINGERPRINT_MATRIX,
                                             URL_KNOTOID_SUB_KNOTTED_CORE,
                                             URL_KNOTOID_SUB_SEARCH_RAW], 'out_dir_knotoids', create_separate_dirs=False)
#dd.get_all()


def get_chain_details(pdb, chain):
    url = 'https://knotprot.cent.uw.edu.pl/view/{0}/{1}/'.format(pdb, chain)
    data = pd.read_html(url, flavor='bs4', header=0, encoding='UTF8')
    return data[6]

get_chain_details('6ymb', 'A')

# Get list of knot types for every chain
data = pd.read_csv('https://knotprot.cent.uw.edu.pl/knotted_types.txt', delimiter=' ')
print(data)

# Get list of cysteine knots:
data = pd.read_csv('https://knotprot.cent.uw.edu.pl/cysteine.txt', delimiter=';')
print(data)

# Get list of redundant chains with main knot type, chain length and tails
data = pd.read_csv('https://knotprot.cent.uw.edu.pl/_red_chains_knotted_N_C', delimiter=';')
print(data)

