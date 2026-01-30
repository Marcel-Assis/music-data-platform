# src/ingest_itunes.py
import requests
# Fazer uma requisição à API do iTunes para buscar músicas de um artista específico
url = "https://itunes.apple.com/search"
params = {"term": "coldplay", "limit": 2, "media": "music"}

response = requests.get(url, params=params)
data = response.json()

print(data.keys())  # mostra as chaves principais do JSON

import json
# Salvar os dados brutos em um arquivo JSON
with open("data/raw/itunes_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

    import csv

results = data["results"]
# Processar os dados e salvar em um arquivo CSV
rows = []
for item in results:
    rows.append({
        "trackName": item.get("trackName"),
        "artistName": item.get("artistName"),
        "collectionName": item.get("collectionName"),
        "releaseDate": item.get("releaseDate"),
        "primaryGenreName": item.get("primaryGenreName")
    })

with open("data/processed/itunes_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)