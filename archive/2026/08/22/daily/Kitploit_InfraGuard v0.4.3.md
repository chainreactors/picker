---
title: InfraGuard v0.4.3
url: https://kitploit.com/en/posts/github-whispergate-infraguard-v043
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:56:58.482141
---

# InfraGuard v0.4.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13111/647e44e4a50935ac1c3c0b10bef42ec8906b897938a005928fc01537f6a57837.png)

New releaseAug 22, 2026

# InfraGuard v0.4.3

InfraGuard is a Command & Control Redirection Proxy and Manager which protects your Red Team Infrastructure against threat attribution

Share

![InfraGuard Logo](https://raw.githubusercontent.com/whispergate/infraguard/HEAD/images/infraguard_logo.svg)

Red team infrastructure tracker and C2 redirector -- a modern alternative to [RedWarden](https://github.com/mgeeky/RedWarden).

InfraGuard sits between the internet and your C2 teamserver, validating every inbound request against your malleable C2 profile and blocking anything that doesn't conform. Scanners, bots, and blue team probes get redirected to a decoy site while legitimate beacon traffic passes through to your teamserver.

![Mythic Callbacks Xenon](https://assets.kitploit.com/production/public/readmes/13111/138183b23f18b337f98125de6d7a1becdf8ac4d627f0f7511db4a9fb960c0da0.png)
![InfraGuard Dashboard](https://assets.kitploit.com/production/public/readmes/13111/3630e89649f317ab65d29811a9d6259f71c632607d076297e0c8f52a1a4af02a.png)

## Architecture

![Architecture Diagram](https://assets.kitploit.com/production/public/readmes/13111/647e44e4a50935ac1c3c0b10bef42ec8906b897938a005928fc01537f6a57837.png)

## Features

### Proxying & Listeners

* **Multi-domain proxying** -- proxy multiple domains simultaneously, each with independent C2 profiles, upstreams, and rules
* **Multi-protocol listeners** -- HTTP/HTTPS, DNS, MQTT, and WebSocket listeners running simultaneously with shared IP intelligence and event tracking
* **Circuit breaker** -- per-upstream failure protection with closed/open/half-open states; falls through to the domain's drop action when backends are unreachable
* **Protocol failover** -- automatic failover and failback between listener protocols ranked by priority

### C2 Profile Support

* **C2 profile validation** -- parse and enforce Cobalt Strike, Mythic, Brute Ratel C4, Sliver, Havoc, Nighthawk, and PoshC2 profiles as redirector rules
* **Hot-swappable profiles** -- swap a domain's active C2 profile at runtime from the dashboard without restarting the proxy
* **Profile generation wizard** -- generate new C2 profiles from scratch for all 8 supported types via a guided form, or import and upload existing profiles with automatic type detection and validation
* **AI-assisted profile generation** -- optional Ollama integration provides a chat panel in the dashboard for profile creation help and OPSEC advice

### Filter Pipeline

* **Scoring-based filter pipeline** -- 10 filters each contribute a 0.0--1.0 score; configurable threshold determines block/allow. Filters: JA3, IP, bot, header, DNS, geo, profile, replay, enumeration, sandbox.
* **JA3 TLS fingerprint filtering** -- block Masscan, ZGrab2, Shodan, curl, Python requests, and Nmap at the TLS handshake layer before any HTTP data is exchanged; works via reverse-proxy header or custom asyncio protocol; optional allowlist mode enforces beacon JA3
* **Sandbox and headless browser detection** -- score-accumulation across HTTP signals: HeadlessChrome UA, missing Accept-Language, Chrome without sec-ch-ua, Safe Links and msnbot scanner UAs, non-browser Accept ordering
* **Path enumeration detection** -- per-IP unique URI tracking in a sliding window; blocks dirbuster/ffuf/gobuster before they map URI space
* **DNS subdomain enumeration detection** -- tracks NXDOMAIN responses per client IP; auto-blocks source IPs on threshold breach
* **Anti-bot / anti-crawling** -- 40+ known scanner/bot User-Agent patterns, header anomaly detection
* **Replay protection** -- reject duplicate requests by content hash; hashes persisted to SQLite so protection survives restarts
* **Drop actions** -- redirect, TCP reset, proxy to decoy site, or tarpit (slow-drip response to waste scanner time)

### Intelligence

* **IP intelligence** -- built-in CIDR blocklists for 19 security vendor ranges (Shodan, Censys, Rapid7, etc.), GeoIP filtering, reverse DNS keyword matching
* **Threat intel feeds** -- auto-update blocklists from public sources (abuse.ch, Emerging Threats, Spamhaus DROP, Binary Defense) with configurable refresh interval and disk caching
* **Dynamic IP blocking** -- block IPs outside whitelisted ranges; auto-whitelist IPs after N valid C2 requests
* **Whitelist enrichment** -- whitelisted CIDRs are auto-enriched with ASN, organization, country, and continent data on startup via GeoIP databases
* **Burn detection** -- Certificate Transparency log monitoring via crt.sh, domain reputation self-monitoring via URLhaus/OpenPhish/Google Safe Browsing, and cross-domain analyst detection when a single IP accesses multiple operator domains
* **Burn confidence scoring** -- continuous 0--100 score from 6 weighted signals: JA3 diversity, volume spikes, new ASNs, CT log exposure, reputation hits, and failed auth attempts. Includes recommended actions: monitor, rotate, or immediate burn.
* **Canary token injection** -- tracking pixels, honeypot links, and honeypot forms auto-injected into decoy pages to detect blue team investigation
* **Passive DNS monitoring** -- polls CIRCL PDNS for external resolution of your domains; detects new records, NXDOMAIN spikes, and first-seen exposure

### Payload Delivery

* **Content delivery routes** -- serve payloads, decoys, and static files at specific paths via PwnDrop, Mythic file store, local filesystem, or HTTP proxy backends; optional conditional delivery to serve real content to targets and decoys to scanners
* **Mythic file staging** -- `mythic_file` backend proxies Mythic's `/direct/download/{uuid}` at clean URLs; fixed UUID or proxy mode; access control provided by InfraGuard's filter stack
* **One-time payload tokens** -- tokens issued automatically when a beacon is dynamically whitelisted; atomic single-use SQLite enforcement prevents URL replay by analysts or sandboxes; configurable TTL and max-use count
* **Per-route rate limiting** -- sliding-window per-IP download rate limiter on content routes; exceeding the limit serves the configured scanner decoy or 429
* **Delivery guards** -- environment keying for content routes: require beacon IP, UA allowlist, required header values, forbidden headers; failed checks serve domain drop action, not a raw 403
* **Phishing campaign tokens** -- gate phishing pages behind per-campaign tokens embedded in email links; static token list or HMAC-signed self-validating tokens with configurable TTL

### Resilience

* **Infrastructure rotation** -- one-click blue-green Terraform rotation across 5 cloud providers with pre-flight checks, rollback, and age-encrypted state
* **Rotation scheduling** -- automated rotation policies: fixed interval, burn-triggered, request-count threshold, and staggered rolling
* **Domain fronting** -- CDN-based C2 routing via SNI/Host header split with CDN header stripping and SSRF protection
* **Dead man's switch** -- operator heartbeat TTL that auto-stops C2 forwarding if the operator fails to check in
* **Edge proxies** -- Cloudflare Worker and AWS Lambda for domain fronting through CDN infrastructure, edge country blocking, and host rewriting

### Dashboard & Operator Tools

* **Web dashboard** -- real-time SPA with login page, live request feed, domain stats, top blocked IPs, WebSocket event streaming, and inline block/whitelist/unblock actions
* **Decoy page management** -- list, preview, and edit decoy HTML pages directly from the dashboard
* **Command Post** -- multi-instance aggregation dashboard that merges stats, requests, and live ...