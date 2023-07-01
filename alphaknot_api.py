from spyprot.ilbsm_database_downloader import ILBSMDatabaseDownloader, AlphaKnotDatabaseDownloader
import pandas as pd

SEARCH_STRING = 'https://alphaknot.cent.uw.edu.pl/browse/?field=Organism&val=HUMAN&conj=NOT&field=Knot_type&val=Unknown&conj=AND&field=pLDDT_knotcore&val=%3E90&raw=1&result_cols=Knot_type%3BCategory%3BUniprot%3BOrganism%3BpLDDT_knotcore%3BProtein_name%3B'
#SEARCH_STRING = 'https://alphaknot.cent.uw.edu.pl/browse/?field=organism&val=HUMAN&conj=NOT&field=Knot_type&val=Unknown&conj=AND&field=Protein_name&val=Mucin%25&array=0&raw=1'

# Original CIF/PDB file
URL_KNOT_MODEL = 'https://alphaknot.cent.uw.edu.pl/model_file/{3}/{0}-F{1}-v{2}.cif'
# AlphaFold v1 - Knot Map, detailed data etc.
URL_KNOT_MATRIX_SVG = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{3}/{0}/{1}/{0}-F{1}_48.svg'
URL_KNOT_MATRIX_ARROWS_SVG = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{3}/{0}/{1}/{0}-F{1}_48_AR.svg'
URL_RAW_DATA = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{3}/{0}/{1}/{0}-F{1}.txt'
#URL_RAW_DATA = 'https://alphaknot.cent.uw.edu.pl/static/files/1/{0}/{1}/{2}/{1}-F{2}.txt'

dd = AlphaKnotDatabaseDownloader(SEARCH_STRING, [ #URL_KNOT_MODEL,
                                             URL_KNOT_MATRIX_SVG,
                                             URL_KNOT_MATRIX_ARROWS_SVG], 'out_dir', create_separate_dirs=False)
dd.get_all()



# Get list of all models in the database
data = pd.read_csv('https://alphaknot.cent.uw.edu.pl/_all.txt.gz', delimiter=' ')
print(data)

