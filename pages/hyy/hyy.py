from dash import html
from dash import dcc
from pages.hyy.hyy_data import hyy_dataframe
import dash_bootstrap_components as dbc

image_path = 'assets/Hyy_feynman.png'

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Sample"),
                dcc.Dropdown(
                    id="sample-variable",
                    options=[
                        {"label": "Sample "+str(col), "value": str(col)} for col in hyy_dataframe()['sample'].unique()
                    ],
                    value="A",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Energy"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                        {"label": col, "value": col} for col in hyy_dataframe().columns
                    ],
                    value="sepal width (cm)",
                ),
            ]
        ),
    ],
    body=True,
)

layout = dbc.Container(
    [
        html.H1("HYY Analysis"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Col(
                        [
                            html.Div(
                                html.Img(
                                    src=image_path, 
                                    style={
                                        'height':'100%', 
                                        'width':'100%'}
                                    )
                                ),
                            html.Hr(),
                            html.Div(controls)
                        ], align='center'), 
                    md=3),
                dbc.Col(
                    html.Iframe(
                                id="hyy-graph", 
                                srcDoc=None,
                                style={
                                    'border-width': '5', 
                                    'width': '100%',
                                    'height': '500px'}
                            ), md=9),
            ],
            align="center",
        ),
        html.Hr(),
        dbc.Row(
            dbc.Col(
                align="center",
                id="col-hyy")
        )
    ],
    fluid=True,
)