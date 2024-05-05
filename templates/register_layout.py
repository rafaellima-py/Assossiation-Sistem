import dash
from dash import html
import dash_bootstrap_components as dbc

layout_register = dbc.Row(
    className='vh-100 align-items-center justify-content-center',  # Centraliza vertical e horizontalmente
    children=[
        # Primeiro cartão com raio de borda apenas no lado esquerdo
        dbc.Card(
            style={
                'width': '5%',
                'height': '80%',
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
                'height': '80%',
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
                        
                        # Instrução para registro
                        html.Div([
                            html.Label('Preencha o formulário para registrar-se', className='mb-3'),
                            
                            # Campo de entrada para nome completo
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='person')),  # Ícone de pessoa
                                dbc.Input(type='text', placeholder='Nome completo'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para CPF com ícone de documento
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='badge')),  # Ícone de documento
                                dbc.Input(type='text', placeholder='CPF'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para número de WhatsApp com ícone de telefone
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='phone')),  # Ícone de telefone
                                dbc.Input(type='text', placeholder='WhatsApp'),
                            ], className='mb-3'),

                            # Campo de entrada para senha com ícone de cadeado
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='lock')),  # Ícone de cadeado
                                dbc.Input(type='password', placeholder='Senha'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para confirmação de senha com ícone de cadeado
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='lock')),  # Ícone de cadeado
                                dbc.Input(type='password', placeholder='Confirme a senha'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para verso do RG com ícone de documento
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='material-icons', children='badge')),  # Ícone de documento
                                dbc.Input(type='file', placeholder='Verso do RG'),
                            ], className='mb-3'),

                            # Botão de registro
                            dbc.Button('Registrar-se', color='primary', className='w-100', style={
                                'margin-top': '10px',
                                'background-color': '#508bfc'
                            }),
                        ]),
                        
                        # Link caso a pessoa já tenha uma conta
                        html.A('Já possui uma conta? Faça login', href='/', className='d-block mt-3', style={'text-align': 'center'}),
                    ],
                ),
            ],
        ),
    ],
)
