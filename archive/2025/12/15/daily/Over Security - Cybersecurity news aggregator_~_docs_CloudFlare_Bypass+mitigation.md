---
title: ~/docs/CloudFlare/Bypass+mitigation
url: https://blog.lobsec.com/2025/12/ladozione-di-una-cdn-e-prassi-standard-per-la-mitigazione-dei-vettori-di-attacco-di-layer-7-e-per-loccultamento-dellindirizzo-ip-dorigine-origin-ip/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-15
fetch_date: 2025-12-16T03:24:12.870937
---

# ~/docs/CloudFlare/Bypass+mitigation

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# ~/docs/CloudFlare/Bypass+mitigation

2025-12-15 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

Lo sappiamo tutti: in un panorama digitale in continua evoluzione, la sicurezza informatica non è più un optional, ma un pilastro fondamentale di qualsiasi infrastruttura web seria. La recente decisione di migrare l’infrastruttura di questo blog sotto la “protezione” di Cloudflare non è stata solo una mossa per l’ottimizzazione delle performance, ma un passo per rinforzare la postura di sicurezza.

Questo post esplorerà due aspetti critici: come è stato tecnicamente integrato Cloudflare con la configurazione Nginx, quali sono i limiti di questa soluzione, come mitigarli e gli attacchi più comuni in uno scenario di offuscamento delle risorse esposte.

## Cloudflare e Nginx

Per prima cosa è stato creato uno script che permetta di interrogare e scaricare le liste degli IP della CDN di Cloudflare: questo script può essere inserito in un job cron per tenere costantemente aggiornate le subnet.

```
#!/bin/bash

# File di configurazione Nginx in cui verranno salvate le direttive 'allow'
NGINX_ALLOW_CONF="/etc/nginx/conf.d/cloudflare_allow_ips.conf"

# URL da cui scaricare gli IP di Cloudflare (IPv4 e IPv6)
IPV4_URL="https://www.cloudflare.com/ips-v4/"
IPV6_URL="https://www.cloudflare.com/ips-v6/"

# Percorso temporaneo per i file scaricati
TEMP_IPV4=$(mktemp)
TEMP_IPV6=$(mktemp)

# 1. Scarica gli IP di Cloudflare
echo "Scarico gli intervalli IP Cloudflare..."
curl -s $IPV4_URL > $TEMP_IPV4
if [ $? -ne 0 ]; then
    echo "ERRORE: Impossibile scaricare gli IP IPv4 di Cloudflare."
    rm -f $TEMP_IPV4 $TEMP_IPV6
    exit 1
fi

curl -s $IPV6_URL > $TEMP_IPV6
if [ $? -ne 0 ]; then
    echo "ERRORE: Impossibile scaricare gli IP IPv6 di Cloudflare."
    rm -f $TEMP_IPV4 $TEMP_IPV6
    exit 1
fi

# 2. Genera il nuovo file di configurazione Nginx
echo "Generazione del file di configurazione Nginx..."
cat <<EOF > $NGINX_ALLOW_CONF
# Aggiornato da script il $(date)
#
# Permetti solo il traffico Cloudflare (IPv4)
$(cat $TEMP_IPV4 | sed 's/^/allow /g; s/$/;/g')

# Permetti solo il traffico Cloudflare (IPv6)
$(cat $TEMP_IPV6 | sed 's/^/allow /g; s/$/;/g')

# Blocca tutto il traffico restante
deny all;
EOF

# 3. Pulisci i file temporanei
rm -f $TEMP_IPV4 $TEMP_IPV6
```

Lo script crea un file dentro la /etc/nginx/conf.d/ chiamato cloudflare\_allow\_ips.conf che avrà questa sintassi

```
# Aggiornato da script il Thu Dec 11 18:55:48 UTC 2025
#
# Permetti solo il traffico Cloudflare (IPv4)
allow 173.245.48.0/20;
allow 103.21.244.0/22;
allow 103.22.200.0/22;
allow 103.31.4.0/22;
allow 141.101.64.0/18;
allow 108.162.192.0/18;
allow 190.93.240.0/20;
allow 188.114.96.0/20;
allow 197.234.240.0/22;
allow 198.41.128.0/17;
allow 162.158.0.0/15;
allow 104.16.0.0/13;
allow 104.24.0.0/14;
allow 172.64.0.0/13;
allow 131.0.72.0/22;

# Permetti solo il traffico Cloudflare (IPv6)
allow 2400:cb00::/32;
allow 2606:4700::/32;
allow 2803:f800::/32;
allow 2405:b500::/32;
allow 2405:8100::/32;
allow 2a06:98c0::/29;
allow 2c0f:f248::/32;

# Blocca tutto il traffico restante
deny all;
```

