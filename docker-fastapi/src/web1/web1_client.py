import logging

import grpc

import web1_pb2
import web1_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = web1_pb2_grpc.Web1Stub(channel)
        print('----- SayHello -----')
        response = stub.SayHello(web1_pb2.HelloRequest(name='WEB1'))
        print(response.message)
        print()
        print('----- SayHelloAgain -----')
        response = stub.SayHelloAgain(web1_pb2.HelloRequest(name='WEB1AGAIN'))
        print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()