---
title: Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug
url: https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:51.625031
---

# Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

![cybersecurity](data:image/svg+xml;base64...)

# [Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug](https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html)

**Swati Khandelwal**Aug 05, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGDed_n3TJGLHvhq2MkwkQTsKgIv_rOw24MRfYCoHnHiOK7r-VbitMrwXXF9H_Gwbegba20Dla1FLyK70-OQRVxiHfikBFrz6jei3QK5u4ApbR4aYuLikQj1YHU2IzA1V4fnR7Wgcp8H1NoYzSeTTOUd4dNTuE71jNUNq-P4yk0H9FkW55wivMDdNe0nE/s1700-e365/veeam.jpg)

HashiCorp, Veeam, and the Django Software Foundation have patched 11 vulnerabilities across Terraform MCP Server, Veeam Service Provider Console, and Django.

The three most serious:

* An unauthenticated flaw in Veeam's console that hands over a managed agent's credentials, rated 9.5
* A cross-tenant flaw in HashiCorp's MCP server that lets one user's Terraform token be reused for later users' requests, scored a maximum 10.0 on its CVE record
* A flaw in GeoDjango's spatial lookups that can write a file to disk and, on some setups, run code, reachable by a staff user with view permission on a registered model containing a spatial field

Each has a fix available now. Operators should update Terraform MCP Server to version 1.1.0 or later, Veeam Service Provider Console to 9.3.0.35057, and Django to 6.0.8 or 5.2.17.

Exposure is configuration-dependent: HashiCorp's bugs affect Streamable HTTP rather than stdio, Veeam's flaws affect version 9 builds before 9.3, and Django's documented admin attack path requires a staff account with view permission for a model containing a spatial field.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

None of the three advisories says the flaws are under active exploitation, and as of August 5, 2026, none of the eleven CVEs appears in CISA's Known Exploited Vulnerabilities catalog, and no public proof-of-concept has surfaced.

## Impersonate an agent, take its credentials

Veeam Service Provider Console, the multi-tenant console that hosting firms and managed service providers use to run and monitor customer backups, got four fixes in build 9.3.0.35057, detailed in a [security bulletin published August 4](https://www.veeam.com/kb4893). Two are critical. Veeam released the build on July 29.

* The one to watch is **CVE-2026-58073** (CVSS score: 9.5), which lets an unauthenticated attacker impersonate a managed agent and obtain that agent's credentials. Its CVSS vector rates attack complexity as high.
* The second critical flaw, **CVE-2026-58072** (CVSS score: 9.0), is an arbitrary file write on the management server that can lead to remote code execution and requires a low-privilege account.

The 9.5 reads as the worst of the two because it needs no login, but its high attack complexity is the reason the vector is not a straight-line exploit; unauthenticated here does not mean easy.

Two high-severity bugs round out the set: **CVE-2026-58067**, an unauthenticated memory-exhaustion denial of service, and **CVE-2026-58071**, which exposes the proxied appliance API as Portal Administrator during a short window after an administrator session begins.

All four affect VSPC 9.2.1.33875 and every earlier version 9 build. The fix is the upgrade to 9.3.0.35057.

This is the second critical patch cycle for the console in roughly three months. In May, Veeam fixed [CVE-2026-32998](https://www.veeam.com/kb4853), a 9.4-rated remote code execution bug tied to alarm script execution.

## One tenant's token, reused for the next

HashiCorp's Terraform MCP server, which connects AI assistants to Terraform over the Model Context Protocol, carries three related flaws in its Streamable HTTP transport, [disclosed July 28 and fixed in version 1.1.0](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606). HashiCorp released the fixed build on July 14, followed by version 1.2.0 on August 4.

Deployments that run only in stdio mode, the local single-user setup, are unaffected. The bugs live in the multi-user HTTP mode meant for centralized, shared deployments, the configuration HashiCorp promoted when it made the server [generally available in June](https://www.hashicorp.com/en/blog/terraform-mcp-server-is-now-generally-available).

The most severe is **CVE-2026-16498** (CVSS score: 10.0), a cross-tenant credential-reuse bug in stateless HTTP mode. The underlying MCP library does not assign unique session identifiers, and the server's credential cache relied on those identifiers to tell users apart.

One user's Terraform token could therefore be reused for later users' requests regardless of the token they supplied. The root is an assumption about the layer beneath the tool: the server used those session identifiers to keep tenants apart, and in stateless mode the MCP library did not provide unique ones.

A second flaw, **CVE-2026-16496** (CVSS score: 8.9), is the stateful-mode version of the isolation failure. Stateful mode is the default when the server runs centrally.

Its cache used the MCP session ID as its sole lookup key, without binding the cached client to the token that created it. That let a user who obtained another user's session ID run tool calls with that user's Terraform client and reach resources allowed by the victim's token.

Juan Pablo Martinez Kuhn of Coinspect reported the flaw; HashiCorp found the other two internally.

The third, **CVE-2026-14869** (CVSS score: 8.6), is a server-side request forgery flaw. Request middleware rejected a client-supplied Terraform address when it arrived as an HTTP header but not when the same value came through a query parameter.

An unauthenticated caller able to reach the Streamable HTTP listener could make the server send its configured bearer token to an attacker-controlled endpoint.

Two things complicate reading the CVSS numbers as a priority order. They are not on one scale: Veeam scores on CVSS 4.0 and the HashiCorp records on 3.1, so the 9.5 and the 10.0 are not the same measurement.

And the two isolation flaws land on different configurations: the 10.0 (CVE-2026-16498) affects stateless mode, which an operator has to enable deliberately, while the 8.9 (CVE-2026-16496) affects the stateful mode t...