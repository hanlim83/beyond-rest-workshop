# python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ms1.proto

from flask import Flask, request, jsonify
import grpc
import ms1_pb2
import ms1_pb2_grpc

app = Flask(__name__)
channel = grpc.insecure_channel('localhost:50051')
stub = ms1_pb2_grpc.CommunicationServiceStub(channel)

@app.route('/send_message', methods=['POST'])
def send_message():
    request_data = request.json
    message = request_data.get('message')
    if message:
        grpc_response = stub.SendMessage(ms1_pb2.MessageRequest(message=message))
        return jsonify({'response': grpc_response.message})
    else:
        return jsonify({'error': 'Message not provided'}), 400

if __name__ == '__main__':
    app.run(port='5000', debug=True)

