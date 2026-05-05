# https://qiita.com/tinymouse/items/b7d19c332ebcfa627043

import langchain_ollama
import langchain_core.prompts


model = langchain_ollama.OllamaLLM(
    model="gemma4"
)
prompt = langchain_core.prompts.chat.ChatPromptTemplate.from_template(
    """Question: {query}
    Answer:"""
)
query = "Function Callingとは何ですか？"

chain = (prompt | model)
output = chain.invoke({"query": query})

print(output)
