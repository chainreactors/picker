---
title: eMudhra to Exit Global SSLTLS Business After 8 Intermediate CA Keys Found Easily Guessable
url: https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html
source: Instapaper: Unread
date: 2026-10-23
fetch_date: 2026-10-24T06:48:21.131616
---

# eMudhra to Exit Global SSLTLS Business After 8 Intermediate CA Keys Found Easily Guessable

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [eMudhra to Exit Global SSL/TLS Business After 8 Intermediate CA Keys Found Easily Guessable](https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html)

**Swati Khandelwal**Oct 22, 2026Cryptography / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5DGeZCzWnHOoA87UbpfzGUlpU9xBK1x5tJsYlWOoKtyEkTRjaN4cW_lMOKdtiSXVPhVMd6JhOMRhvFOxvn853LcLaCBSNK-_m4CDIDGt048SdHQQqu63ZSZ09Ymc3UhqD_TZoLaCM6eIJL6TSYbBVINceAi4paPvjxJ4i9uN3CKZQ2s5bT4Dc_jAcv8I/s1700-nu-rw-lo-l85-e365/ssl.jpg)

**eMudhra**, an Indian certificate authority (CA), will withdraw from its global SSL/TLS certificate business, [its board decided on Thursday](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business). The decision came five days after a researcher [reported recovering the private keys](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html) of eight of its intermediate CA certificates.

eMudhra said it will replace affected customers' certificates with free ones from partners, though its announcement did not name the partners or provide a date for the exit.

Six of those eight were for website (TLS) certificates. Chrome will stop trusting the eMudhra root certificate above them, emSign ECC Root CA - G3. The change is expected to reach users on the morning of October 27, Pacific time.

On October 20, Mozilla decided to stop trusting the same root in Firefox. Removing a root from a browser also cuts off legitimate certificates issued beneath it.

About 30,800 unexpired certificates chained to that root as of October 21, [by Chrome's count](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30) of public Certificate Transparency (CT) logs. Of those, 99.9% were issued through InCommon, the certificate service Internet2 created for the higher education community. InCommon [moved the service onto eMudhra's CertiNext platform](https://internet2.edu/incommon-round-up-may-2026) between April and July this year.

Google has [told website operators](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/) with certificates under that root that they "must immediately acquire and install a new TLS certificate from another PKI hierarchy included in the Chrome Root Store."

Until the transition is complete, eMudhra said, its G1 RSA root certificates will continue to serve customers. G1 is a separate hierarchy from the ECC root, but Chrome is still deciding whether to keep eMudhra's remaining CA certificates in its root store.

eMudhra will keep its revocation and status services running until every SSL/TLS certificate it issued has expired or been replaced. Its other businesses, including digital signature certificates, eSign and the CertiNext platform InCommon uses, will continue.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The announcement does not mention InCommon, or say whether eMudhra will keep issuing new certificates under G1 until it exits.

eMudhra said the global SSL/TLS business brings in about 1% of its revenue. Data sovereignty and compliance rules make it more complex and costly to run, and some large providers give the certificates away free.

The incident's spread on social media has also brought "scrutiny that is out of proportion to SSL/TLS’s place in our business," the company said.

The researcher reported the weak keys to Apple, Google, Microsoft, Mozilla and eMudhra on October 17. Each private key should have been a huge random number, but all eight were below 256, so anyone could work them out almost instantly.

Chrome and Firefox blocked the six TLS intermediates within hours. No website certificate from them had appeared in CT logs before Chrome's block, so none could have been used against Chrome or other software that requires CT logging, Google said.

eMudhra said it never used the eight to issue certificates to websites or users, and that its systems were not breached.

### What Certificate Holders Can Do

[Cornell has told its certificate holders](https://itservicealerts.hosting.cornell.edu/view/7882) to request RSA certificates instead of ECC ones, because "RSA certificates use eMudhra's unaffected root and should work." The university counts more than 300 affected certificates of its own.

[The University of Michigan says](https://safecomputing.umich.edu/security-alerts/root-certificate-authorities-distrusted) InCommon's RSA certificates are not currently affected, but that their root "could become distrusted, too." For now, its main alternative is Let's Encrypt.

eMudhra [has estimated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c19) that about 30,000 certificates need to be moved, and that about 97% of them were issued using ACME, the protocol many servers use to request and renew certificates automatically.

Chrome has told eMudhra that standard ACME clients do not replace certificates outside their renewal window unless they support ACME Renewal Information (ARI) or someone steps in by hand. Moving from the ECC hierarchy to the RSA one may also need changes to client settings.

### Questions Over eMudhra's RSA Root

[Mozilla said on October 20](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c18) that, for now, it was not removing trust in the G1 root, emSign Root CA - G1. [At Stanford](https://uit.stanford.edu/service/ssl/emSign), InCommon certificates chain to that root through an eMudhra CA called emSign Root TLS CA - G1.

On October 14, eMudhra published a certificate revocation list (CRL) for emSign Root TLS CA - G1. A CRL is the signed list of certificates a CA has revoked. This one's signature does not verify against that CA's own key, the researcher who reported the weak keys [said in Mozilla's public bug report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7) on the incident.

A participant in the same bug report [said on Octob...