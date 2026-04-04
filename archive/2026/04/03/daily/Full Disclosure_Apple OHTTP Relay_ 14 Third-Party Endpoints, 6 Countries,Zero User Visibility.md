---
title: Apple OHTTP Relay: 14 Third-Party Endpoints, 6 Countries,	Zero User Visibility
url: https://seclists.org/fulldisclosure/2026/Apr/2
source: Full Disclosure
date: 2026-04-03
fetch_date: 2026-04-04T04:17:51.781509
---

# Apple OHTTP Relay: 14 Third-Party Endpoints, 6 Countries,	Zero User Visibility

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# Apple OHTTP Relay: 14 Third-Party Endpoints, 6 Countries, Zero User Visibility

---

*From*: Joseph Goydish II via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 22 Mar 2026 03:43:13 +0000

---

```
SUMMARY

Apple's Oblivious HTTP relay for Live Caller ID Lookup (iOS 18+) routes
traffic through 14 third-party endpoints across six countries. These include
an anonymous Delaware LLC sharing data with OpenAI, a Russian endpoint
(Yandex), and a Swiss GmbH whose privacy policy names "The Legal Entity to
be Confirmed" as its data controller. None of this is disclosed to users.

This is shared infrastructure. All devices using Live Caller ID Lookup
connect to these providers.

AFFECTED SYSTEMS

All iPhones running iOS 18+ with Live Caller ID Lookup enabled. Apple's
networkserviceproxy daemon executes 98 scheduled background tasks over
48 hours on a 12-hour timer. Caller ID lookups are event-driven (incoming
calls). The timer pattern is inconsistent with stated function.

ENDPOINTS

Extracted from sysdiagnose on three production iPhones (A14, A16, A17 Pro),
March 19-21, 2026. UUIDs persistent across captures.

1. Taiwan Mobile Co., Ltd. — osbstage.twmsolution (Taiwan)
TWSE:3045. Market cap ~$12.9B USD. Fubon Group (Tsai family).
Enterprise arm TWM Solution (Taiwan Fixed Network, AS9924).
UUID C56B1AED-20FE-4B7D-B1EA-D791DA57A549. Terminal relay node.
CT logs show ohttp.osb.twmsolution.com and pir.osb.twmsolution.com
certs issued 2026-03-17/18 by Google Trust Services (WR3).
twmsolution.com registered 2008-01-22, nameservers dns1.tfn.net.tw.
Prior incident: Amazing A32 trojan — factory-installed Chinese malware
on 94,191 subscriber devices (2018-2021), NCC ordered full recall.

2. StopScam LLC — pir.stopscam.ai / ohttp.stopscam.ai (USA, Delaware)
254 Chapman Rd, Suite 208 #20663, Newark, DE 19702.
Registered agent: Republic Registered Agents LLC (Suite 209, same bldg).
No named officers. No humans in any public record.
Apple Developer ID 1795482410. App Store ID 6741771102.
Also publishes "Pray Bible: Daily Prayer" and "Evaari: Daily Journal."
76 CT certs since Nov 2024 including n8n.stopscam.ai (workflow
automation — consistent with data pipeline, not caller ID).
Privacy policy discloses data sharing with OpenAI and Google Cloud.
Privacy policy currently returns HTTP 404. Terms of use hosted on
free Google Sites page. Founded 2024. App v1.0 released 2025-02-20.
IP: 108.181.161.154 (AS40676 Psychz Networks, Dallas TX).
LIVE 2026-03-22: 3 Blind RSA token keys serving. OHTTP gateway active.

3. Kaylee Calderolla / Wipr — pir.kaylees.site (Italy)
Independent developer. Wipr 2 content blocker, 10+ years on App Store.
Apple Developer ID 379876189. Registered business: IMI DI KAYLEE
SERENA CALDEROLLA. P.IVA 04788820266. REA-TV 378040.
Conegliano, Treviso, Veneto, Italy. ATECO 62.02.00 (IT consulting).
CT cert 3019124466 (2020-06-30): CN=giorgiocalderolla.com,
SAN=kaylees.site — ties both identities to same server.
PIR subdomains (pirgateway, pirissuer, pir) appeared August 2025.
IP: 97.107.140.40 (AS63949 Akamai/Linode, NJ).
LIVE 2026-03-22: 3 Blind RSA token keys serving.
Publicly identifiable. Legitimate URL Filter provider enrollment.

4. Aura / Pepper AI — urlfilter.pepperai.aurasvc.io (USA)
Parent of Hotspot Shield, Identity Guard, Betternet.
urlfilter prefix = content filtering. Present in 5/15 Persist files.

5. Yandex — ios-service.cid.yandex.net (Russia)
Russia's largest search engine. Subject to Yarovaya Law (2016) —
metadata/content retention, FSB access. Both ObliviousHop and
ObliviousHopFallback entries with two distinct UUIDs and session keys.

6. Uney GmbH / AutoSec — issuer.autosec.com (Switzerland/UAE/Vietnam)
Baarerstrasse 25, 6300 Zug. Formerly "Quantum Advantage + flyingSwiss
GmbH." Database operated by Smart Artificial Intelligence L.L.C,
Floor 3, H Office Tower, Dubai, UAE. Operations in Ho Chi Minh City.
Shareholder: Roger Daniel Wehrli (200 shares), resides Bangkok.
CTO: Tamas Zumpf. Developer: Phu Hieu Van (UAE).
App Store ID 6738410298. App has 2 total ratings.
Privacy policy data controller: "The Legal Entity to be Confirmed" —
unchanged for 5 months since publication. Collects call metadata,
contact lists, installed apps, SIM info, location, device IDs.
Transfers to "countries including but not limited to India."
EU policy omits India disclosure. No DPO named. No sub-processors.
Language support: Filipino, Indonesian, Thai, Vietnamese.
autosec.com domain registered 2001 (acquired ~2025).
All press releases originate from Dubai, not Zug.
Both primary and fallback OHTTP entries present.

7. Truecaller — privacy-pass-issuer-eu.truecaller.com (Sweden)
Major caller ID service. EU Privacy Pass issuer.

8. Carrement — antispam.carrement.ai (France)
18 Rue Bailey, 14000 Caen. Product: DialogPro (dialogpro.ai).
No named team. Minimal web presence. Hosted AWS Canada.

9. NordVPN — caller-id-issuer.nordvpn.com (Panama/Lithuania)
Consumer VPN provider. Caller ID issuer endpoint.

10. Google — aiplatform.googleapis.com (USA)
AI Platform API. ObliviousHop entry with UUID and session key.

11. Google — safebrowsing.googleapis.com (USA)
Safe Browsing API.

12. Google — generativelanguage.googleapis.com (USA)
Gemini / generative AI API.

13. Google — additional googleapis.com endpoint (USA)
See repository for full list.

14. Google — additional googleapis.com endpoint (USA)
See repository for full list.

VERIFICATION

No jailbreak. No special tooling. Three commands:

$ curl -s https://pir.stopscam.ai/.well-known/private-token-issuer-directory | python3 -m json.tool
$ curl -s https://pir.kaylees.site/.well-known/private-token-issuer-directory | python3 -m json.tool
$ curl -s https://ohttp.stopscam.ai/ohttp-configs | xxd | head -5

CT logs (tamper-proof, public):
https://crt.sh/?q=stopscam.ai (76 certs)
https://crt.sh/?q=kaylees.site (82 certs)
https://crt.sh/?q=%25.twmsolution.com (ohttp/pir subdomains visible)

Confirmed live 2026-03-22 03:32 UTC:
pir.stopscam.ai — HTTP 200, nginx/1.18.0 (Ubuntu), 3 token keys
pir.kaylees.site — HTTP 200, nginx/1.28.2, 3 token keys
ohttp.stopscam.ai — OHTTP gateway config returned

METHODOLOGY

Sysdiagnose captures from iPhone 12 (D53gAP, A14, iOS 26.3.1, AT&T).
62 tracev3 files scanned per capture. Relay indicators in 5/15 Persist
files. Provider domains identified via ObliviousHop-%@ and
ObliviousHopFallback-%@ routing strings with runtime-substituted domains.

Sample offsets (Persist/0xFFFFFFFFFFFF8019.tracev3):
0x06E617 urlfilter.pepperai.aurasvc.io + UUID
0x06E84D osbstage.twmsolution + UUID C56B1AED...
0x06E9E9 kaylees.site + UUID F57473C4...
0x06F19F stopscam.ai + UUID FFBCAD60...
0x06BC83 ObliviousHopFallback-ios-service.cid.yandex.net + session key
0x0C876A ObliviousHop-aiplatform.googleapis.com + session key

TIMELINE

2026-02 Apple PSIRT notified (Ticket OE0104868731498)
2026-02 CISA notified (two VRF tickets)
2026-02 FBI Cyber Division notified (CyWatch + regional)
2026-02 thru 2026-03-21 No substantive response
2026-03-21 Public disclosure (GitHub)
2026-03-12 Full Disclosure mailing list

https://github.com/JGoyd/Fourteen_Endpoints

REFERENCES

RFC 9576 — Privacy Pass Architecture
RFC 9578 — Privacy Pass Issuance Protocol
Apple developer docs:...