import dash

from callbacks import register_callbacks

from layouts import main_layout

app = dash.Dash(__name__)

app.layout = main_layout()

register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
