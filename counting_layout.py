from dash import html
from dash import dcc
from utils import get_image, get_num1, get_num2


def counting_page(fruit_selector):
    return html.Div([
        html.Div([
            dcc.Input(id="user_answer", type="number", placeholder="Enter your answer here",
                      style={"fontSize": "20px"})
        ]),
        html.P(id='fruit_selector'),
        html.Div([
            html.Img(src=get_image(fruit_selector), height=50) for _ in range(get_num1())
        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px', 'align': 'center'}),

        html.Div([
            html.Button("Check", id="check_id", style={"fontSize": "24px"}),
            html.Label(id="math-operations_id"),
            html.Div(id="result")
        ]),

        # Add this line
        dcc.Input(id="page_type", type="text", value="counting", style={"display": "none"}),

    ], style={'margin': '0 auto', 'width': '70%'})
