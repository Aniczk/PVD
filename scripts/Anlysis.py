#!/usr/bin/env python3

from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt
import copy
import sys
from download_and_prepare_sequences import list_of_proteins

organism = sys.argv[1] + ' ' + sys.argv[2]
proteins = list(sys.argv[3:])

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



print("Number of amino acids of each protein")
print(aa_quantity_list)
print("\nCounts the number times an amino acid is repeated in the protein sequence and return list of dicts.")
print(count_aa_list)
print("\nMolecular weight of a protein in Dalton unit")
print(aa_content_molecular_weight_list)
"""
Grand average of hydropathicity index (GRAVY) is used to represent the hydrophobicity value of a peptide,
which calculates the sum of the hydropathy values of all the amino acids divided by the sequence length.
Positive GRAVY values indicate hydrophobic, negative values mean hydrophilic.
"""
print("\nPositive GRAVY values indicate hydrophobic, negative values mean hydrophilic.")
print(aa_gravy_values)
print(aa_gravy_list)
print("\nThe presence of aromatic amino acids in seq [%]. Based on frequency of Phe+Trp+Tyr."
	  "\nCalculates the aromaticity value of a protein according to Lobry & Gautier (1994, Nucleic Acids Res., 22, 3174-3180).")
print(aa_aromatic_list)
print("\nIsoelectric point it is the pH at which a protein contains on average the same number of positive and negative charges"
	  "\nso that the total charge of the entire population is zero so it is electrically neutral."
	  "\nAlgorithm according to a note by David L. Tabb, 6/28/03")
print(aa_isoelectric_list)

print("\nThis method tests a protein for stability. Any value above 40 means the protein is unstable (=has a short half life)"
	  "\nImplementation of the method of Guruprasad et al. (1990, Protein Engineering, 4, 155-161).")
print(aa_instability_values)
print(aa_instability_list)
print("\nMethod returns a list of the fraction of amino acids which tend to be in helix, turn or sheet:"
	  "\nhelix: V (Valine), I (Isoleucine), Y (Tyrosine), F (Phenylalanine), W (Tryptophan), L (Leucine),"
	  "\nturn: N (Asparagine), P (Proline), G (Glycine), S (Serine),"
	  "\nsheet: E (Glutamic acid), M (Methionine), A (Alanine), L (Leucine)."
	  "\nFor each protein every element represent percent [%] respectively helix, turn and sheet occurrence")
print(percent_structure_list)
print("\nCalculate the molar extinction coefficient."
	  "\nCalculates the molar extinction coefficient assuming cysteines (reduced) and cystines residues (Cys-Cys-bond)"
	  "\n[reduced - with reduced cysteines, oxidized - with disulfid bridges]")
print(epsilon_prot_list)

print("\nImplementation of the flexibility method of Vihinen et al. (1994, Proteins, 19, 141-149)."
	  "\nTo view the change along a protein sequence can be plotted, with flexibility as scale")
print(flexibility_list)



# # # example
# plt.plot(flexibility_list[0])
# plt.show()
