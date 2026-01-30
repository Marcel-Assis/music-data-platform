# Script para ingestão de dados da API do iTunes

import requests
import json
import csv

# Fazendo uma requisição GET para a API do iTunes
url = "https://itunes.apple.com/search"
params = {"term": "coldplay", "limit": 2, "media": "music"}
response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

# Salvando os dados em arquivos JSON bruto
data = {"artist": "Coldplay", "track": "Yellow"}

with open("data/raw/itunes_data.json", "w") as file:
    json.dump(data, file, indent=2)

rows = [
    {"track": "Yellow", "artist": "Coldplay"},
    {"track": "Fix You", "artist": "Coldplay"},
]
# Salvar os dados processados em CSV processados
with open("data/processed/itunes_data.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["track", "artist"])
    writer.writeheader()
    writer.writerows(rows)