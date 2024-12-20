import random

def ShuffleList(collection):
    random.shuffle(collection)

def BubbleSort(collection):
    while not IsSorted(collection):
        for i in range(len(collection)):
            if i + 1 >= len(collection):
                return
            if collection[i] > collection[i + 1]:
                Swap(collection, i, i + 1)

def GnomeSort(collection):
    i = 0
    while i < len(collection):
        if i - 1 < 0:
            i += 1
        if i >= len(collection):
            return
        
        if collection[i - 1] > collection[i]:
            Swap(collection, i - 1, i)
            i -= 1
        else: i += 1

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
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers)

    ShuffleList(numbers)
    print(numbers)
    
    while True:
        GnomeSort(numbers)
        print(numbers)

        if IsSorted(numbers):
            break