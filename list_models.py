from groq import Groq
import os

# Make sure your API key is set in this terminal
client = Groq(api_key=os.getenv("Groq_API_KEY"))

# List all models your key has access to
for model in client.models.list():
    print(model)

