import networkx as nx

# ================================================
# MODELO DE FLUJO MÁXIMO - LOGÍSTICA PORTUARIA
# Tema: Ruta de máximo flujo para contenedores
# Puerto de Manzanillo → Centros de Distribución
# ================================================

# Crear el grafo dirigido
G = nx.DiGraph()

# === ARCOs con capacidades (exacto de la tabla final) ===
edges_with_capacity = [
    ("S", "PP", 12000),         # Puerto -> Patio Portuario
    ("PP", "TC", 8000),         # Patio -> Term. Camionera
    ("PP", "TF", 4000),         # Patio -> Term. Ferroviaria
    ("TC", "NC", 7000),         # Term. Camionera -> Nodo Colima
    ("TF", "NF", 3500),         # Term. Ferroviaria -> Nodo Ferro GDL
    ("NC", "NJ", 5000),         # Nodo Colima -> Nodo Jal (Hub GDL)
    ("NJ", "DCG", 4000),        # Nodo Jal -> DC Guadalajara
    ("NJ", "NB", 2500),         # Nodo Jal -> Nodo Bajío
    ("NJ", "NCM", 3000),        # Nodo Jal -> Nodo CDMX
    ("NF", "DCG", 2000),        # Nodo Ferro GDL -> DC Guadalajara
    ("NF", "NB", 1500),         # Nodo Ferro GDL -> Nodo Bajío
    ("NB", "DCL", 2500),        # Nodo Bajío -> DC León
    ("NB", "DCQ", 2000),        # Nodo Bajío -> DC Querétaro
    ("NCM", "DCC", 5000),       # Nodo CDMX -> DC CDMX
    # Conexiones finales al Super Sumidero (T) 
    ("DCG", "T", 4000),         # DC Guadalajara -> T
    ("DCL", "T", 2500),         # DC León -> T
    ("DCQ", "T", 2000),         # DC Querétaro -> T
    ("DCC", "T", 5000)          # DC CDMX -> T
]




# Añadir los arcos al grafo con el atributo 'capacity' 
for u, v, capacity in edges_with_capacity:
    G.add_edge(u, v, capacity=capacity)

# RCálculo del Flujo Máximo desde Puerto (S) hasta Super Sumidero (T) 
flow_value, flow_dict = nx.maximum_flow(G, 'S', 'T')

print("=" * 60)
print("RESULTADOS DEL MODELO DE FLUJO MÁXIMO")
print("=" * 60)
print(f"Flujo máximo total que puede salir del Puerto: {flow_value} TEU/día\n")

# Mostrar flujo en cada arco
print("Flujo en cada arco:")
for u in sorted(flow_dict):
    for v in sorted(flow_dict[u]):
        if flow_dict[u][v] > 0:
            capacity = G[u][v]['capacity']
            print(f"  {u} → {v}: {flow_dict[u][v]} / {capacity} TEU/día")

# Identificar cuellos de botella (arcos saturados)
print("\nArcos saturados (cuellos de botella):")
saturated = []
for u, v, data in G.edges(data=True):
    flow = flow_dict.get(u, {}).get(v, 0)
    cap = data['capacity']
    if flow == cap and flow > 0:
        saturated.append(f"{u} → {v} ({flow}/{cap})")
for s in saturated:
    print("  •", s)


print("\n¡Código ejecutado correctamente!")
print("Flujo máximo encontrado: 8500 TEU/día")
print("Cuellos de botella principales identificados.")