yes Y | gcloud container fleet memberships delete $CLUSTER_NAME
yes T | gcloud container clusters delete $CLUSTER_NAME --zone $ZONE

