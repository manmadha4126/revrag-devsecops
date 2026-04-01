# 🔐 Security Audit Report – RevRag DevSecOps Assignment

## 📌 Security Audit Summary

* Removed hardcoded secrets
* Used secure and minimal base image
* Avoided running container as root
* Reduced attack surface
* Secured CI/CD pipeline
* Added Trivy vulnerability scanning
* Enforced failure on CRITICAL vulnerabilities
* Removed privileged container usage
* Implemented secure image tagging

---

# 🔍 Detailed Security Audit

## 🐳 Dockerfile Audit & Fixes

### 1. Use of `node:latest`

**Issue:**
Using `latest` tag leads to unpredictable builds and potential vulnerabilities.

**Fix:**
Replaced with `node:20-alpine`.

**Reason:**
Ensures consistency and reduces attack surface due to smaller image size.

---

### 2. Copying Entire Context (`COPY . .`)

**Issue:**
May include sensitive files like `.env` or `.git`.

**Fix:**
Copied only `package*.json` first, then application code.

**Reason:**
Improves security and build efficiency.

---

### 3. Use of `npm install`

**Issue:**
Can result in inconsistent dependency installation.

**Fix:**
Replaced with `npm ci --only=production`.

**Reason:**
Ensures deterministic builds.

---

### 4. Hardcoded Secrets

**Issue:**
Secrets embedded in image layers can be extracted.

**Fix:**
Removed all hardcoded secrets.

**Reason:**
Secrets should be managed externally (e.g., environment variables or secret managers).

---

### 5. Unnecessary Packages

**Issue:**
Installing tools like `curl`, `vim`, `wget` increases attack surface.

**Fix:**
Removed unnecessary packages.

**Reason:**
Minimal images are more secure.

---

### 6. Running as Root User

**Issue:**
Root access increases impact of compromise.

**Fix:**
Created and used a non-root user.

**Reason:**
Follows least privilege principle.

---

### 7. Exposing Port 22

**Issue:**
SSH inside container is unnecessary and insecure.

**Fix:**
Removed `EXPOSE 22`.

**Reason:**
Containers should not expose SSH.

---

# ⚙️ CI/CD Pipeline Audit & Fixes

### 1. Hardcoded Credentials

**Issue:**
Secrets exposed in repository.

**Fix:**
Moved to GitHub Secrets.

**Reason:**
Prevents credential leakage.

---

### 2. Outdated GitHub Actions

**Issue:**
Older versions may contain vulnerabilities.

**Fix:**
Updated to latest versions.

---

### 3. Use of `latest` Tag

**Issue:**
No traceability.

**Fix:**
Used commit SHA for tagging.

**Reason:**
Improves traceability and rollback.

---

### 4. Insecure Docker Login

**Issue:**
Password exposure risk.

**Fix:**
Used `--password-stdin`.

---

### 5. Use of `--privileged`

**Issue:**
Grants full host access.

**Fix:**
Removed privileged mode.

**Reason:**
Prevents host compromise.

---

### 6. Insecure SSH Option

**Issue:**
`StrictHostKeyChecking=no` allows MITM attacks.

**Fix:**
Recommended secure SSH practices.

---

# 🛡️ Vulnerability Scanning (Trivy)

## Implementation

Trivy scan is integrated into the CI/CD pipeline after the Docker image build step.

## Behavior

* Scans the built image
* Fails pipeline on CRITICAL vulnerabilities
* Generates a report as an artifact

## Why After Build?

Ensures the actual container image (including dependencies) is scanned.

---

## ⚠️ Trivy Scan Enforcement

The pipeline is intentionally configured to fail when CRITICAL vulnerabilities are detected.

This ensures:

* Vulnerable images are not deployed
* Security is enforced early (shift-left approach)
* Developers are alerted immediately

In real-world environments, this would trigger remediation workflows.

---

# 🧠 Decision Questions

## Q1 — Vulnerability Management

If CRITICAL CVEs exist but cannot be fixed immediately:

* Assess exploitability
* Apply temporary mitigations
* Document and communicate risk
* Plan future remediation

**Approach:** Risk mitigation and controlled acceptance.

---

## Q2 — Container Security (`--privileged`)

Even in internal systems:

* Provides root-level host access
* Enables lateral movement if compromised

**Conclusion:** Avoid using privileged containers.

---

## Q3 — Git History & Secrets

Removing secrets from code is insufficient:

* Secrets persist in git history
* Must rotate credentials
* Remove history using tools (BFG / git filter-repo)
* Audit access logs

---

## Q4 — Trade-off (Pinning Actions)

Best practice:

* Pin critical actions to versions/SHAs
* Use Dependabot for updates

**Balance:** Security and maintainability.

---

# 🧾 Conclusion

This project demonstrates DevSecOps principles by:

* Eliminating insecure configurations
* Applying least privilege
* Securing CI/CD workflows
* Integrating automated vulnerability scanning

> A failing pipeline due to security checks is a success in preventing insecure deployments.
