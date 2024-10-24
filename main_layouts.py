from dash import html, dcc
from addition_layout import math_addition_table
from subtraction_layout import math_subtraction_table
from counting_layout import counting_page


def main_layout(operation=4, is_start=True):
    """Generate the main layout based on the operation."""

    # Define instruction and content for each operation
    operations = {
        0: {"instruction": "How many Bananas do you see?", "content": counting_page()},
        1: {"instruction": "Click on equals to get help", "content": math_addition_table()},
        2: {"instruction": "", "content": math_subtraction_table()},
    }

    # Default to operation selection if operation is not specified
    if operation == 4:
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
        instruction = ""
    else:
        content = operations.get(operation, {"content": html.Div("Invalid operation")})["content"]
        instruction = operations.get(operation, {"instruction": ""})["instruction"]

    # Dynamically display Start/Next buttons
    button_style = {"fontSize": "24px"}
    start_style = {**button_style, "display": "inline" if is_start else "none"}
    next_style = {**button_style, "display": "none" if is_start else "inline"}

    return html.Div([
        html.Div([
            html.Button("Start", id="start_id", n_clicks=0, style=start_style),
            html.Button("Next", id="next_id", n_clicks=0, style=next_style),
            html.Span(style={'marginRight': '350px'}),
        ], style={'textAlign': 'right'}),
        html.Div([
            html.H1("Math Web Application"),
            html.H3(instruction, style={'color': 'blue'})
        ], style={'display': 'block', 'textAlign': 'center'}),
        content,
    ], style={'textAlign': 'center', 'width': '100%', 'background': '#87CEEB'}, id="main_layout")