---
title: SSRF in Anthropic mcp-server-fetch and Microsoft playwright-mcp — publicly disclosed via GitHub issues
url: https://seclists.org/fulldisclosure/2026/May/22
source: Full Disclosure
date: 2026-05-26
fetch_date: 2026-05-27T06:12:48.291098
---

# SSRF in Anthropic mcp-server-fetch and Microsoft playwright-mcp — publicly disclosed via GitHub issues

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SSRF in Anthropic mcp-server-fetch and Microsoft playwright-mcp — publicly disclosed via GitHub issues

---

*From*: outreach () posentia net
*Date*: Mon, 25 May 2026 20:10:43 +0000

---

```
-----BEGIN SECURITY ADVISORY-----

Title: Server-Side Request Forgery (SSRF) in Anthropic mcp-server-fetch and Microsoft playwright-mcp
Author: Syed Anas Mohiuddin <anasmohiuddinsyed () gmail com>
Date: May 25, 2026
CVSS: 7.5 (HIGH) — AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
References: Already public via GitHub issues (see below)

== AFFECTED PRODUCTS ==

1. Anthropic mcp-server-fetch (modelcontextprotocol/servers)
   All versions as of May 2026
   GitHub: https://github.com/modelcontextprotocol/servers
   Public issues: #4116, #4143, #4205

2. Microsoft playwright-mcp
   All versions as of May 2026
   GitHub: https://github.com/microsoft/playwright-mcp
   Public issue: #1626

== VULNERABILITY DESCRIPTION ==

Both MCP servers accept arbitrary URLs passed by the AI agent/client without
any allowlist enforcement, IP range blocking, or internal network filtering.
This enables Server-Side Request Forgery (SSRF) attacks via prompt injection:

Attack chain:
  1. Attacker embeds malicious instruction in a webpage
  2. AI agent fetches the page via mcp-server-fetch or playwright-mcp
  3. Embedded instruction redirects the agent to fetch the cloud metadata endpoint
  4. Agent calls fetch_url("http://169.254.169.254/latest/meta-data/iam/security-credentials/";)
  5. IMDSv1 returns IAM credentials without authentication
  6. Agent includes credentials in its next response
  7. Credentials exfiltrated

Additional finding in mcp-server-fetch:
The get_prompt handler calls fetch_url() directly without invoking
check_may_autonomously_fetch_url(), bypassing the robots.txt autonomy guard
through a structurally distinct code path (logic bypass).

== DISCOVERY ==

Found using mcp-safeguard, an open-source automated security scanner for MCP servers.
pip install mcp-safeguard
https://pypi.org/project/mcp-safeguard/

Scanning 54 production MCP servers: 27.8% had HIGH/CRITICAL findings.
8/54 (14.8%) confirmed SSRF. 7/54 credential exposure.

== DISCLOSURE TIMELINE ==

May 2026: Findings discovered via mcp-safeguard
May 2026: Reported to Anthropic Security (security () anthropic com)
May 2026: Reported to Microsoft MSRC (secure () microsoft com)
May 2026: Issues already publicly visible on GitHub (see References above)
May 2026: Public advisory posted to Full Disclosure

== MITIGATIONS ==

For MCP server operators:
- Enforce URL allowlists (only fetch from approved domains)
- Block RFC1918 and link-local ranges at the application layer
- Use IMDSv2 (requires session token; not fetchable via simple HTTP)
- Pin resolved IPs before making TCP connections (prevents DNS rebinding)
- Validate redirect destinations before following

For AI agent deployments:
- Review all MCP servers in your stack using mcp-safeguard
- Apply network-level SSRF mitigations (cloud security groups, VPC policies)
- Disable IMDSv1 on all EC2 instances

== REFERENCES ==

Public GitHub issues (already disclosed):
- https://github.com/modelcontextprotocol/servers/issues/4116
- https://github.com/modelcontextprotocol/servers/issues/4143
- https://github.com/modelcontextprotocol/servers/issues/4205
- https://github.com/microsoft/playwright-mcp/issues/1626

Protocol Pivoting preprint (cross-protocol attack escalation):
https://zenodo.org/records/20371152

mcp-safeguard (detection tool):
https://pypi.org/project/mcp-safeguard/

-----END SECURITY ADVISORY-----

Syed Anas Mohiuddin
AI Security Researcher
anasmohiuddinsyed () gmail com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **SSRF in Anthropic mcp-server-fetch and Microsoft playwright-mcp — publicly disclosed via GitHub issues** *outreach (May 25)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")