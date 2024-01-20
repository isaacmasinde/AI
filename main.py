from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model", 
  messages=[
    {"role": "system", "content": "answer stating with abraham linch"},
    {"role": "user", "content": "Write the code to extract the files in python"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)