# Geo-Distributed Clusters with Google Cloud, Kubernetes, and Istio
Multi-National and Multi-Region Kubernetes Architecture for Web Applications with smart Geo-Aware Routing, which routes users to the nearest server.

## Prerequisites
- kubectl
- google cloud platform billing account
- linux machine (for Istio method only)

## Getting Started

### 1. Google Cloud Setup
```
cd gke
./1-create_cluster_australia.sh
./1-create_cluster_e_asia.sh
./1-create_cluster_se_asia.sh
./1.5-fleet.sh
./2-mcs.sh
./3-config-cluster.sh
```
This creates GKE clusters to the explicitly specified regions. Change the regions according to your needs.
`2-mcs.sh` and `3-config-cluster.sh` is exclusively for MultiCluster method, which creates custom MultiCluster resources and specifies the main config cluster.

### 2a. MultiCluster Method
```
./1--startup.sh
./2-mc.sh
```
This creates the Services and Deployments for the 3-tiered architecture, consisting of a backend, db, and frontend (vegeta load testing).

Google Cloud's MultiCluster resource automatically routes requests to the nearest server.

### 2b. Istio / Anthos Service Mesh (ASM) Method
```
./0-setup.sh              
./1-install.sh
./2-enable-logging.sh
./4-verify-multicluster.sh
kubectl apply -f destrule.yaml
```
The istio method requires a bit more resource, mainly installing Anthos Service Mesh through asmcli. Finally, a DestinationRule resource is applied to enable Locality Load Balancing, a Geo-Aware Load Balancer which routes requests to the nearest server.

```
./1-asm-startup.sh
```
Finally, deploy the respective kubernetes architecture web application.
