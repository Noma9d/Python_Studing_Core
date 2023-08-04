from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key, val in self.data.items():
            if value == val:
                keys.append(key)

        return keys


dict = LookUpKeyDict()

dict[1] = 'a'
dict[2] = 'b'

print(dict.lookup_key('a'))