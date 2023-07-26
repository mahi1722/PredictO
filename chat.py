import openai

openai.api_key = "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"  # My key don't over use


def chat(query):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])

    return response.choices[0].message.content

# print(chat('Tell me about Diabetes')) /// Testing Code
