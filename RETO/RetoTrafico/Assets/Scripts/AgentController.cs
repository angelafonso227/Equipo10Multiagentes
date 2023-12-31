﻿// TC2008B. Sistemas Multiagentes y Gráficas Computacionales
// C# client to interact with Python. Based on the code provided by Sergio Ruiz.
// Octavio Navarro. October 2023

using System;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Networking;

[Serializable]
public class AgentData
{
    /*
    The AgentData class is used to store the data of each agent.
    
    Attributes:
        id (string): The id of the agent.
        x (float): The x coordinate of the agent.
        y (float): The y coordinate of the agent.
        z (float): The z coordinate of the agent.
    */
    public string id;
    public float x, y, z;
    public bool eliminado;
    public bool estado;

    public AgentData(string id, float x, float y, float z, bool eliminado)
    {
        this.id = id;
        this.x = x;
        this.y = y;
        this.z = z;
        this.eliminado= eliminado;
        this.estado = estado;
    }
}
[Serializable]

public class AgentsData
{
    public List<AgentData> positions;
    public List<AgentData> estado;
    public List<AgentData> eliminado;

    public AgentsData()
    {
        this.positions = new List<AgentData>();
        this.estado = new List<AgentData>();
        this.eliminado = new List<AgentData>();
    }
}
public class AgentController : MonoBehaviour
{
    /*
    The AgentController class is used to control the agents in the simulation.

    Attributes:
        serverUrl (string): The url of the server.
        getAgentsEndpoint (string): The endpoint to get the agents data.
        getObstaclesEndpoint (string): The endpoint to get the obstacles data.
        sendConfigEndpoint (string): The endpoint to send the configuration.
        updateEndpoint (string): The endpoint to update the simulation.
        agentsData (AgentsData): The data of the agents.
        obstacleData (AgentsData): The data of the obstacles.
        agents (Dictionary<string, GameObject>): A dictionary of the agents.
        prevPositions (Dictionary<string, Vector3>): A dictionary of the previous positions of the agents.
        currPositions (Dictionary<string, Vector3>): A dictionary of the current positions of the agents.
        updated (bool): A boolean to know if the simulation has been updated.
        started (bool): A boolean to know if the simulation has started.
        agentPrefab (GameObject): The prefab of the agents.
        obstaclePrefab (GameObject): The prefab of the obstacles.
        floor (GameObject): The floor of the simulation.
        NAgents (int): The number of agents.
        width (int): The width of the simulation.
        height (int): The height of the simulation.
        timeToUpdate (float): The time to update the simulation.
        timer (float): The timer to update the simulation.
        dt (float): The delta time.
    */
    string serverUrl = "http://localhost:8585";
    string getAgentsEndpoint = "/getAgents";
    string getObstaclesEndpoint = "/getObstacles";
    string sendConfigEndpoint = "/init";
    string updateEndpoint = "/update";
    string getRoadsEndpoint = "/getRoads";
    string getTrafficLightsEndpoint = "/getTrafficLights";
    string getDestinationsEndpoint = "/getDestinations";
    AgentsData agentsData, obstacleData, lightData;
    Dictionary<string, GameObject> agents;
    Dictionary<string, Vector3> prevPositions, currPositions;
    Dictionary<string, GameObject> wheels = new Dictionary<string, GameObject>();
    List<GameObject> lucesList = new List<GameObject>();


    bool updated = false, started = false;

    public GameObject agentPrefab, obstaclePrefab, floor, wheelPrefab, lightPrefab;

    public int NAgents, width, height;
    public float timeToUpdate = 5.0f;
    private float timer, dt;

    void Start()
    {
        agentsData = new AgentsData();
        obstacleData = new AgentsData();
        lightData = new AgentsData();

        prevPositions = new Dictionary<string, Vector3>();
        currPositions = new Dictionary<string, Vector3>();

        agents = new Dictionary<string, GameObject>();

        floor.transform.localScale = new Vector3((float)width / 10, 1, (float)height / 10);
        floor.transform.localPosition = new Vector3((float)width / 2 - 0.5f, 0, (float)height / 2 - 0.5f);

        timer = timeToUpdate;

        // Launches a couroutine to send the configuration to the server.
        StartCoroutine(SendConfiguration());
    }

