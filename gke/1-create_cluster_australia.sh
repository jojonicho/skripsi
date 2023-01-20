export PROJECT_ID=`gcloud config get-value project` && \
export M_TYPE=e2-micro && \
export ZONE=australia-southeast1-a && \
export CLUSTER_NAME=${PROJECT_ID}-${RANDOM} && \
gcloud services enable container.googleapis.com && \
gcloud container clusters create $CLUSTER_NAME \
--cluster-version latest \
--machine-type=$M_TYPE \
--num-nodes 4 \
--zone $ZONE \
--workload-pool=$PROJECT_ID.svc.id.goog \
--project $PROJECT_ID

