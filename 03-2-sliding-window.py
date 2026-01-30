import torch
from torch.utils.data import Dataset, DataLoader
import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


class GPTDatasetV1(Dataset):
    def __init__(self, text, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []

        token_ids = tokenizer.encode(text)

        for i in range()
