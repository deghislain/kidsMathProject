from dash.dependencies import Input, Output, State
from dash import html, dcc
from utils import BANANA_IMAGE, update_numbers, get_num1, get_num2
from main_layouts import main_layout

operations = []
def register_callbacks(app):
    @app.callback(
        Output("result", "children"),
        [Input("check_id", "n_clicks")],
        [State("user_answer", "value")],
        prevent_initial_call=True
    )
    def calculate(n_clicks, user_answer):
        correct_answer = get_num1() + get_num2()
        if user_answer == correct_answer:
            return html.Div([html.P("Correct!"), html.P(f"The answer is indeed {correct_answer}.")],
                            style={'color': 'green', 'fontSize': '24px'})
        elif user_answer is None:
            return html.P("Please enter your answer.")
        else:
            return html.Div([html.P("Incorrect."), html.P(f"Try Again.")],
                            style={'color': 'red', 'fontSize': '24px'})

    @app.callback(
        Output("resp_banana", "children"),
        [Input("equals_id", "n_clicks")]
        , prevent_initial_call=True
    )
    def add_show_images(n_clicks):
        resp = get_num1() + get_num2()
        return html.Td(html.Div([html.Img(src=BANANA_IMAGE, height=50) for _ in range(resp)], id="resp",
                                style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '10px',
                                       'align': 'center'}))

    @app.callback(
        Output('main_layout', 'children'),
        Input('next_id', 'n_clicks'),
        Input('start_id', 'n_clicks'),
        [State("math-operation", "value")],
        prevent_initial_call=True
    )
    def refresh_page(next_id, start_id, value):
        print("refresh_page next_id", next_id)
        if int(start_id) > 0:
            operations = value
            print("refresh_page next_id", value)
            if 'addition' in operations:
                return main_layout(True, False)
        if int(next_id) > 0:
            update_numbers()
            return dcc.Location(href='/', id='redirect')
        return main_layout()
