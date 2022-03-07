import requests

# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Armazena a resposta da API em uma variavel
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explora informaçoes sobre os repositorios
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Analiza o primeiro repositorio
repo_dict = repo_dicts[0]
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
