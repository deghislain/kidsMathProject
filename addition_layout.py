from dash import html
from dash import dcc
from utils import BANANA_IMAGE, get_num1, get_num2


def math_addition_table():
    return html.Table([
        html.Tr([
            html.Td(html.P(id="num1-display", children=get_num1(),
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                  'fontSize': '24px'})),
            html.Button('✚', id='add_id', style={'margin': '0px 50px', 'marginTop': '20px'}),
            html.Td(html.P(id="NUM2-display", children=get_num2(),
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                  'fontSize': '24px'})),
            html.Button('⁼', id='equals_id', style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '24px'}),
            html.Td(dcc.Input(id="user_answer", type="number", placeholder="Enter your answer here",
                              style={"fontSize": "20px"}))
        ]),
        html.Div(style={'height': '50px'}),
        html.Tr([
            html.Td(html.Div([html.Img(src=BANANA_IMAGE, height=50) for _ in range(get_num1())],
                             style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                    'align': 'center'})),
            html.Td(),
            html.Td(html.Div([html.Img(src=BANANA_IMAGE, height=50) for _ in range(get_num2())],
                             style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                    'align': 'center'})),

            html.Td(id="math-operations_id"),
            html.Td(id="resp_banana")
        ]),
        html.Div(style={'height': '50px'}),

        html.Tr([
            html.Td(dcc.Input(id="sub_number", type="number", value="0", style={"display": "none"})),
            html.Td(id="remove_id"),
            html.Td(html.Button("Check", id="check_id", style={"fontSize": "24px"})),
            html.Td( dcc.Input(id="page_type", type="text", value="addition", style={"display": "none"})),
            html.Td(html.Div(id="result"))
        ])
    ], style={'margin': '0 auto', 'width': '70%'})
