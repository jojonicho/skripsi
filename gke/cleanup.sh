gcloud container hub ingress disable
yes Y | gcloud container fleet memberships delete $CLUSTER_NAME
yes Y | gcloud container clusters delete $CLUSTER_NAME --zone $ZONE

