export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"

kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- curl -i http://ta-server-service.sharedvpc:8080/todos

