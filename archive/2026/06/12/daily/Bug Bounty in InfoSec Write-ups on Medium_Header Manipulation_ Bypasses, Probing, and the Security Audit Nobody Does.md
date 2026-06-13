---
title: Header Manipulation: Bypasses, Probing, and the Security Audit Nobody Does
url: https://infosecwriteups.com/header-manipulation-bypasses-probing-and-the-security-audit-nobody-does-62e85ad28cb0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-12
fetch_date: 2026-06-13T06:10:09.505834
---

# Header Manipulation: Bypasses, Probing, and the Security Audit Nobody Does

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fheader-manipulation-bypasses-probing-and-the-security-audit-nobody-does-62e85ad28cb0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fheader-manipulation-bypasses-probing-and-the-security-audit-nobody-does-62e85ad28cb0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-62e85ad28cb0---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-62e85ad28cb0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Header Manipulation: Bypasses, Probing, and the Security Audit Nobody Does

## *Request headers are not metadata. They are inputs, and inputs can be manipulated.*

[![Roshan Rajbanshi](https://miro.medium.com/v2/resize:fill:64:64/1*dXjfhSqh-q_u_X4OBuJUpQ.png)](https://medium.com/%40roshanrajbanshi2022?source=post_page---byline--62e85ad28cb0---------------------------------------)

[Roshan Rajbanshi](https://medium.com/%40roshanrajbanshi2022?source=post_page---byline--62e85ad28cb0---------------------------------------)

11 min read

·

23 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D62e85ad28cb0&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fheader-manipulation-bypasses-probing-and-the-security-audit-nobody-does-62e85ad28cb0&source=---header_actions--62e85ad28cb0---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

> ***Series:*** *curl — The Request Engine You Never Learned Properly* ***Article:*** *7 of 16*

Request headers are not just metadata. They are inputs. And like any input that reaches server-side logic, they can be manipulated — to bypass access controls, probe for misconfigurations, spoof identity, and test security posture.

This article covers the header manipulation techniques that show up constantly on THM/HTB machines and in real web application testing: Host header attacks, IP spoofing headers, 403 bypass patterns, CORS misconfiguration testing, and the security header audit that most beginners skip entirely.

Most techniques here are one flag or one `-H` addition away from a curl command you already know how to write.

## The `-H` Flag as an Attack Surface

You have used `-H` for Content-Type and Authorization. The same flag is the entry point for every manipulation technique in this article.

```
curl -H "Header-Name: value" http://target.com
```

A header is just a key-value pair sent as part of the HTTP request. The server reads it and acts on it — or ignores it. Your job is to find the headers that affect server behavior in ways the developer did not intend.

Multiple `-H` flags stack. This single command sends three attack-relevant headers simultaneously:

```
curl -H "X-Forwarded-For: 127.0.0.1" \
     -H "X-Real-IP: 127.0.0.1" \
     -H "Host: internal.target.com" \
     http://127.0.0.1:8080/admin
```

```
==================================================
  curl Lab Echo Server
==================================================
METHOD       : GET
PATH         : /admin
FULL URL     : /admin
--- REQUEST HEADERS ---
  Host: internal.target.com
  User-Agent: curl/7.68.0
  Accept: */*
  X-Forwarded-For: 127.0.0.1
  X-Real-IP: 127.0.0.1
--- QUERY STRING PARAMS ---
  (none)
--- RAW BODY ---
  (empty)
--- PARSED BODY PARAMS ---
  (none)
==================================================
```

Press enter or click to view image in full size

![]()

Three attack headers, one command. The echo server shows `Host` overridden to an internal hostname and both IP headers spoofed — exactly as sent, no browser normalisation stripping the payload.

curl sends exactly what you specify. The echo server confirms all three headers arrived intact at the application layer — `Host` overridden, both IP headers spoofed. That said, in real deployments, proxies, load balancers, and application frameworks may rewrite or strip certain headers before they reach the application. What curl sends and what the application ultimately reads are not always identical.

## Host Header Attacks

The `Host` header tells the server which virtual host to serve. On servers running multiple sites, this is how the server knows which application to route the request to.

Manipulating the `Host` header — and its override cousin `X-Forwarded-Host` — lets you probe for virtual hosts that are not publicly advertised:

```
curl -H "Host: internal.target.com" http://target.com
curl -H "Host: admin.target.com" http://target.com
curl -H "Host: dev.target.com" http://target.com
curl -H "Host: staging.target.com" http://target.com
curl -H "X-Forwarded-Host: admin.target.com" http://target.com
```

Run each and compare response sizes and content against the baseline. A response that differs — in size, content, or status code — indicates the server is routing to a different virtual host at that address. Internal applications, development environments, and admin interfaces are commonly found this way.

Beyond virtual host discovery, Host header manipulation is also the foundation of password reset poisoning (poisoning the reset link generated server-side) and cache poisoning (storing a malicious response under a legitimate cache key). Those are covered in depth elsewhere — the recon step here is the same.

`--resolve` **for clean DNS mapping:**

When you want to test a specific IP address with a custom hostname, without modifying `/etc/hosts`:

```
curl --resolve target.com:80:192.168.1.100 http://target.com
curl --resolve admin.target.com:443:192.168.1.100 https://admin.target.com
```

`--resolve host:port:ip` tells curl to resolve that hostname to that IP for this request only. No system-wide DNS change, no file modification, no cleanup needed.

## IP Restriction Bypass: X-Forwarded-For and X-Real-IP

Some applications restrict access based on the client’s IP address. “Only allow requests from 127.0.0.1” or “only allow requests from internal network ranges” are common access control patterns.

When a reverse proxy sits in front of the application, the application may read the client’s IP from the `X-Forwarded-For` header rather than the TCP connection's source address. `X-Forwarded-For` is a de facto standard and typically carries a comma-separated list of addresses — the client IP, then each proxy in the chain. If the application trusts this header without validation and reads the first value in the list, you can prepend a spoofed IP.

```
curl -s -H "...