import openai
openai.api_key = "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"

prompt = "Hello, can you introduce yourself?"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7)
answer = response.choices[0].text.strip()

print(answer)