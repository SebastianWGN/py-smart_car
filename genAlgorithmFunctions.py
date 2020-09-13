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


def selectPair():
    return

def crossover():
    return

def mutation():
    return


def evolution():
    return

