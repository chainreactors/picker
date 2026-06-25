---
title: a CVE dispute
url: https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/
source: daniel.haxx.se
date: 2026-06-24
fetch_date: 2026-06-25T06:08:44.395019
---

# a CVE dispute

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/09/CVE.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# a CVE dispute

[June 24, 2026](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/#respond)

A few years years ago the curl project signed up and [became a CNA](https://daniel.haxx.se/blog/2024/01/16/curl-is-a-cna/). This means that we are masters of and can allocate our own CVE identifiers. For any security problems within our territory, it is we who decides if the issue should get a CVE or not. No more [bogus CVEs](https://daniel.haxx.se/blog/2023/09/05/bogus-cve-follow-ups/).

## 57 CVEs

During these years we have published *fifty-seven* separate [security vulnerabilities](https://curl.se/docs/security.html) with their associated CVE identifiers. Getting a CVE for an issue is easy and really quickly done when you are a CNA. No hassle, no friction and as we are a small and lean security team it just works as smoothly as you could ask. Just an API call and we have new number.

Being a CNA is low maintenance, as there really is nothing extra we need to do. We already had an established and proven [process for receiving, managing and assessing vulnerability reports](https://curl.se/dev/vuln-disclosure.html) before we became a CNA since we are a responsible and well-run Open Source project. Becoming a CNA just made the process easier as we now don’t need to involve any outsider at all.

## Assess

For every report we work hard to first assess and decide if the issue is actually a vulnerability or a security problem at all.

If we deem that there is a security problem in there, we then grade it into LOW, MEDIUM, HIGH or CRITICAL. Since we don’t know how users use curl or libcurl we cannot take that into account but rather observe and set a severity of the problem from a pure curl point of view.

It’s a rough indication how we see the problem but of course every user that actually are affected by the problem might rate it differently.

## Lower than LOW

For a rare few issues we can *imagine* that there could be a minuscule risk but because of the set of extreme requirements and convoluted steps to get there, we deem the risk so small that in practice no user is *likely* to ever reach it. Internally we tend to call that an issue with a severity level lower than LOW. Issues we believe we serve humanity better by *not* issuing a CVE for. To avoid the security dance when it seems unnecessary.

## The cost of a CVE

libcurl is installed in somewhere around *thirty billion instances* on the globe. If we imagine that at least a sizeable portion of those installs are managed by people who want to make sure they use a secure version, it means that every CVE we publish trigger activities in many security teams all over the world, leading to a significant number of patches and subsequent software updates.

Every CVE thus has this huge cost tied to it. A cost that does not land on us and we don’t really see or feel it, but a cost on the ecosystem I believe we should not ignore. We should act responsibly. Never ignore real problems of course, but also to make sure we don’t ring the alarm for theoretical problems that will not trigger any vulnerability.

## The dispute

Our first ever CVE dispute since we became a CNA reached us on February 10th, 2026 for a report submitted to us two months earlier. The reporter thinks we should have assigned [their reported problem](https://hackerone.com/reports/3455037) a CVE but we think not. Now they want to force the issue to get a CVE anyway, by escalating the situation to MITRE.

Yes, it makes you wonder *why* it is that important to have this as a CVE, but I will avoid speculations for now.

I replied to MITRE explaining that we considered and debated the issue and we remain happy with our previous decision. I linked them the original report and discussion to show them.

## Hostname with a leading dot

The issue is quite technical (of course) but is based on a bug in curl’s function that checks if the used hostname matches a wildcard provided in a certificate.

First: the user must use a hostname in a URL with a *leading* dot, like `https://.example.com/`

This name is not possible to use with DNS (it is an illegal name there), but you can provide an IP address for it in your `/etc/hosts` file or similar, but still this condition is already making this issue really niche.

Why would a user ever do this? Well, there *could* be a redirect to such a host name from a malicious server if the application allows redirects but getting the address for the host is still a challenge and mostly requires a local attacker present add that.

Then: if curl can find an address for the illegal DNS hostname, the site curl connects to, also needs to have a wildcard certificate for the name `*.example.com` where the tail of the wildcard needs to match the name in the URL.

If curl was built to use an OpenSSL flavor or Schannel for TLS (remember that curl supports many different TLS backends), it then calls the `Curl_cert_hostcheck()` function to check if the wildcard covers the used hostname.

**This function had a bug**. The above mention combination then erroneously would return TRUE. A match. When in reality it is not a match according to the spec.

We fixed this problem on [December 8, 2025](https://github.com/curl/curl/commit/2535c4298fede065c80b9255328c18b68d739522), and we added unit tests for exactly this scenario to make sure that the problem doesn’t come back. For all security issues at several below HIGH, we fix them asap so that was just our normal procedure. We then continued to discuss if this was worthy of a CVE or not.

## Lower than LOW

It should be *extremely rare* that anyone uses a dot prefixed name, unless you are in an internal and controlled environment where you use something else than DNS for resolving.

It is not possible to trick an application to use a dot prefixed arbitrary name as it will fail to resolve.

The explicitly set, weirdly dot prefixed name, then needs to connect to a host that has a wildcard set for that same name and an attacker manage to run this impostor host and can now serve the application malicious data because curl did not properly reject the connection because of the wildcard mismatch.

A series of highly unlikely conditions that all need to be fulfilled for this to become a vulnerability. A lower than LOW situation. Too unlikely; no CVE.

## Again in May

On May 28, we were *again* contacted by MITRE *in the same case,* asking again for our rationale for not giving this issue a CVE. We responded with virtually the same wording as before and linking again to the same original Hackerone issue and discussion thread. It’s all public information really.

## Again in June

On June 15, we were *again* contacted by MITRE asking for the reasoning behind our decision to not give a CVE for this issue.

We replied with similar wording again. Linking to the same issue, again.

This seems like a *great* system.

## Verdict

On June 24 we finally got the verdict. It is not considered a security vulnerability.

```
Hello Yuhao,

Thank you for your participation in the CVE dispute process regarding the reported issue affecting
curl through 8.17.0.

The MITRE TL-Root has completed its review of the information provided by all parties involved,
including the materials submitted by you and the res...