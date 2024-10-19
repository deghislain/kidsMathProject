import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
from addition import math_addition_table
from utils import get_banana_image
import random

app = dash.Dash(__name__)

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
resp = 0

app.layout = html.Div([
    html.Div([
        html.H1("Math Web Application"),
        html.H3("Click on equals to get help", style={'color': 'blue'})
    ], style={'display': 'block', 'textAlign': 'center'}),
    math_addition_table(num1, num2),  # Call the separate component here
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
    banana_image = get_banana_image()
    return html.Td(html.Div([html.Img(src=banana_image, height=50) for _ in range(resp)], id="resp",
                            style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                   'align': 'center'}))


if __name__ == '__main__':
    app.run_server()
