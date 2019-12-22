list = [[1],[1,1],[1], [1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1]]

class Sort:
    greatest = 0
    def __init__(self, arr):
        self.arr = arr

    def getLongest(self):
        for i in self.arr:
            if (len(i) > self.greatest):
                self.greatest = len(i)
        return self.greatest

    def organize(self):
        sorted =[]
        while self.arr:
            array = Sort(self.arr)
            for i in self.arr:
                if(len(i) == array.getLongest()):
                    sorted.append(i)
                    self.arr.remove(i)
        return sorted

List = Sort(list)
List = List.organize()
for elem in List:
    for i in elem:
        print(i, end="")
    print(' ')
