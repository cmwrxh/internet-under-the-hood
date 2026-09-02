# Measurement Tools

## DNS Resolution Path
`dig +trace api.example.com @1.1.1.1`
Shows every DNS server queried and response time per hop.

## Latency and TTFB
`curl -w "dns: %{time_namelookup}\ntcp: %{time_connect}\ntls: %{time_appconnect}\nttfb: %{time_starttransfer}\n" -o /dev/null -s https://api.example.com`
Measures DNS, TCP handshake, TLS handshake, and time-to-first-byte.

## Path and Hop Analysis
`mtr --report --report-cycles 10 api.example.com`
Shows every router between you and the server, plus latency per hop.

## TLS Handshake Inspection
`openssl s_client -connect api.example.com:443 -tls1_3`
Verifies TLS version, cipher, and certificate chain.
