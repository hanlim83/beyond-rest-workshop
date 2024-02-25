import grpc
from concurrent import futures
import ms1_pb2 as ms1_pb2
import ms1_pb2_grpc as ms1_pb2_grpc

class CommunicationServicer(ms1_pb2_grpc.CommunicationServiceServicer):
    def SendMessage(self, request, context):
        return ms1_pb2.MessageResponse(message=f"Server received: {request.message}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ms1_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()