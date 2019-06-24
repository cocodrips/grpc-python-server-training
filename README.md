## setup
`pip install -r requirements.txt`

## Generate gRPC code
```
$ mkdir proto_python
$ python -m grpc_tools.protoc -Iproto --python_out=proto_python --grpc_python_out=proto_python proto/hello.proto 
```

## Test
```bash
$ npm install -g grpcc
# Run server
$ python -m grpc_training.server

# test request
$ grpcc -p proto/hello.proto -a localhost:50051 -i --eval 'client.sayHello({ name: "world" }, printReply)'

# Output
# {
#   "message": "Hello, world"
# }
``` 