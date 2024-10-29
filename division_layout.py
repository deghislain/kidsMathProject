from dash import html
from dash import dcc
from utils import get_image, get_num1, get_num2


image_names = ['icon1', 'icon2', 'icon3', 'icon4', 'icon5']  # replace with your image names


def math_division_table(image_name):
    return html.Div([
        html.Div([
            html.Table([
                html.Tr([
                    html.Td(html.P(id="num1-display", children=get_num1(),
                                   style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                          'fontSize': '24px'})),
                    html.Td(),
                    html.Td(
                        html.Button('÷', id='add_id', style={'margin': '0px 50px', 'marginTop': '20px'})),
                    html.Td(html.P(id="num2-display", children=get_num2(),
                                   style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                          'fontSize': '24px'})),
                    html.Td(
                        html.Button('⁼', id='equals_id',
                                    style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '24px'})),
                    html.Td(),
                ]),
                html.Tr([
                    html.Td(html.Div([html.Img(src=get_image(image_name), height=50) for _ in range(get_num1())],
                                     style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                            'align': 'center'})),
                    html.Td(id="math-operations_id"),
                    html.Td(),
                    html.Td(
                        html.Div(
                            [html.Img(src=get_image(image_name), height=50) for image_name in image_names[:get_num2()]],
                            style={'display': 'grid', 'gridTemplateColumns': 'repeat(5, 1fr)', 'gap': '10px',
                                   'align': 'center'}
                            )
                    ),
                    html.Td(id="resp_banana"),
                    html.Td(),
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(id='fruit_selector'),
                    html.Td(),
                    html.Td([
                        html.Button('÷', id='div_id',
                                    style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '20px'}),
                        dcc.Input(id="div_number", type="number", placeholder="Enter a number here", value=1,
                                  debounce=True,
                                  style={"fontSize": "20px", "width": "200px", "textAlign": "center"})
                    ]),
                    html.Td(),
                    html.Td(html.Div(id="result"))
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(id='fruit_selector'),
                    html.Td(dcc.Input(id="page_type", type="text", value="subtraction", style={"display": "none"})),
                    html.Td(),
                    html.Td(html.Button("Check", id="check_id", style={"fontSize": "24px"})),
                    html.Td(html.Div(id="result")),
                ])
            ], style={'width': '100%'}),
        ],
            style={'width': '60%', 'display': 'inline-block', 'vertical-align': 'top'}),
        html.Div([
            html.Table([
                html.Tr([
                    html.Td(dcc.Input(id="user_answer", type="number", placeholder="Enter your answer here",
                                      style={"fontSize": "20px"}))
                ]),
            ], style={'width': '100%'}),
        ],
            style={'width': '38%', 'display': 'inline-block', 'vertical-align': 'top'})
    ],
        style={'margin': '0 auto', 'width': '98%'})
