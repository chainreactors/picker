---
title: New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA
url: https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html
source: The Hacker News
date: 2026-08-10
fetch_date: 2026-08-11T03:31:51.451865
---

# New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA

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

# [New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA](https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html)

**Swati Khandelwal**Aug 10, 2026Identity Security / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWKCkGCqH-c6Yaqkd_NnzFQijViu34tjAEsdl9tl2CmZLHL4m1rLhezO76zF6XFRTGS9Sr4R3jhMD7z15QV0BMqG948bjg8SoZb_j6HtQajd0PUDR8Tmw06GMqDwS6VhAtH-ZNtD06lzb9KMhJsHi-Vvkps0n6bl6C8n6rSBHCldBuc1cMczr30h11N-8/s1700-e365/passkeys.jpg)

Three separate research efforts last week demonstrated ways to defeat passkey protections without breaking the cryptography they rest on.

Passkeys are designed to replace reusable passwords and resist phishing. The attacks instead reused signed authentication material that Windows had exposed, abused a cloud-synced passkey system from malware already on the victim's machine, and used a [Windows Hello for Business](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html#phishing-resistant-windows-login) key from a compromised user session without a fresh PIN or biometric check. None cracked the math.

The impact is not the same in all three cases.

* SpecterOps showed a Windows and Microsoft Entra ID chain that could impersonate privileged users while satisfying phishing-resistant multifactor authentication (MFA); that chain reused signed authentication material rather than stealing the authenticator's private key.
* Unit 42 showed attacks against [Google Password Manager in Chrome](https://thehackernews.com/2026/08/google-password-manager-attacks-could.html), including a path that recovers the private keys for a victim's synced passkeys.
* Independent researcher [Dirk-jan Mollema showed](https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html) that malware already running in a signed-in Windows session can use a hardware-bound Windows Hello for Business key without asking the user to unlock it again.

The fixes and mitigations differ too. Microsoft's Windows logging vulnerability, **CVE-2026-34348**, has a vendor CVSS score of 6.5 and a Microsoft security update. Microsoft told The Hacker News that it has also applied mitigations for the reported issue involving passkey relay assertions.

Microsoft's Entra [migration guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement), last updated August 3, 2026, continues to describe passkeys as resistant to replay attacks. The public Microsoft advisory tied to CVE-2026-34348 covers the Windows Event Logging Service issue, while the company's response did not provide technical details about the scope of the separate Entra-side mitigations.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

"We appreciate the work of SpecterOps for reporting this through a coordinated vulnerability disclosure. We have applied mitigations for the reported issue involving passkey relay assertions and continue investing in security enhancements across authentication methods. We recommend adopting a least-privilege access approach, using phishing-resistant authentication methods, and maintaining endpoint protections by embracing a [Zero Trust](https://www.microsoft.com/en-us/security/business/zero-trust) security model to be better protected," a Microsoft spokesperson told The Hacker News.

The Unit 42 and Mollema findings also show why no single choice between synced and device-bound passkeys closes the broader attack surface.

The Hacker News has also reached out to SpecterOps for further detail on its latest testing and will update this story with any response.

## The login Windows kept

SpecterOps principal security researcher Michael Grafnetter presented the firm's [Pass-the-Passkey research](https://specterops.io/wp-content/uploads/sites/3/2026/08/Pass-the-Passkey_A4_v2.pdf) at Black Hat USA 2026 on August 5.

SpecterOps says Windows stored past YubiKey signatures in cleartext where authenticated unprivileged users, including remote users, could read them. The firm says chaining those signatures with weaknesses in Microsoft Entra ID's passkey validation allowed privileged-user impersonation despite policies requiring phishing-resistant MFA.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhWoSqie2wunO5gAM8ZO_idZF62oVhnX9TBpz1EBIZc_hqXs9-lCQPAFURsrHTqYubrhZZS0A5l4cQ7jNS4dYA5-wJG0xD2245uKB-fXuK1fEyzvNwQaeBvOwouN50vBss5hjLE-T5YFCgAP-oOfFwqwbSWxvO50yK-MCkXzLzfrA-FjqCADW5BjLM-sQ/s1700-e365/ms-key.jpg)

The Windows issue is tracked as [CVE-2026-34348](https://nvd.nist.gov/vuln/detail/CVE-2026-34348), an information-disclosure vulnerability in the Windows Event Logging Service. Microsoft's affected-product data covers releases across Windows 10, Windows 11 and Windows Server. The CVE's product scope does not establish that SpecterOps' full passkey chain works identically on every listed Windows release.

In this chain, the attacker does not need to extract the private key from a YubiKey or other authenticator. The dangerous material is an already generated signature that Windows retained and that SpecterOps says Entra ID accepted in the replay chain. That is a narrower failure than breaking FIDO2, but it can still produce the result defenders care about: an attacker authenticating as someone else.

## The master key behind Google's synced passkeys

[Unit 42's Pass-ta-key research](https://thehackernews.com/2026/08/google-password-manager-attacks-could.html) targets Google Password Manager's synced-passkey system in Chrome on Windows. All three attacks described by the team start with malware already running on the victim's endpoint, without requiring an administrator-level privilege escalation.

The first path abuses Chrome's device identity machinery to obtain the signatures needed to act like a legitimate Google Password Manager client without a new device unlock or user interaction. Unit 42 demonstrated the technique against eBay even though the site requested user verification; after the researchers reported the problem, eBay changed its validation of the WebAuthn user-verification flag.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R...