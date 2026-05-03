
# 🚢 RMPC-ctr

**Modelo de Flujo Máximo para Logística Portuaria en México**

## 📌 Descripción

Este proyecto implementa un modelo de **flujo máximo** aplicado a la logística de contenedores desde el **Puerto de Manzanillo** hacia centros de distribución estratégicos en México.

El objetivo es **maximizar el flujo de contenedores (TEU/día)** a través de una red multimodal (carretera + ferroviaria), respetando las capacidades reales de infraestructura y detectando **cuellos de botella operativos**. 

---

## 🧠 Problema

Se modela una red logística donde:

* **Origen (S):** Puerto de Manzanillo
* **Destino (T):** Super sumidero (demanda total)
* **Nodos intermedios:** patios, terminales, nodos carreteros/ferroviarios
* **Destinos reales:**

  * Guadalajara
  * León
  * Querétaro
  * CDMX

El problema consiste en resolver un modelo de **máximo flujo en redes dirigidas con capacidad**. 

---

## ⚙️ Tecnologías utilizadas

* **Python 3**
* **NetworkX** (algoritmos de grafos)
* Algoritmo: **Edmonds-Karp (Ford-Fulkerson)** 

---

## 📦 Instalación

```bash
pip install networkx
```

O:

```bash
python -m pip install networkx
```

---

## ▶️ Uso

Ejecuta el script:

```bash
python script_PIA_2019712.py
```

---

## 📊 Modelo Matemático

### Variables

* ( X_{i,j} ): flujo de contenedores (TEU/día) en el arco ( (i,j) )

### Función objetivo

Maximizar el flujo total desde el puerto:

[
\max Z = \sum x_{S,j}
]

### Restricciones

1. **Capacidad:**
   [
   0 \leq X_{i,j} \leq C_{i,j}
   ]

2. **Conservación de flujo:**
   [
   \sum X_{i,k} = \sum X_{k,j}
   ]



---

## 🌐 Estructura del grafo

La red incluye:

* Transporte **portuario**
* Transporte **carretero**
* Transporte **ferroviario**
* Centros de distribución (DCs)

Ejemplo de arcos:

```python
("S", "PP", 12000)
("PP", "TC", 8000)
("PP", "TF", 4000)
...
("DCG", "T", 4000)
```
---

## 📚 Referencias

* ASIPONA Manzanillo
* SICT (Secretaría de Infraestructura, Comunicaciones y Transportes)
* Datos logísticos 2025–2026
---

## 👨‍💻 Autor

**Guillermo Bautista Hernández**
Facultad de Ciencias Físico Matemáticas – UANL
