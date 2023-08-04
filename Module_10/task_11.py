from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for i in self.data:
            if i.isdigit():
                count += 1
        
        return count
    

str = NumberString('1fgr2rge3err4')

print(str.number_count())