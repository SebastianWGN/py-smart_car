from random import choices
import random as r
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
        k=populationSize
    )

    results = []
    for i in range (0, len(mixedList), 2):
        results.append((mixedList[i],mixedList[i+1]))
        
    return results


def crossover(parents, populationSize, prevGenerationList):
    #for each parents
    #generate a random point
    #crossover 2 times
    results = []
    for i in range(len(parents)):
        for _ in range(populationSize//len(parents)):
            point = r.randint(0,populationSize)
            end = len(prevGenerationList[0])
            results.append( prevGenerationList[parents[i][0]][0:point] + prevGenerationList[parents[i][1]][point:end] )

    return results

def mutation(populationSize, generationList, mutationRate):
    #for each genome
    #generate a random probability
    #if > p, then mutate randomly
    results = []
    for i in range(len(generationList)):
        p = r.randint(0,100)/100
        if mutationRate > p:
            #mutation
            idx = r.randint(0,len(generationList[0])-1)
            generationList[i][idx] = generationList[i][idx] * -1
        results.append(generationList[i])

    return results


def evolution():
    return

