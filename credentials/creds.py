import os

groq_creds = {
    "api_key": os.environ.get("GROQ_API_KEY"),
    "model_name": os.environ.get("MODEL_NAME"),
}
