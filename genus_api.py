import pandas as pd

from database_downloader import DatabaseDownloader

data = pd.read_csv('https://genus.fuw.edu.pl/_all_genus', delimiter=';')
print(data)



SEARCH_STRING = 'https://genus.fuw.edu.pl/browse/?moltag=hydrolase%2Fpeptide&set=True&is_rna=&raw=1'

# Genus Proteins
URL_BONDS_PROTEIN = 'https://genus.fuw.edu.pl/file/{0}/{1}/{0}_{1}.chimera'
URL_BONDS_RNA = 'https://genus.fuw.edu.pl/file/{0}/{1}/{0}_{1}.rna'
URL_STRUCT_CSV = 'https://genus.fuw.edu.pl/file/{0}/{1}/{0}_{1}.struct_csv'
URL_RENUMBERED = 'https://genus.fuw.edu.pl/file/{0}/{1}/{0}_{1}.pdb.gz'
URL_CHAIN_XYZ = 'https://genus.fuw.edu.pl/chains/{0}/{1}/chain.xyz.txt'

dd = DatabaseDownloader(SEARCH_STRING, [URL_BONDS_PROTEIN,
                                        URL_STRUCT_CSV,
                                        URL_RENUMBERED,
                                        URL_CHAIN_XYZ], 'out_dir', create_separate_dirs=False)
dd.get_all()

