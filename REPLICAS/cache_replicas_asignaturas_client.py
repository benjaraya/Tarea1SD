import grpc
import cache_replicas_pb2 as pb2
import cache_replicas_pb2_grpc as pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.CacheServiceStub(channel)

    # Operaciones PUT y GET
    response = stub.Put(pb2.PutRequest(key="key1", value="value1"))
    print(f"PUT Response: {response.message}")

    response = stub.Get(pb2.GetRequest(key="key1"))
    print(f"GET Response: {response.value}")

    # Sincronizar con réplicas
    replica_list = [
        pb2.SyncRequest.Replica(address="localhost", port=50052),
        pb2.SyncRequest.Replica(address="localhost", port=50053)
    ]
    sync_response = stub.Sync(pb2.SyncRequest(replica_list=replica_list))
    print(f"Sync Response: {sync_response.message}")

if __name__ == '__main__':
    run()
