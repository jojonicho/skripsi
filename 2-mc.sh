# only execute on config cluster
kubectl apply -f mci.yaml
kubectl apply -f mcs.yaml
kubectl describe mci ta-server-ingress
