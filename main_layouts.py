from dash import html, dcc
from addition_layout import math_addition_table
from subtraction_layout import math_subtraction_table
from counting_layout import counting_page
from division_layout import math_division_table
from multiplication_layout import math_multiplication_table


def main_layout(operation=5, is_start=True, err_msg=None, image_name='Banana'):
    """Generate the main layout based on the operation."""

    # Define instruction and content for each operation
    operations = {
        0: {"instruction": "How many Bananas do you see?", "content": counting_page(image_name)},
        1: {"instruction": "Click on equals to get help", "content": math_addition_table(image_name)},
        2: {"instruction": "", "content": math_subtraction_table(image_name)},
        3: {"instruction": "Click on equals to get help", "content": math_division_table(image_name)},
        4: {"instruction": "Click on equals to get help", "content": math_multiplication_table(image_name)},
    }

    # Default to operation selection if operation is not specified
    if operation == 5:
        content = html.Div([
            html.Div([
                html.Label('Select your favorite fruit:', style={'color': 'blue', 'fontSize': '24px'}),
                dcc.RadioItems(
                    id='fruit_selector',
                    options=[
                        {'label': 'Banana', 'value': 'Banana'},
                        {'label': 'Apple', 'value': 'Apple'},
                        {'label': 'Grape', 'value': 'Grape'}
                    ],
                    value='Banana'  # default selected value
                )
            ], style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '49%'}),

            html.Div([
                html.Label('Chose operations:', style={'color': 'blue', 'fontSize': '24px'}),
                dcc.Checklist(
                    id="math-operations_id",
                    options=[
                        {"label": "Counting", "value": "counting"},
                        {"label": "Addition", "value": "addition"},
                        {"label": "Subtraction", "value": "subtraction"},
                        {"label": "Division", "value": "division"},
                        {"label": "Multiplication", "value": "multiplication"},
                    ],
                    value=[],
                    labelStyle={'display': 'block'}
                )
            ], style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '49%'}),

            html.Div(id='selected-fruit')
        ], style={'textAlign': 'center', 'width': '100%', 'height': '100%', 'background': '#87CEEB'})

        instruction = ""
        if err_msg:
            instruction = err_msg

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
            html.Span(style={'marginRight': '350px'}, id="err_msg"),
        ], style={'textAlign': 'right'}),
        html.Div([
            html.H1("Math Web Application"),
            html.H3(instruction, style={'color': 'blue'})
        ], style={'display': 'block', 'textAlign': 'center'}),
        content,
    ], style={
        'textAlign': 'center',
        'width': '100vw',
        'height': '100vh',
        'background': '#87CEEB',
        'margin': '0',
        'padding': '0',
        'overflow': 'hidden'
    }, id="main_layout")
