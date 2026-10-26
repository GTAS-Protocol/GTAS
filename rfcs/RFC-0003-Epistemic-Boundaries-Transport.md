# RFC-0003: Context-Bound Epistemic Boundary Predicates & Transport Mechanics

- **RFC Number:** 0003
- **Title:** Context-Bound Epistemic Boundary Predicates and Transport Mechanics
- **Status:** Draft / Open Request for Comments
- **Category:** Protocol Standard / Transport Architecture
- **Author:** GTAS Protocol Specification Group (`noreply@gtas-protocol.org`)
- **Created:** 2026-10-26

---

## 1. Abstract

RFC-0003 defines the serialization formats, network transport protocols, and predicate evaluation rules for transmitting epistemic anchors ($\mathcal{A}$) across decentralized nodes. To enforce non-transitive domain boundaries ($A + B \neq C$) and prevent context bleed, all transport payloads must carry explicit boundary descriptors validated at each routing hop.

---

## 2. Context Boundary Syntax ($\mathcal{C}$)

Context predicates are serialized using deterministic JSON-LD schemata defining the spatial, temporal, and ontological scope of an anchor.

### Example Context Descriptor (`ContextPredicate`)
```json
{
  "@context": "[https://gtas-protocol.org/ns/v1](https://gtas-protocol.org/ns/v1)",
  "@type": "EpistemicContext",
  "domainId": "urn:gtas:domain:empirical-physics:thermodynamics",
  "temporalBounds": {
    "effectiveFrom": "2026-01-01T00:00:00Z",
    "expiresAt": "2028-01-01T00:00:00Z"
  },
  "ontologicalConstraints": {
    "allowTransitivity": false,
    "maxDelegationDepth": 0
  }
}
```

---

## 3. Transport Wire Format

Anchors transmitted across the GTAS peer-to-peer transport layer utilize Protocol Buffers (Protobuf v3) for compact, deterministic serialization.

### Protocol Buffer Definition (`gtas_anchor.proto`)
```protobuf
syntax = "proto3";

package gtas.v1;

message EpistemicAnchorPayload {
  bytes payload_hash = 1;          // BLAKE3 hash commitment (H_payload)
  bytes context_commitment = 2;    // Hash of the ContextPredicate
  double ground_truth_quotient = 3;// Current GTQ(t) score in [0.0, 1.0]
  uint64 timestamp_posix = 4;      // UTC POSIX timestamp of validation
  bytes zk_proof_bytes = 5;        // Serialized ZK-PoP proof (pi_PoP)
}

message TransportEnvelope {
  string protocol_version = 1;     // e.g., "gtas-1.0.0-RC1"
  EpistemicAnchorPayload anchor = 2;
  bytes sender_signature = 3;      // Protocol node signature (non-identity)
}
```

---

## 4. Epistemic Routing & Isolation Enforcement

When a transport node receives a `TransportEnvelope`, it MUST execute the following validation sequence before rebroadcasting or indexing:

1. **Context Boundary Check:** Verify that the incoming context commitment matches the local node's routing domain permissions. If $\mathcal{C}_{\text{incoming}} \neq \mathcal{C}_{\text{node}}$, drop packet (Isolation Enforcement).
2. **GTQ Decay Evaluation:** Compute current $\text{GTQ}(t)$ using the decay equation from RFC-0001. If $\text{GTQ}(t) < \text{Threshold}_{\text{min}}$, reject anchor propagation.
3. **ZK-PoP Verification:** Pass `zk_proof_bytes` to the circuit verifier contract.