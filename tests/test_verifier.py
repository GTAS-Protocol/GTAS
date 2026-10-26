#!/usr/bin/env python3
"""
GTAS Reference Verifier Test Suite
Specification: RFC-0001 through RFC-0004
"""

import pytest
import time
from sdk.verifier import EpistemicAnchor, evaluate_anchor

def test_anchor_initialization():
    anchor = EpistemicAnchor(
        payload="Test empirical observation",
        context_domain="urn:gtas:domain:test",
        gtq_initial=1.0,
        lambda_coeff=0.05
    )
    assert anchor.payload_hash is not None
    assert len(anchor.payload_hash) == 128  # BLAKE2b default hex digest length (64 bytes = 128 hex chars)

def test_context_isolation_enforcement():
    anchor_a = EpistemicAnchor(
        payload="Data A",
        context_domain="urn:gtas:domain:alpha",
        gtq_initial=1.0,
        lambda_coeff=0.05
    )
    
    # Matching domain verification should pass
    assert anchor_a.verify_domain("urn:gtas:domain:alpha") is True
    
    # Cross-domain contamination attempt must fail (A + B != C)
    assert anchor_a.verify_domain("urn:gtas:domain:beta") is False

def test_bayesian_decay():
    anchor = EpistemicAnchor(
        payload="Decay test payload",
        context_domain="urn:gtas:domain:decay",
        gtq_initial=1.0,
        lambda_coeff=0.1
    )
    
    initial_gtq = anchor.current_gtq
    # Simulate elapsed time
    time.sleep(0.1)
    decayed_gtq = anchor.get_current_gtq()
    
    assert decayed_gtq < initial_gtq

def test_evaluate_anchor_logic():
    anchor = EpistemicAnchor(
        payload="Evaluation test",
        context_domain="urn:gtas:domain:eval",
        gtq_initial=0.9,
        lambda_coeff=0.05
    )
    
    # Valid evaluation within matching domain and high enough GTQ
    result = evaluate_anchor(anchor, target_domain="urn:gtas:domain:eval", min_gtq_threshold=0.5)
    assert result is True
    
    # Failed evaluation due to domain mismatch
    result_mismatch = evaluate_anchor(anchor, target_domain="urn:gtas:domain:wrong", min_gtq_threshold=0.5)
    assert result_mismatch is False