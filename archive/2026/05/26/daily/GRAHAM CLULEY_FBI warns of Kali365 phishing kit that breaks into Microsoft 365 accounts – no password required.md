---
title: FBI warns of Kali365 phishing kit that breaks into Microsoft 365 accounts – no password required
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/fbi-kali365-phishing-kit-breaks-microsoft-365-accounts-no-password-required
source: GRAHAM CLULEY
date: 2026-05-26
fetch_date: 2026-05-27T06:12:40.962917
---

# FBI warns of Kali365 phishing kit that breaks into Microsoft 365 accounts – no password required

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

3 min read

# FBI warns of Kali365 phishing kit that breaks into Microsoft 365 accounts — no password required

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

May 26, 2026

  ![FBI warns of Kali365 phishing kit that breaks into Microsoft 365 accounts — no password required](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/05/microsoft-365-phishing-hooks.jpeg "FBI warns of Kali365 phishing kit that breaks into Microsoft 365 accounts — no password required")

So, you've enabled multi-factor authentication. You've taught your staff never to type their passwords into dodgy-looking login pages. Surely your Microsoft 365 accounts are safe now?

Well, think again.

The FBI has issued an [advisory](https://www.ic3.gov/PSA/2026/PSA260521) warning about a phishing-as-a-service platform that has recently emerged, which can hijack Microsoft 365 accounts without ever stealing a password. And it has no difficulty waltzing past MFA while it's at it.

Kali365 is a subscription service for scammers that was first spotted in April 2026, and has been promoted largely through Telegram.

It is a turnkey toolkit that allows even non-technical fraudsters to run sophisticated phishing campaigns, reportedly for as little as US $250 per month or $2,000 a year.

Subscribers to Kali365 have access to AI-generated phishing lures, automated campaign templates, real-time dashboards for tracking targets, and the ability to capture OAuth tokens. In other words, it's everything even a complete newbie would need to launch a phishing attack.

And the threat is not hypothetical. Security researchers documented [hundreds of Kali365 attacks](https://arcticwolf.com/resources/blog/token-bingo-dont-let-your-code-be-the-winner/) in April alone, hitting organisations cross North America and Europe.

The common factor in the attacks? The victim had deployed MFA.

What makes Kali365 so successful I suspect is that it does not need to fool victims with a fake login page. Instead, it abuses a legitimate Microsoft feature.

If you have ever signed into a streaming service like Amazon Prime or Netflix on a smart TV you have probably been promoted to type a short code into a website on your phone.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2026/05/amazon-device-registration-screen.jpeg)

If you've done that, you've used "device code flow." That's the technology which allows a gadget to borrow an authenticated session from another device.

The Kali365 attack works the same way. You receive a phishing email which is disguised as a message from a trusted cloud service, asking you to visit a Microsoft verification page and enter a code.

You go to the *genuine* Microsoft page and type in the code. You may think you have acted entirely safely.

After all, it was a genuine Microsoft domain, your password manager recognised it correctly, the site's SSL certificate is valid, and there are no typos in the URL.

However, what you have actually done is authorise an *attacker's* device to access *your* account.

Microsoft hands the criminal an OAuth token - proof you are logged in - granting them unfettered access to your Microsoft Outlook, Teams, and OneDrive with no password and no further prompts to enter an MFA code.

In short, there is no fake website to spot, and no misspelt domain name. The single stolen token can unlock other cloud apps, potentially turning one careless click into a wide-ranging security incident.

The thing to remember here is that MFA stops attackers from logging in *as you*. It does nothing to prevent you from *granting access* to an attacker through a workflow that Microsoft considers entirely legitimate.

The criminals are never asked to answer an MFA challenge, because as far as Microsoft is concerned the victim already has.

And this is why the FBI's top recommendation is to block device code flow, with a conditional access policy in Microsoft Entra ID where appropriate. You will probably want to exclude emergency access accounts so you don't accidentally lock yourself out entirely.

And it is always a good idea to roll-out phishing-resistant MFA, such as hardware security keys, which tie authentication to a physical device and are much harder to circumnavigate.

The FBI's Internet Crime Complaint Center is encouraging victims to report incidents to it via its website at [ic3.gov](https://www.ic3.gov/).

tags

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

---

### Author

---

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=150&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[## Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s.

[View all posts](/en-us/blog/hotforsecurity/author/gcluley)

---

## You might also like

#### Bookmarks

---

![loader](https://download.bitdefender.com/resources/themes/draco/images/lite_v2/blog-images/loader-white.svg "loader")

[Legal Information](https://www.bitdefender.com/site/view/legal-terms.html "Legal Information") | [Privacy Policy](https://www.bitdefender.com/site/view/legal-privacy-policy-for-bitdefender-websites.html "Privacy Policy") | [Contact Us](https://www.bitdefender.com/site/Main/contact/1 "Contact Us")

Copyright © 1997 - 2026 Bitdefender.