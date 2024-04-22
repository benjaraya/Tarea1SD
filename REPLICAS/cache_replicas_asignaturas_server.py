import grpc
import time
import json
import cache_replicas_pb2 as pb2
import cache_replicas_pb2_grpc as pb2_grpc
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Datos de las asignaturas y salas
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

class CacheServicer(pb2_grpc.CacheServiceServicer):
    def __init__(self):
        self.cache = {}
        self.replicas = []  # Lista de réplicas

    def Get(self, request, context):
        key = request.key
        if key in self.cache:
            return pb2.GetResponse(value=self.cache[key])
        else:
            return pb2.GetResponse(value="Key not found")

    def Put(self, request, context):
        key = request.key
        value = request.value
        self.cache[key] = value
        print("Data stored in cache:")
        for k, v in self.cache.items():
            print(f"{k}: {v}")
        return pb2.PutResponse(message="Data stored successfully")

    def Sync(self, request, context):
        # Sincronizar datos con las réplicas
        for replica in request.replica_list:
            channel = grpc.insecure_channel(f"{replica.address}:{replica.port}")
            stub = pb2_grpc.CacheServiceStub(channel)
            try:
                response = stub.Sync(pb2.SyncRequest(replica_list=[]))
                print(f"Syncing with replica {replica.address}:{replica.port}: {response.message}")
            except grpc.RpcError as e:
                print(f"Error syncing with replica {replica.address}:{replica.port}: {e}")

        return pb2.SyncResponse(message="Syncing completed")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CacheServiceServicer_to_server(CacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Cache Server with Replicas and Asignaturas running on port 50051...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
