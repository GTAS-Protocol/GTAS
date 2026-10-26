# RFC-0004: Post-Quantum Cryptographic Migration & Lattice-Based ZK-PoP

- **RFC Number:** 0004
- **Title:** Post-Quantum Cryptographic Migration and Lattice-Based ZK-PoP
- **Status:** Draft / Open Request for Comments
- **Category:** Protocol Standard / Cryptographic Security
- **Author:** GTAS Protocol Specification Group (`noreply@gtas-protocol.org`)
- **Created:** 2026-10-26

---

## 1. Abstract

While core hash commitments (`BLAKE3`, `SHA-256`) are inherently quantum-resistant via Grover's bounds, standard pairing-friendly elliptic curves (e.g., BN254, BLS12-381) utilized in Groth16 and early PLONK ZK-proof systems are vulnerable to Shor's algorithm. RFC-0004 defines the migration path toward post-quantum zero-knowledge proofs (FRI-based STARKs / lattice-based polynomial commitments) and post-quantum transport signatures.

---

## 2. Post-Quantum Threat Matrix

| Primitive Layer | Current Algorithm | Quantum Vulnerability | Post-Quantum Target |
| :--- | :--- | :--- | :--- |
| **Payload Hash** | BLAKE3 / SHA-256 | Secure (Grover quadratic) | Retain (BLAKE3) |
| **ZK Provenance ($\pi_{\text{PoP}}$)** | Pairing-Friendly Curves | Critical (Shor's Algorithm) | FRI-based STARKs / Lattice Commitments |
| **Transport Signatures** | ECDSA / Ed25519 | Critical (Shor's Algorithm) | ML-DSA (Dilithium) / SPHINCS+ |

---

## 3. Lattice-Based & STARK-Friendly ZK-PoP Primitives

To eliminate reliance on discrete logarithms over elliptic curves, GTAS Phase-2 nodes MUST support STARK-based argument systems where verification relies on symmetric cryptography (hashes) rather than algebraic pairings.

### 3.1 FRI Polynomial Commitment Scheme
Instead of pairing equations, ZK-PoP proofs under RFC-0004 utilize Fast Reed-Solomon Interactive Oracle Proofs of Proximity (FRI) operating over binary or extension fields:

$$\text{Verify}_{\text{STARK}}(\pi_{\text{PQC}}, H_{\text{payload}}, \mathcal{C}) \to \{0, 1\}$$

---

## 4. Post-Quantum Transport Signatures (`sender_signature`)

Transport envelopes defined in RFC-0003 must transition node authentication keys to NIST-standardized post-quantum signature schemes:
* **Primary Recommendation:** ML-DSA (CRYSTALS-Dilithium) for high-throughput node synchronization.
* **Stateless Alternative:** SPHINCS+ (SLH-DSA) for hash-based signature security without structured lattice assumptions.