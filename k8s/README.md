# Kubernetes

Practice manifests for learning the basic Kubernetes objects (Pods,
ReplicaSets, Deployments, Services).

## tutorial/

Working through the basic Kubernetes objects, each in its own
manifest. All use the `nginx` image and the `app: myapp` label.

| File | Object |
|---|---|
| `pods/pod.yml` | A single Pod |
| `pods/nginx.yml` | A second Pod (used alongside the ReplicaSet/Deployment) |
| `replicasets/replicaset.yml` | ReplicaSet with 3 replicas |
| `deployments/deployment.yml` | Deployment with 6 replicas |
| `service/service-definition.yml` | NodePort Service (80 → 30004) |

### How to work through it

Any Kubernetes cluster works — a local sandbox is easiest, e.g.
[kind](https://kind.sigs.k8s.io/) (requires Docker):

```sh
brew install kind kubectl   # macOS; Linux: see the kind docs
kind create cluster
```

Then apply in object order and observe:

```sh
kubectl apply -f tutorial/pods/pod.yml
kubectl get pods -o wide

kubectl apply -f tutorial/replicasets/replicaset.yml
kubectl get replicasets, pods

kubectl apply -f tutorial/deployments/deployment.yml
kubectl get deployments, pods

kubectl apply -f tutorial/service/service-definition.yml
kubectl get svc
# NodePort 30004 on any node IP
```

Clean up between experiments with
`kubectl delete -f tutorial/<file>`.
