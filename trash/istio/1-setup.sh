istioctl install --set profile=demo -y
kubectl create ns sharedvpc
kubens sharedvpc
kubectl label namespace sharedvpc istio-injection=enabled
