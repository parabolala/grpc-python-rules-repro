load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "client",
    srcs = ["client.py"],
    deps = [
        "//proto:foo_py_pb2",
        "//service/proto:service_py_pb2_grpc",
    ],
)
