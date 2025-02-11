import random
import pandas as pd
import requests
from datetime import datetime, timedelta

# Configurações do Datasets

NUM_ESPECIALISTAS = 141
NUM_LIDERES = 7
NUM_LIGACOES_DIA = 1500
PERCENTUAL_TMO_ALTO = 0.2
TMO_PADRAO = (4,7)
TMO_ALTO = (8,12)


def obter_nomes_wikipedia(quantidade):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": "Category:American_film_actors",
        "cmlimit": quantidade
    }
    response = requests.get(url, params=params).json()
    nomes = [item["title"] for item in response["query"]["categorymembers"]]
    return list(set(nomes))  # Garante que os nomes sejam únicos


nomes = obter_nomes_wikipedia(NUM_ESPECIALISTAS + NUM_LIDERES)

df_nomes = pd.DataFrame(nomes)

print(df_nomes.sample(50))