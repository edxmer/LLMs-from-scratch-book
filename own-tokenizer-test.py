import re

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

all_tokens = re.split("([.,:;?_!'\"()!]|--|\\s)", raw_text)
all_tokens = [item.strip() for item in all_tokens if item.strip()]
all_tokens = sorted(set(all_tokens))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])


class SimpleTokenizer:
    def __init__(self, tokens):
        self.id_to_word = tokens
        self.word_to_id = {e:i for i,e in enumerate(self.id_to_word)}
    def text_to_ids(self, text):
        preprocessed = re.split("([.,:;?_!'\"()!]|--|\\s)", text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        return [self.word_to_id[word] if word in self.word_to_id.keys() else self.word_to_id["<|unk|>"] for word in preprocessed]
    def ids_to_words(self, ids):
        text = " ".join([self.id_to_word[id] for id in ids])
        text = re.sub("\\s+([,.:;?!\"()\\\\'])", r'\1', text)
        return text

tokenizer = SimpleTokenizer(all_tokens)

t1 = "Hello, do you like tea?"
t2 = "In the sunlit terraces of the palace."

ts = " <|endoftext|> ".join([t1, t2])

ids = tokenizer.text_to_ids(ts)
print(ids[:50])
words = tokenizer.ids_to_words(ids)
print(words[:400])


