"""
Authors: Bessie Li
Consulted: Sabrina Wang
Date: 11/1/23
Purpose: CS111 trainInventory task
"""

def printInventory(lists):
    """print the car number with the information of all the cars with it"""
    for i in range(len(lists)):
        print("Car # "+str(i))
        for name, weight in lists[i]:
            print(str(weight) + " kg "+ str(name)) 
                
def totalWeightOf(train, item):
    """returns the sum of the weight if the item matches"""
    sum = 0
    for x in train:
        for name, weight in x:
            if item == name:
                sum += weight
    return(sum)

def listItems(train, item):
    """if the item matches, it adds it to the list"""
    list = []
    for x in train:
        for name, weight in x:
            if name == item:
                list += [(name, weight)]
    return(list)
    
def listWeights(train):
    """finds the weight of each car and puts it into the list"""
    sum = []
    for x in train:
        sum1 = 0
        for name, weight in x:
            sum1 += weight
        sum += [sum1]
    return sum

def heaviestCar(train):
    """returns the index of the max weight car"""
    max = 0
    index = 0
    for i in range(len(train)):
        for name, weight in train[i]:
            if weight > max:
                max = weight
                index = i
    return(index)    

def itemWeight(item):
    """returns the weight if given one tuple"""
    return(item[1])


def inventoryByWeight(train):
    """sorts the list by train weight"""
    sorted2 = []
    for x in train:
        for y in x:
            sorted2.append(y)
    sorted1 = sorted(sorted2, key=itemWeight)
    return sorted1