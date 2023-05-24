export CLIENT_ZONE_ASIA="$(kubectl get pods | grep -o 'ta-client-deployment-\w*-\w*\b')"
#kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- sh -c "curl -s $VIP_FLEET/todos"

#echo "GET http://$VIP_FLEET/todos" | vegeta attack -name=10rps -rate=10 -duration=5s > results.10rps.bin

#vegeta report -type=text results.10rps.bin

# TODO do this for 10 50 100
# create list of 10 50 100


RPS_LIST=(10 50 100)
OUTPUT_DIR=$1
mkdir $OUTPUT_DIR

for RPS in "${RPS_LIST[@]}"
do
  sleep 20
  # attack
  
  #echo "GET http://$VIP_FLEET/todos" | vegeta attack -name=${RPS}rps -rate=$RPS -duration=5s > ${OUTPUT_DIR}/results.${RPS}rps.bin

  # generate report
  #vegeta report -type=text ${OUTPUT_DIR}/results.${RPS}rps.bin

  #kubectl run vegeta --rm --attach --restart=Never --image="peterevans/vegeta" -- sh -c \
  #"echo 'GET http://$VIP_FLEET/todos' | vegeta attack -name=${RPS}rps -rate=$RPS -duration=5s | cat results.${RPS}rps.bin" > ${OUTPUT_DIR}/results.${RPS}rps.bin
  kubectl run vegeta --attach --restart=Never --image="peterevans/vegeta" -- sh -c \
    "echo 'GET http://$VIP_FLEET/todos' | vegeta attack -rate=$RPS -duration=5s -output=ha.bin && cat ha.bin" > ${OUTPUT_DIR}/results.${RPS}rps.bin

  vegeta report -type=text ${OUTPUT_DIR}/results.${RPS}rps.bin
  vegeta report -type=json $OUTPUT_DIR/results.${RPS}rps.bin > $OUTPUT_DIR/${RPS}.json

  kubectl delete pod vegeta

done
