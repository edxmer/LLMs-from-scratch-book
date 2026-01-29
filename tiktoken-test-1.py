import tiktoken

with open("the_verdict.txt", "r") as f:
    raw_text = f.read()

tokenizer = tiktoken.get_encoding("gpt2")

t = "Akwirw ier"

integers = tokenizer.encode(t)

print(integers, tokenizer.decode(integers))

for i in integers:
    print(i, tokenizer.decode([i]))
