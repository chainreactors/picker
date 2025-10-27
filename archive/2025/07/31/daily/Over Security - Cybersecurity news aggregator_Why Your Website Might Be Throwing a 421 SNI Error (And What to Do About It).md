---
title: Why Your Website Might Be Throwing a 421 SNI Error (And What to Do About It)
url: https://blog.sucuri.net/2025/07/why-your-website-might-be-throwing-a-421-sni-error-and-what-to-do-about-it.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-31
fetch_date: 2025-10-06T23:53:39.622491
---

# Why Your Website Might Be Throwing a 421 SNI Error (And What to Do About It)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [HTTP Errors](https://blog.sucuri.net/category/http-errors)
* [Security Education](https://blog.sucuri.net/category/security-education)

# Why Your Website Might Be Throwing a 421 SNI Error (And What to Do About It)

[![](https://secure.gravatar.com/avatar/a4279e88699c65065bb98c4cdfe5a2b6d92871222bf48497bb57af68b2ef6019?s=60&d=mm&r=g)](https://blog.sucuri.net/author/marc2)

[Marc Kranat](https://blog.sucuri.net/author/marc2)

* July 30, 2025

![Why Your Website Might Be Throwing a 421 SNI Error](https://blog.sucuri.net/wp-content/uploads/2025/07/Why-Your-Website-Might-Be-Throwing-a-421-SNI-Error-820x410.png)

So, your support team is suddenly flooded with tickets about “421 Misdirected Request” errors, and you’re wondering if the internet is just having a bad day. Spoiler: it’s not. But Apache might be.

Let’s break down what’s going on, why it’s happening now, and how to fix it—whether you’re using Plesk, cPanel, or flying solo with your own Apache setup.

## What Is a 421 SNI Error Anyway?

The HTTP 421 “Misdirected Request” error is Apache’s way of saying:

*“Hey, I wasn’t expecting **you** on this connection.”*

This happens when the **Server Name Indication (SNI)** in the TLS handshake doesn’t match the hostname Apache is expecting. In simpler terms, Apache gets confused when it receives a request without knowing which site it’s supposed to serve, especially when multiple sites are hosted on the same IP.

## A Brief History of SNI

SNI was introduced to solve the problem of hosting multiple HTTPS sites on a single IP address. Before SNI, each HTTPS site needed its own IP. With SNI, the client tells the server which hostname it wants during the TLS handshake, so Apache can serve the right certificate and content.

But here’s the kicker: if the client (like nginx) doesn’t pass the hostname correctly, Apache throws a tantrum—cue the 421 error.

## Why Is This Happening Now?

Recent Apache updates (notably 2.4.64) introduced stricter handling of SNI to patch several CVEs. These changes mean Apache now refuses to serve requests that don’t include a valid SNI header. This is great for security, but it’s also breaking things left and right.

### CVEs Behind the Curtain

The Apache update addressed multiple CVEs, including:

* **CVE-2024-38474:** Improper SNI handling in reverse proxy scenarios
* **CVE-2024-38475:** TLS hostname confusion leading to potential MITM
* **CVE-2024-38476:** Misrouting of requests in multi-tenant environments

## How to Confirm It’s the Host’s Fault

Here’s a quick terminal test to see if the issue is with the backend Apache server replacing the domain and host IP with your own:

```
curl -IkH 'host:domain.com' https://192.168.0.1
```

If you get a `421`, the server isn’t handling SNI properly. If you get a `200`, the issue lies elsewhere.

## Fixes for the 421 Error

### ✅ If You’re Using Plesk

Plesk has released hotfixes in versions **18.0.70.3** and **18.0.71.1**. If you’re on an older version, you can manually patch it by adding the following to your nginx config:

```
proxy_ssl_server_name on;
proxy_ssl_name $host;
proxy_ssl_session_reuse off;
```

Then restart nginx:

```
systemctl restart nginx
```

[Full Plesk article →](https://support.plesk.com/hc/en-us/articles/33500191748887-Websites-hosted-in-Plesk-are-not-accessible-after-a-recent-Apache-update-421-Misdirected-Request)

### ✅ If You’re Using cPanel

cPanel temporarily rolled back the Apache update in **ea-apache24-2.4.64-3** and recommends updating via:

```
/scripts/upcp
```

Or manually:

```
dnf update ea-*   # AlmaLinux
yum update ea-*   # CentOS
apt upgrade       # Ubuntu
```

[Full cPanel article →](https://support.cpanel.net/hc/en-us/articles/33724988525207-Websites-experiencing-421-Misdirected-requests-after-upgrading-to-CloudLinux-s-ea-apache24-2-4-64)

### If You’re Not Using Plesk or cPanel

You’ll need to manually ensure that your reverse proxy (nginx, HAProxy, etc.) is passing the correct SNI headers. In nginx, that means:

```
proxy_ssl_server_name on;
proxy_ssl_name $host;
proxy_ssl_session_reuse off;
```

Also, double-check that your Apache virtual hosts are configured with `ServerName` and `ServerAlias` directives that match the expected hostnames.

## Bonus: What We Did Internally

Our security team enabled **“force hostname over TLS”** on all sites using our WAF. This ensures that even if we connect directly to a misconfigured Apache server, we’re still sending the correct SNI. It’s a belt-and-suspenders approach, and it’s working well so far.

## Final Thoughts

This is one of those “security update meets real-world chaos” moments. The fix is simple once you know what’s going on–but until then, it’s a head-scratcher. Hopefully, this post saves you a few...