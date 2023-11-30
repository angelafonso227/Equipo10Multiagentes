from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from randomAgents.agent import Car, Destination, Obstacle, Traffic_Light, Road
import json
import random
import time

class CityModel(Model):
    """ 
        Creates a model based on a city map.

        Args:
            N: Number of agents in the simulation
    """
    def __init__(self, N):

        # Load the map dictionary. The dictionary maps the characters in the map file to the corresponding agent.
        dataDictionary = json.load(open('D:/Documentos/ACTIVIDADES TEC/QUINTO SEMESTRE/Multiagentes/Equipo10Multiagentes/RETO/Server/randomAgents/city_files/mapDictionary.json'))

        self.num_agents = N
        self.traffic_lights = []
        self.destinations_positions = [(4, 22), (13, 22), (11, 20), (21, 20), (3, 19), (2, 15), (21, 15), (5, 14), (11, 14), (17, 14), (19, 7), (2, 6), (11, 6), (5, 4), (14, 3), (21, 3)]
        

        # Load the map file. The map file is a text file where each character represents an agent.
        with open('D:/Documentos/ACTIVIDADES TEC/QUINTO SEMESTRE/Multiagentes/Equipo10Multiagentes/RETO/Server/randomAgents/city_files/2023_base.txt') as baseFile:
            lines = baseFile.readlines()
            self.width = len(lines[0])-1
            self.height = len(lines)

            self.grid = MultiGrid(self.width, self.height, torus=False) 
            self.schedule = RandomActivation(self)
            
            # for i in range(self.num_agents):
            #     a = Car(i + 1000, self) 
            #     self.schedule.add(a)
            #     pos = (0, 0)
            #     self.grid.place_agent(a, pos)
                
            # Goes through each character in the map file and creates the corresponding agent.
            for r, row in enumerate(lines):
                for c, col in enumerate(row):
                    if col in ["v", "^", ">", "<", "1", "2", "3", "4"]:
                        agent = Road(f"r_{r*self.width+c}", self, dataDictionary[col])
                        self.grid.place_agent(agent, (c, self.height - r - 1))

                    elif col in ["R", "r", "L", "l", "U", "u", "D", "d"]:
                        change_frequency = 15 if col in ["R", "L", "U", "D"] else 7
                        agent = Traffic_Light(f"tl_{r*self.width+c}", self, False if col in ["R", "L", "U", "D"] else True, dataDictionary[col], change_frequency)
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        self.schedule.add(agent)
                        self.traffic_lights.append(agent)

                    elif col == "#":
                        agent = Obstacle(f"ob_{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))

                    elif col == "F":
                        agent = Destination(f"d_{r*self.width+c}", self)
                        self.schedule.add(agent)
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        x, y = agent.pos
                        self.destinations_positions.append((x, y))
                        
                        
            print("Destinations: ", self.destinations_positions)
        
        self.running = True

    def add_car(self):
        # new_agent = Car(self.num_agents + 1000, self)
        # self.num_agents += 1
        # #pos = (0, 0)
        # corner_options = [(0, 0), (0, self.grid.height-1), (self.grid.width-1, 0), (self.grid.width-1, self.grid.height-1)]
        # pos = random.choice(corner_options)
        # self.grid.place_agent(new_agent, pos)
        # self.schedule.add(new_agent)
        for _ in range(4):
            new_agent = Car(self.num_agents + 1000, self)
            self.num_agents += 1

            # Seleccionar una esquina aleatoria
            corner_options = [(0, 0), (0, self.grid.height-1), (self.grid.width-1, 0), (self.grid.width-1, self.grid.height-1)]
            pos = random.choice(corner_options)

            # Verificar si la celda está ocupada, esperar si es necesario
            # while self.grid.is_cell_occupied(pos):
            #     time.sleep(0.1)  # Esperar 0.1 segundos antes de verificar nuevamente
            #     pos = random.choice(corner_options)
            agent_type_to_avoid = Car
            while isinstance(self.grid.get_cell_list_contents(pos)[0], agent_type_to_avoid):
                time.sleep(0.1)  # Esperar 0.1 segundos antes de verificar nuevamente
                pos = random.choice(corner_options)

            # Colocar el nuevo agente en la celda
            self.grid.place_agent(new_agent, pos)
            self.schedule.add(new_agent)

    def step(self):
        '''Advance the model by one step.'''
        # Añade un nuevo carro cada 4 pasos
        if self.schedule.steps % 5 == 0:
            if self.num_agents <=3000:
                self.add_car()
            else: 
                pass

        self.schedule.step()
