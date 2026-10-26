# Contributing to the Ground Truth Anchoring Standard (GTAS)

Thank you for your interest in contributing to GTAS. GTAS is a decentralized, un-ownable, open-source protocol designed to establish verifiable information provenance, combat synthetic data poisoning, and enforce context-bound epistemic reasoning.

## 1. Core Principles

* **Public Domain Utility:** All contributions are dedicated to the public domain under the Creative Commons Zero (CC0 1.0) license / MIT License.
* **Pseudonymity & Decoupling:** Authorship of RFCs and protocol specifications is attributed strictly to protocol identities or cryptographic keys. Contributors are encouraged to preserve identity decoupling.
* **Falsifiability & Precision:** Protocol modifications must be mathematically or logically falsifiable. Empirical claims require explicit zero-knowledge verification schemas or context-bound proofs.

## 2. How to Propose an RFC

1. **Check Existing RFCs:** Review `/rfcs/` to ensure your proposed concept or layer extension does not duplicate existing specifications.
2. **Draft the Specification:** Create a new markdown file in `/rfcs/` following the naming convention:
   `RFC-XXXX-Short-Title.md`
3. **Use the Standard RFC Template:**
   * Title and Metadata (Status, Category, Author email/key, Date)
   * Abstract & Motivation
   * Technical & Mathematical Specifications
   * Security & Threat Model
   * Backward Compatibility
4. **Submit a Pull Request:** Open a PR against the `main` branch.

## 3. Pull Request Guidelines

* **Commit Identity:** Ensure your commit author identity matches your intended public persona or the decoupled protocol default (`GTAS-Protocol`).
* **Atomic Changes:** Keep pull requests focused on a single RFC, bug fix, or translation update.
* **Review Process:** RFC proposals require a 14-day public commentary period before transitioning from `Draft` to `Accepted`.