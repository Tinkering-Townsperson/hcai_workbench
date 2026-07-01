import requests
from pprint import pp

model_list = "https://ai.hackclub.com/proxy/v1/models"

MODELS = set()

response = requests.get(model_list)
response.raise_for_status()
result = response.json()["data"]

for model in result:
	if model["architecture"]["output_modalities"] == ["text",]:
		MODELS.add(model["id"])

MODELS = sorted(MODELS)

if __name__ == "__main__":
	pp(MODELS)
	print(len(MODELS))
