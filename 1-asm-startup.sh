kubectl create ns sharedvpc
kubens sharedvpc
kubectl label namespace sharedvpc \
    istio-injection- istio.io/rev=asm-managed --overwrite

kubectl apply -f redis.yaml
kubectl apply -f server.yaml
kubectl apply -f client.yaml

