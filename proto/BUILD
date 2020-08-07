load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_proto_library")

package(
    default_visibility = ["//visibility:public"],
)

proto_library(
    name = "foo_proto",
    srcs = [
        "foo.proto",
    ],
    #import_prefix = "repro",
)

py_proto_library(
    name = "foo_py_pb2",
    deps = [":foo_proto"],
)
