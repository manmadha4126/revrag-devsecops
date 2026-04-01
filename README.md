A secure and containerized machine learning inference service with comprehensive DevSecOps practices.

## Overview

This project implements a containerized inference service with security auditing, automated deployment, and best practices for production environments.

## Features

- Containerized application using Docker
- GitHub Actions CI/CD pipeline
- Security audit and vulnerability scanning
- Comprehensive documentation and reflection

## Project Structure

```
.
├── Dockerfile              # Container configuration
├── .dockerignore           # Docker build ignore rules
├── inference.py            # Main inference service
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── SECURITY_AUDIT.md      # Security assessment
├── REFLECTION.md          # Project reflection and learnings
└── .github/
	└── workflows/
		└── deploy.yml     # GitHub Actions deployment workflow
```

## Getting Started

### Prerequisites

- Docker (20.10+)
- Python 3.11+
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd revrag-devsecops
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

```bash
python inference.py
```

### Running in Docker

```bash
docker build -t revrag-inference .
docker run -p 8000:8000 revrag-inference
```

## Deployment

The project uses GitHub Actions for automated deployment. See `.github/workflows/deploy.yml` for configuration.

## Security

Please refer to [SECURITY_AUDIT.md](SECURITY_AUDIT.md) for security assessment and practices.

## Reflection

See [REFLECTION.md](REFLECTION.md) for project insights and learnings.

## License

MIT License
https://github.com/manmadha4126/revrag-devsecops