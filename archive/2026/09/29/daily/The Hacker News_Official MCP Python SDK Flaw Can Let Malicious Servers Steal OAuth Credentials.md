---
title: Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials
url: https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html
source: The Hacker News
date: 2026-09-29
fetch_date: 2026-09-30T07:42:59.891038
---

# Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials](https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html)

**Swati Khandelwal**Sep 29, 2026Identity Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2N5owhsoQXHTQV74afwfngdyitjwcW37BHLX2QKkq6xZAxP8_AOXAh1ODPj5DyvvmMUq3mKH9eR2B1r7owc6djzLViK2U4BY_hw3rTWmaHjhFEyyh8LPlUMPZ7MdWkqN7bjtQyMByBLrsI5m0mAU9y-IbrsAe9OPhZXHN63AWwuv_1OB5MSrpRdVZ9CM/s1700-nu-rw-lo-l85-e365/mcp-python.jpg)

A malicious MCP server could trick an application built on the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-qx49-fqc8-xw99) into handing over the OAuth credentials it uses to log in to a real service, the SDK's maintainers said in a security advisory.

Affected versions sent the client secret, the authorization code, and the PKCE proof key to a token endpoint the attacker controlled. The fix is in versions 1.30.0 and 2.2.0.

The Model Context Protocol (MCP) is an open standard for connecting AI applications to outside tools and data, and this package is its official Python SDK for building MCP servers and clients.

With the stolen credentials, the attacker can request a valid access token from the real login service. Cycode, the security firm that [reported the flaw](https://cycode.com/blog/mcp-python-sdk-oauth-account-takeover/), demonstrated that full exchange in a test and says the resulting token carries whatever permissions the app was granted. The client secret is long-lived, so it keeps working until it is changed.

The flaw is rated high (7.5) for the two providers that run without a person present. Scored for the interactive provider, where someone has to start the sign-in, it is 6.5. No CVE had been assigned as of September 29.

### How a server steals the credentials

When an MCP client needs to log in, it asks the server it is connecting to where its login service, called the authorization server, can be found. On the affected versions, the SDK did not always check that answer. A malicious server could point it at a login service of the attacker's choosing, either by naming the attacker's own server or by serving login details that name the user's real service while sending the credentials elsewhere.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The client then sends its secret, its authorization code, and its PKCE proof key to the attacker instead of the real service. The proof key is a one-time value designed to prevent a stolen authorization code from being reused, so handing it over defeats that protection as well.

With the interactive provider, the person still has to approve a sign-in. Cycode says the page they approve is the genuine login page, so nothing looks wrong. The two machine-to-machine providers need no sign-in and no person at all.

### Who is affected

An application is affected if it uses the SDK as an MCP client over HTTP with one of the OAuth providers OAuthClientProvider, ClientCredentialsOAuthProvider, PrivateKeyJWTOAuthProvider, or the deprecated 1.x RFC7523OAuthClientProvider, and it can connect to a server it does not fully control while holding credentials for a real login service. MCP servers built with the SDK, local (stdio) clients, and clients that attach their own tokens are not affected.

| Line | Affected | Fixed in |
| --- | --- | --- |
| 1.x | 1.9.1 through 1.29.1 | 1.30.0 |
| 2.x | 2.0.0 through 2.1.1 | 2.2.0 |

### What to do

Upgrade to [1.30.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) on the 1.x line or [2.2.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) on the 2.x line. In the fixed versions, the client works out which login service it expects before fetching any details and refuses any that name a different one.

Upgrading is not the whole fix for two of the providers. If you use ClientCredentialsOAuthProvider or PrivateKeyJWTOAuthProvider, the advisory says ["upgrading changes nothing until you also pass issuer="](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-qx49-fqc8-xw99) to name the login service those credentials belong to. Without it, they still follow whichever server the MCP server points them at.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

On 1.30.0, the warning about this is a standard deprecation warning, which Python hides by default, so it is easy to miss. The deprecated RFC7523OAuthClientProvider has no issuer= option at all, so move to one of the other two providers.

After upgrading, clear any stored OAuth client registrations once, because older ones are not tied to a login service and stay that way. If a client may already have connected to an untrusted server, rotate its client secret and revoke its tokens at the login service. On older versions, there is no workaround other than connecting only to MCP servers you trust.

### Disclosure

The issuer checks shipped in the 1.30.0 and 2.2.0 release notes on September 7, listed under behavior changes rather than as a security fix. The advisory followed on September 28, the same day Cycode published its writeup. The advisory credits eight reporters, including Cycode's researcher.

Neither the advisory nor Cycode reports any attacks using the flaw, and none has been reported elsewhere.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**S...