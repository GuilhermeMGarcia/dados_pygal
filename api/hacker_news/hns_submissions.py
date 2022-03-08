import requests
import pygal
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Processa informaçoes sobre cada artigo submetido
submission_ids = r.json()
names, plot_dicts = [], []
repo_dicts = []
for submission_id in submission_ids[:30]:
    # Cria uma chamada de API separada para cada artigo submetido
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    repo_dicts.append(submission_r.json())

repo_dicts = sorted(repo_dicts, key=itemgetter('score'),
                          reverse=True)

for repo_dict in repo_dicts:
    names.append(repo_dict['title'])
    plot_dict = {
        'value': repo_dict['score'],
        'xlink': repo_dict.get('url'),
    }
    plot_dicts.append(plot_dict)



# Cria a visualizaçao
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend =False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Hacker News'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('news.svg')