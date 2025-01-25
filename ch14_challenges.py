class Square():
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

    def __repr__(self):
        return """This square has four sides: {} by {} by {} by {}.""".format(self.s1,self.s1,self.s1,self.s1)

a_square = Square(3.3)
print(a_square)

def compare(a, b):
    return a is b

print(compare("schiper", "schiper"))
print(compare(7.5, 7.50))
