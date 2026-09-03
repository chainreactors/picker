---
title: GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends
url: https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html
source: The Hacker News
date: 2026-09-02
fetch_date: 2026-09-03T07:02:42.629498
---

# GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends](https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html)

**Swati Khandelwal**Sep 02, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWjRcj8Bn8kWovv1-oDjSP61hMxx5U8u28qVJSPdP7mRBCNbs5EJjjDrWWk7SFC2FraZe_j3T-oouRqSRtoTr-YMPGGuOphIGNRj4-Fx0eVgMahD3-L62vWUxYLg7TpH7plqVqnAb1e3k0-G8Vertd-WUyt994d-nJKA8bcY9QozeWJ6ad4ozwVOf0fnE/s1700-nu-rw-lo-l85-e365/geone.gif)

Two vulnerabilities in **GeoNetwork** can be chained to achieve unauthenticated remote code execution (RCE) on the open-source geospatial metadata catalog, which sits behind many government and agency geoportals.

The project shipped fixes in versions 4.4.12 and 4.2.17 on July 8, 2026, and published the vulnerability details on August 31.

GeoNetwork originated at the United Nations Food and Agriculture Organization and is maintained under the Open Source Geospatial Foundation (OSGeo). It is a core component of many Spatial Data Infrastructure deployments across Europe and beyond, including the backend of the European INSPIRE geoportal.

The chain combines a missing authorization check with an unsafe transformation engine. The first flaw, **CVE-2026-63219** (CVSS score: 8.6), is a missing authorization check on the formatter upload endpoint.

The unauthenticated file upload flaw allows an anonymous user to write arbitrary .xsl or .zip formatter files to the GeoNetwork formatter directory, which, on its own, constitutes unauthorized write access to server storage.

"An unauthenticated attacker can upload arbitrary .xsl or .zip formatter files to the server," the project said in [the advisory](https://github.com/geonetwork/core-geonetwork/security/advisories/GHSA-mh22-prqr-vf42).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The second flaw, CVE-2026-58400 (CVSS score: 9.1), is an [unsafe configuration of the Saxon](https://github.com/geonetwork/core-geonetwork/security/advisories/GHSA-x898-729x-cc3r) Extensible Stylesheet Language Transformations (XSLT) processor used to render formatters.

The engine runs with secure processing enabled and Java extension functions disabled, so any stylesheet it loads can call java.lang.Runtime.exec() or java.lang.ProcessBuilder and run operating-system commands as the GeoNetwork process user.

On its own, that second flaw requires privileges to upload a formatter, which is why it is scored as needing high privileges. Chaining it with the upload flaw removes that precondition, because the upload is reachable without authentication.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJOdCLNcunQXdDyN7r6M69wVIVN9lCdvh-HTmIydTihXsUKQAHKfPc5F7ShFXKJG1OgClZe6txs3SoHbUTIte_YdK0xQGJvEzGolc_zOKqq9zloeNlwSyLVCHsPbyKW1Uc9RAah36L7XkekjTnQC60KZGarSXTEMoomuRUXFAi-bCgA87GlAelMwF_1Vo/s1700-nu-rw-lo-l85-e365/geo-1.jpg)

An attacker first uploads a malicious formatter through the unprotected endpoint. A follow-up GET request to a public record then triggers the Saxon engine to execute the stylesheet, which delivers code execution. Security vendor Ethiack, whose researcher Rafael Castilho [reported the flaws](https://ethiack.com/info-hub/research/geonetwork-preauth-RCE), said the chain is reachable starting with version 4.0.6, when the formatter endpoint was refactored, and the authorization line was dropped.

Ethiack said it fingerprinted 121 internet-exposed GeoNetwork deployments running affected versions across 39 countries, and that 89 percent of them were government-, military-, or national-agency-related.

Those figures describe exposed instances running vulnerable versions, not confirmed victims or compromises, and the fingerprinting is single-sourced to the vendor.

All 4.4.x releases up to and including 4.4.11 and all 4.2.x releases up to and including 4.2.16 are affected, and the flaws are fixed in 4.4.12 and 4.2.17.

"All users are strongly encouraged to upgrade to 4.4.12 or 4.2.17 as soon as possible," the project said in its release announcement.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Until the update is applied, administrators can block write methods to the formatter endpoint at the reverse proxy, thereby blocking legitimate formatter uploads through the admin console.

The advisory lists the following interim rules -

* **Apache httpd** - deny POST, PUT, and PATCH requests to the /geonetwork/srv/api/formatters location.
* **Nginx** - restrict the same location to GET, HEAD, and OPTIONS methods.

The flaws were fixed roughly eight weeks before the advisories were published. The Hacker News found no reference to the GeoNetwork flaws in CISA's Known Exploited Vulnerabilities catalog as of the disclosure, and no public reporting of exploitation in the wild.

The disclosure follows a run of security issues across the wider geospatial stack. Last year, a critical GeoServer flaw (CVE-2024-36401, CVSS score: 9.8) was [exploited into botnets](https://thehackernews.com/2024/09/geoserver-vulnerability-targeted-by.html), cryptocurrency miners, and the SideWalk backdoor, and a GeoServer XML External Entity (XXE) flaw (CVE-2025-58360) was [added to CISA's KEV catalog](https://thehackernews.com/2025/12/cisa-flags-actively-exploited-geoserver.html) in December 2025 after evidence of active exploitation. Last month, a separate unauthenticated SQL injection to RCE in GeoServer, disclosed as [a GeoServer zero-day](https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html), came under active probing shortly after it went public.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/comp...