# How to setup two-tier application deployment on kubernetes cluster

## First setup kubernetes kubeadm cluster

Use kubeadm_installation.md to setup kubeadm

## SetUp

- First clone the code to your master machine

```bash
git clone https://github.com/NomadicSatyam/StudentRegistrationCRUDProject.git
```

- Move to k8s directory

```bash
cd StudentRegistrationCRUDProject/k8s
```

- Now, execute below commands one by one

```bash
kubectl apply -f two-tier-deployment.yml
```

```bash
kubectl apply -f two-tier-deployment-svc.yml
```

```bash
kubectl apply -f mysql-deployment.yml
```

```bash
kubectl apply -f mysql-deployment-svc.yml
```

```bash
kubectl apply -f persistent-volume.yml
```

```bash
kubectl apply -f persistent-volume-claim.yml
```
