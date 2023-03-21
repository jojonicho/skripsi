rm -rf $CLUSTER_NAME
gcloud container hub mesh disable
yes y | gcloud services disable \
  anthos.googleapis.com \
  --project=$PROJECT_ID --force

