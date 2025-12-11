---
title: HTTPS certificate industry phasing out less secure domain validation methods
url: http://security.googleblog.com/2025/12/https-certificate-industry-phasing-out.html
source: Google Online Security Blog
date: 2025-12-10
fetch_date: 2025-12-11T03:23:00.483378
---

# HTTPS certificate industry phasing out less secure domain validation methods

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [HTTPS certificate industry phasing out less secure domain validation methods](https://security.googleblog.com/2025/12/https-certificate-industry-phasing-out.html "HTTPS certificate industry phasing out less secure domain validation methods")

December 10, 2025

Posted by Chrome Root Program Team

Secure connections are the backbone of the modern web, but a certificate is only as trustworthy as the validation process and issuance practices behind it. Recently, the [Chrome Root Program](https://security.googleblog.com/2023/05/how-chrome-root-program-keeps-users-safe.html) and the [CA/Browser Forum](https://cabforum.org/) have taken decisive steps toward a more secure internet by adopting new security requirements for HTTPS certificate issuers.

These initiatives, driven by Ballots [SC-080](https://cabforum.org/2024/11/14/ballot-sc080v3-sunset-the-use-of-whois-to-identify-domain-contacts-and-relying-dcv-methods/), [SC-090](https://cabforum.org/2025/11/20/ballot-sc-090-gradually-sunset-all-remaining-email-based-phone-based-and-crossover-validation-methods-from-sections-3.2.2.4-and-3.2.2.5/), and [SC-091](https://cabforum.org/2025/11/12/ballot-sc-091-sunset-3.2.2.5.3-reverse-address-lookup-validation-proposal-of-new-dns-based-validation-using-persistent-dcv-txt-record-for-ip-addresses/), will sunset 11 legacy methods for Domain Control Validation. By retiring these outdated practices, which rely on weaker verification signals like physical mail, phone calls, or emails, we are closing potential loopholes for attackers and pushing the ecosystem toward automated, cryptographically verifiable security.

To allow affected website operators to transition smoothly, the deprecation will be phased in, with its full security value realized by March 2028.

This effort is a key part of our public roadmap, “[Moving Forward, Together,](https://www.chromium.org/Home/chromium-security/root-ca-policy/moving-forward-together/)” launched in 2022. Our vision is to improve security by modernizing infrastructure and promoting agility through automation. While "Moving Forward, Together" sets the aspirational direction, the recent updates to the [TLS Baseline Requirements](https://cabforum.org/working-groups/server/baseline-requirements/requirements/) turn that vision into policy. This builds on our momentum from earlier this year, including the successful [advocacy for the adoption of other security enhancing initiatives](https://security.googleblog.com/2025/03/new-security-requirements-adopted-by.html) as industry-wide standards.

**What’s Domain Control Validation?**

Domain Control Validation is a security-critical process designed to ensure certificates are only issued to the legitimate domain operator. This prevents unauthorized entities from obtaining a certificate for a domain they do not control. Without this check, an attacker could obtain a valid certificate for a legitimate website and use it to impersonate that site or intercept web traffic.

Before issuing a certificate, a Certification Authority (CA) must verify that the requestor legitimately controls the domain. Most modern validation relies on “challenge-response” mechanisms, for example, a CA might provide a random value for the requestor to place in a specific location, like a DNS TXT record, which the CA then verifies.

Historically, other methods validated control through indirect means, such as looking up contact information in WHOIS records or sending an email to a domain contact. These methods have been proven vulnerable ([example](https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/)) and the recent efforts retire these weaker checks in favor of robust, automated alternatives.

**Raising the floor of security**

The recently passed CA/Browser Forum Server Certificate Working Group Ballots introduce a phased sunset of the following Domain Control Validation methods. Alternative existing methods offer stronger security assurances against attackers trying to obtain fraudulent certificates – and the alternative methods are getting [stronger](https://security.googleblog.com/2025/03/new-security-requirements-adopted-by.html) over time, too.

Sunsetted methods relying on email:

* [Email, Fax, SMS, or Postal Mail to Domain Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32242-email-fax-sms-or-postal-mail-to-domain-contact)
* [Email, Fax, SMS, or Postal Mail to IP Address Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32252-email-fax-sms-or-postal-mail-to-ip-address-contact)
* [Constructed Email to Domain Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32244-constructed-email-to-domain-contact)
* [Email to DNS CAA Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#322413-email-to-dns-caa-contact)
* [Email to DNS TXT Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#322414-email-to-dns-txt-contact)

Sunsetted methods relying on phone:

* [Phone Contact with Domain Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32243-phone-contact-with-domain-contact)
* [Phone Contact with DNS TXT Record Phone Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#322416-phone-contact-with-dns-txt-record-phone-contact)
* [Phone Contact with DNS CAA Phone Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#322417-phone-contact-with-dns-caa-phone-contact)
* [Phone Contact with IP Address Contact](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32255-phone-contact-with-ip-address-contact)

Sunsetted method relying on a reverse lookup:

* [IP Address](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32248-ip-address)
* [Reverse Address Lookup](https://cabforum.org/working-groups/server/baseline-requirements/requirements/#32253-reverse-address-lookup)

For everyday users, these changes are invisible - and that’s the point. But, behind the scenes, they make it harder for attackers to trick a CA into issuing a certificate for a domain they don’t control. This reduces the risk that stale or indirect signals, (like outdated WHOIS data, complex phone and email ecosystems, or inherited infrastructure) can be abused. These changes push the ecosystem toward standardized (e.g., [ACME](https://datatracker.ietf.org/doc/html/rfc8555/)), modern, and auditable Domain Control Validation methods. They increase agility and resilience by encouraging site owners to transition to modern Domain Control Validation methods, creating opportunities for faster and more efficient certificate lifecycle management through [automation](https://blog.chromium.org/2023/10/unlocking-power-of-tls-certificate.html).

These initiatives remove weak links in how trust is established on the internet. That leads to a safer browsing experience **for everyone**, not just users of a single browser, platform, or website.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/4435347292960683010)

[**](https://security.googleblog.com/)
**

[**](https://security.googleblog.com/2025/12/further-hardening-android-gpus.html "Older Post")

![](data...