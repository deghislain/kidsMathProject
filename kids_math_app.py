import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import random
import base64

app = dash.Dash(__name__)

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
resp = 0

with open("banana.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

banana_image = f"data:image/png;base64,{encoded_image}"

app.layout = html.Div([
    html.Div([
        html.H1("Math Web Application"),
        html.H3("Click on equals to get help", style={'color': 'blue'})
    ], style={'display': 'block', 'textAlign': 'center'}),
    html.Table([
        html.Tr([
            html.Td(html.P(id="num1-display", children=num1,
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px', 'fontSize': '24px'})),
            html.Button('✚', id='add_id', style={'margin': '0px 50px', 'marginTop': '20px'}),
            html.Td(html.P(id="num2-display", children=num2,
                           style={'textAlign': 'center', 'border': '2px solid #ccc', 'padding': '5px', 'fontSize': '24px'})),
            html.Button('⁼', id='equals_id', style={'margin': '0px 50px', 'marginTop': '20px', 'fontSize': '24px'}),
            html.Td(dcc.Input(id="user_answer", type="number", placeholder="Enter your answer here", style={"fontSize": "20px"}))
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
    ], style={'margin': '0 auto', 'width': '70%'}),
], style={'textAlign': 'center', 'width': '100%', 'background': ' #87CEEB'})


@app.callback(
    Output("result", "children"),
    [Input("check_id", "n_clicks")],
    [State("user_answer", "value")],
    prevent_initial_call=True
)
def calculate(n_clicks, user_answer):
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        return html.Div([html.P("Correct!"), html.P(f"The answer is indeed {correct_answer}.")],
                        style={'color': 'green', 'fontSize': '24px'})
    elif user_answer is None:
        return html.P("Please enter your answer.")
    else:
        return html.Div([html.P("Incorrect."), html.P(f"The correct answer is {correct_answer}.")],
                        style={'color': 'red', 'fontSize': '24px'})


@app.callback(
    Output("resp_banana", "children"),
    [Input("equals_id", "n_clicks")]
    , prevent_initial_call=True
)
def add_show_images(n_clicks):
    resp = num1 + num2
    return html.Td(html.Div([html.Img(src=banana_image, height=50) for _ in range(resp)], id="resp",
                            style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                   'align': 'center'}))


if __name__ == '__main__':
    app.run_server()
