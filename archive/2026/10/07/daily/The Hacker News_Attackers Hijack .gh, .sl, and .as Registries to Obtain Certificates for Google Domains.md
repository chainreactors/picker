---
title: Attackers Hijack .gh, .sl, and .as Registries to Obtain Certificates for Google Domains
url: https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html
source: The Hacker News
date: 2026-10-07
fetch_date: 2026-10-08T08:08:35.894738
---

# Attackers Hijack .gh, .sl, and .as Registries to Obtain Certificates for Google Domains

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

# [Attackers Hijack .gh, .sl, and .as Registries to Obtain Certificates for Google Domains](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html)

**Swati Khandelwal**Oct 07, 2026Web Security / Domain Hijacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlqu6e-ijwp1hAEuYyfUUL9hV5kwu0cIe1cMibzayov0GdV2FkSpwvF10YKcxLyw1AUNdKF54RV9o3bfeshwWIWdda1AvgNm4iu6t9F16pb1jOVDQRXBoRjw2uueD4Ov7oEzjPJV7pXgK1U-MzkkqRKgHqP207GG2pqtkRQ09IVZ94HvSlBVArvu7tkNE/s1700-nu-rw-lo-l85-e365/google-tls.jpg)

Attackers compromised three country-code top-level domains (ccTLDs) and obtained unauthorized HTTPS certificates for several Google domains, Google [said on October 6](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/).

Google's own systems were not breached, but any domain ending in .gh (Ghana), .sl (Sierra Leone) or .as (American Samoa) was put at risk. With such a certificate, an attacker could pose as the real site over an encrypted connection and read the private data sent to it.

Chrome blocked the unauthorized certificates for Google's domains through [CRLSets](https://www.chromium.org/Home/chromium-security/crlsets/), its way of quickly blocking certificates in emergencies, Google said. The company also worked with the certificate authorities (CAs) that issued the certificates to have them revoked, a step meant to protect people using other browsers and apps.

Google did not name the domains. [Certificate Transparency](https://certificate.transparency.dev/howctworks/) (CT) logs are the public record of certificates issued by CAs. They show at least 12 certificates issued between September 22 and 27 for Google and YouTube names under the three ccTLDs, including google.com.gh, google.sl and google.as.

A CA issues a certificate once the applicant shows control of the domain, for example by adding a record to the domain's DNS. The attackers changed authoritative DNS records during the hijacks, and Google has no reason to believe the CAs did anything wrong, the company said.

### What Certificate Logs Show

The Hacker News found the certificates on October 7 through two CT search services, ctlogs.dev and Cert Spotter. The 12 certificates are for seven domains. Let's Encrypt issued 11 of them and ZeroSSL issued one.

The certificates were recorded in the logs on three days, one ccTLD at a time: .gh on September 22, .sl on September 25, and .as on September 27.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

All 12 are domain-validated certificates, issued after a check that the applicant controls the domain. In the records reviewed, which go back to at least September 10, every other certificate for google.com.gh, google.sl and google.as came from Google Trust Services, Google's own CA.

"Yes, certificates for Google and YouTube were issued, and have been revoked," Matthew McPherrin, a Let's Encrypt staff member, [wrote on the CA's community forum](https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941/2) on October 7, in reply to a user who asked whether Let's Encrypt certificates were issued during the hijacks.

Only a small set of Google and YouTube names was searched, so the total may be higher. Google said CT data also pointed to other organizations it believes were hit by the same attacks, including well-known global brands and widely used online services. It did not name them.

| # | Names on Certificate | Issuer | First Logged | Revoked |
| --- | --- | --- | --- | --- |
| 1 | `*.youtube.com.gh`, `youtube.com.gh` | Let's Encrypt | Sep 22, 11:03 | Sep 26, 02:41 |
| 2 | `*.google.com.gh`, `google.com.gh` | Let's Encrypt | Sep 22, 11:59 | Sep 26, 02:41 |
| 3 | `*.google.sl`, `google.sl` | Let's Encrypt | Sep 25, 04:36 | Oct 1, 19:36 |
| 4 | `google.sl`, `www.google.sl` | Let's Encrypt | Sep 25, 04:36 | Oct 1, 19:36 |
| 5 | `google.com.sl`, `www.google.com.sl` | ZeroSSL | Sep 25, 04:51 | Sep 26, 14:56 |
| 6 | `*.google.com.sl`, `google.com.sl` | Let's Encrypt | Sep 25, 04:51 | Oct 1, 19:36 |
| 7 | `www.youtube.sl`, `youtube.sl` | Let's Encrypt | Sep 25, 06:06 | Oct 1, 19:36 |
| 8 | `*.youtube.sl`, `youtube.sl` | Let's Encrypt | Sep 25, 06:07 | Oct 1, 19:36 |
| 9 | `google.as`, `www.google.as` | Let's Encrypt | Sep 27, 03:33 | Oct 1, 19:18 |
| 10 | `*.google.as`, `google.as` | Let's Encrypt | Sep 27, 03:43 | Oct 1, 19:18 |
| 11 | `google.as`, `www.google.as` | Let's Encrypt | Sep 27, 04:17 | Oct 1, 19:18 |
| 12 | `*.youtube.as`, `youtube.as` | Let's Encrypt | Sep 27, 04:37 | Oct 1, 19:18 |

### What the Response Covers

On October 7, Cert Spotter's records showed all 12 certificates as revoked. The two .gh certificates and the ZeroSSL certificate were revoked on September 26, and the other nine on October 1.

The shortest gap between a certificate's first log entry and its revocation was about a day and a half. The longest was nearly a week. The first .as certificate was recorded on September 27, about a day after the .gh certificates were revoked.

Google said it learned of the hijacks the week before its October 6 post and acted immediately. It did not give dates for the hijacks or for its own actions.

Google also blocked in Chrome the certificates it found for other organizations, and it contacted those organizations where it could.

Chrome users do not need to do anything, Google said. Domain owners should not rely on the browser to protect their users.

Because DNS hijacks are complex, "we cannot guarantee that our analysis identified every affected domain," the Chrome Secure Web and Networking Team wrote, adding that Chrome's blocks do not reliably protect people who use other browsers.

Google's post does not say whether any of the certificates was used to pose as a Google site or read users' data. It does not name the attackers, say how the ccTLDs were compromised, or say whether they have been s...