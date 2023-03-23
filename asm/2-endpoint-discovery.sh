kubectl create configmap asm-options -n istio-system --from-file <(echo '{"data":{"multicluster_mode":"connected"}}')
