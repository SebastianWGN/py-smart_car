import pygame	
import random
import math 

from genAlgorithmFunctions import populate, selection, crossover, mutation
from models.car import Car
from models.obstacle import Obstacle
from message import generation_message_display, genoma_message_display, time_message_display, maxtime_message_display

#colours
from utils.obstaclesFactory import generateObstacles

grey = (118,119,110)
black = (0,0,0)

#Semilla del random
random.seed(3)

backasfalt = pygame.image.load("assets/asfalto.jpg") #imagen del asfalto
backgroundleft=pygame.image.load("assets/left.png")	#imagen del cesped izquierdo
backgroundright=pygame.image.load("assets/right.png")	#imagen del cesped derecho
bkg=pygame.image.load("assets/background.jpg")

asfaltLeftLimitX = 330
asfaltRightLimitX = 670

def background(display):
	display.blit(backasfalt, (0, 0))
	display.blit(backgroundleft,(0,0))	    #set left side position of background image at x axis & y axis
	display.blit(backgroundright,(666,0))	#set right side position of background image at x axis & y axis


#Function that verifies collision with obstacle
def crashWithObstacle(obstacle: Obstacle, car: Car) -> bool:
	if car.y < obstacle.y + obstacle.height:  # if obstacle car not pass
		if car.x > obstacle.x and car.x < obstacle.x + obstacle.width \
				or car.x + car.width > obstacle.x and car.x + car.width < obstacle.x + obstacle.width:
			return True
	else:
		return False

#Function that verifies colission with asphalt boundaries
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


mutationRate = 0.3
parents = []
# Generamos el carro
theCar = Car(475, 540, 52)

# Tamaño de la población
sizePopulation = 10

maxTime = 0 

#Logic in game
def game_loop(display):		#all the function are called using this function
	global maxTime
	bkgy = 0
	itMoved = False

	# Indice de la lista de direcciones en ejecución que ira aumentando para acceder a la siguiente lista (Genoma)
	currentDirection = 0

	# Indice del obstáculo que irá aumentando para acceder al siguiente obstáculo
	obstaclesCounter = 0

	# Matriz de tiempos donde cada elemento es lo que tarda en terminar el recorrido
	# una determinada lista de direcciones en una generación
	#timeList: rows are generations, columns are genomas
	timeList = [[0.0 for _ in range(sizePopulation)]]

	# Generación inicial
	currentGeneration = 0
	time = 0
	

	# Generamos la lista de obstaculos
	obstacleList = generateObstacles()
	sizeObstacles = len(obstacleList)  # Tamaño de la lista de obstaculos

	# Creamos la población de direcciones inicial
	currentListDirections = []
	currentListDirections.append(populate(sizeObstacles, sizePopulation))

	#iteration for every genoma
	bumped = False	
	while not bumped:	#game is started
		for event in pygame.event.get(): 	#if any input is given
			if event.type==pygame.QUIT:		#if quit input is given
			#bumped=True		#game is stopped
				pygame.quit()
				quit()
		rel_y = bkgy % 1200
		display.blit(bkg, (0, rel_y - 1200))
		if rel_y < 600:
			display.blit(bkg, (0, rel_y))
		bkgy += 10
		time += 0.1



		if currentDirection < sizePopulation:
			#MAX TIME
			if max(timeList[currentGeneration]) > maxTime:
				maxTime = math.trunc(max(timeList[currentGeneration]))

			if obstaclesCounter == sizeObstacles:
				timeList[currentGeneration][currentDirection] = time
				print("Generación: " + str(currentGeneration + 1))
				print("Dirección (Genoma): " + str(currentDirection + 1))
				print("Tiempo(Genoma): " + str(timeList[currentGeneration][currentDirection]))
				print("Tiempo maximo: " + str(maxTime))
				time = 0
				currentDirection += 1
				obstaclesCounter = 0
				obstacleList = generateObstacles()
				sizeObstacles = len(obstacleList)

		#Previous generation ended
		else:
			#MAX TIME
			if max(timeList[currentGeneration]) > maxTime:
				maxTime = math.trunc(max(timeList[currentGeneration]))

			#SELECTION HERE
			global parents
			parents = selection(sizePopulation, timeList[currentGeneration])

			#CROSSOVER
			#newGenerationDirections = populate(sizeObstacles, sizePopulation)
			currentListDirections.append(crossover(parents, sizePopulation, currentListDirections[currentGeneration] ))
	
			#MUTATION
			global mutationRate
			currentListDirections[currentGeneration] = mutation(sizePopulation, currentListDirections[currentGeneration], mutationRate)

			currentGeneration += 1
			#print(timeList[currentGeneration][currentDirection])
			timeList.append([0.0 for _ in range(sizePopulation)])
			time = 0
			currentDirection = 0
			obstaclesCounter = 0

			obstacleList = generateObstacles()
			sizeObstacles = len(obstacleList)


		########### MOVE CONDITION FOR THE CAR ###########
		if not itMoved:
			itMoved = carMoves(obstacleList[obstaclesCounter],
					 theCar,
					 currentListDirections[currentGeneration][currentDirection][obstaclesCounter])

		################################


		############# DISPLAYS #############
		#background(display)

		#Para que me explique pepino la utilidad
		obstacleList[obstaclesCounter].y -= (obstacleList[obstaclesCounter].speed/4)
		obstacleList[obstaclesCounter].draw(display)
		obstacleList[obstaclesCounter].y += obstacleList[obstaclesCounter].speed

		generation_message_display("Generación: " + str(currentGeneration + 1), display)
		genoma_message_display("Genoma: " + str(currentDirection + 1), display)
		time_message_display("Tiempo: " + str(math.trunc(time)), display)
		maxtime_message_display("Tiempo máximo: " + str(maxTime), display)
		theCar.draw(display)
		################################

			
		######## PASSED OBSTACLE WITHOUT CRASH ########

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

		#detect crashes
		if crashedWithAsfalt or crashedWithObstacle:
			theCar.crash(display)
			theCar.setX(475)
			itMoved = False
			if currentDirection == sizePopulation:

				"""
				ESTO NUNCA SE EJECUTA
				#continue with next generation
				print(timeList[currentGeneration][currentDirection])
				timeList.append([0.0 for _ in range(sizePopulation)])
				currentDirection = 0
				obstaclesCounter = 0
				currentGeneration += 1
				newGenerationDirections = populate(sizeObstacles, sizePopulation)
				currentListDirections = newGenerationDirections
				time = 0
				"""
			else:
				#continue with next genome
				timeList[currentGeneration][currentDirection] = time
				print("Generación: " + str(currentGeneration + 1))
				print("Dirección (Genoma): " + str(currentDirection + 1))
				print("Tiempo que tarda: " + str(timeList[currentGeneration][currentDirection]))
				print("Tiempo maximo: " + str(maxTime))
				obstaclesCounter = 0
				currentDirection += 1
				time = 0
				
			
			obstacleList = generateObstacles()
			sizeObstacles = len(obstacleList)
			crashedWithAsfalt = False
			crashedWithObstacle = False
			continue
		################################



		pygame.display.update()		#update the display	

