---
title: TREVORspray – Credential Spray Toolkit for Azure, Okta, OWA & More
url: https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2025-07-15
fetch_date: 2025-10-06T23:17:03.031606
---

# TREVORspray – Credential Spray Toolkit for Azure, Okta, OWA & More

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# TREVORspray – Credential Spray Toolkit for Azure, Okta, OWA & More

July 14, 2025

Views: 675

**TREVORspray** is a purpose-built password spraying utility designed for red teams and offensive security operators conducting credential-based attacks across modern authentication systems. Developed and maintained by Black Lantern Security, it supports services such as Microsoft 365, Okta, and Outlook Web Access (OWA), offering precise control, stealth options, and modern detection evasion capabilities for password guessing campaigns.

![TREVORspray - Credential Spray Toolkit for Azure, Okta, OWA & More](https://www.darknet.org.uk/wp-content/uploads/2025/07/TREVORspray-Credential-Spray-Toolkit-for-Azure-Okta-OWA-More-640x427.jpg)

## Overview

Password spraying remains a popular initial access vector, especially in hybrid or cloud-first organisations using single sign-on (SSO) or federated identity systems. TREVORspray is designed to optimise this vector by supporting multi-target services while avoiding account lockouts and noisy logging. It builds on the experience of previous tools like MailSniper and Burp macros, while modernising the delivery and targeting mechanisms for 2024 and beyond.

## Supported Services

TREVORspray supports multiple authentication providers, making it suitable for varied environments:

* Microsoft 365 login via Azure Active Directory
* Okta SSO portals
* Outlook Web Access (OWA)
* Generic login forms (via POST profiles)

This broad support allows red teams to perform credential spraying across organisations with different cloud configurations or legacy on-prem services using a consistent interface.

## Key Features

* Throttle logic to avoid account lockouts
* Detailed logging and reporting on valid credentials
* Configurable HTTP POST profiles for custom endpoints
* Proxy and user-agent support for obfuscation
* Fails open on service anomalies to avoid hard stops

The tool also includes a YAML-based configuration setup, which allows the reuse of common scenarios and easy automation across red team engagements.

## Detection Avoidance Tactics

TREVORspray includes several built-in evasion techniques such as randomised User-Agent strings, time-based throttling, and adaptive retries to bypass lockout thresholds and reduce SIEM alerts. These tactics help it blend into regular login activity, mainly when attacks are distributed across multiple IPs or proxies.

In addition, TREVORspray’s support for Okta and OWA provides operators with access to portals that often lack the brute-force protections enforced on Microsoft login endpoints, making it more effective than older tools limited to a single login domain.

## Use Case in Red Team Campaigns

Credential spraying remains highly effective in enterprise environments, especially when paired with password reuse or exposed credential lists from data breaches. During red team assessments, TREVORspray allows operators to scale these attacks without alerting SOCs, provided they follow best practices for timing and endpoint selection.

It is beneficial in pre-phishing phases, where valid email-password combinations can be harvested and reused for lateral movement or mailbox exploitation. When combined with phishing payloads, valid credentials also enable OAuth token theft or MFA fatigue-style attacks.

## Installing & Using TREVORspray

To install TREVORspray:

pip install git+https://github.com/blacklanternsecurity/trevorproxy

|  |  |
| --- | --- |
| 1 | pip install git+https://github.com/blacklanternsecurity/trevorproxy |

Example:  Spray against discovered “token\_endpoint” URL

trevorspray -u emails.txt -p 'Welcome123' --url https://login.windows.net/b439d764-cafe-babe-ac05-2e37deadbeef/oauth2/token

|  |  |
| --- | --- |
| 1 | trevorspray -u emails.txt -p 'Welcome123' --url https://login.windows.net/b439d764-cafe-babe-ac05-2e37deadbeef/oauth2/token |

And full usage options:

$ trevorspray --help
usage: trevorspray &#91;-h] &#91;-m {owa,okta,auth0,anyconnect,jumpcloud,adfs,msol,example}] &#91;-up USERPASS &#91;USERPASS ...]] &#91;-u USERS &#91;USERS ...]] &#91;-p PASSWORDS &#91;PASSWORDS ...]] &#91;--url URL]
&#91;-r DOMAIN] &#91;--export-tenants FILE] &#91;-t THREADS] &#91;-f] &#91;-d DELAY] &#91;-ld LOCKOUT\_DELAY] &#91;-j JITTER] &#91;-e] &#91;-nl] &#91;--ignore-lockouts] &#91;--timeout TIMEOUT] &#91;--random-useragent]
&#91;-6] &#91;--proxy PROXY] &#91;-v] &#91;-s USER@SERVER &#91;USER@SERVER ...]] &#91;-i KEY] &#91;-b BASE\_PORT] &#91;-n] &#91;--subnet SUBNET] &#91;--interface INTERFACE]
A password sprayer with the option to load-balance traffic through SSH hosts
options:
-h, --help show this help message and exit
basic arguments:
-m, --module {owa,okta,auth0,anyconnect,jumpcloud,adfs,msol,example}
Spray module to use (default: msol)
-up, --userpass USERPASS &#91;USERPASS ...]
file(s) containing username and password pairs (format: 'username:password')
-u, --users USERS &#91;USERS ...]
Usernames(s) and/or file(s) containing usernames
-p, --passwords PASSWORDS &#91;PASSWORDS ...]
Password(s) and/or file(s) containing passwords
--url URL The URL to spray against
-r, --recon, --enumerate DOMAIN
Retrieves MX records and info related to authentication, email, Azure, Microsoft 365, etc. If --usernames are specified, this also enables username enumeration.
--export-tenants FILE
Export all discovered tenant domains to a file
advanced arguments:
Round-robin traffic through remote systems via SSH (overrides --threads)
-t, --threads THREADS
Max number of concurrent requests (default: 1)
-f, --force Try all usernames/passwords even if they've been tried before
-d, --delay DELAY Sleep for this many seconds between requests
-ld, --lockout-delay LOCKOUT\_DELAY
Sleep for this many additional seconds when a lockout is encountered
-j, --jitter JITTER Add a random delay of up to this many seconds between requests
-e, --exit-on-success
Stop spray when a valid cred is found
-nl, --no-loot Don't execute loot activites for valid accounts
--ignore-lockouts Forces the spray to continue and not stop when multiple account lockouts are detected
--timeout TIMEOUT Connection timeout in seconds (default: 10)
--random-useragent Add a random value to the User-Agent for each request
-6, --prefer-ipv6 Prefer IPv6 over IPv4
--proxy PROXY Proxy to use for HTTP and HTTPS requests
-v, --verbose, --debug
Show which proxy is being used for each request
SSH Proxy:
Round-robin traffic through remote systems via SSH (overrides --threads)
-s, --ssh USER@SERVER &#91;USER@SERVER ...]
Round-robin load-balance through these SSH hosts (user@host) NOTE: Current IP address is also used once per round
-i, -k, --key KEY Use this SSH key when connecting to proxy hosts
-b, --base-port BASE\_PORT
Base listening port to use for SOCKS proxies
-n, --no-current-ip Don't spray from the current IP, only use SSH proxies
Subnet Proxy:
Send traffic from random addresses within IP subnet
--subnet SUBNET Subnet to send packets from
--interface INTERF...