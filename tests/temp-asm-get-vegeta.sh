export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-vegeta-deployment-\w*-\w*\b')"

kubectl exec -it $CLIENT_ZONE_ASIA -c ta-vegeta -- "echo 'GET http://ta-server-service.sharedvpc:8080/todos' | vegeta attack -rate=$RPS -duration=5s -output=ha.bin && cat ha.bin" > ${OUTPUT_DIR}/results.${RPS}rps.bin

