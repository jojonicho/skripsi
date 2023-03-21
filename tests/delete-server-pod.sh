export SERVER_POD="$(kubectl get pods | grep -o 'ta-server-deployment-\w*-\w*\b')"
kubectl delete pod $SERVER_POD
