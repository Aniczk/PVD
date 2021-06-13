import biotite.database.entrez as entrez
import biotite.sequence.io.fasta as fasta
import os
import shutil

# Find UIDs for SwissProt/UniProt entries

protein_list = ['TPH1', 'COMT', 'SLC18A2', 'HTR1B', 'HTR2C', 'HTR2A', 'MAOA',
                'TPH2', 'HTR1A', 'HTR7', 'SLC6A4', 'GABBR2', 'POMC', 'GNAI3',
                'NPY', 'ADCY1', 'PDYN', 'GRM2', 'GRM3', 'GABBR1']


def download_files(protein_list):
    for g in protein_list:
        query = entrez.SimpleQuery(g, "Gene Name") & entrez.SimpleQuery("Homo sapiens", "Organism") & entrez.SimpleQuery(
            "srcdb_swiss-prot", "Properties")
        # print("QUERY")
        # print(query)
        # print('-------------------')
        uids = entrez.search(query, db_name="protein")
        # print(uids)
        # Download FASTA file containing the sequence(s)
        # from NCBI Entrez database
        entrez.fetch_single_file(uids, g + ".fasta", db_name="protein", ret_type="fasta")


def convert_files_to_list(files):
    seqs = []
    for f in files:
        # Read file
        ff = fasta.FastaFile()
        ff.read(f)
        # Convert first sequence in file to 'ProteinSequence' object
        seqs.append(str(fasta.get_sequence(ff)))
    return seqs


def create_files_list(protein_list):
    return [f + '.fasta' for f in protein_list]


def prepare():
    # Prepare temporary folder to store files
    # If directory exists delete existing one
    temp_dir = os.getcwd() + '/temp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.mkdir('temp')
    os.chdir(temp_dir)


def clean_up():
    # Go back to parent directory and remove temp
    os.chdir(os.getcwd()[:-5])
    shutil.rmtree(os.getcwd() + '/temp')


prepare()
download_files(protein_list)
print(convert_files_to_list(create_files_list(protein_list)))
clean_up()
