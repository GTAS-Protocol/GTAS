# GTAS Test Suite

This directory contains automated unit and integration tests for the Ground Truth Anchoring Standard (GTAS) reference SDK and protocol components.

## Test Components

### `test_verifier.py`
An automated test suite powered by `pytest` designed to validate the correctness of `sdk/verifier.py`.

#### Key Test Scenarios
1. **Anchor Initialization & Hashing:** Verifies that cryptographic hash commitments ($H_{\text{payload}}$) are correctly generated using BLAKE2b with the expected 64-character hex digest length.
2. **Epistemic Domain Isolation ($A + B \neq C$):** Asserts that context domain boundaries strictly validate matching domains and reject cross-domain attempts.
3. **Bayesian Confidence Decay:** Tests real-time exponential decay calculations over elapsed time intervals ($\Delta t$).
4. **Evaluation Logic:** Validates the end-to-end `evaluate_anchor` wrapper function across successful verifications and safety rejections.

## Running Tests

To run the test suite locally using `pytest`:

```bash
# Install test dependencies (if not already installed)
pip install pytest

# Execute tests from the repository root
pytest