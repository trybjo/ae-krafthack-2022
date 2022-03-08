import plotly.express as px
import pandas as pd

tensile_values = ['Bolt_1_Tensile', 'Bolt_2_Tensile', 'Bolt_3_Tensile', 'Bolt_4_Tensile',
       'Bolt_5_Tensile', 'Bolt_6_Tensile']

torsion_values = [
    'Bolt_1_Torsion',
    'Bolt_2_Torsion',
    'Bolt_3_Torsion',
    'Bolt_4_Torsion',
    'Bolt_5_Torsion',
    'Bolt_6_Torsion'
]

def plot_tensile_values(df,n_samples):

    for col in tensile_values:
        fig = px.line(df.loc[:,[col,'operation_mode']].sample(n_samples).sort_index(),color='operation_mode')
        fig.show()


def plot_torsion_values(df,n_samples):

    for col in torsion_values:
        fig = px.line(df.loc[:,[col]].sample(n_samples).sort_index())
        fig.show()





