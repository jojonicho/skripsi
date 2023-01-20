export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"
kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- sh -c 'curl  http://ta-server-service:8000/todos'
