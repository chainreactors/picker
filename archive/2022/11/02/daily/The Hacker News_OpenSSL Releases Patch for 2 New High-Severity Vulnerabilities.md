---
title: OpenSSL Releases Patch for 2 New High-Severity Vulnerabilities
url: https://thehackernews.com/2022/11/just-in-openssl-releases-patch-for-2.html
source: The Hacker News
date: 2022-11-02
fetch_date: 2025-10-03T21:34:53.172132
---

# OpenSSL Releases Patch for 2 New High-Severity Vulnerabilities

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [OpenSSL Releases Patch for 2 New High-Severity Vulnerabilities](https://thehackernews.com/2022/11/just-in-openssl-releases-patch-for-2.html)

**Nov 01, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEist19_xjjwBTCyA4-B0zS5OAZpwcCgqw_8BD8FdIRZN9aH7Oz1jvzcxlsqG04SqmevXsbdz6SN1vAFsypICWzRFRXtP-H035HczQg7Yb_m7usSJR2mB2Bsd4jdEP0Fm5V2HiUkKpXQmSqQsAlVwa5lo0Ob3txPFRGeZQl8xrubVfZV68dOWGs_qm-d/s790-rw-e365/openssl.jpg)

The OpenSSL project has rolled out fixes to contain two high-severity flaws in its widely used cryptography library that could result in a denial-of-service (DoS) and remote code execution.

The issues, tracked as [CVE-2022-3602 and CVE-2022-3786](https://www.openssl.org/news/vulnerabilities.html), have been described as buffer overrun vulnerabilities that can be triggered during X.509 certificate verification by supplying a specially-crafted email address.

"In a TLS client, this can be triggered by connecting to a malicious server," OpenSSL said in an advisory for CVE-2022-3786. "In a TLS server, this can be triggered if the server requests client authentication and a malicious client connects."

OpenSSL is an [open source implementation](https://thehackernews.com/2022/07/openssl-releases-patch-for-high.html) of the SSL and TLS protocols used for secure communication and is baked into several operating systems and a [wide range of software](https://github.com/NCSC-NL/OpenSSL-2022/tree/main/software).

Versions 3.0.0 through 3.0.6 of the library are affected by the new flaws, which has been remediated in version 3.0.7. It's worth noting that the commonly deployed OpenSSL 1.x versions are not vulnerable.

Per data shared by [Censys](https://censys.io/critical-vulnerability-in-openssl/), about 7,062 hosts are said to run a susceptible version of OpenSSL as of October 30, 2022, with a majority of those located in the U.S., Germany, Japan, China, Czechia, the U.K., France, Russia, Canada, and the Netherlands.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While CVE-2022-3602 was [initially treated](https://mta.openssl.org/pipermail/openssl-announce/2022-October/000238.html) as a Critical vulnerability, its severity has since been [downgraded](https://www.openssl.org/blog/blog/2022/11/01/email-address-overflows/) to High, citing stack overflow protections in modern platforms. Security researchers Polar Bear and Viktor Dukhovni have been credited with reporting CVE-2022-3602 and CVE-2022-3786 on October 17 and 18, 2022.

The OpenSSL Project further noted the bugs were introduced in OpenSSL 3.0.0 as part of [punycode](https://en.wikipedia.org/wiki/Punycode) decoding functionality that's currently used for processing email address name constraints in X.509 certificates.

Despite the change in severity, OpenSSL said it considers "these issues to be serious vulnerabilities and affected users are encouraged to upgrade as soon as possible."

Cybersecurity firm Rapid7 [pointed out](https://www.rapid7.com/blog/post/2022/11/01/cve-2022-3786-and-cve-2022-3602-two-high-severity-buffer-overflows-in-openssl-fixed/) that "exploitability is significantly limited," as the [flaws](https://securitylabs.datadoghq.com/articles/openssl-november-1-vulnerabilities/) occur "after certificate verification and requires either a CA to have signed the malicious certificate or for the application to continue certificate verification despite failure to construct a path to a trusted issuer."

"Specifically, implementations that are configured for mutual authentication, where both the client and the server are providing OpenSSL-provided certificates for authentication, should definitely be fast-tracking this update," Tod Beardsley, director of research at Rapid7, said.

Brian Fox, co-founder and CTO at software supply chain management firm Sonatype, reiterated the high level of difficulty required for weaponizing the flaws.

"The vulnerability requires a malformed certificate that is trusted or signed by a naming authority," Fox said. "That means that authorities should be able to quickly prevent certificates designed to target this vulnerability from being created, further limiting the scope."

Version 3.0, the current release of OpenSSL, is [bundled](https://www.akamai.com/blog/security-research/openssl-vulnerability-how-to-effectively-prepare) with [Linux operating system](https://snyk.io/blog/new-openssl-critical-vulnerability/) flavors such as CentOS, Fedora, Kali, Linux Mint, openSUSE Leap, and Ubuntu. [Apple's macOS](https://isc.sans.edu/diary/Critical%2BOpenSSL%2B30%2BUpdate%2BReleased%2BPatches%2BCVE20223786%2BCVE20223602/29208/), on the other hand, uses LibreSSL. Container images built using affected versions of Linux are also impacted.

According to an [advisory](https://www.docker.com/blog/security-advisory-critical-openssl-vulnerability/) published by Docker, roughly 1,000 image repositories could be affected across various Docker Official Images and Docker Verified Publisher images.

"The new OpenSSL vulnerability does not affect the issuance or use of certificates," Tim Callan, chief compliance officer at Sectigo, [said](https://sectigo.com/resource-library/openssl-vulnerability-patch-released) in a statement. "No organization needs to revoke or reissue certificates based on this vulnerability."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The last critical flaw addressed by OpenSSL was in September 2016, when it closed out [CVE-2016-6309](https://nvd.nist.gov/vuln/detail/CVE-2016-6309), a use-after-free bug that could result in a crash or execution of arbitrary code.

There are close to 240,000 publicly accessible servers worldwide running versions of OpenSSL that are still vulnerable to Heartbleed eight years after its initial discovery, Rezilion researchers Yotam Perkal and Ofri Ouzan [said](https://www.rezilion.com/blog/clearing-the-fog-over-the-new-openssl-vulnerabilities/...