export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"

#kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- sh -c "curl -s $VIP_FLEET/todos"

#kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- curl -X POST "$VIP_FLEET/todos" -H 'Content-Type: application/json' -d '{"title": "AUSTRALIA"}'

kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- curl -X POST $VIP_FLEET/todos -H 'Content-Type: application/json' -d "{\"title\": \"$CLUSTER_NAME\"}"

#kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- curl -X POST $VIP_FLEET/todos -H 'Content-Type: application/json' -d '{"title": "'"$CLUSTER_NAME"'"}'
