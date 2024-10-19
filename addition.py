import dash_html_components as html
import dash_core_components as dcc
from utils import get_banana_image


def math_addition_table(num1, num2):
    banana_image = get_banana_image()
    return html.Table([
        html.Tr([
            html.Td(html.P(id="num1-display", children=num1,
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                  'fontSize': '24px'})),
            html.Button('✚', id='add_id', style={'margin': '0px 50px', 'marginTop': '20px'}),
            html.Td(html.P(id="num2-display", children=num2,
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px',
                                  'fontSize': '24px'})),
            html.Button('⁼', id='equals_id', style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '24px'}),
            html.Td(dcc.Input(id="user_answer", type="number", placeholder="Enter your answer here",
                              style={"fontSize": "20px"}))
        ]),
        html.Div(style={'height': '50px'}),
        html.Tr([
            html.Td(html.Div([html.Img(src=banana_image, height=50) for _ in range(num1)],
                             style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                    'align': 'center'})),
            html.Td(),
            html.Td(html.Div([html.Img(src=banana_image, height=50) for _ in range(num2)],
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
