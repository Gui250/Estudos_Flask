import urllib.request
import json


def resultado_filmes(tipo):
    if tipo == 'Populares':
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=e498cf2c94f441a0e95a44d59fa47e03'
    elif tipo == 'Animação':
          url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=e498cf2c94f441a0e95a44d59fa47e03'
    elif tipo == '2010':
        url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=e498cf2c94f441a0e95a44d59fa47e03'


    resposta = urllib.request.urlopen(url)

    dados = resposta.read()

    dados_json = json.loads(dados)

    return dados_json['results']
