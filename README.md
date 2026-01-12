# 🚀 Argo CD GitOps – Python FastAPI Application

This project demonstrates a **complete GitOps workflow** using **Argo CD**, **Kubernetes**, **Docker**, and a **Python FastAPI** application.
All application deployments are managed via **Git as the single source of truth**.

Whenever the GitHub repository changes, Argo CD automatically synchronizes the Kubernetes cluster.

---

# 🧩 Architecture

```
GitHub Repository
        ↓
     Argo CD
        ↓
   Kubernetes Cluster
        ↓
 Python FastAPI Application
```

---

# 🛠 Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| Python (FastAPI) | Backend application             |
| Docker           | Containerization                |
| Kubernetes       | Container orchestration         |
| Argo CD          | GitOps continuous delivery      |
| GitHub           | Source of truth for deployments |

---

# 📁 Repository Structure

```
argocd-python-gitops/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    └── service.yaml
```

---

# 🧪 Application Endpoints

| Endpoint  | Description                |
| --------- | -------------------------- |
| `/`       | Returns deployment message |
| `/health` | Health check               |

---

# 🐳 Docker Image

The application is built and pushed to Docker Hub as:

```
usmanfarooq317/python-argocd-app:latest
```

This image is used by Kubernetes and pulled securely using an `imagePullSecret`.

---

# 🚀 Deployment Flow

1. Developer pushes code to GitHub
2. Argo CD detects the change
3. Argo CD pulls Kubernetes manifests
4. Kubernetes deploys the new version
5. Application updates automatically

No manual kubectl commands are needed after setup.

---

# 📦 Kubernetes Setup

### Create Namespace

```bash
kubectl create namespace gitops
```

---

### Create Docker Hub Secret

(Use your Docker Hub Access Token)

```bash
kubectl create secret docker-registry dockerhub-secret \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=usmanfarooq317 \
  --docker-password=<YOUR_TOKEN> \
  --docker-email=you@example.com \
  -n gitops
```

---

# 📄 Deployment Configuration

The deployment uses the private Docker image:

```yaml
image: usmanfarooq317/python-argocd-app:latest
```

and pulls it securely using:

```yaml
imagePullSecrets:
  - name: dockerhub-secret
```

---

# 🔄 Argo CD Installation

```bash
kubectl create namespace argocd

kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

---

# 🌐 Access Argo CD

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open in browser:

```
https://localhost:8080
```

Get login password:

```bash
kubectl get secret argocd-initial-admin-secret -n argocd \
  -o jsonpath="{.data.password}" | base64 -d
```

---

# 📦 Create Argo CD Application

In Argo CD UI:

| Field            | Value                                                            |
| ---------------- | ---------------------------------------------------------------- |
| Application Name | python-gitops                                                    |
| Project          | default                                                          |
| Repository URL   | Your GitHub repo                                                 |
| Path             | k8s                                                              |
| Cluster          | [https://kubernetes.default.svc](https://kubernetes.default.svc) |
| Namespace        | gitops                                                           |
| Sync Policy      | Automatic                                                        |

Click **Create → Sync**

---

# 🔍 Verify Deployment

```bash
kubectl get pods -n gitops
kubectl get svc -n gitops
```

Access the application:

```
http://<NodeIP>:<NodePort>
```

---

# 🔥 GitOps in Action

Modify `main.py`, commit and push:

```bash
git commit -am "Update message"
git push
```

Argo CD will automatically redeploy the new version to Kubernetes.

---

# 📌 Why This Project Matters

This project demonstrates:

* Real GitOps workflow
* Production-style Kubernetes deployment
* Secure private image pulling
* Continuous delivery with Argo CD
* Zero-downtime updates

---

# 📄 Author

**Usman Farooq**
DevOps | Kubernetes | Cloud | GitOps
