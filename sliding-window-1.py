import tiktoken

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = tiktoken.get_encoding("gpt2")

enc_text = tokenizer.encode(raw_text)

enc_sample = enc_text[50:100]

# the token size determines how much data the LLM will get for input for training
context_size = 4

for i in range(len(enc_sample) - context_size):
    # x is the input, and y is the expected output
    x = enc_sample[i:i+context_size]
    y = enc_sample[i+context_size]

    print(x, "->", y)
    print(tokenizer.decode(x), "->", tokenizer.decode([y]))
    print()