    private void Update()
    {
        if (timer < 0)
        {
            timer = timeToUpdate;
            updated = false;
            StartCoroutine(UpdateSimulation());
        }

        if (updated)
        {
            timer -= Time.deltaTime;
            dt = 1.0f - (timer / timeToUpdate);

            // Iterates over the agents to update their positions.
            // The positions are interpolated between the previous and current positions.
            foreach (var agent in currPositions)
            {
                Vector3 currentPosition = agent.Value;
                Vector3 previousPosition = prevPositions[agent.Key];

                Vector3 interpolated = Vector3.Lerp(previousPosition, currentPosition, dt);
                Vector3 direction = currentPosition - interpolated;

                agents[agent.Key].transform.localPosition = interpolated;
                if (direction != Vector3.zero) agents[agent.Key].transform.rotation = Quaternion.LookRotation(direction);
            }

            // float t = (timer / timeToUpdate);
            // dt = t * t * ( 3f - 2f*t);
        }
    }
    

    IEnumerator UpdateSimulation()
    {
        UnityWebRequest www = UnityWebRequest.Get(serverUrl + updateEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
            Debug.Log(www.error);
        else
        {
            StartCoroutine(GetAgentsData());
        }
    }

    IEnumerator SendConfiguration()
    {
        /*
        The SendConfiguration method is used to send the configuration to the server.

        It uses a WWWForm to send the data to the server, and then it uses a UnityWebRequest to send the form.
        */
        WWWForm form = new WWWForm();

        form.AddField("NAgents", NAgents.ToString());
        form.AddField("width", width.ToString());
        form.AddField("height", height.ToString());

        UnityWebRequest www = UnityWebRequest.Post(serverUrl + sendConfigEndpoint, form);
        www.SetRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log("Configuration upload complete!");
            Debug.Log("Getting Agents positions");

            // Once the configuration has been sent, it launches a coroutine to get the agents data.
            StartCoroutine(GetAgentsData());
            StartCoroutine(GetObstacleData());
            StartCoroutine(GetTrafficLightData());
        }
    }

