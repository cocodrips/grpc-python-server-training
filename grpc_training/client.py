
import sys
import pathlib
import grpc

root = pathlib.Path(__name__).parent.resolve()
sys.path.insert(0, str(root / '../proto_python'))

import hello_pb2, hello_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='nyan'))
    print('message', response.message)


if __name__ == '__main__':
    run()
