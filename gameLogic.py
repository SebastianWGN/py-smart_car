import pygame	
import random

from genAlgorithmFunctions import populate
from models.car import Car
from models.obstacle import Obstacle

#colours
from utils.obstaclesFactory import generateObstacles

grey = (118,119,110)
black = (0,0,0)

#Semilla del random
random.seed(3)

backasfalt = pygame.image.load("assets/asfalto.jpg") #imagen del asfalto
backgroundleft=pygame.image.load("assets/left.png")	#imagen del cesped izquierdo
backgroundright=pygame.image.load("assets/right.png")	#imagen del cesped derecho

asfaltLeftLimitX = 330
asfaltRightLimitX = 670

def background(display):
	display.blit(backasfalt, (0, 0))
	display.blit(backgroundleft,(0,0))	    #set left side position of background image at x axis & y axis
	display.blit(backgroundright,(666,0))	#set right side position of background image at x axis & y axis


def crashWithObstacle(obstacle: Obstacle, car: Car) -> bool:
	if car.y < obstacle.y + obstacle.height:  # if obstacle car not pass
		if car.x > obstacle.x and car.x < obstacle.x + obstacle.width \
				or car.x + car.width > obstacle.x and car.x + car.width < obstacle.x + obstacle.width:
			return True
	else:
		return False


def crashWithAsfaltLimit(car: Car, asfaltLimitLeft: float, asfaltLimitRight: float) -> bool:
	if car.x < asfaltLeftLimitX or car.x > asfaltRightLimitX - car.width:
		return True
	else:
		return False

def carMoves(obstacle: Obstacle, car: Car, currentDirection: int):
	if obstacle.y > 0:
		if car.y - (obstacle.y + obstacle.height) < 10:
				car.move(currentDirection)
				return True
	return False



# Generamos el carro
theCar = Car(475, 540, 52)

# Tamaño de la población
sizePopulation = 10


#Logic in game
def game_loop(display):		#all the function are called using this function

	itMoved = False

	# Indice de la lista de direcciones en ejecución que ira aumentando para acceder a la siguiente lista (Genoma)
	currentDirection = 0

	# Indice del obstáculo que irá aumentando para acceder al siguiente obstáculo
	obstaclesCounter = 0

	# Matriz de tiempos donde cada elemento es lo que tarda en terminar el recorrido
	# una determinada lista de direcciones en una generación
	timeList = [[0.0 for _ in range(sizePopulation)]]

	# Generación inicial
	currentGeneration = 0

	time = 0

	# Generamos la lista de obstaculos
	obstacleList = generateObstacles()
	sizeObstacles = len(obstacleList)  # Tamaño de la lista de obstaculos

	# Creamos la población de direcciones inicial
	currentListDirections = populate(sizeObstacles, sizePopulation)

	bumped = False	#if game is not any problem to start
	while not bumped:	#game is start
		for event in pygame.event.get(): 	#if any input is given
			if event.type==pygame.QUIT:		#if quit input is given
			#	bumped=True		#game is stop
				pygame.quit()
				quit()

		time += 1

		if currentDirection < sizePopulation:
			if obstaclesCounter == sizeObstacles:
				timeList[currentGeneration][currentDirection] = time/3
				print("Generación: " + str(currentGeneration))
				print("Dirección (Genoma): " + str(currentDirection))
				print("Tiempo que tarda: " + str(timeList[currentGeneration][currentDirection]))
				time = 0
				currentDirection += 1
				obstaclesCounter = 0
				obstacleList = generateObstacles()
				sizeObstacles = len(obstacleList)


		else:
			currentGeneration += 1
			print(timeList[currentGeneration][currentDirection])
			timeList.append([0.0 for _ in range(sizePopulation)])
			time = 0
			currentDirection = 0
			obstaclesCounter = 0
			newGenerationDirections = populate(sizeObstacles, sizePopulation)
			currentListDirections = newGenerationDirections
			obstacleList = generateObstacles()
			sizeObstacles = len(obstacleList)


		########### MOVE CONDITION FOR THE CAR ###########
		if not itMoved:
			itMoved = carMoves(obstacleList[obstaclesCounter],
					 theCar,
					 currentListDirections[currentDirection][obstaclesCounter])

		################################


		############# DISPLAYS #############
		background(display)

		#Para que me explique pepino la utilidad
		obstacleList[obstaclesCounter].y -= (obstacleList[obstaclesCounter].speed/4)
		obstacleList[obstaclesCounter].draw(display)
		obstacleList[obstaclesCounter].y += obstacleList[obstaclesCounter].speed

		theCar.draw(display)
		################################


		
		######## PASSED OBSTACLE ########

		if obstacleList[obstaclesCounter].y > 600:
			obstaclesCounter += 1
			itMoved = False

		################################

		#COLOCAR CONDICIÓN DE CREACIÓN DE GENERACIÓN SIGUIENTE

		####### CRASH CONDITIONS #######

		# Car crash with one of the asfalt limits
		crashedWithAsfalt = crashWithAsfaltLimit(theCar, asfaltLeftLimitX, asfaltRightLimitX)

		# Car crash with the obstacle
		crashedWithObstacle = crashWithObstacle(obstacleList[obstaclesCounter], theCar)


		if crashedWithAsfalt or crashedWithObstacle:
			theCar.crash(display)

			if currentDirection == sizePopulation:
				print(timeList[currentGeneration][currentDirection])
				timeList.append([0.0 for _ in range(sizePopulation)])
				currentDirection = 0
				obstaclesCounter = 0
				currentGeneration += 1
				newGenerationDirections = populate(sizeObstacles, sizePopulation)
				currentListDirections = newGenerationDirections
				time = 0
			else:
				timeList[currentGeneration][currentDirection] = time / 3
				print("Generación: " + str(currentGeneration))
				print("Dirección (Genoma): " + str(currentDirection))
				print("Tiempo que tarda: " + str(timeList[currentGeneration][currentDirection]))
				obstaclesCounter = 0
				currentDirection += 1
				time = 0
			theCar.setX(475)
			obstacleList = generateObstacles()
			sizeObstacles = len(obstacleList)
			crashedWithAsfalt = False
			crashedWithObstacle = False
			continue
		################################



		pygame.display.update()		#update the display	

