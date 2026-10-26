# GTAS CI/CD & Automation Workflows

This directory contains the GitHub Actions workflow definitions that automate protocol synchronization, identity enforcement, and automated testing across the GTAS repository.

## Workflow Index

### 1. `protocol-sync.yml`
- **Trigger:** Push to `main`.
- **Purpose:** Configures protocol authorship identity (`GTAS-Protocol`) and verifies a clean commit state across history.

### 2. `pytest-ci.yml`
- **Trigger:** Push or Pull Request on `main`.
- **Purpose:** Automatically provisions a Python 3.10 environment, installs dependencies (`pytest`), and executes the SDK reference verifier test suite (`tests/test_verifier.py`) to prevent regressions.