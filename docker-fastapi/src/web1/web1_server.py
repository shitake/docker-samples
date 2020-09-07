from concurrent import futures
import logging

import grpc

import web1_pb2
import web1_pb2_grpc


class Web1Servicer(web1_pb2_grpc.Web1Servicer):

    def SayHello(self, request, context):
        return web1_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return web1_pb2.HelloReply(message='Hello again, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    web1_pb2_grpc.add_Web1Servicer_to_server(Web1Servicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()