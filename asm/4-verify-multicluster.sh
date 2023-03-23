export ASM_VERSION="$(./asmcli --version)"
export SAMPLES_DIR=$CLUSTER_NAME/istio-${ASM_VERSION%+*}
kubectl get controlplanerevision -n istio-system
