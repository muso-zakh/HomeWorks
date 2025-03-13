class Talabalar:
    def __init__(self, ism: str, yosh: int, id:int):
        self.ism = ism
        self.yosh = yosh
        self.id = id

    def __eq__(self, other):
        return self.id == other.id
        
t1 = Talabalar('muso', 16, 8989)
t2 = Talabalar('umar', 14, 8787)

t3 = Talabalar('oka', 17, 8989)

print(t1 == t2)
print(t1 == t3)