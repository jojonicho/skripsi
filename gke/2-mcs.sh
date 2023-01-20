gcloud container clusters update $CLUSTER_NAME \
    --zone=$ZONE \
    --workload-pool=$PROJECT_ID.svc.id.goog

gcloud services enable \
    multiclusterservicediscovery.googleapis.com \
    gkehub.googleapis.com \
    cloudresourcemanager.googleapis.com \
    trafficdirector.googleapis.com \
    dns.googleapis.com \
    --project=$PROJECT_ID

gcloud container hub multi-cluster-services enable \
    --project $PROJECT_ID

gcloud container fleet memberships register $CLUSTER_NAME \
   --gke-cluster $ZONE/$CLUSTER_NAME \
   --enable-workload-identity \
   --project $PROJECT_ID

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member "serviceAccount:$PROJECT_ID.svc.id.goog[gke-mcs/gke-mcs-importer]" \
    --role "roles/compute.networkViewer"
