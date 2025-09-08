from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.1",
    temperature=0.7,
    num_predict=120,
    base_url="http://localhost:11434",
    # other params...
)

input_text = "Como llego el protestantismo a America Latina "
# response = llm.invoke(input_text)
# print(response)

for chunk in llm.stream(input_text):
    print(chunk, end="")

# stream:
# async for chunk in llm.astream(input_text):
#     print(chunk, end="")