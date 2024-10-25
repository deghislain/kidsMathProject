import dash
from dash.dependencies import Input, Output, State
from dash import html
from utils import get_image, update_numbers, get_num1, get_num2, get_chosen_operation
from main_layouts import main_layout
import random

operations = []

chosen_image = ''


def register_callbacks(app):
    @app.callback(
        Output("result", "children"),
        [Input("check_id", "n_clicks")],
        [State("user_answer", "value"), State("page_type", "value")],
        prevent_initial_call=True
    )
    def calculate(n_clicks, user_answer, page_type):
        """Check user's answer and return feedback."""
        correct_answer = None
        if page_type == "addition":
            correct_answer = get_num1() + get_num2()
        elif page_type == "subtraction":
            num2, num1 = min(get_num1(), get_num2()), max(get_num1(), get_num2())
            correct_answer = num1 - num2
        if user_answer is None:
            return html.P("Please enter your answer.", style={'color': 'blue', 'fontSize': '24px'})

        is_correct = (user_answer == correct_answer) or (page_type == "counting" and user_answer == get_num1())
        message = f"The answer is indeed {correct_answer}." if is_correct else "Try Again."
        color = "green" if is_correct else "red"

        return html.Div(
            [html.P("Correct!" if is_correct else "Incorrect."), html.P(message)],
            style={'color': color, 'fontSize': '24px'}
        )

    @app.callback(
        Output("resp_banana", "children"),
        [Input("equals_id", "n_clicks"),
         Input("remove_id", "n_clicks")],
        [State("sub_number", "value"), State("page_type", "value")],
        prevent_initial_call=True
    )
    def add_show_images(equals_id, remove_id, sub_number, page_type):
        """Display bananas representing the correct answer."""
        ctx = dash.callback_context
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]
        correct_answer = None
        if trigger == 'equals_id' and page_type == "addition":
            correct_answer = get_num1() + get_num2()
        elif sub_number >= 0 and trigger == 'remove_id':
            num2, num1 = min(get_num1(), get_num2()), max(get_num1(), get_num2())
            correct_answer = num1 - sub_number
            if correct_answer is None or correct_answer < 0:
                return html.P(f"Invalid number. Enter a number smaller than {get_num1()}",
                              style={'color': 'red', 'fontSize': '24px'})
        return html.Td(
            html.Div(
                [html.Img(src=get_image(chosen_image), height=50) for _ in range(correct_answer)],
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
        [State("math-operations_id", "value"), State("fruit_selector", "value")],
        prevent_initial_call=True
    )
    def next_page(next_id, start_id, value, fruit_selector):
        chosen_image = fruit_selector
        """Navigate to the next exercise or start a new one."""
        ctx = dash.callback_context
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger == 'start_id':
            return get_next_exercise(value, chosen_image)
        elif trigger == 'next_id':
            update_numbers()
            return get_next_exercise(chosen_image)
        return main_layout()


def get_next_exercise(value=None, fruit_selector=None):
    """Get the next exercise based on the current operations."""
    global operations
    if value:
        operations = value
    if len(operations) > 1:
        return main_layout(random.randint(0, len(operations) - 1), False, fruit_selector)
    elif len(operations) == 1:
        return main_layout(get_chosen_operation(operations), False, fruit_selector)
    else:
        return main_layout(err_msg="Please chose an operation")
