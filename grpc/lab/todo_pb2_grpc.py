# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todo_pb2 as todo__pb2


class TodoServiceStub(object):
    """Unary RPC RemoveAllTasks has already been implemented for you
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTask = channel.unary_unary(
                '/todo.TodoService/AddTask',
                request_serializer=todo__pb2.TaskRequest.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )
        self.GetTasks = channel.unary_unary(
                '/todo.TodoService/GetTasks',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.TasksList.FromString,
                )
        self.RemoveAllTasks = channel.unary_unary(
                '/todo.TodoService/RemoveAllTasks',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.TasksList.FromString,
                )
        self.GetTaskHistory = channel.unary_stream(
                '/todo.TodoService/GetTaskHistory',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )
        self.AddMultipleTasks = channel.stream_unary(
                '/todo.TodoService/AddMultipleTasks',
                request_serializer=todo__pb2.TaskRequest.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )


class TodoServiceServicer(object):
    """Unary RPC RemoveAllTasks has already been implemented for you
    """

    def AddTask(self, request, context):
        """1. Implement Unary RPC AddTask that sends a single TaskRequest from client and server returns single TaskResponse
        TODO
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTasks(self, request, context):
        """2. Implement Unary RPC GetTasks that does not require input from client and server returns single TaskList 
        TODO
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveAllTasks(self, request, context):
        """3. Implement Unary RPC RemoveAllTasks that deletes all the task and return an empty Tasklist
        TODO
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskHistory(self, request, context):
        """4. Implement Server streaming RPC GetTaskHistory that does not require input from client 
        and server returns a stream of TaskResponse 
        TODO
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMultipleTasks(self, request_iterator, context):
        """5. Implement Client streaming RPC AddMultipleTasks that sends a stream of TaskReqyest from client
        and server returns a single TaskResponse 
        TODO
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=todo__pb2.TaskRequest.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
            'GetTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTasks,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.TasksList.SerializeToString,
            ),
            'RemoveAllTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveAllTasks,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.TasksList.SerializeToString,
            ),
            'GetTaskHistory': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTaskHistory,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
            'AddMultipleTasks': grpc.stream_unary_rpc_method_handler(
                    servicer.AddMultipleTasks,
                    request_deserializer=todo__pb2.TaskRequest.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Unary RPC RemoveAllTasks has already been implemented for you
    """

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/AddTask',
            todo__pb2.TaskRequest.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/GetTasks',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveAllTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/RemoveAllTasks',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/todo.TodoService/GetTaskHistory',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMultipleTasks(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/todo.TodoService/AddMultipleTasks',
            todo__pb2.TaskRequest.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
