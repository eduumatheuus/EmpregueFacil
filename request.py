import requests

# Suas credenciais da Adzuna
app_id = "c69808a7"
api_key = "804c5796af3dc2b43768d242dbc4af43"

# URL da API Adzuna para buscar vagas no Brasil
url = f"https://api.adzuna.com/v1/api/jobs/br/search/1?app_id={app_id}&app_key={api_key}&results_per_page=50&what=Uberlândia"

# Fazer requisição GET
response = requests.get(url)

# Checar se a requisição foi bem-sucedida
if response.status_code == 200:
    jobs = response.json()
    # Exibir as vagas de emprego
    for job in jobs['results']:
        print(f"Título: {job['title']}")
        print(f"Empresa: {job['company']['display_name']}")
        print(f"Local: {job['location']['display_name']}")
        print(f"Descrição: {job['description']}")
        print(f"URL: {job['redirect_url']}\n")
else:
    print(f"Erro na requisição: {response.status_code}")
