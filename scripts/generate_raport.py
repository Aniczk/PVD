#!/usr/bin/env python3

import os
from visualize import mol_weight,gravy
from Anlysis import *
import dominate
from dominate.tags import *
import glob


class Generate():
    """
    Generating HTML report that contains comparision of
    proteins that User provided via web application.

    """
    def __init__(self):
        pass

    def html_generator(self):
        """

        :return: ready html file
        """

        doc = dominate.document(title="Comparasion report")

        with doc.head:
            link(rel='stylesheet', href="https://www.w3schools.com/w3css/4/w3.css")
        with doc:
            with div(cls='w3-container'):
                h1('Basic information.')
                p(f'Molecular weight for {proteins[0]} and {proteins[1]} are respectively {str(aa_content_molecular_weight_list[0])} and {str(aa_content_molecular_weight_list[1])} (in daltons)')
                p(f'Grand average of hydropathicity index (GRAVY) represents the hydrophobicity value of a peptide. Positive GRAVY values indicate hydrophobic, negative values mean hydrophilic.')
                p(f'GRAVY value for {proteins[0]} is {aa_gravy_values[0]} and for {proteins[1]} equals {aa_gravy_values[1]}')
                h1('Amico acid content comparision (percentage).')
                a('table', href='aa_dataframe.html')
                h1('Flexibility')
                p(f'Proteins are dynamic entities, and they possess an inherent flexibility that allows them to function through molecular interactions within the cell, among cells and even between organisms')
                p(f'Here, flexibility is presented from Vihinien et.al (1994, Proteins, 19, 141-149.) method')
                img(src='flexibility.png')
                h1('Secondary structure')
                p('Represented as occurrence of three ways the protein can fold within secondary structure.')
                img(src='ss_fraction.png')
                h1('Isoelectric point and aromaticity.')
                p('Isoelectric point it is the pH at which a protein contains on average the same number of positive and negative charges.')
                p('The presence of aromatic amino acids in seq [%]. Based on frequency of Phe+Trp+Tyr.')
                img(src='iso_and_arom.png')
                h1('Molar extinction coefficient.')
                p('Calculates the molar extinction coefficient assuming cysteines (reduced) and cystines residues (Cys-Cys-bond)')
                p('The molar attenuation coefficient is a measurement of how strongly a chemical species attenuates light at a given wavelength.')
                img(src='epsilon.png')
                h1('Instability of proteins.')
                p('Measuring stability of the proteins. Any value above 40 means the protein is unstable, which means it has a short half life')
                img(src='instability.png')

        with open('report.html', 'w') as f:
            f.write(doc.render())

# Saving report
generate = Generate()
generate.html_generator()
