from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "gpt-oss:20b",
    validate_model_on_init = True,
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
llm.invoke(messages)



stream = llm.stream(messages)
full = next(stream)
for chunk in stream:
    full += chunk
full
