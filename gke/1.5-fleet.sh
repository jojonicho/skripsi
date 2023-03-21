gcloud container clusters update $CLUSTER_NAME \
    --zone=$ZONE \
    --workload-pool=$PROJECT_ID.svc.id.goog

gcloud container fleet memberships register $CLUSTER_NAME \
   --gke-cluster $ZONE/$CLUSTER_NAME \
   --enable-workload-identity \
   --project $PROJECT_ID

