gcloud container hub mesh enable --project=$PROJECT_ID

gcloud container hub mesh update \
  --management=automatic \
  --memberships=$CLUSTER_NAME \
  --project=$PROJECT_ID

gcloud container hub mesh describe --project $PROJECT_ID

gcloud services enable \
  anthos.googleapis.com \
  --project=$PROJECT_ID
