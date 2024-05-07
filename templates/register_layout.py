from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *
from request_api import cadastro

# Layout do registro
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
                                dbc.InputGroupText(html.I(className='bi bi-person')),  # Ícone de pessoa
                                dbc.Input(type='text', placeholder='Nome completo', id='nome'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para CPF com ícone de documento
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='bi bi-card-text')),  # Ícone de documento
                                dbc.Input(type='text', placeholder='CPF', id='cpf'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para número de WhatsApp com ícone de telefone
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='bi bi-telephone')),  # Ícone de telefone
                                dbc.Input(type='text', placeholder='WhatsApp', id='whatsapp'),
                            ], className='mb-3'),

                            # Campo de entrada para data de nascimento com ícone de calendário
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='bi bi-calendar')),  # Ícone de calendário
                                dbc.Input(type='date', placeholder='Data de nascimento', id='nascimento'),
                            ], className='mb-3'),

                            # Campo de entrada para senha com ícone de cadeado
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='bi bi-lock')),  # Ícone de cadeado
                                dbc.Input(type='password', placeholder='Senha', id='senha'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para confirmação de senha com ícone de cadeado
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='bi bi-lock')),  # Ícone de cadeado
                                dbc.Input(type='password', placeholder='Confirme a senha', id='conf_senha'),
                            ], className='mb-3'),
                            
                            # Campo de entrada para verso do RG com ícone de documento
                            dbc.InputGroup([
                                dbc.InputGroupText(html.I(className='bi bi-card-text')),  # Ícone de documento
                                dbc.Input(type='file', placeholder='Verso do RG', id='verso'),
                            ], className='mb-3'),

                            # Botão de registro
                            dbc.Button('Registrar-se', color='primary', id='register_btn', className='w-100', style={
                                'margin-top': '10px',
                                'background-color': '#508bfc'
                            }),
                        ]),
                        html.P('', id='status_register'),
                        
                        # Link caso a pessoa já tenha uma conta
                        html.A('Já possui uma conta? Faça login', href='/', className='d-block mt-3', style={'text-align': 'center'}),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output('status_register', 'children'),
    [Input('register_btn', 'n_clicks')],
    [State('nome', 'value'),
     State('cpf', 'value'),
     State('whatsapp', 'value'),
     State('nascimento', 'value'),
     State('senha', 'value'),
     State('conf_senha', 'value'),
     State('verso', 'value')]
)
def verificar_registro(n_clicks, nome, cpf, whatsapp, nascimento, senha, conf_senha, verso):
    if n_clicks is None:
        return ''  # Se o botão não foi clicado, não exibe mensagem
    
    mensagens_erro = {}
    
    # Verificar se os campos obrigatórios estão preenchidos
    if not nome:
        mensagens_erro['nome'] = 'Nome completo é obrigatório.'
    if not cpf:
        mensagens_erro['cpf'] = 'CPF é obrigatório.'
    if not whatsapp:
        mensagens_erro['whatsapp'] = 'Número de WhatsApp é obrigatório.'
    if not nascimento:
        mensagens_erro['nascimento'] = 'Data de nascimento é obrigatória.'
    if not senha:
        mensagens_erro['senha'] = 'Senha é obrigatória.'
    if not conf_senha:
        mensagens_erro['conf_senha'] = 'Confirmação de senha é obrigatória.'
    if not verso:
        mensagens_erro['verso'] = 'Foto do verso do RG é obrigatória.'
        
    # Verificar se as senhas correspondem
    if senha and conf_senha and senha != conf_senha:
        mensagens_erro['conf_senha'] = 'As senhas não correspondem.'
    
    # Se houver mensagens de erro, mostre-as
    if mensagens_erro:
        return html.Ul([html.Li(msg) for msg in mensagens_erro.values()])
    
    # Caso contrário, faça o registro
    response_message = cadastro(cpf, senha, nome, whatsapp, nascimento, verso)
    
    # Verificar a resposta da API e retornar a mensagem correspondente
    if response_message['message'] == 'Cadastro realizado com sucesso':
        return 'Cadastro realizado com sucesso!'
    else:
        return response_message['message']
