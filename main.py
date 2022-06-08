from abc import ABC

class Count(ABC) :
    address = ""
    def __init__(self,address):
        self.address = address

    def calculateFreqs(self):
        pass
class  ListCount(Count):

    def __init__(self,address):
        Count.__init__(self,address)

    def calculateFreqs(self,address):
        list = []
        file = open(address)
        read_list = file.readline().split()

        for i in read_list:
            if i not in list:
                list.append(i)
        for i in range(0, len(list)):
            print(read_list.count(list[i]), " -> ", list[i])




class  DictCount(ListCount):
    def _init_(self, address):
        Count._init_(self, address)

    def calculateFreqs(self, address):
        dict = {}
        file = open(address)
        read_dict = file.readline()

        for i in read_dict.split():
            dict[i] = dict.get(i, 0) + 1
        for i in dict:
            print("{} : {}".format(i, dict[i]))

myObject = "C:\\Users\\MONSTER\\Desktop\\Doctor_Strange.txt"
print("\n*LAB - 8 - LIST*\n")
list_file = ListCount(myObject)
list_file.calculateFreqs(myObject)

print("\n*LAB - 8 - DICT*\n")
dict_file = DictCount(myObject)
dict_file.calculateFreqs(myObject)