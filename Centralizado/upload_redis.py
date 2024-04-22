import json
import redis

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Datos a subir
data = [
    {"Asignatura": "Matemáticas", "Sala": "A101"},
    {"Asignatura": "Física", "Sala": "A102"},
    {"Asignatura": "Química", "Sala": "A103"},
    {"Asignatura": "Biología", "Sala": "A104"},
    {"Asignatura": "Literatura", "Sala": "A105"},
    {"Asignatura": "Historia", "Sala": "A101"},
    {"Asignatura": "Geografía", "Sala": "A102"},
    {"Asignatura": "Economía", "Sala": "A103"},
    {"Asignatura": "Arte", "Sala": "A104"},
    {"Asignatura": "Música", "Sala": "A105"}
]

# Convertir a formato JSON
json_data = json.dumps(data)

# Subir a Redis
for item in data:
    asignatura = item["Asignatura"]
    sala = item["Sala"]
    r.set(asignatura, sala)

print("Datos subidos a Redis.")