    IEnumerator GetAgentsData()
    {
        // The GetAgentsData method is used to get the agents data from the server.

        UnityWebRequest www = UnityWebRequest.Get(serverUrl + getAgentsEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
            Debug.Log(www.error);
        else
        {
            // Once the data has been received, it is stored in the agentsData variable.
            // Then, it iterates over the agentsData.positions list to update the agents positions.
            agentsData = JsonUtility.FromJson<AgentsData>(www.downloadHandler.text);

            foreach (AgentData agent in agentsData.positions)
            {
                Vector3 newAgentPosition = new Vector3(agent.x, agent.y, agent.z);

                if (agent.eliminado)
                {
                    // Destruir el objeto si está marcado como eliminado
                    Destroy(agents[agent.id]);
                    continue; // Saltar a la siguiente iteración del bucle
                }

                if (!prevPositions.ContainsKey(agent.id))
                {
                    prevPositions[agent.id] = newAgentPosition;
                    agents[agent.id] = Instantiate(agentPrefab, newAgentPosition, Quaternion.identity);
                    agents[agent.id].transform.localScale = new Vector3(0.2f, 0.2f, 0.2f);

                    // Instancia de ruedas y las hace hijos del objeto principal
                    GameObject wheel1 = Instantiate(wheelPrefab, newAgentPosition + new Vector3(0.2f, 0.055f, 0.288f), Quaternion.Euler(0, 0, 0));
                    GameObject wheel2 = Instantiate(wheelPrefab, newAgentPosition + new Vector3(0.2f, 0.055f, -0.255f), Quaternion.Euler(0, 0, 0));
                    GameObject wheel3 = Instantiate(wheelPrefab, newAgentPosition + new Vector3(-0.2f, 0.055f, -0.255f), Quaternion.Euler(0, 0, 0));
                    GameObject wheel4 = Instantiate(wheelPrefab, newAgentPosition + new Vector3(-0.2f, 0.055f, 0.288f), Quaternion.Euler(0, 0, 0));

                    wheel1.transform.localScale = new Vector3(0.05f, 0.05f, 0.05f);
                    wheel2.transform.localScale = new Vector3(0.05f, 0.05f, 0.05f);
                    wheel3.transform.localScale = new Vector3(0.05f, 0.05f, 0.05f);
                    wheel4.transform.localScale = new Vector3(0.05f, 0.05f, 0.05f);

                    wheel1.transform.parent = agents[agent.id].transform;
                    wheel2.transform.parent = agents[agent.id].transform;
                    wheel3.transform.parent = agents[agent.id].transform;
                    wheel4.transform.parent = agents[agent.id].transform;
                }
                else
                {
                    Vector3 currentPosition = new Vector3();
                    if (currPositions.TryGetValue(agent.id, out currentPosition))
                        prevPositions[agent.id] = currentPosition;
                    currPositions[agent.id] = newAgentPosition;
                }
            }
            updated = true;
            if (!started) started = true;
        }
    }




void InstantiateWheel(Vector3 position)
{
    GameObject wheel = Instantiate(wheelPrefab, position, Quaternion.Euler(0, -90, 0));
    // Ajusta la escala, posición, rotación o cualquier otra configuración específica que necesites para las ruedas.
}


    IEnumerator GetObstacleData()
    {
        UnityWebRequest www = UnityWebRequest.Get(serverUrl + getObstaclesEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
            Debug.Log(www.error);
        else
        {
            obstacleData = JsonUtility.FromJson<AgentsData>(www.downloadHandler.text);

            Debug.Log(obstacleData.positions);

            foreach (AgentData obstacle in obstacleData.positions)
            {
                Instantiate(obstaclePrefab, new Vector3(obstacle.x, obstacle.y, obstacle.z), Quaternion.identity);
            }
        }
    }

    IEnumerator GetTrafficLightData()
    {
        UnityWebRequest www = UnityWebRequest.Get(serverUrl + getTrafficLightsEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            lightData = JsonUtility.FromJson<AgentsData>(www.downloadHandler.text);

            Debug.Log(lightData.positions);

            foreach (AgentData light in lightData.positions)
            {
                GameObject luces = Instantiate(lightPrefab, new Vector3(light.x, light.y + 1, light.z), Quaternion.identity);
                luces.name = light.id; // Asignar un nombre único a la luz
                lucesList.Add(luces);

                // Supongamos que la luz tiene un componente de tipo Light. Ajusta esto según tu implementación.
                Light luzComponent = luces.GetComponent<Light>();

                if (luzComponent != null)
                {
                    // Asignar color según el estado de la luz
                    if (light.estado)
                    {
                        luzComponent.color = Color.green;
                    }
                    else
                    {
                        luzComponent.color = Color.red;
                    }
                }
                else
                {
                    Debug.LogError("No se encontró el componente Light en el objeto luces.");
                }
            }
        }
    }

    // Método para actualizar el color de la luz después del cambio de estado
    void UpdateLightColor(AgentData light)
    {
        // Supongamos que light.id es el identificador único de la luz
        GameObject luzToUpdate = lucesList.Find(luz => luz.name == light.id);

        if (luzToUpdate != null)
        {
            Light luzComponent = luzToUpdate.GetComponent<Light>();

            if (luzComponent != null)
            {
                // Actualizar color según el nuevo estado de la luz
                if (light.estado)
                {
                    luzComponent.color = Color.green;
                }
                else
                {
                    luzComponent.color = Color.red;
                }
            }
        }
    }

}