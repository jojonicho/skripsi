export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"
export VIP_FLEET="$(kubectl describe mci ta-server-ingress | grep -w 'VIP:' | tail -1 | sed 's/VIP:[[:space:]]*//; s/^[[:space:]]*//')"

kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- curl -X POST $VIP_FLEET/todos -H 'Content-Type: application/json' -d "{\"title\": \"$CLUSTER_NAME\"}"

