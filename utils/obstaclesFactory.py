from models.obstacle import Obstacle


def generateObstacles():
    lista = []
    xCarril1 = 394
    xCarril2 = xCarril1 + 52 + 60
    xCarril3 = xCarril2 + 52 + 60
    fh = open('text_files\\obstacles.txt')

    for line in fh.readlines():
        for n in line.strip():
            if int(n) == 1:
                lista.append(Obstacle(xCarril1, -120, 52, 100, 0, 10))
            elif int(n) == 2:
                lista.append(Obstacle(xCarril2, -120, 52, 100, 1, 10))
            elif int(n) == 3:
                lista.append(Obstacle(xCarril3, -120, 52, 100, 2, 10))
    return lista
