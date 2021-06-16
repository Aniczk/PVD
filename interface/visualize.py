#!/usr/bin/env python3

import seaborn as sns
from typing import List, Dict, Tuple, Union, Optional
import matplotlib.patches as mpatches
from Anlysis import *
import pandas as pd


class Visualizer():
    """
    Accepts data structures such as lists and plots it.
    Plots can take different forms, for example bar plots.
    Also some of the created attributes of the class will
    be present as just regular string description. Provided
    data structures are representation of proteins' sequences
    and in such structure proteins' features are implemented.
    Those features can be mentioned:

    1. Amino acid content (in percentage).
    2. Molecular weight.
    3. Hydropathicity index (GRAVY).
    4. Aromaticity value (based on frequency of Phe+Trp+Tyr aa in protein)
    5. Isoelectric point.
    6. Stability of the protein.
    7. Secondary structure fraction.
    8. Molar extinction coefficient.
    9. Flexibility of the protein.

    """

    def __init__(self, aa_content: List[Dict], mol_weight: List[int], gravy: List[int], arm_value: List[int],
                 iso_point: List[int], stability: List[int], sec_structure: List[list], epsilon: List[int],
                 flex: List[list], protein_id:List[str]):
        """
        Process input to structure that will be used to create string
        description or specific plot.

        :param aa_content:
        :param mol_weight:
        :param gravy:
        :param arm_value:
        :param iso_point:
        :param stability:
        :param sec_structure:
        :param epsilon:
        :param flex:

        :return: Various plots describing proteins features.
        """
        self.aa_content = aa_content
        self.mol_weight = mol_weight
        self.gravy = gravy
        self.arm_value = arm_value
        self.iso_point = iso_point
        self.stability = stability
        self.sec_structure = sec_structure
        self.epsilon = epsilon
        self.flex = flex
        self.protein_id = protein_id

    def aa_content_dataframe(self):
        """

        :return:
        """
        aa_final_dict = {}
        for aa_dict in count_aa_list:
            for key, value in aa_dict.items():
                if key not in aa_final_dict:
                    aa_final_dict[key] = [value]
                else:
                    aa_final_dict[key].append(value)

        df = pd.DataFrame.from_dict(aa_final_dict)
        df = df.transpose()
        df.columns = proteins
        df.to_html('aa_dataframe.html')


    def plot_flexibility(self):
        """
        :return:
        """

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
        fig.suptitle("Flexibility of each protein", fontweight='bold')
        ax1.plot(flexibility_list[0], color='r')
        ax2.plot(flexibility_list[1], color='c')
        ax1.set_xlabel(proteins[0], fontweight='bold')
        ax2.set_xlabel(proteins[1], fontweight='bold')
        plt.savefig('flexibility.png')


    def instability(self):
        """
        :return: Dynamic barplot for instability. Depends
        on the instability value the bar will change its color.
        """
        colors = [] # for dynamic bars coloring
        fig_in, axi = plt.subplots(1, 1, figsize=(10, 5))
        fig_in.suptitle('Instability of protein', fontsize=14.0, fontweight='bold')
        for value in aa_instability_values:
            if value > 40:
                colors.append('orangered')
            elif value <= 40:
                colors.append('forestgreen')

        axi.bar(proteins, aa_instability_values, color=colors, width=0.5)
        stable = mpatches.Patch(color='forestgreen', label='stable')
        unstable = mpatches.Patch(color='orangered', label='unstable')
        axi.legend(loc='center', handles=[stable, unstable])

        plt.savefig('instability.png')


    def second_structure(self):
        """
        :return: Barplot describing fraction of amino acids
        which tend to be in helix, turn or sheet
        """
        formations = ['Helix','Turn','Sheet'] # categorical data plot on xaxs
        colors = ['yellowgreen','olivedrab','darkolivegreen'] # setting bar colors
        fig_s, (axs1, axs2) = plt.subplots(1, 2, figsize=(10, 5))
        fig_s.suptitle('Secondary structure fraction',fontsize=14.0)
        axs1.bar(formations,secondary_structure_fraction_list[0],color=colors, edgecolor='black')
        axs1.set_title(proteins[0], fontweight='bold')
        axs2.bar(formations, secondary_structure_fraction_list[1], color=colors, edgecolor='black')
        axs2.set_title(proteins[1], fontweight='bold')
        axs1.set_ylabel('Percentage')

        plt.savefig('ss_fraction.png')

    def iso_and_arom_plot(self):
        """
        :return:
        """
        iso_elec_df = to_dataframe(proteins,'Isoelectric',aa_isoelectric_list)
        aromaticity_df = to_dataframe(proteins,'Aromaticity',aa_aromatic_list)
        fig, (barplot1, barplot2) = plt.subplots(1, 2, figsize=(10, 5))
        sns.barplot(data=iso_elec_df, x='ID', y='Isoelectric', ax=barplot1)
        sns.barplot(data=aromaticity_df, x='ID', y='Aromaticity', ax=barplot2)

        plt.savefig('iso_and_arom.png')


    def epsilon_value(self):
        """
        :return: Plotting molar extinction coefficient
        """
        categories = ['Reduced cysteines', 'Disulfid bridges']
        fig, (bplot1, bplot2) = plt.subplots(1, 2, figsize=(10, 5))
        fig.suptitle('Molar extinction coefficient', fontsize=14.0)
        bplot1.bar(categories, epsilon_prot_list[0], color=['r', 'y'], edgecolor='black')
        bplot1.set_title(proteins[0], fontweight='bold')
        bplot2.bar(categories, epsilon_prot_list[1], color=['r', 'y'], edgecolor='black')
        bplot2.set_title(proteins[1], fontweight='bold')

        plt.savefig('epsilon.png')



# generating png files and dataframe in html
vis = Visualizer(count_aa_list,aa_content_molecular_weight,aa_gravy_list,
           aa_aromatic_list,aa_isoelectric_list, aa_instability_values,
           percent_structure_list,epsilon_prot_list,flexibility_list,proteins)
mol_weight = vis.mol_weight
gravy = vis.gravy
vis.aa_content_dataframe()
vis.plot_flexibility()
vis.second_structure()
vis.iso_and_arom_plot()
vis.epsilon_value()
vis.instability()
