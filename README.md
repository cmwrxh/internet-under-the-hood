[![Network Health Check](https://github.com/cmwrxh/internet-under-the-hood/actions/workflows/network-health.yml/badge.svg)](https://github.com/cmwrxh/internet-under-the-hood/actions/workflows/network-health.yml)
![Status](https://img.shields.io/badge/Status-Active-success)
![Maintained](https://img.shields.io/badge/Maintained-Yes-blue)
![Domain](https://img.shields.io/badge/Domain-Networking-orange)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Bash-yellow)
![Labs](https://img.shields.io/badge/Labs-Wireshark%20%7C%20curl%20%7C%20OpenSSL-purple)

# 🌐 Internet Under The Hood
### Observing, Measuring, and Explaining Real Internet Behavior (DNS • CDN • TLS • HTTP/2 • HTTP/3/QUIC • BGP • Streaming)

This repository documents and measures how internet protocols behave in **real environments**.

Not theory.  
**Real traffic. Real experiments. Real measurements.**

---

## 🧭 Request Journey Map

```text
User
 ↓
DNS resolution (who is the server?)
 ↓
CDN edge selection (which nearby server?)
 ↓
TLS handshake (secure channel)
 ↓
HTTP transport (HTTP/2 vs HTTP/3/QUIC)
 ↓
BGP routing (how packets travel globally)
 ↓
Streaming ABR (HLS/DASH adaptation)
 ↓
Content delivered
