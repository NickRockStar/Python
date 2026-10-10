class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, 0)


d = MyDict({"a": 1, "b": 2})
print(d.get("a"))
print(d.get("c"))
