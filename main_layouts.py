from dash import html
from dash import dcc
from addition_layout import math_addition_table


def main_layout(operation=False, is_start = True):
    content = math_addition_table() if operation else html.Div([
        dcc.Checklist(
            id="math-operation",
            options=[
                {"label": "Addition", "value": "addition"},
                {"label": "Subtraction", "value": "subtraction"},
                {"label": "Multiplication", "value": "multiplication"},
            ],
            value=[],
            labelStyle={'display': 'block'}
        ),
    ], style={'display': 'block', 'textAlign': 'center'})

    return html.Div([
        html.Div([
            html.Button("Start", id="start_id", n_clicks=0, style={"fontSize": "24px", "display": "inline" if is_start else "none"}),
            html.Button("Next", id="next_id", n_clicks=0, style={"fontSize": "24px", "display": "none" if is_start else "inline"}),
            html.Span(style={'marginRight': '350px'}),
        ], style={'textAlign': 'right'}),
        html.Div([
            html.H1("Math Web Application"),
            html.H3("Click on equals to get help", style={'color': 'blue'})
        ], style={'display': 'block', 'textAlign': 'center'}),
        content,

    ], style={'textAlign': 'center', 'width': '100%', 'background': ' #87CEEB'}, id="main_layout")
