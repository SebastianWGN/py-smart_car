from random import choices
from typing import List

Genoma = List[int]


def generateGenoma(length: int) -> Genoma:
    return choices([-1, 0, 1], k=length)

def populate(length: int, size: int):
    #Generar "size" genomas de "length" términos
    return [generateGenoma(length) for _ in range(size)]

def fitness():
    return


def selection(populationSize, fitnessList ):
    #elegir padres
    weights = []
    sum = 0
    for element in fitnessList:
        sum += element
    for i in range(len(fitnessList)):
        weights.append(fitnessList[i]/sum)

    mixedList = choices(
        population= list(range(0,populationSize)),
        weights= weights,
        k=populationSize//2
    )

    results = []
    for i in range (0, len(mixedList)//2, 2):
        results.append((mixedList[i],mixedList[i+1]))
    return results


def crossover():
    return

def mutation():
    return


def evolution():
    return

