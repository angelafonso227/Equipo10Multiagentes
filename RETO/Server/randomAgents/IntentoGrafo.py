import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos
for i in range(415, 0, -1):
    G.add_node(str(i))

#Izquierda en x24
for i in range(1, 24):
    G.add_edge(str(i+1), str(i))
#Izquierda en x23
for i in range (25, 48):
    G.add_edge(str(i+1), str(i))
#Derecha en x1
for i in range (95, 137,2):
    G.add_edge(str(i+2), str(i))
#Derecha en x0
for i in range (96, 138,2):
    G.add_edge(str(i+2), str(i))
#Abajo en y1
for i in range (140,180,2):
    G.add_edge(str(i+2), str(i))
#Abajo en y0
for i in range (139,179,2):
    G.add_edge(str(i+2), str(i))
#Arriba y24
for i in range(50, 90, 2):
    G.add_edge(str(i + 2), str(i))
#Arriba y3
for i in range(49,89, 2):
    G.add_edge(str(i + 2), str(i))
#Arriba y10
for i in range(223, 263, 2):
    G.add_edge(str(i + 2), str(i))
#Arriba y9
for i in range(222, 244, 2):
    G.add_edge(str(i + 2), str(i))
#Arriba y9 pt2
for i in range(248, 262, 2):
    G.add_edge(str(i + 2), str(i))
