# nginx ssl.conf
server {
    listen 443 ssl http2;
    listen 443 ssl http3 quic;  # QUIC for HTTP/3
    
    ssl_certificate     /etc/ssl/certs/api.example.com.crt;
    ssl_certificate_key /etc/ssl/private/api.example.com.key;
    
    ssl_protocols       TLSv1.3;
    ssl_ciphers         TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256;
    ssl_prefer_server_ciphers off;
    
    # 0-RTT early data
    ssl_early_data on;
    
    # OCSP stapling (eliminates extra lookup)
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 1.0.0.1 valid=300s;
    
    add_header Alt-Svc 'h3=":443"; ma=86400';
}
