# GTAS SDK & Reference Verifier

This directory contains reference implementations of the core GTAS verification routines, dynamic Bayesian confidence decay calculators, and epistemic isolation enforcement logic specified in RFC-0001 through RFC-0004.

## Core Components

### verifier.py
A zero-dependency Python 3 reference script for anchor creation, context domain matching, and confidence score evaluation.

#### Key Features
1. BLAKE2b Payload Hashing: Generates deterministic cryptographic hash commitments (H_payload).
2. Epistemic Isolation (A + B != C): Validates context domain boundaries to prevent cross-domain context bleed.
3. Decaying Bayesian Confidence (GTQ): Evaluates real-time exponential decay based on time elapsed and volatility coefficient.

## Quick Start

### 1. Run Built-in Verification Test
Execute the script directly in your terminal:
python3 sdk/verifier.py

### 2. Programmatic Usage Example
Import the verifier classes into your own modules:
from sdk.verifier import EpistemicAnchor, evaluate_anchor

# Instantiate an epistemic anchor
anchor = EpistemicAnchor(
    payload="Empirical observation payload data.",
    context_domain="urn:gtas:domain:empirical-physics:thermodynamics",
    lambda_coeff=0.01
)

# Evaluate anchor validity against a target domain
is_valid = evaluate_anchor(
    anchor=anchor,
    target_domain="urn:gtas:domain:empirical-physics:thermodynamics",
    min_threshold=0.5
)