export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"

kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- sh -c "curl -s $VIP_FLEET/todos"
