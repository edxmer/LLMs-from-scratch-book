import tiktoken
# Tiktoken uses byte-pair encoding, so it can handle most unknown words and symbols.
# Byte pair encoding works by first including all simple characters and symbols, adding combinations for the most common ones based on the training data


with open("the_verdict.txt", "r") as f:
    raw_text = f.read()

# the gpt2 encoder has 50257 tokens
tokenizer = tiktoken.get_encoding("gpt2")


t = "Akwirw ier"



integers = tokenizer.encode(t)

print(integers, tokenizer.decode(integers))

for i in integers:
    print(i, "-", tokenizer.decode([i]))
