from collections import defaultdict, UserDict
from itertools import count

class MagicHash(UserDict):
    # noinspection PyMissingConstructor
    def __init__(self):
        self.data = defaultdict(count().__next__)
        self.id2word = {}
        self.lastid = -1

    @classmethod
    def create_from_keys(cls, keys, freezed=True):
        ret = cls()
        length = len(keys)
        generator = zip(keys, range(length))
        ret.data = dict(generator) if freezed else defaultdict(count(length).__next__, generator)
        ret.id2word = dict(zip(ret.data.values(), ret.data.keys()))
        return ret

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.id2word[item]
        else:
            i = self.data[item]
            if i > self.lastid:
                self.id2word[i] = item
                self.lastid = i
            return i

    def rename(self, oldName, newName):
        self.data[newName] = self.data.pop(oldName)
        self.id2word[self.data[newName]] = newName

    def freeze(self):
        self.data.default_factory = None

    def pop(self, toDel):
        val = self.data.pop(toDel)
        self.id2word.pop(val)
        return val

