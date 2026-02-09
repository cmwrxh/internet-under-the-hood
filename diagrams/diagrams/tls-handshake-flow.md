
Create: `diagrams/tls-handshake-flow.md`

```md
# TLS Handshake Flow (Conceptual)

```text
Client                          Server
  | --- ClientHello ------------> |
  | <--- ServerHello ------------ |
  | <--- Certificate ------------ |
  | <--- (TLS1.3) Key Share ----- |
  | --- Finished ----------------> |
  | <--- Finished --------------- |
  | ===== Encrypted Traffic ===== |
