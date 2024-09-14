import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
# Carregar variáveis do arquivo .env
load_dotenv(dotenv_path=r'D:\Denis\Dev\profile\.env')

# Dados do seu aplicativo LinkedIn
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
STATE = os.getenv('STATE')

# Passo 1: Obter o código de autorização
def get_authorization_code_url():
    auth_url = "https://www.linkedin.com/oauth/v2/authorization"
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'r_liteprofile r_emailaddress',
        'state': STATE
    }
    return f"{auth_url}?{urlencode(params)}"

def main():
    # Passo 1: Mostrar URL de autorização
    print("Vá para o seguinte URL para obter o código de autorização:")
    print(get_authorization_code_url())

    # Solicitar o código de autorização do usuário
    authorization_code = input("Cole o código de autorização aqui: ")

    if not authorization_code:
        print("Código de autorização não fornecido. Saindo...")
        return

    # Passo 2: Obter o token de acesso
    def get_access_token(authorization_code):
        token_url = "https://www.linkedin.com/oauth/v2/accessToken"
        params = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(token_url, data=params, headers=headers)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return response.json()

    # Obter o token de acesso
    try:
        token_response = get_access_token(authorization_code)
        access_token = token_response.get('access_token')
        if not access_token:
            print("Não foi possível obter o token de acesso.")
            return
        print(f"Access Token: {access_token}")

    except requests.RequestException as e:
        print(f"Erro ao obter o token de acesso: {e}")
        return

    # Passo 3: Obter dados do perfil
    def get_linkedin_profile(access_token):
        profile_url = "https://api.linkedin.com/v2/me"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        response = requests.get(profile_url, headers=headers)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return response.json()

    # Passo 4: Obter o endereço de e-mail
    def get_linkedin_email(access_token):
        email_url = "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        response = requests.get(email_url, headers=headers)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return response.json()

    # Exemplo de uso
    try:
        profile = get_linkedin_profile(access_token)
        print("Perfil do LinkedIn:")
        print(profile)
        
        email = get_linkedin_email(access_token)
        print("Endereço de Email do LinkedIn:")
        print(email)

    except requests.RequestException as e:
        print(f"Erro ao obter dados do perfil ou e-mail: {e}")

if __name__ == "__main__":
    main()
