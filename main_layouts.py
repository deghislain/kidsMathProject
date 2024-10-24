from dash import html
from dash import dcc
from addition_layout import math_addition_table
from subtraction_layout import math_subtraction_table
from counting_layout import counting_page


def main_layout(operation=4, is_start=True):
    content = None
    instruction = ""
    if operation == 0:
        instruction = "How many Bananas do you see?"
        content = counting_page()
    elif operation == 1:
        instruction = "Click on equals to get help"
        content = math_addition_table()
    elif operation == 2:
        content = math_subtraction_table()
    else:
        content = html.Div([
            dcc.Checklist(
                id="math-operations_id",
                options=[
                    {"label": "Counting", "value": "counting"},
                    {"label": "Addition", "value": "addition"},
                    {"label": "Subtraction", "value": "subtraction"},
                ],
                value=[],
                labelStyle={'display': 'block'}
            ),
        ], style={'display': 'block', 'textAlign': 'center'})

    return html.Div([
        html.Div([
            html.Button("Start", id="start_id", n_clicks=0,
                        style={"fontSize": "24px", "display": "inline" if is_start else "none"}),
            html.Button("Next", id="next_id", n_clicks=0,
                        style={"fontSize": "24px", "display": "none" if is_start else "inline"}),
            html.Span(style={'marginRight': '350px'}),
        ], style={'textAlign': 'right'}),
        html.Div([
            html.H1("Math Web Application"),
            html.H3(instruction, style={'color': 'blue'})
        ], style={'display': 'block', 'textAlign': 'center'}),
        content,

    ], style={'textAlign': 'center', 'width': '100%', 'background': ' #87CEEB'}, id="main_layout")
