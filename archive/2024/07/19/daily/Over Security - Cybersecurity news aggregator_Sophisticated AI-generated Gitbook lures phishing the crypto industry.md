---
title: Sophisticated AI-generated Gitbook lures phishing the crypto industry
url: https://www.netcraft.com/blog/ai-generated-gitbook-lures-phishing-the-crypto-industry/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-19
fetch_date: 2025-10-06T17:42:57.332949
---

# Sophisticated AI-generated Gitbook lures phishing the crypto industry

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[Pricing](../get-pricing)

[Contact Us](../contact)

[Report Fraud](https://report.netcraft.com/)

[Login](https://services.netcraft.com/)

Platform

Solutions

[Why Netcraft](../why-netcraft)

Resources

Company

[GET Demo](../book-a-demo)

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[Pricing](../get-pricing)

[Contact Us](../contact)

[Report Fraud](https://report.netcraft.com/)

[Login](https://services.netcraft.com/)

Platform

Solutions

[Why Netcraft](../why-netcraft)

Resources

Company

[GET Demo](../book-a-demo)

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[## ALL POSTS](../resources/blog)

[## ALL POSTS](../resources/blog)

[## ALL POSTS](../resources/blog)

# Sophisticated AI-generated Gitbook lures phishing the crypto industry

By

By

By

Bilaal Rashid

Bilaal Rashid

Bilaal Rashid

|

|

|

July 17, 2024

July 17, 2024

July 17, 2024

![](https://framerusercontent.com/images/jxxRGtMLzq6QxJ4GYRCCbx2QFQ.svg?width=27&height=28)

![](https://framerusercontent.com/images/qxE8AF5N0tvgi2NQPrJxo2Fjec8.svg?width=27&height=28)

![](https://framerusercontent.com/images/iPf6JKc4mxyBKQ0kzbQ3awaw.svg?width=27&height=28)

![Reddit logo](https://framerusercontent.com/images/SgQ1svDD2syGHlolx4eeBq0UPA.svg?width=28&height=29)

![](https://framerusercontent.com/images/OvIZoc9zdYHfrOLzrAEwSXY9ro.png?width=1424&height=718)

![](https://framerusercontent.com/images/OvIZoc9zdYHfrOLzrAEwSXY9ro.png?width=1424&height=718)

![](https://framerusercontent.com/images/OvIZoc9zdYHfrOLzrAEwSXY9ro.png?width=1424&height=718)

![](https://framerusercontent.com/images/OvIZoc9zdYHfrOLzrAEwSXY9ro.png?width=1424&height=718)

For the past year, Netcraft researchers have been tracking a threat actor using generative AI to assist in the creation of 17,000+ phishing and lure sites. These sites operate as infrastructure for phishing attacks that target more than 30 major crypto brands, including Coinbase, Crypto.com, Metamask, Trezor, and others.

These sites form part of a sophisticated, multi-step attack. The attack utilizes lure sites to hook victims, phishing sites to capture details, and a Traffic Distribution System (TDS) used to mask the relationships between attack infrastructure. With advanced deception techniques, like the ability to capture 2-factor authentication codes, this campaign highlights several of the most innovative capabilities of modern multi-channel phishing threats.

As phishing attacks become [more complex than ever](https://www.netcraft.com/blog/popular-email-platform-used-to-impersonate-itself/), recent advancements in generative AI further enhance these attacks by enabling threat actors to rapidly automate the creation of unique content that convincingly impersonates a wide variety of targets. The use of gen AI is also evident in other forms of cybercrime, such as [donation scams](https://www.netcraft.com/blog/trumped-up-crypto-donation-scams/) and [Advance Fee Fraud](https://www.netcraft.com/blog/flipping-the-script-on-pig-butchering/).

Interestingly, many of these AI-generated lure sites do not link to a phishing website, which appears deliberate. These are likely not designed for victims but instead suggest an attempt to flood the Web with similar content, making it harder to find the malicious needles in an AI-generated haystack. Without gen-AI, this new deception technique would be impossible for criminals, even criminal groups, to deploy at scale. For those combatting these threats, utilizing AI, ML, and automated techniques to detect and monitor threats is paramount in identifying and disrupting these nefarious techniques at any scale.

## Anatomy of the attack

The attack starts with the victim visiting an AI-generated lure site. Lure sites hook unsuspecting victims into a scam and encourage them to complete an action, such as visiting another site, downloading a file, or sending an email. Commonly, lures are shared through various channels like email, SMS, social media, and SEO hacking. One widespread method used by this threat actor is distributing these links in the comment section of legitimate websites.

![](https://framerusercontent.com/images/RdIzghkGqsOeB3oStmJmKMU3qf0.png?width=1423&height=934)

hxxp[://]forum[.]technikboard[.]net/index[.]php?page=UserBlogEntry&entryID=8

These lure sites are hosted on Gitbook, a documentation platform that targets software developers and offers a free tier requiring only an email address to sign up. Supported by vast amounts of content to increase credibility, the lure sites entice the victim by claiming to offer advice and tutorials for products from a wide range of brands in the crypto industry.

![](https://framerusercontent.com/images/mVrT3UUYimHYhoXARsaovWfx9Y.png?width=1024&height=768)

*Example of an AI-generated lure site on hxxps[://]helpstrezorhardwrewallet[.]gitbook[.]io/us*

Most sites contain a call-to-action link, which directs the user to a redirect URL on one of many [.]com domains. These URLs contain a Universally Unique Identifier (UUID) in the path to track which brand or lure site the victim visited. All these domains appear to be purpose-registered with Key Systems and hosted by Amazon.

![](https://framerusercontent.com/images/mOCs2cx6GpPc7MqVjNGXkjld6U.png?width=1024&height=279)

*Formatted extract from hxxps[://]helps-trezorhardwrewallet[.]gitbook[.]io/us*

These redirect URLs use advanced Traffic Distribution Systems (TDSes), which can choose the redirect destination based on various factors. For example, if the TDS thinks the visitor is a victim, it will redirect them to a phishing site. When the TDS detects that the visitor is a security researcher, it will instead redirect them to the target brandâs legitimate site, attempting to cloak the existence of the phishing attack.

![](https://framerusercontent.com/images/ArsnTJwGUvLx5MvJX762ivO9Xw.png?width=1024&height=688)![](https://framerusercontent.com/images/Ks4nw7XeXdw2N5Cerbu2SVAs7zk.png?width=484&height=363)

*Visiting hxxps[://]shotheatsgnovel[.]com/1479dd91-86b0-4518-9970-ca644964c5e7 from an IP address the TDS classified as a security researcher (left) and an IP address classified as a victim (right)*

The end phishing sites in this campaign aim to obtain one of two sets of credentials: the victimâs login details for the cryptocurrency platform or the seed recovery phrase for the victimâs wallet. If required by the platform, these phishing sites can even exfiltrate the victimâs 2-factor authentication codes, undermining the protection from this trusted layer of security.

![](https://framerusercontent.com/images/lqkbuWOn3hgTv2nZyRtl6N8jQc.png?width=1024&height=697)![](https://framerusercontent.com/images/OC3F4pGIV5nG7egXGir0PjpawNU.png?width=1024&height=768)

*Left hxxps[://]trazeorwalllet[.]azurewebsites[.]net/*, right *hxxps[://]bitmartesnc[.]azurewebsites[.]net/*.

With either set of credentials, the threat actor can steal all the victimâs funds or sell the credentials on an underground marketplace for another criminal to do so. The pseudo-anonymous nature of cryptocurrency payments offers the threat actor a high degree of anonymity, making it highly desirable for cybercriminals. Even after [accounts are drained](https://www.netcraft.com/blog/ipfs-powered-crypto-drainer-scams-leveraging-look-alike-cdns/), they are still valuable to criminals since they have already passed Know Your Customer (KYC) requirements and could be used to launder money.

This campaignâs lure and phishing sites are hosted on Microsoft Azureâs App Service platform (azurewebsites[.]net). As seen in previous attacks, such as the [Phishception attack we ...