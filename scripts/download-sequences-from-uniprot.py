import biotite.database.entrez as entrez
import biotite.sequence as seq
import biotite.sequence.io.fasta as fasta
# Find UIDs for SwissProt/UniProt entries

protein_list = ['TPH1','COMT','SLC18A2','HTR1B','HTR2C','HTR2A','MAOA',
            'TPH2','HTR1A','HTR7','SLC6A4','GABBR2','POMC','GNAI3',
            'NPY','ADCY1','PDYN','GRM2','GRM3','GABBR1']
for g in protein_list:
	query =   entrez.SimpleQuery(g, "Gene Name") & entrez.SimpleQuery("Homo sapiens", "Organism") & entrez.SimpleQuery("srcdb_swiss-prot", "Properties")
	print("QUERY")
	print(query)
	print('-------------------')
	uids = entrez.search(query, db_name="protein")
	print(uids)

	# Download FASTA file containing the sequence(s)
	# from NCBI Entrez database
	file_name = entrez.fetch_single_file(uids, g + ".fasta", db_name="protein", ret_type="fasta")
	# Read file
	fasta_file = fasta.FastaFile()
	fasta_file.read(file_name)
	print(fasta_file)

	# Convert first sequence in file to 'ProteinSequence' object
	seq = fasta.get_sequence(fasta_file)
	print(seq)