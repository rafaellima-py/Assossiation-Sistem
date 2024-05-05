import dash
from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc
import templates
import base

from app import *
from dash_bootstrap_templates import ThemeSwitchAIO

import templates.login_layout
import templates.register_layout

# =================================== Style =================================== #

template_theme1 = 'flatly'
template_theme2 = 'darkly'
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

# ================================ Read Pages ================================= #

app.layout = dbc.Container(
    className='vh-100', # Define a largura e altura como 100% e remove padding
    children=[
        dcc.Location(id='url'), # Adiciona o componente Location para rastrear a URL
        dbc.Container(id='page-content') # Um contêiner para o conteúdo de diferentes páginas
    ]
)

# ================================= CallBacks ================================= #

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return templates.login_layout.layout_login
    
    elif pathname == '/register':
        return templates.register_layout.layout_register

if __name__ == '__main__':
    app.run_server(debug=True)
