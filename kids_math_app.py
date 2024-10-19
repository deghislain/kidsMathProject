import dash
from dash import html
from addition import math_addition_table
from callbacks import register_callbacks


def main_layout():
    return html.Div([
        html.Div([
            html.Button("Skip", id="skip_id", style={"fontSize": "24px"}),
            html.Span(style={'marginRight': '350px'}),
        ], style={'textAlign': 'right'}),  # Add style here
        html.Div([
            html.H1("Math Web Application"),
            html.H3("Click on equals to get help", style={'color': 'blue'})
        ], style={'display': 'block', 'textAlign': 'center'}),
        math_addition_table(),

    ], style={'textAlign': 'center', 'width': '100%', 'background': ' #87CEEB'}, id="main_layout")


app = dash.Dash(__name__)

app.layout = main_layout()

register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
