"""
TO COMPILE PROTOCOL BUFFERS (PROTOBUF) FILE INTO PYTHON CODE FOR gRPC   

python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. todo.proto

1. -m grpc_tools.protoc => Invokes Protocol Buffers compiler (protoc) using grpc_tools.protoc (Python module) 
2. -I .                 => Specifies dir to search for imported .proto files. (.) indicates search current dir for imports 
3. --python_out=.       => Specifies dir where generated python code should be placed. (.) sets it to curr dir 
4. --grpc_python_out=.  => Specifies dir where generated gRPC python code should be placed. (.) sets to curr dir 
5. todo.proto           => Specific Protocol Buffers file user wants to compile
"""

import grpc
from concurrent import futures
import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServiceServicer):
    def __init__(self, *args, **kwargs):
        self.tasks = []

    def AddTask(self, request, context):
        """
        Adds a task to the list of tasks.

        Args:
            request: The TaskRequest containing the task to be added.
            context: The RPC context.

        Returns:
            TaskResponse: A TaskResponse indicating the success of the operation.
        """
        # 1: Extract the task from the request

        # 2: Add the task to the list of tasks

        # 3: Return a TaskResponse indicating with the message: 'Task "{task}" added successfully.'
        raise NotImplementedError

    def GetTasks(self, request, context):
        """
        Retrieves the list of tasks.

        Args:
            request: An Empty request (no input required).
            context: The RPC context.

        Returns:
            TasksList: A TasksList containing the list of tasks.
        """
        # 1: Return a TasksList containing the list of tasks
        raise NotImplementedError

    def RemoveAllTasks(self, request, context):
        """
        Removes all tasks from the list.

        Args:
            request: An Empty request (no input required).
            context: The RPC context.

        Returns:
            TaskResponse: A TaskResponse indicating the success of the operation.
        """
        # 1: Reinitialise tasks to be an empty list

        # 2: Return a TaskResponse indicating with the message:  'All tasks deleted'

        raise NotImplementedError
    
    def AddMultipleTasks(self, request_iterator, context):
        """
        Adds multiple tasks to the list of tasks.

        Args:
            request_iterator: An iterator over TaskRequest objects containing the tasks to be added.
            context: The RPC context.

        Returns:
            TaskResponse: A TaskResponse indicating the success of the operation.
        """
        added_tasks = []
        
        # 1: Iterate over the request_iterator to extract and add each task
        # HINT: to extract task from request_iterator child, call child.task   

        # 2: Return a TaskResponse indicating with the messsage 'Tasks {added_tasks} added successfully.'
        raise NotImplementedError
    
    def GetTaskHistory(self, request, context):
        """
        Retrieves the history of tasks added.

        Args:
            request: An Empty request (no input required).
            context: The RPC context.

        Returns:
            TaskResponse: A TaskResponse indicating the success of the operation.
        """
        # 1: Iterate over the list of tasks to generate task history messages with index and task
        # HINT 1: You can use enumerate to get index and task simultaneously
        # HINT 2: Try using print, you will encounter an error, think of what other ways
        # python enables you to suspends the function's execution and returns a value to the caller 
        raise NotImplementedError


def serve():
    """
    DO NOT DELETE CODE BELOW
    """   
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started on port 50051...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
