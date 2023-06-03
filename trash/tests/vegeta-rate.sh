export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"

OUTPUT_DIR=$1
mkdir $OUTPUT_DIR

sleep 20
# attack

kubectl run vegeta --attach --restart=Never --image="peterevans/vegeta" -- sh -c \
  "echo 'GET http://$VIP_FLEET/todos' | vegeta attack -rate=infinity -duration=5s -output=ha.bin && cat ha.bin" > ${OUTPUT_DIR}/results.rps.bin

vegeta report -type=text ${OUTPUT_DIR}/results.rps.bin
kubectl delete pod vegeta

