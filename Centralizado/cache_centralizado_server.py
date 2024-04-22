import grpc
from concurrent import futures
import time
import sqlite3
import cache_centralizado_pb2 as pb2
import cache_centralizado_pb2_grpc as pb2_grpc  # Importa pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class CacheServicer(pb2_grpc.CacheServiceServicer):
    def _init_(self):
        self.cache = {}

    def Get(self, request, context):
        key = request.key
        if key in self.cache:
            return pb2.GetResponse(value=self.cache[key])
        else:
            return pb2.GetResponse(value="Key not found")

    def Put(self, request, context):
        self.cache[request.key] = request.value
        print("Data stored in cache:")
        for key, value in self.cache.items():
            print(f"{key}: {value}")
        return pb2.PutResponse(message="Data stored successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CacheServiceServicer_to_server(CacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Cache Server (Centralizado) running on port 50051...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '_main_':
    serve()