import grpc
import cache_centralizado_pb2 as pb2
import cache_centralizado_pb2_grpc as pb2_grpc
import time  # Importa time para medir el tiempo

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.CacheServiceStub(channel)

    # Recorrer la data de asignaturas y salas
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

    for item in data:
        asignatura = item["Asignatura"]
        sala = item["Sala"]

        # PUT Example
        start_time = time.time()  # Tiempo de inicio PUT
        response = stub.Put(pb2.PutRequest(key=asignatura, value=sala))
        end_time = time.time()    # Tiempo de fin PUT
        print(f"PUT {asignatura}: {response.message}, Tiempo: {end_time - start_time:.4f} segundos")

        # GET Example
        start_time = time.time()  # Tiempo de inicio GET
        response = stub.Get(pb2.GetRequest(key=asignatura))
        end_time = time.time()    # Tiempo de fin GET
        print(f"GET {asignatura}: {response.value}, Tiempo: {end_time - start_time:.4f} segundos")

if _name_ == '_main_':
    run()
    