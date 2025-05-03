import ollama

response = ollama.list()
ollama.chat
# 
# print(response)
# to chat any to the model
res = ollama.chat(
    model='llama3.2',
    messages=[
        {'role': 'user', 'content': 'why is the ocean so salty?'}
    ],
    stream = True,
)
# for chunk in res:
#     print(chunk['message']['content'], end = "", flush = True)

# == generate example ===
res = ollama.generate(
    model = "llama3.2",
    prompt = "why is the sky blue?",

)

# show 
print(ollama.show("llama3.2"))