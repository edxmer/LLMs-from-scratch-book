import tiktoken

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = tiktoken.get_encoding("gpt2")

enc_text = tokenizer.encode(raw_text)

enc_sample = enc_text[50:100]

# the token size determines how much data the LLM will get for input for training
context_size = 4




# without chunks
print("WITHOUT CHUNKS:\n\n")
for i in range(len(enc_sample) - context_size):
    input_array = enc_sample[i:i+context_size]
    expected_output = enc_sample[i+context_size]

    print(input_array, "->", expected_output)
    print(tokenizer.decode(input_array), "->", tokenizer.decode([expected_output]))
    print()



# with input-output chunks
print("WITH CHUNKS:\n\n")
for i in range(len(enc_sample) - context_size):
    input_chunk = enc_sample[i:i+context_size]
    output_chunk = enc_sample[i+1:i+context_size+1]

    print(input_chunk)
    print((len(str(input_chunk[0])) + 1) * " ", output_chunk)

    input_decoded = tokenizer.decode(input_chunk)
    output_decoded = tokenizer.decode(output_chunk)

    print(input_decoded)
    print((len(tokenizer.decode([input_chunk[0]])) - 1) * " ", output_decoded)
    print("\n")

"""
The advantage of the chunk approach is that every chunk basically contains 4 training samples

For example:

that was what the
     was what the women

Here we can use the following training samples:
    that -> was
    that was -> what
    that was what -> the
    that was what the -> women

This makes the models capable of predicting the next word from many different sized chunks, which in turn makes the model more capable
"""
