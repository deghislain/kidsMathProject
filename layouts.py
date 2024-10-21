from dash import html
from dash import dcc
from utils import BANANA_IMAGE, get_num1, get_num2


def math_addition_table():
    print("math_addition_table")
    print("NUM1", get_num1())
    print("NUM2", get_num2())
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

            html.Td(),
            html.Td(id="resp_banana")
        ]),
        html.Div(style={'height': '50px'}),

        html.Tr([
            html.Td(),
            html.Td(),
            html.Td(html.Button("Check", id="check_id", style={"fontSize": "24px"})),
            html.Td(),
            html.Td(html.Div(id="result"))
        ])
    ], style={'margin': '0 auto', 'width': '70%'})


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
