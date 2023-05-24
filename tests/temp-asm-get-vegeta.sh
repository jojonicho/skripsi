export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-vegeta-deployment-\w*-\w*\b')"

#RPS_LIST=(10 50 100)
RPS_LIST=(10)
OUTPUT_DIR=$1
mkdir $OUTPUT_DIR

for RPS in "${RPS_LIST[@]}"
do
  kubectl exec -it $CLIENT_ZONE_ASIA -c ta-vegeta -- "echo 'GET http://ta-server-service.sharedvpc:8080/todos' | vegeta attack -rate=$RPS -duration=5s -output=ha.bin && cat ha.bin" > ${OUTPUT_DIR}/results.${RPS}rps.bin

  #vegeta report -type=text ${OUTPUT_DIR}/results.${RPS}rps.bin
  #vegeta report -type=json $OUTPUT_DIR/results.${RPS}rps.bin > $OUTPUT_DIR/${RPS}.json
done