Il file dovrà successivamente essere inserito nel blocco *http* della configurazione di nginx (/etc/nginx/nginx.conf) se si vuole che le impostazioni vengano implementate su tutti i virtual host, diversamente dovranno essere inserite nei blocchi di configurazioni del singolo virtual host.

### Migliorie aggiuntive

Sebbene CF aggiunga molti di questi headers ritengo essere importante aggiungerli comunque alle configurazioni originali: questo perchè laddove si volesse anche solo momentaneamente bypassare il proxy, si garantirebbe un buon livello di sicurezza crittografica di transito.

#### Headers

```
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Permissions-Policy "interest-cohort=()" always; # blocca FLoC
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
```

#### TLS

Limitate le versioni TLS, andando a deprecare quelle obsolete

```
ssl_protocols TLSv1.2 TLSv1.3;
```

#### Cipher

```
ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
```

## I problemi

Per il momento abbiamo esplorato come limitare tutte le connessioni in ingresso sull’nginx: tuttavia questo non è sufficiente in quanto il server, se un attaccante fosse in grado di scoprire il vero indirizzo dietro il WAF (in seguito vedremmo un esempio pratico di come fare), accetterà comunque tutte le connessioni in ingresso rendendolo di fatto passibile ad attacchi di tipo DDoS, SSRF, Amplification, etc.

![](https://blog.lobsec.com/wp-content/uploads/2025/12/image-1024x183.png)

Dimostrazione di come le connessioni dirette all’IP reale del server non vengano bloccate

La soluzione ottimale è quella di agire direttamente sul firewall di sistema, andando a bloccare immediatamente il traffico in ingresso laddove si dovesse presentare da un IP non appartenente alla CDN.

## Cloudflare e IPTables

Lo script in bash scarica gli intervalli IP di Cloudflare (IPv4 e IPv6) e aggiunge le regole corrispondenti a `iptables` e `ip6tables` per permettere solo il traffico in ingresso proveniente da quegli indirizzi sulle porte 80 (HTTP) e 443 (HTTPS).

Lo script include anche una funzione per pulire le regole precedenti prima di aggiungere le nuove, rendendolo ideale per l’esecuzione periodica (ad esempio, tramite `cron`).

```
#!/bin/bash

# ===============================================
# Configurazione
# ===============================================
IPTABLES_V4_URL="https://www.cloudflare.com/ips-v4/"
IPTABLES_V6_URL="https://www.cloudflare.com/ips-v6/"
LOG_FILE="/var/log/cloudflare_iptables.log"
# Iniziale delle catene personalizzate per una facile pulizia
IPT_CHAIN="CLOUDFLARE_V4"
IP6T_CHAIN="CLOUDFLARE_V6"

# Porte da permettere
PORTS="80,443"

# ===============================================
# Funzioni
# ===============================================

# Funzione per loggare i messaggi
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Funzione per pulire le regole esistenti di Cloudflare
cleanup_existing_rules() {
    log "Pulizia delle catene e delle regole esistenti di Cloudflare..."

    # 1. Pulizia catena IPv4 (iptables)
    iptables -D INPUT -p tcp -m multiport --dports "$PORTS" -j "$IPT_CHAIN" 2>/dev/null
    iptables -F "$IPT_CHAIN" 2>/dev/null
    iptables -X "$IPT_CHAIN" 2>/dev/null

    # 2. Pulizia catena IPv6 (ip6tables)
    ip6tables -D INPUT -p tcp -m multiport --dports "$PORTS" -j "$IP6T_CHAIN" 2>/dev/null
    ip6tables -F "$IP6T_CHAIN" 2>/dev/null
    ip6tables -X "$IP6T_CHAIN" 2>/dev/null

    log "Pulizia completata."
}

# Funzione principale per aggiornare le regole
update_cloudflare_rules() {
    # 1. Creazione catene personalizzate
    iptables -N "$IPT_CHAIN" || log "La catena $IPT_CHAIN esiste già o errore nella creazione."
    ip6tables -N "$IP6T_CHAIN" || log "La catena $IP6T_CHAIN esiste già o errore nella creazione."

    # 2. Aggiunta delle regole alle catene INPUT (solo se non esistono già)
    # L'uso di "-C" (Check) è più sicuro
    if ! iptables -C INPUT -p tcp -m multiport --dports "$PORTS" -j "$IPT_CHAIN" 2>/dev/null; then
        iptables -I INPUT -p tcp -m multiport --dports "$PORTS" -j "$IPT_CHAIN"
        log "Regola di salto IPv4 aggiunta alla catena INPUT."
    else
        log "Regola di salto IPv4 già esistente nella catena INPUT."
    fi

    if ! ip6...