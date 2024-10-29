from dash import html
from dash import dcc
from utils import get_image, get_num1, get_num2


def math_subtraction_table(fruit_selector):
    num2, num1 = min(get_num1(), get_num2()), max(get_num1(), get_num2())
    return html.Table([
        html.Tr([
            html.Td(html.P(id="num1-display", children=num1,
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                  'fontSize': '24px'})),
            html.Button('━', id='add_id', style={'margin': '0px 50px', 'marginTop': '20px'}),
            html.Td(html.P(id="num2-display", children=num2,
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                  'fontSize': '24px'})),
            html.Button('⁼', id='equals_id', style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '24px'}),
            html.Td(dcc.Input(id="user_answer", type="number", placeholder="Enter your answer here",
                              style={"fontSize": "20px"}))
        ]),
        html.Div(style={'height': '50px'}),
        html.Tr([
            html.Td(html.Div([html.Img(src=get_image(fruit_selector), height=50) for _ in range(num1)],
                             style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                    'align': 'center'})),
            html.Td(id="math-operations_id"),
            html.Td(),
            html.Td([
                html.Button('━', id='remove_id', style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '20px'}),
                dcc.Input(id="sub_number", type="number", placeholder="Enter a number here", value=0,debounce=True,
                              style={"fontSize": "20px","width": "200px", "textAlign": "center"})
                     ]),
            html.Td(id="resp_banana")
        ]),
        html.Div(style={'height': '50px'}),

        html.Tr([
            html.Td( id="equals_div_layout_id"),
            html.Td( id='fruit_selector'),
            html.Td(html.Button("Check", id="check_id", style={"fontSize": "24px"})),
            html.Td(dcc.Input(id="page_type", type="text", value="subtraction", style={"display": "none"})),
            html.Td(html.Div(id="result"))
        ])
    ], style={'margin': '0 auto', 'width': '70%'})
