import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *

# Menu lateral
side_menu = dbc.Offcanvas(
    id='side-menu',
    children=[
        # Adiciona as opções do menu lateral
        dbc.ListGroup([
            dbc.ListGroupItem('Dashboard', href='/dashboard', id='nav_dashboard', action=True),
            dbc.ListGroupItem('Dados Pessoais', href='/dados-pessoais', id='nav_dados_pessoais', action=True),
            dbc.ListGroupItem('Dependentes', href='/dependentes', id='nav_dependentes', action=True),
            dbc.ListGroupItem('Indicações', href='/indicacoes', id='nav_indicacoes', action=True),
            dbc.ListGroupItem('Marketing', href='/marketing', id='nav_marketing', action=True),
            dbc.ListGroupItem('Sair', href='/sair', id='nav_sair', action=True)
        ], flush=True)
    ],
    placement='start',  # Coloca o menu lateral à esquerda
    scrollable=True,  # Permite rolar a lista
    is_open=False,  # Inicialmente fechado
)

# Crie a barra de navegação (navbar)
navbar = dbc.Navbar(
    dbc.Container(
        children=[
            # Adiciona o botão do menu hambúrguer
            dbc.Button(
                html.I(className='fas fa-bars'),  # Ícone de barras (hambúrguer)
                id='nav-button',
                className='me-2',
                n_clicks=0,
                color='primary',
                style={'background-color': '#508bfc'}  # Cor de fundo do botão
            ),
            html.Img(src='/static/images/moverbrasil2.png', alt='Logo', style={'width': '200px', 'height': 'auto'})
        ],
        fluid=True  # Define o contêiner como fluido
    ),
    color='dark',
    dark=True,
    className='w-100'  # Classe para largura total
)

# Layout
layout = dbc.Container(
    [
        # Navbar
        navbar,
        # Menu lateral
        side_menu,
        # Placeholder para o conteúdo da página
        html.Div(id='page-content')
    ],
    fluid=True  # Define o contêiner como fluido
)

# Callback para abrir e fechar o menu lateral
@app.callback(
    Output('side-menu', 'is_open'),
    [Input('nav-button', 'n_clicks')],
    [State('side-menu', 'is_open')]
)
def toggle_side_menu(n_clicks, is_open):
    if n_clicks > 0:
        return not is_open
    return is_open
