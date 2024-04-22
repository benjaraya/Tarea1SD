import grpc
import cache_particionamiento_pb2 as pb2
import cache_particionamiento_pb2_grpc as pb2_grpc

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
        partition_key = asignatura[0].upper()  # Obtener la primera letra como clave de partición

        # PUT Example
        response = stub.Put(pb2.PutRequest(key=asignatura, value=sala))
        print(f"PUT {asignatura}: {response.message}")

        # GET Example
        response = stub.Get(pb2.GetRequest(key=asignatura))
        print(f"GET {asignatura}: {response.value}")

        # Utilizar la partición para PUT y GET
        partition_response = stub.Get(pb2.GetRequest(key=partition_key))
        print(f"GET Partition {partition_key}: {partition_response.value}")

    print("Finished")

if __name__ == '_main_':
    run()