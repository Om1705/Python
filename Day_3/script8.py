#!/usr/bin/python3



#           Inheritance



class CDAC:
    x = 0
    name = ""
    def __init__(self,n):
        self.name=n
        print(self.name,"contructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)


class Footballfan(CDAC):
    point=0
    def touch(self):
        self.point = self.point +7
        self.party()
        print(self.name,"points",self.point)


s = CDAC("Om")
s.party()

j=Footballfan("CC")
j.party()
j.touch()

