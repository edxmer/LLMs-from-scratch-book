*The data for training is the short story "The Verdict" by Edith Wharton*

## Files

### 1. `01-own-tokenizer-test.py`
Making a tokenizer by simply using the words and symbols in the training data

* **Pros:**
    * Simple, and easy to implement
* **Cons:**
    * If a word comes up that is not included in the tokenizer's original training data, it will have to use the `<|unk|>` token

### 2. `02-tiktoken-test.py`
In this file I test out OpenAI's "tiktoken" tokenizer, which uses byte-pair encoding

* **Pros:**
    * Can handle unkown words that come up
* **Cons:**
    * It is pretty complicated to implement efficiently, but luckily there are open source byte-pair tokenizers

### 3. `03-1-sliding-window.py`
In this file, I implement a very basic sliding window input-expected output generator, which is usually the way an LLM is trained, by predicting the next word.

There can be 2 approaches, the ones with, and without chunks:

> **Without chunks**
>
> You simply take a *context_size* element subsequence from the array and use it as input, then take the element after them, and use it as the expected output.

> **With chuncks**
>
> You take a *context_size* length subsequence from the array, then take another *context_size* length subsequence shifted by one. Then you do *context size* predictions on these. This will make it more efficient on the gpu, and also make the model capable of making predictions from different sized inputs.
