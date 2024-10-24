import dash
from dash.dependencies import Input, Output, State
from dash import html, dcc
from utils import BANANA_IMAGE, update_numbers, get_num1, get_num2
from main_layouts import main_layout
import random

operations = []


def register_callbacks(app):
    @app.callback(
        Output("result", "children"),
        [Input("check_id", "n_clicks")],
        [State("user_answer", "value"), State("page_type", "value")],
        prevent_initial_call=True
    )
    def calculate(n_clicks, user_answer, page_type):
        """Check user's answer and return feedback."""
        correct_answer = get_num1() + get_num2()
        if user_answer is None:
            return html.P("Please enter your answer.")

        is_correct = (user_answer == correct_answer) or (page_type == "counting" and user_answer == get_num1())
        message = f"The answer is indeed {correct_answer}." if is_correct else "Try Again."
        color = "green" if is_correct else "red"

        return html.Div(
            [html.P("Correct!" if is_correct else "Incorrect."), html.P(message)],
            style={'color': color, 'fontSize': '24px'}
        )

    @app.callback(
        Output("resp_banana", "children"),
        [Input("equals_id", "n_clicks")],
        prevent_initial_call=True
    )
    def add_show_images(n_clicks):
        """Display bananas representing the correct answer."""
        correct_answer = get_num1() + get_num2()
        return html.Td(
            html.Div(
                [html.Img(src=BANANA_IMAGE, height=50) for _ in range(correct_answer)],
                id="resp",
                style={
                    'display': 'grid',
                    'gridTemplateColumns': 'repeat(3, 1fr)',
                    'gap': '10px',
                    'align': 'center'
                }
            )
        )

    @app.callback(
        Output('main_layout', 'children'),
        [Input('next_id', 'n_clicks'), Input('start_id', 'n_clicks')],
        [State("math-operations_id", "value")],
        prevent_initial_call=True
    )
    def next_page(next_id, start_id, value):
        """Navigate to the next exercise or start a new one."""
        ctx = dash.callback_context
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger == 'start_id':
            return get_next_exercise(value)
        elif trigger == 'next_id':
            update_numbers()
            return get_next_exercise()
        return main_layout()


def get_next_exercise(value=None):
    """Get the next exercise based on the current operations."""
    global operations
    if value:
        operations = value
    if len(operations) > 1:
        return main_layout(random.randint(0, len(operations) - 1), False)
    else:
        return main_layout(0, False)