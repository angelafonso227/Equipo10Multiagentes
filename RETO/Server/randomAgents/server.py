# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python flask server to interact with Unity. Based on the code provided by Sergio Ruiz.
# Octavio Navarro. October 2023git 

from flask import Flask, request, jsonify
# from randomAgents.model import RandomModel
from randomAgents.model2 import CityModel
# from randomAgents.agent import RandomAgent, ObstacleAgent
from randomAgents.agent2 import Car, Road, Traffic_Light, Destination, Spawn, Obstacle


app = Flask("Traffic example")

@app.route('/init', methods=['POST'])
def initModel():
    global currentStep, cityModel

    if request.method == 'POST':
        # number_agents = int(request.form.get('NAgents'))
        # width = int(request.form.get('width'))
        # height = int(request.form.get('height'))
        currentStep = 0

        print(request.form)
        # print(number_agents, width, height)
        cityModel = CityModel()

        return jsonify({"message":"Parameters recieved, model initiated."})

@app.route('/getAgents', methods=['GET'])
def getAgents():
    global cityModel

    if request.method == 'GET':
        # for a in cityModel.grid.coord_iter():
        #     print(a)
        agentPositions = [{"id": str(agent.unique_id), "x": pos[0], "y":0, "z":pos[1]} 
                          for agents, pos in cityModel.grid.coord_iter() 
                          for agent in agents
                          if isinstance(agent, Car)]

        return jsonify({'positions':agentPositions})

@app.route('/getObstacles', methods=['GET'])
def getObstacles():
    global cityModel

    if request.method == 'GET':
        obstaclePositions = [{"id": str(agent.unique_id), "x": pos[0], "y":0, "z":pos[1]} 
                          for agents, pos in cityModel.grid.coord_iter() 
                          for agent in agents
                          if isinstance(agent, Obstacle)]
        
        return jsonify({'positions':obstaclePositions})

@app.route('/getRoads', methods=['GET'])
def getRoads():
    global cityModel

    if request.method == 'GET':
        roadPositions = [{"id": str(agent.unique_id), "x": pos[0], "y":0, "z":pos[1]} 
                          for agents, pos in cityModel.grid.coord_iter() 
                          for agent in agents
                          if isinstance(agent, Road)]

        return jsonify({'positions':roadPositions})

@app.route('/getTrafficLights', methods=['GET'])
def getTrafficLights():
    global cityModel

    if request.method == 'GET':
        trafficLightPositions = [{"id": str(agent.unique_id), "x": pos[0], "y":0, "z":pos[1]} 
                                for agents, pos in cityModel.grid.coord_iter() 
                                for agent in agents
                                if isinstance(agent, Traffic_Light)]

        return jsonify({'positions':trafficLightPositions})

@app.route('/getDestinations', methods=['GET'])
def getDestinations():
    global cityModel

    if request.method == 'GET':
        destinationPositions = [{"id": str(agent.unique_id), "x": pos[0], "y":0, "z":pos[1]} 
                                for agents, pos in cityModel.grid.coord_iter() 
                                for agent in agents
                                if isinstance(agent, Destination)]

        return jsonify({'positions':destinationPositions})

@app.route('/getSpawns', methods=['GET'])
def getSpawns():
    global cityModel

    if request.method == 'GET':
        spawnPositions = [{"id": str(agent.unique_id), "x": pos[0], "y":0, "z":pos[1]} 
                          for agents, pos in cityModel.grid.coord_iter() 
                          for agent in agents
                          if isinstance(agent, Spawn)]

        return jsonify({'positions':spawnPositions})

@app.route('/update', methods=['GET'])
def updateModel():
    global currentStep, cityModel
    if request.method == 'GET':
        cityModel.step()
        currentStep += 1
        return jsonify({'message':f'Model updated to step {currentStep}.', 'currentStep':currentStep})

if _name=='__main_':
    app.run(host="localhost", port=8585, debug=True)