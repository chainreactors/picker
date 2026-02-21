---
title: SigmaWare Stealer Analysis - Intelshare
url: https://www.intelshare.me/posts/sigmaware.html
source: Over Security - Cybersecurity news aggregator
date: 2026-02-20
fetch_date: 2026-02-21T04:00:58.784560
---

# SigmaWare Stealer Analysis - Intelshare

[Intelshare](../index.html)

[ABOUT](../about.html)
[RESEARCH](../research.html)
[BLOG](../blog.html)

# // MALWARE INTELLIGENCE

SigmaWare Stealer

DATE:
February 14, 2026

CATEGORY:
MALWARE Intelligence

Investigation of suspicious samples on VirusTotal revealed multiple malicious files communicating
with infrastructure linked to **SigmaWare Stealer**, a commercial information stealer
distributed within underground communities.

Static and behavioral analysis confirms credential theft, screen capture,
and surveillance capabilities matching SigmaWare’s advertised features.

## VirusTotal Sample Evidence

Basic sample information observed in VirusTotal:

![](../Images/VT%20screenshot%20basic.png)

Behavioral execution showing stealer activities:

![](../Images/VT%20%20behavior.png)

## Advertised Capabilities

The malware dashboard advertises capabilities including:

* Live screen capture
* Remote screenshots
* File theft
* Network credential stealing
* Anti-VM and sandbox bypass

![](../Images/sigmware%20dashboard.png)

## Operator Attribution

The operation appears linked to underground actor **hasar0001**,
active on cybercrime forums and marketplaces.

![](../Images/sigmwarelolzprofile.png)

Telegram infrastructure used for communication:

https://t.me/hasar0001
https://t.me/sigmawarecc

![](../Images/sigmawaretgaccount.png)

## Panel Country Lock Feature

User of Sigmaware can restrict panel login to selected countries.

![](../Images/sigmwareallowcountrylock.png)

## Indicators of Compromise

01a49dff1a0b7a80662bab088204cc19ef728926c677bd147d93959bddfd881f

3d81d7c34040cf7eef01263d38d819331dc717b377c2b590b1538cdb25c7404e

e978a9f59e82c82775c0dd4da03971396d782c5cd9047b15228a458cc42b70b2

a8ae3c5ecaf6e261d4a46ec30ea88ee72b8a81f83440f73cd88a3a5fbf6c102f

sigmaware[.]store

## Conclusion

SigmaWare operates as a commercial stealer platform providing credential theft
and surveillance functionality. Observed telemetry and OSINT correlations indicate
active underground distribution.

[← BACK TO BLOG](../blog.html)

Intelshare

© 2026 Intelshare - Cyber Threat Intelligence Research