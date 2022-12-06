from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        html.H1("This is the Header!"),
        html.Hr(),
        html.P("This is a meaningful paragraph"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Col(
                        [
                            html.Div(
                                html.Img(
                                    src='assets/HiggsSimplified.png', 
                                    style={
                                        'height':'100%', 
                                        'width':'100%'}
                                    )
                                ),
                            html.Hr(),
                            html.Div(html.P("I'm a Paragraph in Column 1"))
                        ], align='center'), 
                    md=8),
                dbc.Col(
                    [
                        html.H3("Fun Facts"),
                        html.P("I'm a paragraph in Column 2")
                    ], md=4),
            ],
            align="center",
        ),
        html.Hr(),
        dbc.Row(
            dbc.Col(
                align="center",
                id="col-random",
                children=[
                    html.H2("Higgs Infographic")
                ])
        )
    ],
    fluid=True,
)