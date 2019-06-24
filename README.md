## setup
`pip install -r requirements.txt`

## Generate gRPC code
```
$  python -m grpc_tools.protoc -Iproto --python_out=grpc_training/proto --grpc_python_out=grpc_training/proto proto/hello.proto 
```