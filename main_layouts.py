from dash import html
from dash import dcc
from addition_layout import math_addition_table


def main_layout():
    return html.Div([
        dcc.Interval(
            id='interval-component',
            interval=1000,  # in milliseconds (e.g., 10 seconds)
            n_intervals=0
        ),
        html.Div([
            html.Button("Next", id="next_id", n_clicks=0, style={"fontSize": "24px"}),
            html.Span(style={'marginRight': '350px'}),
        ], style={'textAlign': 'right'}),  # Add style here
        html.Div([
            html.H1("Math Web Application"),
            html.H3("Click on equals to get help", style={'color': 'blue'})
        ], style={'display': 'block', 'textAlign': 'center'}),
        math_addition_table(),

    ], style={'textAlign': 'center', 'width': '100%', 'background': ' #87CEEB'}, id="main_layout")
