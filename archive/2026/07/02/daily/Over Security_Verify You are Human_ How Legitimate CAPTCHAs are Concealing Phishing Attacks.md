---
title: Verify You are Human: How Legitimate CAPTCHAs are Concealing Phishing Attacks
url: https://pixmsecurity.com/blog/blog/verify-you-are-human-how-legitimate-captchas-are-turning-the-tables-and-concealing-phishing-attacks/
source: Over Security
date: 2026-07-02
fetch_date: 2026-07-03T05:48:40.051164
---

# Verify You are Human: How Legitimate CAPTCHAs are Concealing Phishing Attacks

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

# Verify You are Human: How Legitimate CAPTCHAs are Concealing Phishing Attacks

![](https://pixmsecurity.com/wp-content/uploads/2026/07/captcha.png)

Between June 23 and 30, the phishing we detected in enterprise browsers clustered around two themes that also dominated the week’s security headlines: fake e-card “invitations” that harvest corporate credentials and fake “virus” warnings that push victims to phone a scammer. Both leaned on infrastructure users are trained to trust to slip past reputation filters, including CAPTCHAs to conceal attacks and gain user trust. Here’s what we saw.

## Malicious Domains Observed

* qavniro[.]vu
* hovex[.]sbs
* metrxevent51[.]top
* celeebrationpartyy[.]one
* check.apucv[.]vu
* bakersflame[.]in (second-stage Google credential page)
* viruswarning0625uski6ky2[.]z13[.]web[.]core[.]windows[.]net
* viruswarning0626uspv0rkm[.]z13[.]web[.]core[.]windows[.]net
* viruswarning0626usshj03g[.]z13[.]web[.]core[.]windows[.]net
* viruswarning0630usphtcaw[.]z13[.]web[.]core[.]windows[.]net
* 1012qhjrwepzzclfwtpzgghq-bqadcfaghxhvcegy[.]z03[.]azurefd[.]net
* strmnflxsd.chf.40-81-246-96[.]cpanel[.]site

Scam callback numbers observed: +1 (888) 951-8555, +1 (888) 495-7216, +1 (888) 725-4102, +1 (877) 291-7893 (Windows), and +1-855-920-5991 (Mac).

## Party Invitations That Steal Your Password — and Your OTP

The most persistent thread was a family of invitation- and document-themed lures. We detected pages skinned as Paperless Post, Punchbowl Post, Greenvelope, and Adobe Document Cloud — all real services — each fronting the same credential-harvesting kit.

On June 23, qavniro[.]vu presented a “Paperless Post” invitation; on June 24, hovex[.]sbs used a “Punchbowl Post” skin; on June 25, metrxevent51[.]top ran a “Greenvelope” version; and on June 29, check.apucv[.]vu dressed itself as an “Adobe Document Cloud” shared file. Different wrappers, identical machinery underneath.

The flow is always the same: pick your email provider (Outlook, Office 365, Yahoo, AOL, Gmail), then a login box appears.

![](https://pixmsecurity.com/wp-content/uploads/2026/07/01-invitation-provider-select.jpeg)

Fake invitation page prompting the victim to choose an email provider to “view” the invite.

Enter your password and the page returns “Incorrect Password” — on purpose — to farm a clean second attempt. Then it asks for the one-time code “sent to your phone,” some versions running a five-minute countdown to rush you. Capturing that OTP is what lets an attacker walk straight past MFA.

![](https://pixmsecurity.com/wp-content/uploads/2026/07/02-invitation-fake-incorrect-password.jpeg)

The same kit’s fake “Incorrect Password” error, designed to capture a second, clean password entry.

Two details made the operation pop. First, the Greenvelope variant’s “Gmail” button peeled off to a separate second-stage Google phishing page at bakersflame[.]in — a reminder these kits chain across hosts. Second, and more telling: every one of these invitation domains hid behind Cloudflare.

On disposable TLDs — .vu, .sbs, .top, .one — not one of them resolved to the attacker’s own server. Each pointed at Cloudflare’s edge (the 104.21.x, 172.67.x, and 2606:4700:: addresses Cloudflare hands out), so the real origin stayed invisible and any reputation check saw nothing but Cloudflare. The Adobe-skinned check.apucv[.]vu went a step further and switched on Cloudflare’s genuine “Verify you are human” challenge — not a look-alike graphic, but the real managed-challenge gate, complete with a live \_\_cf\_chl token in the URL. That gate pulls double duty: it makes the page feel legitimate to a victim, and it turns away the automated crawlers and sandboxes that would otherwise flag the phish, helping it stay up longer.

This matches what consumer outlets reported all week. NBC Los Angeles [documented](https://www.nbclosangeles.com/news/local/phishing-scam-electronic-invitation/3881054/) a Southern California victim who lost more than $5,000 to an e-invitation phish, and by late June, warnings were circulating about combined [Punchbowl and Paperless Post lookalikes](https://geekmamas.com/2026/06/26/punchbowl-and-paperless-post-invitation-phishing-scam/). Paperless Post has [confirmed](https://paperlesspost.zendesk.com/hc/en-us/articles/360049322272-Spotting-fake-Paperless-Post-emails-and-spam-texts-How-to-know-what-s-real) it is aware of campaigns impersonating its brand. The tell is simple: real invitation services never make you log into your email to view a card.

## Fake Virus Warnings, Hosted on Microsoft’s Own Cloud

The second theme was tech-support scareware delivered through paid ads. Between June 25 and 30 we repeatedly detected near-identical “Windows Support” pages on Microsoft Azure Blob Storage, all reached through Facebook ad links — the URLs carry Facebook’s utm\_source=fb and fbclid tags. Each page cloned the Microsoft Support site, then buried it under cascading fake “System Error / Memory access violation” dialogs, a fake SmartScreen block naming “Trojan.Spy.Win32,” a “Windows Firewall has locked your session” prompt, and a scripted “Microsoft Support” chat — all funneling to a toll-free number. The pages were effectively identical; only the callback number rotated between deployments.

![](https://pixmsecurity.com/wp-content/uploads/2026/07/03-windows-tech-support-scam-azure.jpeg)

Fake Microsoft “Windows Support” scareware page hosted on Azure Blob Storage, reached via a Facebook ad.

This is the same playbook [Netskope documented in February](https://cyberpress.org/facebook-ads-promote-tech-scam/), when an ad-driven campaign staged Microsoft tech-support scams in Azure Blob containers and hit dozens of U.S. organizations within hours. Five months later it is still running — and still on Azure.

Mac users weren’t spared. On June 29 we detected a variant on Azure Front Door, Microsoft’s CDN, that flipped the branding to Apple: an “Apple\_MacOS locked due to unusual activity” alert with a fake antivirus scan and the number +1-855-920-5991. This one fought back — it spawned runaway browser workers to freeze the tab if you tried to leave, looped an alarm sound, and offered a live chat to reach “an expert.” Hosting a fake Apple warning on Microsoft’s cloud is the entire point: the domain looks trustworthy.

![](https://pixmsecurity.com/wp-content/uploads/2026/07/04-mac-tech-support-scam-azure.jpeg)

Fake Apple/macOS “virus alert” scareware hosted on Azure Front Door.

## A Netflix Look-Alike on Shared Hosting

Rounding out the week, on June 26 we detected a Netflix credential clone on a cpanel.site subdomain. It skipped the email step entirely — the victim’s address was already filled in, so it only asked for the password — and wrapped a fake reCAPTCHA “verification required” gate around the form to look legitimate and slow down analysis. The page was heavily obfuscated, a reminder that even a simple streaming-login phish now s...