---
title: Blind trust: stealing credentials through CSP
url: https://portswigger.net/research/blind-trust-stealing-credentials-through-csp
source: PortSwigger Research
date: 2026-11-11
fetch_date: 2026-11-12T09:01:14.485025
---

# Blind trust: stealing credentials through CSP

[Login](/users)

[ ]

Products    Solutions   [Research](/research) [Academy](/web-security)  Support    Company

[Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[My account](/users/youraccount) [Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[![Burp AT](/_ps-components/0.3.0/fragments/meganav/burp-at.svg) **Burp AT** Agentic AI that extends human-led pentesting.](/burp/burp-at)   [![Burp Suite DAST](/_ps-components/0.3.0/fragments/meganav/enterprise.svg) **Burp Suite DAST** The enterprise-enabled dynamic web vulnerability scanner.](/burp/dast)   [![Burp Suite Professional](/_ps-components/0.3.0/fragments/meganav/professional.svg) **Burp Suite Professional** The world's #1 web penetration testing toolkit.](/burp/pro)   [![Burp Suite Community Edition](/_ps-components/0.3.0/fragments/meganav/community.svg) **Burp Suite Community Edition** The best manual tools to start web security testing.](/burp/communitydownload)  [View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/_ps-components/0.3.0/fragments/meganav/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility** Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)   [**CI-driven scanning** More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)   [**Application security testing** See how our software enables the world to secure the web.](/solutions)   [**DevSecOps** Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)   [**Penetration testing** Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)   [**Automated scanning** Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)   [**Bug bounty hunting** Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)   [**Compliance** Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and DAST?

![Burp Suite Professional vs Burp Suite DAST](/_ps-components/0.3.0/fragments/meganav/burp-suite.jpg)](/burp/dast/resources/dast-vs-professional)

[**Support Center** Get help and advice from our experts on all things Burp.](/support)   [**Documentation** Tutorials and guides for Burp Suite.](/burp/documentation)   [**Get Started - Professional** Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)   [**Get Started - DAST** Get started with Burp Suite DAST.](/burp/documentation/dast/setup)   [**Downloads** Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/_ps-components/0.3.0/fragments/meganav/latest-burp-suite-software-download.jpg)](/burp/releases)

[ ]

Articles

* [Overview](/research)
* [ ]

  Core Topics

  [Black Hat](/research/black-hat)
  [XSS](/research/cross-site-scripting-research)
  [Request Smuggling](/research/request-smuggling)
  [Template Injection](/research/template-injection)
  [Top 10 Hacking Techniques](/research/top-10-web-hacking-techniques)
* [Articles](/research/articles)
* [ ]

  Meet the Researchers

  [James Kettle](/research/james-kettle)
  [Gareth Heyes](/research/gareth-heyes)
  [Zakhar Fedotkin](/research/zakhar-fedotkin)
  [Tom Stacey](/research/tom-stacey)
  [Alex Craig](/research/alex-craig)
* [Talks](/research/talks)
* [RSS](/research/rss)

# Blind trust: stealing credentials through CSP

[ ]

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

* **Published:** Wednesday, 11 November 2026 at 14:26 UTC
* **Updated:** Wednesday, 11 November 2026 at 14:26 UTC

![A picture showing the Burp AT logo with an arrow going round CSP](/cms/images/b2/36/8aba-article-bypassing-csp-article.png)

[Content Security Policy](/web-security/cross-site-scripting/content-security-policy) is supposed to be the safety net that stops an HTML injection from turning into [XSS](/web-security/cross-site-scripting). Usually it works. But sometimes it doesn't, because the policy allows-lists a domain that hosts a JSONP endpoint or an old copy of [AngularJS](/web-security/cross-site-scripting/contexts/client-side-template-injection), or because whoever wrote the policy forgot that one directive doesn't inherit from `default-src`.

Spotting those mistakes by hand is tedious. You read the header, work out which directive actually applies, check every allowed host against the gadgets you remember, then build a proof of concept. So we turned that process into a [Burp AT](/burp/burp-at) skill. Tell Burp AT you want to bypass a [CSP](/web-security/cross-site-scripting/content-security-policy) and it reads the policy, finds the weaknesses and builds you a PoC that exfiltrates to Burp Collaborator.

## What the skill does

The skill runs two checks against the Content-Security-Policy on a response:

* 1. Allow-list gadget lookup. Are any of the allowed script sources known to host a CSP bypass gadget?
* 2. Form-action credential exfiltration. Does the policy let an injected form post back to the page, so credentials can be stolen even when no JavaScript runs at all?

**1. Hunting for gadgets in the allow-list**

A host allow-list is only as strong as the weakest file on any host in it. If script-src allows a domain that serves a JSONP endpoint with a controllable callback, an attacker can load that endpoint as a script and run arbitrary JavaScript from an allowed origin.

The skill comes with a dataset of more than 350 known gadgets provided by
[cspbypass.com](https://cspbypass.com) big thanks to them, each a domain plus a working snippet. To match against it, the script:

* Works out the effective script sources. It follows the browser's fallback chain: `script-src-elem`, then `script-src`, then `default-src`. If none of those are present, scripts are unrestricted.
* Matches hosts the way the browser does. A source can match exactly, or as a \*.example.com wildcard that covers subdomains. A bare \* or a scheme-only source like https: allows any host, and the report says so.
* Intersects multiple policies. When a response sends more than one enforced CSP header, the browser has to satisfy all of them, so a gadget is only reported if every policy allows its domain.
* Handles report-only. If the only header is `Content-Security-Policy-Report-Only`, the skill still analyses it but marks the findings as informational, because that header blocks nothing.
* Flags caveats that change the answer. With `strict-dynamic`, modern browsers ignore the host allow-list, so host gadgets won't fire. A nonce or hash may gate execution. And if `unsafe-inline` appears without a nonce, hash or `strict-dynamic`, you don't need a gadget at all.

Each matching domain comes back with its gadget snippet, along with the effective sources for each policy and any caveats.

**2. Stealing credentials with a self-posting form**

The second check covers the case that's easy to miss. Even when policies block all JavaScript with `default-src 'none'` there is still a way to steal data.

`form-action` does not fall back to `default-src`. If a policy leaves out form-action, forms can submit anywhere. If it sets `form-action 'self'`, forms can still submit to the page itself, and that's all this attack needs.

When the page has a reflected HTML-injection sink, the skill builds a two-stage form:

`?targetParam=<form>
<p><label>Usern...