from dash.dependencies import Input, Output
import plotly.express as px
from app import app
from utils.hyy_functions import *
from pages.hyy.hyy_data import hyy_dataframe


@app.callback(
    Output('hyy-graph', 'srcDoc'),
    Input('sample-variable', 'value'))
def update_figure(selected_value):
    hyy_df = hyy_dataframe()
    filtered_df = hyy_df[hyy_df['sample'] == selected_value]
    lumi = float(filtered_df['lumi'].unique()[0])
    html_fig = plot_data(data=filtered_df, lumi=lumi)
    return html_fig