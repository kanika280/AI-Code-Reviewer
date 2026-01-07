from groq import Groq
import os

# Make sure your API key is set in this terminal
client = Groq(api_key=os.getenv("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"))

# List all models your key has access to
for model in client.models.list():
    print(model)
