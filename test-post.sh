export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"
kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- curl -X POST http://ta-server-service:8000/todos -H 'Content-Type: application/json' -d '{"title": "bob2"}'
