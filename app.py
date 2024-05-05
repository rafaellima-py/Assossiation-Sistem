import dash
import dash_bootstrap_components as dbc

# Define o aplicativo com Dash e os estilos externos usando Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define o servidor WSGI para implantação
server = app.server
