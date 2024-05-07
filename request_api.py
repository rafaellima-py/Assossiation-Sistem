import httpx
import json

def login(cpf, password):
    url = 'https://501f-45-161-94-133.ngrok-free.app/login'

    data = {
        'cpf': cpf,
        'password': password
    }
    
    # Faz a solicitação POST à URL de login com os dados fornecidos
    try:
        response = httpx.post(url, json=data)
        
        # Verifica se a resposta é bem-sucedida
        if response.status_code == 200:
            return json.loads(response.text)
    
    except httpx.RequestError as exc:
        # Trate possíveis erros de conexão
        return {'message': 'Houve um erro no sevidor, não foi possível fazer login'}


def cadastro(cpf, password, name, whatsapp, nascimento, verso):
    registro = 'https://501f-45-161-94-133.ngrok-free.app/cadastro'

    data = {
  "nome_completo": name,
  "password": password,
  "cpf": cpf,
  "data_nascimento": nascimento,
  "foto_rg_verso": verso,
  "whatsapp": whatsapp
}
    
    try:
        request = httpx.post(registro, json=data)
            
        print(request.status_code)
        print(request.text)
        return {'message': 'Cadastro realizado com sucesso'}
    
    except:
        return {'message': 'Algo deu errado no seu cadastro, tente novamente'}