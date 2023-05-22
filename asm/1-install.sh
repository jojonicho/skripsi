./asmcli install \
--project_id ${PROJECT_ID} \
--cluster_name ${CLUSTER_NAME} \
--cluster_location ${ZONE} \
--fleet_id ${PROJECT_ID} \
--output_dir ${CLUSTER_NAME} \
--enable-all \
--ca mesh_ca

kubectl describe controlplanerevision asm-managed -n istio-system
