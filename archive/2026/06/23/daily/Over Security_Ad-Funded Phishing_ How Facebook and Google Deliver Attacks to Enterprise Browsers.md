---
title: Ad-Funded Phishing: How Facebook and Google Deliver Attacks to Enterprise Browsers
url: https://pixmsecurity.com/blog/blog/ad-funded-phishing-heroku-azure-facebook-june-2026/
source: Over Security
date: 2026-06-23
fetch_date: 2026-06-24T06:05:52.371436
---

# Ad-Funded Phishing: How Facebook and Google Deliver Attacks to Enterprise Browsers

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
  + [Case Studies](https://pixmsecurity.com/case-studies/)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# Ad-Funded Phishing: How Facebook and Google Deliver Attacks to Enterprise Browsers

![](https://pixmsecurity.com/wp-content/uploads/2026/06/fb-ad.png)

Between June 16 and June 22, we detected phishing campaigns spanning tech support scams delivered via Facebook ads on Azure infrastructure, Microsoft credential harvesting hosted on Heroku and promoted through Google Ads, Paperless Post invitation lures targeting multiple email providers. What ties them together: these campaign abused trusted infrastructure both to host and deliver their attacks.

## Malicious Domains Observed

`viruswarning0617usl4hg7z.z13.web.core.windows[.]net`

`viruswarning0618usvlbg4m.z13.web.core.windows[.]net`

`loser-16-003-d8023de4cfba.herokuapp[.]com`

`lock-16-002-4654c9f72ff8.herokuapp[.]com`

`secondsightsystilqemsllc[.]vu`

`_wildcard_.lumrix[.]vu`

`shirleysmasonry[.]blog`

`mainwelviolive[.]one`

## Tech Support Scams: Azure Blob Storage Meets Facebook Ads

On June 17th, a user encountered a tech support scam page hosted on Azure Blob Storage at `viruswarning0617usl4hg7z.z13.web.core.windows[.]net`. The page displayed cascading fake “System Error” and “Security” dialogs claiming memory access violations and System32 password requirements, alongside a fabricated Tawk.to chat widget impersonating Microsoft Support. The page directed victims to call +1 (844) 950-5399.

![](https://pixmsecurity.com/wp-content/uploads/2026/06/01-azure-tech-support-scam.jpeg)

Azure-hosted tech support scam with cascading error dialogs and fake Tawk.to chat widget.

On June 18th, we detected a nearly identical variant at `viruswarning0618usvlbg4m.z13.web.core.windows[.]net` using a different phone number — +1 (855) 920-7052. Both pages were delivered via Facebook ad campaigns, with full UTM tracking parameters (`utm_medium=paid&utm_source=fb`) and Facebook click IDs embedded in the URLs. This isn’t opportunistic hosting — it’s paid distribution through a major ad network, directing traffic to Microsoft’s own Azure infrastructure.

![](https://pixmsecurity.com/wp-content/uploads/2026/06/02-azure-tech-support-variant.jpeg)

Second Azure tech support scam variant with different scam phone number, also delivered via Facebook ads.

This pattern aligns with broader reporting: [BleepingComputer documented](https://www.bleepingcomputer.com/news/security/microsoft-tech-support-scams-invade-azure-cloud-services/) similar Azure Blob tech support scam campaigns earlier in 2026, and researchers at [GBHackers found](https://gbhackers.com/azure-tech-support-scams/) attackers weaponizing Bing Ads for the same purpose. What we observed this week adds Facebook as another paid delivery channel.

## Heroku-Hosted Credential Phishing via Google Ads

On June 16th, we detected two Microsoft credential harvesting pages hosted on Heroku — `loser-16-003-d8023de4cfba.herokuapp[.]com` and `lock-16-002-4654c9f72ff8.herokuapp[.]com`. Both presented pixel-perfect Microsoft “Enter password” login pages with pre-populated email addresses.

![](https://pixmsecurity.com/wp-content/uploads/2026/06/03-heroku-microsoft-credential-phish.jpeg)

Microsoft credential phishing page hosted on Heroku with Google Ads tracking parameters.

The URLs contained Google Ads parameters (`gad_source=5`, `gad_campaignid`, `gclid`), indicating these phishing pages were promoted through paid Google search ads. [Malwarebytes has flagged](https://www.malwarebytes.com/blog/detections/herokuapp-com) multiple Heroku subdomains for phishing involvement, and [researchers at Varonis](https://www.techradar.com/pro/security/this-new-cybercrime-platform-lets-hackers-run-malicious-google-ads-and-hide-from-googles-screening-process) identified a platform called 1Campaign specifically designed to help attackers evade Google’s ad review process. The combination of a legitimate PaaS host and paid search placement makes these pages particularly difficult to catch with traditional filtering.

## Paperless Post Lures Target Multiple Email Providers

On June 22nd, we detected two Paperless Post invitation phishing pages hosted on `.vu` domains — `_wildcard_.lumrix[.]vu` and `secondsightsystilqemsllc[.]vu`. The pages impersonated the Greenvelope/Paperless Post brand, presenting “Manage your Online Invitations & Greeting Card” with buttons to “Sign in with Outlook,” “Sign in with Office365,” “Sign in with Gmail Mail,” “Sign in with Yahoo Mail,” “Sign in with AOL,” and “Sign in with Other Mail.”

![](https://pixmsecurity.com/wp-content/uploads/2026/06/05-paperless-post-multi-provider.jpeg)

Paperless Post phishing lure with credential harvesting buttons for six email providers.

This is a broad-net approach — one page harvests credentials from six email providers simultaneously. [McAfee reported](https://www.mcafee.com/blogs/tips-tricks/think-that-party-invite-is-real-fake-e-vite-scams-are-the-new-phishing-trap/) a spike in fake e-vite scams using this exact pattern in 2026, and [Washington University’s InfoSec team](https://informationsecurity.wustl.edu/scam-of-the-month-special-invite/) flagged fake Paperless Post invitations hitting university mailboxes in May 2026.

## Microsoft Credential Harvesting on Compromised Domains

On June 16th, we also detected a Microsoft login phishing page hosted on a compromised `.blog` domain — `shirleysmasonry[.]blog` — with a long obfuscated path suggesting automated deployment. The page was a near-perfect replica of the Microsoft password entry screen.

![](https://pixmsecurity.com/wp-content/uploads/2026/06/06-microsoft-phish-compromised-blog.jpeg)

Microsoft credential phishing page on a compromised .blog domain.

A separate credential page on `mainwelviolive[.]one` used an “AcrobatN” path, spoofing an Adobe/Acrobat document-sharing flow to harvest Office 365 and Hotmail credentials.

## Recommended Mitigations

* **Block or flag the `.vu` TLD and newly registered domains** observed this week at the network perimeter. The `.vu` (Vanuatu) TLD appeared across multiple campaigns and is rarely used in legitimate enterprise traffic.
* **Monitor for Azure Blob Storage URLs paired with tech support keywords.** The `z13.web.core.windows.net` pattern continues to carry Microsoft’s domain reputation while hosting scam content.
* **Flag Heroku-hosted pages reached via paid search ads.** Legitimate enterprises rarely serve login pages from `herokuapp.com` subdomains — this combination is a strong phishing signal.
* **Deploy browser-level security that analyzes page behavior,** not just the domain serving it. Every campaign this week exploited legitimate infrastructure that domain-reputation tools trust by default.

If you are interested in seeing how PIXM can help prevent attacks like these for your organization, book a demo here: [pixmsecurity.com/request-demo/](https://pixmsecurity.com/request-demo/).

Search for:

#### Recent Posts

* [Ad-Funded Phishing: How Facebook and Google Deliver Attacks to E...