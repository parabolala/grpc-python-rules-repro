load("@rules_proto//proto:defs.bzl", "proto_library")
load(
    "@com_github_grpc_grpc//bazel:python_rules.bzl",
    "py_grpc_library",
    "py_proto_library",
)

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "service_proto",
    srcs = ["service.proto"],
    deps = ["//proto:foo_proto"],
)

py_proto_library(
    name = "service_py_pb2",
    deps = [
        ":service_proto",
    ],
)

py_grpc_library(
    name = "service_py_pb2_grpc",
    srcs = [
        ":service_proto",
    ],
    deps = [
        ":service_py_pb2",
    ],
)
