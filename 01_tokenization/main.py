import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")
text="hey there!I am sunayana"

tokens=enc.encode(text)
print("Tokens",tokens)

decoder=enc.decode([48467, 1354, 0, 40, 939, 7334, 114104])
print("decoder",decoder)