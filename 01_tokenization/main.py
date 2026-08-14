import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")
text="hey there!I am sunayana"

tokens=enc.encode(text)
print("Tokens",tokens)