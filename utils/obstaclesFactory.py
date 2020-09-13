from models.obstacle import Obstacle


def generateObstacles():
    lista = []
    xCarril1 = 355
    xCarril2 = 480
    xCarril3 = 595
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
