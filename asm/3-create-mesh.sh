./asmcli create-mesh \
    $PROJECT_ID \
    [[ ! -z "$KUBECONFIG" ]] && echo "$KUBECONFIG" || echo "$HOME/.kube/config"
