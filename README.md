# 🚀 RevRag DevSecOps Assignment – Fix the Pipeline

## 👨‍💻 Author

**Manmadha**

---

## 📌 Objective

This project focuses on auditing and securing a vulnerable DevOps setup, including:

* Dockerfile hardening
* CI/CD pipeline security
* Secret management
* Container vulnerability scanning

The goal is to implement **DevSecOps best practices** and ensure secure, production-ready infrastructure.

---

## 🔐 Key Security Improvements

### 🐳 Dockerfile Hardening

* Replaced `node:latest` with a fixed version (`node:20-alpine`)
* Removed hardcoded secrets
* Eliminated unnecessary packages (curl, vim, wget)
* Avoided running container as root (used non-root user)
* Removed unnecessary port exposure (SSH)

---

### ⚙️ CI/CD Pipeline Security

* Removed hardcoded credentials from workflow
* Used GitHub Secrets for secure authentication
* Updated GitHub Actions to latest stable versions
* Used commit SHA-based image tagging instead of `latest`
* Removed `--privileged` container usage

---

### 🛡️ Vulnerability Scanning (Trivy)

* Integrated Trivy scan into CI/CD pipeline
* Scan runs **after Docker build**
* Pipeline **fails if CRITICAL vulnerabilities are detected**
* Generates scan report as an artifact

---

## ⚠️ Security Enforcement

The pipeline is intentionally designed to **fail when CRITICAL vulnerabilities are found**.

This ensures:

* Vulnerable images are not deployed
* Security is enforced early (Shift-Left Security)
* CI/CD acts as a **security gate**, not just a deployment tool

---

## 📂 Project Structure

```
.
├── Dockerfile
├── inference.py
├── SECURITY_AUDIT.md
├── REFLECTION.md
├── .dockerignore
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## ▶️ How to Run Locally

```bash
docker build -t myapp .
docker run -p 3000:3000 myapp
```

---

## 🔄 CI/CD Workflow

1. Checkout code
2. Build Docker image
3. Run Trivy vulnerability scan
4. Upload scan report
5. (Optional) Push & deploy if secure

---

## 🔗 Submission Links

* **GitHub Repository**:
  https://github.com/manmadha4126/revrag-devsecops

* **Docker Hub**:
  https://hub.docker.com/r/manmadha21/myapp

---

## 🛡️ Security Focus

This project prioritizes:

* Least privilege principle
* Secure secret management
* Minimal attack surface
* Supply chain security
* Automated vulnerability detection

---

## 🧠 DevSecOps Approach

Instead of forcing successful builds, this implementation enforces **security-first CI/CD**, where:

> "A failed build due to vulnerabilities is a success in preventing insecure deployments."

---

## 📢 Note

Pipeline failure due to CRITICAL vulnerabilities is **intentional** and demonstrates enforcement of DevSecOps security practices.

---

## 🙌 Acknowledgment

This assignment demonstrates practical DevSecOps skills, including container security, CI/CD hardening, and automated vulnerability management.

---
