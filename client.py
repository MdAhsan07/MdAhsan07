from openai import OpenAI

client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)