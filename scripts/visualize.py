#!/usr/bin/env python3

import pandas as pd
import numpy as np
import seaborn as sns
from typing import List, Dict, Tuple, Union, Optional
from Anlysis import *

'''
TODO:
- Create class that visualize protein important features:
    1. AA content in dataframe. (Amino acid left, percentage for each of two) Done
    2. Molecular weight and GRAVY as string. Done
    3. Isoelectric [pH x axis and y isoelectric point] and aromaticity and percent secondary  as bar plot.
    4. Flexibility as plot (already is). Done
    5. Stability bar plot (dynamic coloring)
    6. Epsilon String with explanation.
 '''


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

        :return:
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
        # plt.savefig('flexibility.png')

    def second_structure(self):
        """

        :return:
        """
    fig_s, (axs1,axs2) = plt.subplots(1,2, figsize=(9,15))




myClass = Visualizer()
print(myClass.aa_content_dataframe())