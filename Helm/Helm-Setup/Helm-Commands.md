# Helm Commands for Kubernetes

## MySQL Chart

### Create Chart

```bash
helm create mysql-chart
```

### Package Chart

```bash
helm package mysql-chart
```

### Install Chart

```bash
helm install mysql-chart ./mysql-chart
kubectl get pods
```

### Check Helm Charts

```bash
helm list
```

### Uninstall Chart

```bash
helm uninstall mysql-chart
```

**Note:** If any changes are made to the chart, repackage and install again.

```bash
helm package mysql-chart
helm install mysql-chart ./mysql-chart
```

### Enter Pod Bash

Enter the pod where the MySQL container is running.

```bash
kubectl exec -it mysql-chart-c6c4554d6-fdklr -- bash
```

## Django App Chart

### Create Chart

```bash
helm create django-app-chart
```

### Check All Manifests

```bash
helm template django-app-chart
```

### Package Chart

```bash
helm package django-app-chart
```

### Install Package

```bash
helm install django-app-chart ./django-app-chart
```
