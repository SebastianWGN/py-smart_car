from models.obstacle import Obstacle


def generateObstacles():
    speed = 20
    lista = []
    xCarril1 = 355
    xCarril2 = 480
    xCarril3 = 595
    fh = open('text_files\\obstacles.txt')

    for line in fh.readlines():
        for n in line.strip():
            if int(n) == 1:
                lista.append(Obstacle(xCarril1, 320, 52, 100, 0, speed))
            elif int(n) == 2:
                lista.append(Obstacle(xCarril2, 320, 52, 100, 1, speed))
            elif int(n) == 3:
                lista.append(Obstacle(xCarril3, 320, 52, 100, 2, speed))
    return lista
