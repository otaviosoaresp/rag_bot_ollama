def ask_ollama(query, context, model):
    prompt = f"Contexto: {context}\n\nPergunta: {query}\nResposta:"
    response = model.generate(prompt=prompt)
    return response["output"]
