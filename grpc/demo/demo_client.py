import grpc
import json
import demo_pb2
import demo_pb2_grpc

def sendRequest(stub, message):
    response = stub.GetServerResponse(demo_pb2.Request(message=message))
    print(response.message)

def sendRequestClingy(stub, message):
    responses = stub.GetMultipleServerResponse(demo_pb2.Request(message=message))
    for response in responses:
        print(response.message)

def sendRequestJSON(stub, message):
    response = stub.GetServerResponseJSON(demo_pb2.Request(message=message))
    print(response)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = demo_pb2_grpc.DemoStub(channel)

    sendRequest(stub, "Hello, Server!")
    sendRequestClingy(stub, "Hello, Server!")
    sendRequestJSON(stub, json.dumps({"message": "Hello, Server!"}))

if __name__ == '__main__':
    run()