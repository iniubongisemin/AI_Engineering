$ kubectl 
$ kubectl help
$ kubectl apply -f first_manifest.yml

### INSPECTING KUBERNETES MANIFEST
$ cat 01_first_manifest.yml
>>> OUTPUT
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 5
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25.4
        ports:
        - containerPort: 80

### CREATE A DEPLOYMENT
$ kubectl apply -f 01_first_manifest.yml
>>> OUTPUT
deployment.apps/nginx-deployment created

$ kubectl delete -f 01_first_manifest.yml
>>> OUTPUT
deployment.apps "nginx-deployment" deleted

### SCALING & MONITORING A DEPLOYMENT
kubectl apply -f 01_first_manifest.yml
kubectl scale deployment nginx-deployment --replicas 10
cat 01_first_manifest.yml
kubectl get nginx-deployment
kubectl scale deployment nginx-deployment -- replicas 10
kubectl scale deployment nginx-deployment --replicas 3
kubectl get pods

### DEPLOYING & SCALING STATEFUL APPS
more 01_statefulset.yml
kubectl apply -f 01_statefulset
.yml
kubectl get pods
kubectl scale statefulset datacamp-statefulset --replicas 10
