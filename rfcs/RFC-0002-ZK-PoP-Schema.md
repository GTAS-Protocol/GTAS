# RFC-0002: ZK-PoP Circuit Schema & Verification Constraints

- **RFC Number:** 0002
- **Title:** Zero-Knowledge Proof of Provenance (ZK-PoP) Circuit Schema
- **Status:** Draft / Open Request for Comments
- **Category:** Core Protocol Architecture
- **Author:** GTAS Protocol Specification Group (`noreply@gtas-protocol.org`)
- **Created:** 2026-10-26

---

## 1. Abstract

This specification details the cryptographic circuit constraints, witness structures, and verification primitives for the Zero-Knowledge Proof of Provenance (ZK-PoP) specified in RFC-0001. ZK-PoP enables cognitive engines to prove that a generated claim, output, or transformation is cryptographically rooted in an authorized source context $\mathcal{C}$ without disclosing raw data payloads.

---

## 2. Circuit Parameters & Public Inputs

A compliant ZK-PoP verifier operates over a prime order elliptic curve scalar field $\mathbb{F}_p$ (default: BN254 / Alt-BN128 or BLS12-381).

### 2.1 Public Inputs ($\mathbf{x}$)
1. **$H_{\text{payload}} \in \mathbb{F}_p$**: Poseidon / BLAKE3 hash commitment of the public output claim.
2. **$H_{\text{context}} \in \mathbb{F}_p$**: Hash commitment of the context boundary rules $\mathcal{C}$.
3. **$\text{GTQ}_{\text{min}} \in \mathbb{F}_p$**: Minimum acceptable Ground Truth Quotient threshold.
4. **$T_{\text{anchor}} \in \mathbb{F}_p$**: POSIX timestamp of initial anchor creation.

### 2.2 Private Witness ($\mathbf{w}$)
1. **$Payload_{\text{raw}}$**: The full unencrypted claim text or dataset payload.
2. **$\mathcal{C}_{\text{predicate}}$**: The explicit boundary predicates and source evaluation logic.
3. **$\sigma_{\text{source}}$**: Signature or merkle membership proof confirming source authorization.

---

## 3. Arithmetic Constraint System

The constraint system enforces three mandatory conditions inside the ZK circuit:

### Constraint 1: Payload Commitment Integrity
$$\text{Poseidon}(Payload_{\text{raw}}) - H_{\text{payload}} = 0$$

### Constraint 2: Context Boundary Inclusion
$$\text{EvaluateContext}(\mathcal{C}_{\text{predicate}}, Payload_{\text{raw}}) - 1 = 0$$

### Constraint 3: Semantic Bounds Verification
For transformations $T: Payload_{\text{in}} \to Payload_{\text{out}}$, the semantic variance $\Delta$ must satisfy:

$$\Delta = \| E(Payload_{\text{in}}) - E(Payload_{\text{out}}) \|_2 \le \epsilon_{\text{threshold}}$$

Where $E(\cdot)$ represents the circuit-friendly vector embedding commitment function.

---

## 4. Verification Protocol

Verification uses standard non-interactive arguments of knowledge (Groth16 or PLONK verification equation):

$$e(A, B) = e(\alpha, \beta) \cdot e\left(\sum_{i=0}^{\ell} x_i \gamma_i, \delta\right) \cdot e(C, \delta)$$

If the equation balances and $\text{GTQ}(t) \ge \text{GTQ}_{\text{min}}$, the verifier accepts the anchor as valid and un-poisoned.