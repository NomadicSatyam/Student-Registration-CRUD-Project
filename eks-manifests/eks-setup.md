# #ThreeTierApp

## Prerequisites

- Basic knowledge of Docker, and AWS services.
- An AWS account with necessary permissions.

## Setup Steps

### Step 1: IAM Configuration

- Create a user like `eks-admin` with `AdministratorAccess`.
- Generate Security Credentials: Access Key and Secret Access Key For Command Line InterFace .

### Step 2: EC2 Setup

- Launch an Ubuntu instance in your favourite region (eg. region `us-east-1`).
- SSH into the instance from your local machine.

### Step 3: Install AWS CLI v2

```shell
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin --update
```

- Create IAM User With Administration Access

```
aws configure

```

- Give Required Info in Prompt

```
aws --version
```

### Step 4: Install Docker

```shell
sudo apt-get update
sudo apt install docker.io
docker ps
sudo chown $USER /var/run/docker.sock
```

### Step 5: Install kubectl

```shell
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.23.17/2024-01-04/bin/linux/amd64/kubectl

```

```shell
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client

```

### Step 6: Install eksctl

```shell
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```

### Step 7: Setup EKS Cluster

```shell
eksctl create cluster --name two-tier-cluster --region us-east-1 --node-type t2.medium --nodes-min 2 --nodes-max 3

```

```shell
aws eks update-kubeconfig --region us-east-1 --name two-tier-cluster
```

```
kubectl get nodes

```

```
kubectl get pods

```

```
kubectl get svc

```

### Step 8: Run Manifests

- Use Below Command to setup Mysql Database(First Tier)

```shell
kubectl apply -f mysql-secrets.yml -f mysql-configmap.yml -f  mysql-deployment.yml -f mysql-svc.yml
```

- Use Below Command to setup Application(Second Tier)

```shell
kubectl apply -f two-tier-app-deployment.yml -f two-tier-app-svc.yml
```

- Command to see logs

```shell

kubectl logs <pod-name>

```

```shell

kubectl logs <pod-name> -c <Container-Name>

```

```shell
kubectl delete -f mysql-secrets.yml -f mysql-configmap.yml -f  mysql-deployment.yml -f mysql-svc.yml
```

```shell
kubectl delete -f two-tier-app-deployment.yml -f two-tier-app-svc.yml
```

```shell
kubectl create namespace workshop
kubectl apply -f .
kubectl delete -f .
```

### Cleanup

- To delete the EKS cluster:

```shell
eksctl delete cluster --name two-tier-cluster --region us-east-1
```

## Support

For any queries or issues, please open an issue in the repository.

---

Happy Learning! 🚀👨‍💻👩‍💻
