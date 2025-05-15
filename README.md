# Chatbot IA Conversationnelle

Ce projet fournit une IA conversationnelle prête à fonctionner, basée sur Hugging Face Transformers et FastAPI.

## Prérequis

- Python 3.8+
- Docker (optionnel)

## Installation

```bash
# Cloner le projet
unzip chatbot.zip -d chatbot_project
cd chatbot_project

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Utilisation

Envoyez une requête POST à `/chat` avec un JSON :
```json
{
  "prompt": "Bonjour, comment ça va ?"
}
```
Obtenez une réponse JSON avec le texte généré.

## Avec Docker

```bash
# Construire l'image
docker build -t chatbot-ia .

# Lancer le conteneur
docker run -d -p 8000:8000 chatbot-ia
```
