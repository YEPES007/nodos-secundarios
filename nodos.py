from pymongo import MongoClient

# Conexión al Replica Set
client = MongoClient("mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0")
db = client["torneo_futbol"]

from pymongo import MongoClient

# Conexión al Replica Set
client = MongoClient("mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0")
db = client["torneo_futbol"]

# Colecciones
participantes = db["Participantes"]
equipos = db["Equipos"]
encuentros = db["Encuentros"]
resultados = db["Resultados"]
tabla_posiciones = db["TablaPosiciones"]

# Limpiar colecciones antes de insertar nuevos datos (opcional)
participantes.delete_many({})
equipos.delete_many({})
encuentros.delete_many({})
resultados.delete_many({})
tabla_posiciones.delete_many({})

# Insertar documentos en Participantes
participantes.insert_many([
    {
        "_id": "p1",
        "nombre": "Lionel Messi",
        "edad": 36,
        "rol": "jugador",
        "equipo": "Inter Miami",
        "posicion": "Delantero",
        "goles": 10,
        "asistencias": 5
    },
    {
        "_id": "p2",
        "nombre": "Gerardo Martino",
        "edad": 60,
        "rol": "entrenador",
        "equipo": "Inter Miami",
        "experiencia": 20
    },
    {
        "_id": "p3",
        "nombre": "Carlos López",
        "edad": 42,
        "rol": "árbitro",
        "experiencia": 15,
        "licencia": "FIFA"
    }
])

# Insertar documentos en Equipos
equipos.insert_many([
    {
        "_id": "e1",
        "nombre": "Inter Miami",
        "ciudad": "Miami",
        "entrenador": "p2",
        "jugadores": ["p1"],
        "puntos": 15,
        "goles_a_favor": 25,
        "goles_en_contra": 18
    },
    {
        "_id": "e2",
        "nombre": "Los Angeles FC",
        "ciudad": "Los Angeles",
        "entrenador": "p4",
        "jugadores": ["p5"],
        "puntos": 20,
        "goles_a_favor": 30,
        "goles_en_contra": 15
    }
])

# Insertar documento en Encuentros
encuentros.insert_one({
    "_id": "m1",
    "fecha": "2024-11-15",
    "equipo_local": "e1",
    "equipo_visitante": "e2",
    "resultado": {
        "goles_local": 2,
        "goles_visitante": 1
    },
    "arbitro": "p3",
    "estado": "finalizado"
})

# Consultar los documentos para verificar
print("Jugadores en la base de datos:")
for jugador in participantes.find({"rol": "jugador"}):
    print(jugador)

print("\nEncuentros programados:")
for encuentro in encuentros.find():
    print(encuentro)

# Actualizar puntos de un equipo tras un partido
equipos.update_one(
    {"_id": "e1"},
    {"$inc": {"puntos": 3}}  # Incrementa los puntos del equipo local
)

# Consultar tabla de posiciones
print("\nTabla de posiciones:")
for equipo in equipos.find({}, {"nombre": 1, "puntos": 1}):
    print(equipo)
client = MongoClient("mongodb://localhost:27018/?replicaSet=rs0")  # Nodo secundario
db = client["torneo_futbol"]
