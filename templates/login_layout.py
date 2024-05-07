import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *
import request_api

layout_login = dbc.Row(
    className='vh-100 align-items-center justify-content-center',  # Centraliza vertical e horizontalmente
    children=[
        dcc.Location(id='login_redirect', refresh=True), 

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

                            html.P(id='result_login'),
                            
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
    [Output('result_login', 'children'), Output('login_redirect', 'pathname')],
    [Input('login', 'n_clicks')],
    [State('cpf_login', 'value'), State('password_login', 'value')]
)
def verify_login(n_clicks, cpf, password):
    # Inicialmente, nenhuma mensagem de erro e nenhum redirecionamento
    error_message = ''
    redirect_url = None
    
    # Se o botão de login não foi clicado, retorne uma mensagem vazia e nenhum redirecionamento
    if n_clicks is None or n_clicks == 0:
        return '', None
    
    # Verificação do CPF
    if not cpf:
        error_message = 'CPF é obrigatório.'
    else:
        import re
        cpf_pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        if not cpf_pattern.match(cpf):
            error_message = 'Formato de CPF inválido. Use 000.000.000-00.'
    
    # Verificação da senha
    if not password:
        error_message = 'Senha é obrigatória.'
    else:
        min_length = 8
        if len(password) < min_length:
            error_message = f'Senha deve ter pelo menos {min_length} caracteres.'
    
    # Se há uma mensagem de erro, retorne-a
    if error_message:
        return error_message, None
    
    # Chama a função de login da API com os dados fornecidos
    response = request_api.login(cpf, password)
    
    # Verifica a resposta da API
    if response.get('message') == 'sucesso':
        # Retorna mensagem de sucesso e redireciona para '/dashboard'
        return 'Login realizado com sucesso!', '/dashboard'
    
    else:
        # Retorna a mensagem de erro retornada pela API
        return response.get('message', 'Ocorreu um erro no login'), None