import random
from enum import Enum

class SortingAlgorithms(Enum):
    BUBBLE = 0
    GNOME = 1

class Sorter:
    def __init__(self, numberOfItems = 10, sortingAlgorithm = SortingAlgorithms.BUBBLE):
        self.collection = list()
        self.sortingAlgorithm = sortingAlgorithm
        self._currentIndex = 0
        self.Sorted = False

        for i in range(1, numberOfItems + 1):
            self.collection.append(i)
        pass

    def Step(self):
        match self.sortingAlgorithm:
            case SortingAlgorithms.BUBBLE:
                self._currentIndex = BubbleSortStep(self.collection, self._currentIndex)

            case SortingAlgorithms.GNOME:
                self._currentIndex = GnomeSortStep(self.collection, self._currentIndex)
        
        if self._currentIndex == None:
            if IsSorted(self.collection):
                self.Sorted = True
            else: self._currentIndex = 0

    def GetCurrentIndex(self):
        return self._currentIndex

    def ShuffleCollection(self):
        random.shuffle(self.collection)
        self._currentIndex = 0
        self.Sorted = False

    # what ones it is looking at to swap

def ShuffleList(collection):
    random.shuffle(collection)

def BubbleSortStep(collection, i):
    if i + 1 >= len(collection):
        return None
    if collection[i] > collection[i + 1]:
        Swap(collection, i, i + 1)

    return i + 1

def GnomeSortStep(collection, i):
    if i - 1 < 0:
        i += 1
    if i >= len(collection):
        return None
    
    if collection[i - 1] > collection[i]:
        Swap(collection, i - 1, i)
        return i - 1
    else: return i + 1

def IsSorted(collection):
    checking = list(collection)
    checking.sort()
    if collection == checking:
        return True
    else: return False

def Swap(collection, index1, index2):
    a = collection[index1]
    b = collection[index2]

    collection[index1] = b
    collection[index2] = a   

if __name__ == "__main__":
    sorter = Sorter(10, SortingAlgorithms.GNOME)
    ShuffleList(sorter.collection)

    while not sorter.Sorted:
        sorter.Step()
        for i, value in enumerate(sorter.collection):
            if i == sorter.GetCurrentIndex():
                for i in range(value):
                    print(f"\033[38;2;255;0;0mX\033[0m", end="")
            else:
                for i in range(value):
                    print("X", end="")
            print()
        input("")
