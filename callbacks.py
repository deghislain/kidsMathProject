import dash
from dash.dependencies import Input, Output, State
from dash import html
from utils import get_image, update_numbers, get_num1, get_num2, get_chosen_operation, ICONS
from main_layouts import main_layout
import random
times = ['➊', '➋', '➌', '➍', '➎']
operations = []

session = {}


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
        elif page_type == "division":
            correct_answer = int(get_num1() / get_num2())
        elif page_type == "multiplication":
            correct_answer = get_multiplication_answer()

        elif user_answer is None:
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
         Input("remove_id", "n_clicks"),
         Input("equals_div_layout_id", "n_clicks"),
         Input("equals_mult_layout_id", "n_clicks")],
        [State("sub_number", "value"),
         State("page_type", "value")],
        prevent_initial_call=True
    )
    def add_show_images(equals_id, remove_id, equals_div_layout_id, equals_mult_layout_id, sub_number, page_type):
        """Display bananas representing the correct answer."""
        chosen_image = session.get('chosen_image')
        ctx = dash.callback_context
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]

        # Define a dictionary to map triggers to calculation functions
        calculation_functions = {
            'equals_id': lambda: get_num1() + get_num2() if page_type == "addition" else None,
            'remove_id': lambda: max(get_num1(), get_num2()) - sub_number if sub_number >= 0 else None,
            'equals_div_layout_id': lambda: int(get_num1() / get_num2()) if get_num2() != 0 else None,
            'equals_mult_layout_id': lambda: get_multiplication_answer() if get_num2() != 0 else None,
        }

        # Calculate the correct answer
        correct_answer = calculation_functions.get(trigger, lambda: None)()

        # Validate the correct answer
        if correct_answer is None:
            if trigger == 'remove_id':
                return html.P(f"Invalid number. Enter a number smaller than {max(get_num1(), get_num2())}",
                              style={'color': 'red', 'fontSize': '24px'})
            elif trigger == 'equals_div_layout_id':
                return html.P(f"Invalid number. Enter a number smaller or equals to {get_num2()}",
                              style={'color': 'red', 'fontSize': '24px'})

        # Special case for division layout
        if trigger == 'equals_div_layout_id':
            return html.Div([
                html.Tr([
                    html.Td([html.Img(src=get_image(image_name), height=50) for image_name in ICONS[:get_num2()]],
                            style={'display': 'grid', 'gridTemplateColumns': f'repeat({get_num2()}, 1fr)',
                                   'gap': '30%',
                                   'align': 'center'})
                ]),
                html.Tr([
                    html.Td([html.Img(src=get_image(chosen_image), height=50) for _ in range(get_num1())],
                            style={'display': 'grid', 'gridTemplateColumns': f'repeat({get_num2()}, 1fr)',
                                   'gap': '30%',
                                   'align': 'center'})
                ]),
            ])
        if trigger == 'equals_mult_layout_id':
            return html.Div([
                html.Div([
                    html.Tr([
                        html.Td(times[i],style={'color': 'blue', 'fontSize': '30px'}),
                        html.Td([html.Img(src=get_image(chosen_image), height=50) for _ in range(resize_numbers())],
                                style={'display': 'grid', 'gridTemplateColumns': f'repeat({resize_numbers()}, 1fr)',
                                       'gap': '30%', 'align': 'center'})
                    ]),
                    html.Tr([
                        html.Td(),
                        html.Td()
                    ]),
                ]) for i, _ in enumerate(range(resize_numbers(False)))
            ])

        # Return the image grid
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
        """Navigate to the next exercise or start a new one."""
        ctx = dash.callback_context
        if fruit_selector:
            session['chosen_image'] = fruit_selector
        else:
            fruit_selector = str(session.get('chosen_image'))
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger == 'start_id':
            return get_next_exercise(value, fruit_selector)
        elif trigger == 'next_id':
            update_numbers()
            return get_next_exercise(value, fruit_selector)
        return main_layout()


def get_next_exercise(value=None, fruit_selector=None):
    """Get the next exercise based on the current operations."""
    global operations
    if value:
        operations = value
    if len(operations) > 1:
        return main_layout(get_chosen_operation(operations), False, None, fruit_selector)
    elif len(operations) == 1:
        return main_layout(get_chosen_operation(operations), False, None, fruit_selector)
    else:
        return main_layout(err_msg="Please chose an operation")


def get_multiplication_answer():
    """We do not want to multiply numbers over 5"""
    return ((get_num1() if get_num1() <= 5 else 10 - get_num1()) *
            (get_num2() if get_num2() <= 5 else 10 - get_num2()))


def resize_numbers(first_number=True):
    if first_number:
        return get_num1() if get_num1() <= 5 else 10 - get_num1()
    else:
        return get_num2() if get_num2() <= 5 else 10 - get_num2()