#Abajo y15
for i in range(264, 286, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y15
for i in range (290, 304, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y16
for i in range(265, 287, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y16
for i in range(291, 305, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y6
for i in range(181, 205, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y6 pt2
G.add_edge("205","206")
#Abajo y6 pt3
for i in range(206,220, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y7
for i in range(182, 204, 2):
    G.add_edge(str(i), str(i+2))
#Abajo y7 pt2
for i in range(207, 221, 2):
    G.add_edge(str(i), str(i+2))
#derecha x8
for i in range(362, 368, 2):
    G.add_edge(str(i), str(i+2))
#derecha x8 pt2
for i in range(373, 379, 2):
    G.add_edge(str(i), str(i + 2))
#derecha x8 pt3
for i in range(381, 389, 2):
    G.add_edge(str(i), str(i + 2))
#derecha x9 pt
for i in range(361, 367, 2):
    G.add_edge(str(i), str(i + 2))
#derecha x9 pt2
for i in range(372, 378, 2):
    G.add_edge(str(i), str(i + 2))
#derecha x9 pt2
for i in range(380, 388, 2):
    G.add_edge(str(i), str(i + 2))
#izquierda y11
for i in range(352, 360, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y11 pt2
for i in range(343, 349, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y11 pt3
for i in range(333, 339, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y12
for i in range(351, 359, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y12 pt2
for i in range(342, 348, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y12 pt3
for i in range(332, 338, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y17
for i in range(323, 331, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y17 pt 2
for i in range (315, 321, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y17 pt3
for i in range(307, 313, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y18
for i in range(322, 330, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y18 pt2
for i in range(314, 320, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y18 pt3
for i in range(306,312, 2):
    G.add_edge(str(i+2), str(i))
#izquierda y5
for i in range(390, 394):
    G.add_edge(str(i+1), str(i))
#esquina inferior derecha
G.add_edge("96", "93")
G.add_edge("93", "94")
G.add_edge("94", "92")
G.add_edge("92", "90")
G.add_edge("95", "91")
G.add_edge("91", "89")
G.add_edge("91", "92")
##DESTINOS
G.add_edge("29", "400")
G.add_edge("308", "401")
G.add_edge("166", "402")
G.add_edge("197", "403")
G.add_edge("148", "404")
G.add_edge("216", "405")
G.add_edge("38", "406")
G.add_edge("227", "407")
G.add_edge("239", "408")
G.add_edge("255", "409")
G.add_edge("302", "410")
G.add_edge("53", "411")
G.add_edge("63", "412")
G.add_edge("281", "413")
G.add_edge("385", "414")
G.add_edge("87", "415")
#intersecciones
G.add_edge("2", "26")
G.add_edge("26", "180")
G.add_edge("1", "25")
G.add_edge("25", "179")
G.add_edge("7", "31")
G.add_edge("31", "181")
G.add_edge("8", "32")
G.add_edge("32", "182")
G.add_edge("222", "34")
G.add_edge("34", "10")
G.add_edge("223", "35")
G.add_edge("35", "11")
G.add_edge("16", "40")
G.add_edge("40", "264")
G.add_edge("17", "41")
G.add_edge("41", "265")
G.add_edge("49", "47")
G.add_edge("47", "23")
G.add_edge("50", "48")
G.add_edge("48", "24")
G.add_edge("306", "172")
G.add_edge("307", "170")
G.add_edge("332", "160")
G.add_edge("333", "158")
G.add_edge("154", "361")
G.add_edge("152", "362")
G.add_edge("139", "137")
G.add_edge("137", "138")
G.add_edge("140", "135")
G.add_edge("135", "136")
G.add_edge("220", "125")
G.add_edge("221", "123")
G.add_edge("123", "124")
G.add_edge("120", "119")
G.add_edge("119", "262")
G.add_edge("117", "263")
G.add_edge("304", "107")
G.add_edge("305", "105")
G.add_edge("105", "106")
G.add_edge("390", "299")
G.add_edge("83", "394")
G.add_edge("367", "206")
G.add_edge("206", "207")
G.add_edge("207", "370")
G.add_edge("370", "248")
G.add_edge("248", "249")
G.add_edge("249", "372")
G.add_edge("378", "290")
G.add_edge("290", "291")
G.add_edge("291", "380")
G.add_edge("388", "75")
G.add_edge("152", "362")
G.add_edge("368", "208")
G.add_edge("208", "209")
G.add_edge("209", "371")
G.add_edge("371", "250")
G.add_edge("250", "251")
G.add_edge("251", "373")
G.add_edge("379", "292")
G.add_edge("292", "293")
G.add_edge("293", "381")
G.add_edge("389", "77")
G.add_edge("71", "360")
G.add_edge("352", "287")
G.add_edge("287", "286")
G.add_edge("286", "349")
G.add_edge("343", "245")
G.add_edge("245", "244")
G.add_edge("244", "341")
G.add_edge("341", "204")
G.add_edge("204", "203")
G.add_edge("203", "339")
G.add_edge("69", "359")
G.add_edge("351", "285")
G.add_edge("285", "284")
G.add_edge("284", "348")
G.add_edge("342", "243")
G.add_edge("243", "242")
G.add_edge("242", "340")
G.add_edge("340", "202")
G.add_edge("202", "201")
G.add_edge("201", "338")
G.add_edge("59", "331")
G.add_edge("323", "275")
G.add_edge("275", "274")
G.add_edge("274", "321")
G.add_edge("315", "233")
G.add_edge("191", "313")
G.add_edge("57", "330")
G.add_edge("322", "273")
G.add_edge("273", "272")
G.add_edge("272", "320")
G.add_edge("314", "231")
G.add_edge("189", "312")
G.add_edge("247", "350")
G.add_edge("350", "343")
G.add_edge("372", "350")
G.add_edge("369", "367")
G.add_edge("339", "369")
G.add_edge("369", "205")


# Imprimir las aristas para verificar
# # # print(G.edges())

# # # print(G.nodes())


# Definir los nodos de inicio y fin
inicio = "138"
fin = "405"

# Encontrar el camino más corto usando el algoritmo de Dijkstra
camino_mas_corto = nx.shortest_path(G, source=inicio, target=fin, method='dijkstra')

# Imprimir el resultado
print(f"Camino más corto desde {inicio} a {fin}: {camino_mas_corto}")


# Dibujar el grafo
pos = nx.spring_layout(G)  # Asignar posiciones a los nodos
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=5)

# Mostrar el grafo
plt.show()