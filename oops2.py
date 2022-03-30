class StringClass:
    def __init__(self, value):
        self.string = value

    def length(self):
        leng = len(self.string)
        return leng

    def string_to_list(self, str_lst):
        print(list(str_lst))


class PairsPossible(StringClass):
    def __init__(self, text_string):
        StringClass.__init__(self, text_string)
        self.text_string = text_string
        self.allPairs = []

    def getPairs(self):
        return self.allPairs

    def generatePairs(self):
        for s in list(self.text_string):
            for ss in list(self.text_string):
                self.allPairs.append(s + ss)


text_1 = PairsPossible("DELHI")
text_1.generatePairs()
pair_list = text_1.getPairs()
print(pair_list)