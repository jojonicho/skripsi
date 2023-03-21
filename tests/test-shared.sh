for i in {1..10}
do
  kubectl exec -it $CLIENT_ZONE_ASIA -c ta-client -- sh -c 'curl http://ta-server-service.sharedvpc.svc.clusterset.local:8000/todos'
done
