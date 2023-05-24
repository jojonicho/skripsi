cat <<EOF | kubectl apply -f -
apiVersion: v1
data:
  mesh: |-
    accessLogFile: /dev/stdout
kind: ConfigMap
metadata:
  name: istio-asm-managed
  namespace: istio-system
EOF

kubectl get configmap istio-asm-managed -n istio-system -o yaml

