# only execute on config cluster
gcloud container hub ingress enable \
  --config-membership=$CLUSTER_NAME
