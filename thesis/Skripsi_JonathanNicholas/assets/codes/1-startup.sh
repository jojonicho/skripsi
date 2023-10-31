kubectl create ns sharedvpc
kubens sharedvpc
kubectl apply -f redis.yaml
kubectl apply -f server.yaml -l mcs=mcs
kubectl apply -f client.yaml

