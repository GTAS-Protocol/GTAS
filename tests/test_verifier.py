#!/usr/bin/env python3
"""
GTAS Reference Verifier Test Suite
Specification: RFC-0001 through RFC-0004
"""

import time
import pytest
from sdk.verifier import EpistemicAnchor, evaluate_anchor

def test_anchor_initialization():
    anchor = EpistemicAnchor(
        payload="Test empirical observation",
        context_domain="urn:gtas:domain:test",
        gtq_initial=1.0,
        lambda_coeff=0.05
    )
    assert anchor.payload_hash is not None
    assert len(anchor.payload_hash) == 64  # BLAKE2b hex digest length
    assert anchor.compute_current_gtq() == 1.0

def test_context_isolation_enforcement():
    anchor = EpistemicAnchor(
        payload="Physics telemetry data",
        context_domain="urn:gtas:domain:physics",
    )
    # Valid matching domain
    assert anchor.verify_context("urn:gtas:domain:physics") is True
    # Mismatched domain (A + B != C isolation rule)
    assert anchor.verify_context("urn:gtas:domain:finance") is False

def test_bayesian_decay():
    anchor = EpistemicAnchor(
        payload="Decaying observation",
        context_domain="urn:gtas:domain:test",
        gtq_initial=1.0,
        lambda_coeff=1.0
    )
    initial_gtq = anchor.compute_current_gtq()
    # Simulate time passing by checking future decay or mocking delta_t
    # Since compute_current_gtq uses time.time(), we can pass a future timestamp if supported or test decay delta
    time.sleep(0.1)
    decayed_gtq = anchor.compute_current_gtq()
    assert decayed_gtq < initial_gtq

def test_evaluate_anchor_logic(capsys):
    anchor = EpistemicAnchor(
        payload="Valid anchor",
        context_domain="urn:gtas:domain:valid",
        gtq_initial=0.9
    )
    
    # Successful evaluation
    assert evaluate_anchor(anchor, "urn:gtas:domain:valid", min_threshold=0.5) is True
    
    # Failed evaluation due to domain mismatch
    assert evaluate_anchor(anchor, "urn:gtas:domain:invalid", min_threshold=0.5) is False