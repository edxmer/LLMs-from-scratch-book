
# files:
1. `own-tokenizer-test.py` -> Making a tokenizer by simply using the words and symbols in the training data
  - Pros:
    - Simple, and easy to implement
  - Cons: 
    - If a word comes up that is not included in the tokenizer's original training data, it will have to use the `<|unk|>` token
2. `tiktoken-test-1.py` -> In this file I test out OpenAI's "tiktoken" tokenizer, which uses byte-pair encoding
  - Pros:
    - Can handle unkown words that come up
  - Cons:
    - It is pretty complicated to implement efficiently, but luckily there are open source byte-pair tokenizers
3. `sliding-window-1.py` -> In this file, I implement a very basic sliding window input-expected output generator, which is usually the way an LLM is trained, by predicting the next word.

