load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "client",
    srcs = ["client.py"],
    deps = [
        "//service/proto:service_py_pb2_grpc",
    ],
)
