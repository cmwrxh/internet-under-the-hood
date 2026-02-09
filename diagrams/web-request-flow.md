# Web Request Flow (High Level)

```text
Browser
  │
  ├─ DNS query → resolver → authoritative
  │
  ├─ CDN mapping → choose edge POP
  │
  ├─ TLS handshake → negotiate keys/ciphers
  │
  ├─ HTTP request → GET/POST over H2 or H3/QUIC
  │
  └─ Response → content + headers + caching rules


