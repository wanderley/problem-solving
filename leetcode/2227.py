from typing import List, Dict
from collections import Counter

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self._table = dict(zip(keys, values))
        self._dictionary = dictionary
        self._encrypted_dictionary_counter = Counter([
            Encrypter._encrypt(self._table, word)
            for word in dictionary
        ])

    def _encrypt(table: Dict[str, str], word) -> str:
        return "".join([table.get(l, "$") for l in word])

    def encrypt(self, word1: str) -> str:
        return Encrypter._encrypt(self._table, word1)

    def decrypt(self, word2: str) -> int:
        return self._encrypted_dictionary_counter[word2]

e1 = Encrypter(
    keys=["a","b","c","d"],
    values=["ei","zf","ei","am"],
    dictionary=["abcd","acbd","adbc","badc","dacb","cadb","cbda","abad"],
)
assert e1.encrypt("abcd") == "eizfeiam"
assert e1.decrypt("eizfeiam") == 2

e2 = Encrypter(
    keys=["b"],
    values=["ca"],
    dictionary=["aaa","cacbc","bbaba","bb"],
)
assert e2.encrypt("bbb") == "cacaca"
assert e2.decrypt("cacaca") == 0
