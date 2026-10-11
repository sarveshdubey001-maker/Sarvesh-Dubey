# Step 1: Install the OpenAI package
# pip install openai

from openai import OpenAI

# Step 2: Initialize client (make sure your API key is set in environment variables)
client = OpenAI()

# Step 3: Make a simple test request
response = client.responses.create(
    model="gpt-3.5-turbo",   # lightweight model for quick tests
    input="Hello OpenAI! Can you say hi back?"
)

# Step 4: Print the output
print(response.output_text)