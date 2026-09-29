import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.token_to_index = vocab
        self.index_to_token = {value: key for key, value in vocab.items()}

    def encode(self, text):
        encoded = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        encoded = [word.strip() for word in encoded if word.strip()]
        return [self.token_to_index[token] for token in encoded]

    def decode(self, ids):
        text = " ".join([self.index_to_token[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1',text)
        return text

class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.token_to_index = vocab
        self.index_to_token = {value: key for key, value in vocab.items()}

    def encode(self, text):
        encoded = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        encoded = [word.strip() for word in encoded if word.strip()]
        unk_id = self.token_to_index["<|unk|>"]
        ids = [self.token_to_index.get(token, unk_id) for token in encoded]
        return ids

    def decode(self, ids):
        text = " ".join([self.index_to_token[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1',text)
        return text