#!/usr/bin/env python3

from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt
import copy
import sys
from download_and_prepare_sequences import list_of_proteins
import pandas as pd


parameters = sys.argv[1:]

organism = parameters[0] + ' ' + parameters[1]
proteins = parameters[2:]

for i, protein in enumerate(proteins):
	protein = protein.replace(',','')
	proteins[i] = protein

seq_protein = list_of_proteins(proteins,organism)

# Raw dict that will be updated with an input data.
# It prevents from making dictionaries of aa_content with different lengths.
# Thus such data structure will make it easy to create visualization.
raw_aa_dict = {'A': 0,'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J':0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                         'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0,'X':0, 'Y': 0,'Z': 0}

aa_quantity_list, count_aa_list, aa_content_molecular_weight_list, aa_gravy_values, aa_gravy_list, aa_aromatic_list, aa_isoelectric_list, aa_instability_list, \
flexibility_list, aa_instability_values, secondary_structure_fraction_list, percent_structure_list, epsilon_prot_list = [], [], [], [], [], [], [], [], [], [], [], [], []

for seq in seq_protein:
	aa_quantity = len(seq)
	aa_quantity_list.append(aa_quantity)
	analysed_seq = ProteinAnalysis(seq)
	count_aa = analysed_seq.count_amino_acids()
	raw_temp_aa_dict = copy.deepcopy(raw_aa_dict)
	raw_temp_aa_dict.update((k,count_aa[k]) for k in raw_aa_dict.keys() & count_aa.keys())
	count_aa_list.append(raw_temp_aa_dict)
	aa_content_molecular_weight = round(analysed_seq.molecular_weight(), 3)
	aa_content_molecular_weight_list.append(aa_content_molecular_weight)
	aa_gravy = round(analysed_seq.gravy(), 3)
	if aa_gravy < 0:
		aa_gravy_list.append("hydrophilic")
	else:
		aa_gravy_list.append("hydrophobic")
	aa_gravy_values.append(aa_gravy)
	aa_aromatic = round((analysed_seq.aromaticity()*100), 2)
	aa_aromatic_list.append(aa_aromatic)
	aa_isoelectric = round(analysed_seq.isoelectric_point(), 3)
	aa_isoelectric_list.append(aa_isoelectric)
	aa_instability = round(analysed_seq.instability_index(), 2)
	if aa_instability == 40:
		aa_instability_list.append("has a short half life")
	if aa_instability > 40:
		aa_instability_list.append("unstable")
	else:
		aa_instability_list.append("stable")
	aa_instability_values.append(aa_instability)
	epsilon_prot = analysed_seq.molar_extinction_coefficient()
	epsilon_prot_list.append(epsilon_prot)
	flexibility = analysed_seq.flexibility()
	flexibility_list.insert(-1, flexibility)
	secondary_structure_fraction = analysed_seq.secondary_structure_fraction()
	secondary_structure_fraction_list.append(list(secondary_structure_fraction))
	
for protein in secondary_structure_fraction_list:
	percent_structure = [round(structure*100, 2) for structure in protein]
	percent_structure_list.append(percent_structure)


def to_dataframe(proteins_id,char,char_list):
	"""
	transforms dictionary ,that contains proteins'
	features and respectively protein id,
	into dataframe. Both functiona parameteres
	are lists.
	"""
	dictionary = {'ID':proteins_id,char: char_list}

	# transforming values to a vector
	# so it could be used for visualization
	data_frame = pd.DataFrame.from_dict(dictionary)
	return data_frame

print("koniec")