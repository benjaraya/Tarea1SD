import grpc
import time
import cache_particionamiento_pb2 as pb2
import cache_particionamiento_pb2_grpc as pb2_grpc
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class CacheServicer(pb2_grpc.CacheServiceServicer):
    def _init_(self):
        # Crear un diccionario de cachés para cada partición
        self.partitions = {}

    def Get(self, request, context):
        partition_key = request.key[0].upper()  # Tomar la primera letra como clave de partición
        key = request.key

        # Verificar si la partición existe en el diccionario de cachés
        if partition_key in self.partitions:
            partition_cache = self.partitions[partition_key]

            if key in partition_cache:
                return pb2.GetResponse(value=partition_cache[key])
            else:
                return pb2.GetResponse(value="Key not found")
        else:
            return pb2.GetResponse(value="Partition not found")

    def Put(self, request, context):
        partition_key = request.key[0].upper()  # Tomar la primera letra como clave de partición
        key = request.key
        value = request.value

        # Verificar si la partición existe en el diccionario de cachés
        if partition_key in self.partitions:
            partition_cache = self.partitions[partition_key]
            partition_cache[key] = value
            print(f"Data stored in cache ({partition_key}):")
            for k, v in partition_cache.items():
                print(f"{k}: {v}")
            return pb2.PutResponse(message="Data stored successfully")
        else:
            return pb2.PutResponse(message="Partition not found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CacheServiceServicer_to_server(CacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Cache Server (Particionamiento) running on port 50051...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '_main_':
    serve()