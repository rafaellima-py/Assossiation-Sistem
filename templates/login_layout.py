import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from app import *

layout_login = dbc.Row(
    className='vh-100 align-items-center justify-content-center',  # Centraliza vertical e horizontalmente
    children=[
        # Primeiro cartão com raio de borda apenas no lado esquerdo
        dbc.Card(
            style={
                'width': '5%',
                'height': '60%',
                'padding': '5%',
                'background': 'linear-gradient(to right, rgba(106, 17, 203, 1), rgba(37, 117, 252, 1))',
                'border-radius': '15px 0 0 15px'  # Raio de borda de 15px nos cantos superior esquerdo e inferior esquerdo
            },
            children=[
                dbc.CardBody(
                    children=[
                        # Você pode adicionar qualquer conteúdo aqui
                    ]
                )
            ]
        ),

        # Segundo cartão com raio de borda apenas no lado direito
        dbc.Card(
            className='shadow',
            style={
                'width': '45%',
                'height': '60%',
                'padding': '5%',
                'border-radius': '0 15px 15px 0',  # Raio de borda de 15px nos cantos superior direito e inferior direito
            },
            children=[
                dbc.CardBody(
                    className='text-center align-items-center',
                    children=[
                        # Logo da empresa
                        html.Div([
                            html.Img(src='caminho/para/logo.png', alt='Logo', style={'width': '100px', 'margin-bottom': '20px'}),
                            html.H2('Mover Brasil', className='mb-4'),
                        ]),
                        
                        # Instrução para login
                        html.Div([
                            html.Label('Entre com sua conta', className='mb-3'),
                            
                            # Campo de entrada para CPF com ícone de pessoa
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='person')),  # Ícone de pessoa
                                dbc.Input(type='text', placeholder='CPF', id='cpf_login'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para senha com ícone de cadeado
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='lock')),  # Ícone de cadeado
                                dbc.Input(type='password', placeholder='Senha', id='password_login'),
                                html.P(id='result_login')
                            ], className='mb-3'),
                            
                            # Checkbox para "Lembrar login"
                            dbc.Checklist(
                                options=[{"label": "Lembrar login", "value": "lembrar"}],
                                value=[],
                                id='remember-login',
                                inline=True,
                                className='mb-3'
                            ),
                            
                            # Link para "Esqueci a senha"
                            html.A('Esqueci a senha', href='#', className='mb-3 d-block', style={'text-align': 'right'}),
                            
                            # Botão de login
                            dbc.Button('Entrar', color='primary', id='login',className='w-100', style={
                                'margin-top': '10px',
                                'background-color': '#508bfc'
                            }),
                            
                            # Link para "Registrar-se"
                            html.A('Registrar-se agora', href='/register', className='d-block mt-3', style={'text-align': 'center'}),
                        ]),
                    ],
                ),
            ],
        ),
    ],
)

# =============================== Callbaks ===================================== #

@app.callback(
    Output('result_login', 'children'),
    Input('cpf_login', 'value'),
    Input('password_login', 'value'),
    Input('login', 'n_clicks')
)
def verify_login(cpf, password, n_clicks):
    # Se o botão de login não foi clicado ainda, retorne uma mensagem vazia
    if n_clicks is None or n_clicks == 0:
        return ''
    
    # Verifica se CPF e senha estão corretos
    if cpf == '12345678900' and password == 'senha_secreta':
        return 'Login bem-sucedido!'
    else:
        return 'CPF ou senha incorretos.'
