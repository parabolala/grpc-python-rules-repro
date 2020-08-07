import sys
import pprint
pprint.pprint(sys.path)

from repro.service.proto import service_pb2_grpc

print(service_pb2_grpc)
print(dir(service_pb2_grpc))
print(service_pb2_grpc.FooServiceStub)
