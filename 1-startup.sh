kubectl create ns sharedvpc
kubens sharedvpc
kubectl apply -f redis.yaml
kubectl apply -f server.yaml -l service=ta-server
kubectl apply -f client.yaml

