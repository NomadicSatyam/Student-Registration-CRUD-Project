# Kubeadm Installation Guide

This guide outlines the steps needed to set up a Kubernetes cluster using kubeadm.

## Pre-requisites

- Ubuntu OS (Xenial or later)
- sudo privileges
- Internet access
- t2.medium instance type or higher

---

## Both Master & Worker Node

Run the following commands on both the master and worker nodes to prepare them for kubeadm.

```bash
# using 'sudo su' is not a good practice.
sudo apt update
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo apt install docker.io -y

sudo systemctl enable --now docker # enable and start in single command.

# Adding GPG keys.
curl -fsSL "https://packages.cloud.google.com/apt/doc/apt-key.gpg" | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/kubernetes-archive-keyring.gpg

# Add the repository to the sourcelist.
echo 'deb https://packages.cloud.google.com/apt kubernetes-xenial main' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt update
sudo apt install kubeadm=1.20.0-00 kubectl=1.20.0-00 kubelet=1.20.0-00 -y
```

**Sample Command run on master node**

<kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/a.png)</kbd>

<kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/b.png)</kbd>

<kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/c.png)</kbd>

---

## Master Node

1. Initialize the Kubernetes master node.

   ```bash
   sudo kubeadm init
   ```

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/d.png)</kbd>

   After succesfully running, your Kubernetes control plane will be initialized successfully.

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/e.png)</kbd>

2. Set up local kubeconfig (both for root user and normal user):

   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/f.png)</kbd>

3. Apply Weave network:

   ```bash
   kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
   ```

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/g.png)</kbd>

4. Generate a token for worker nodes to join:

   ```bash
   sudo kubeadm token create --print-join-command
   ```

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/h.png)</kbd>

5. Expose port 6443 in the Security group for the Worker to connect to Master Node

<kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/i.png)</kbd>

---

## Worker Node

1. Run the following commands on the worker node.

   ```bash
   sudo kubeadm reset pre-flight checks
   ```

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/j.png)</kbd>

2. Paste the join command you got from the master node and append `--v=5` at the end.
   _Make sure either you are working as sudo user or use `sudo` before the command_

   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/k.png)</kbd>

   After succesful join->
   <kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/l.png)</kbd>

---

## Verify Cluster Connection

On Master Node:

```bash
kubectl get nodes
```

<kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/m.png)</kbd>

---

## Optional: Labeling Nodes

If you want to label worker nodes, you can use the following command:

```bash
kubectl label node <node-name> node-role.kubernetes.io/worker=worker
```

---

## Optional: Test a demo Pod

If you want to test a demo pod, you can use the following command:

```bash
kubectl run hello-world-pod --image=busybox --restart=Never --command -- sh -c "echo 'Hello, World' && sleep 3600"
```

<kbd>![image](https://github.com/NomadicSatyam/Github-Repo-Resouces/blob/dev/Kubeadm%20Install%20Guide/n.png)</kbd>
