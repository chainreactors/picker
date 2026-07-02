---
title: UK Cybercrime Journal: Argos Account Takeover Fraud
url: https://blog.bushidotoken.net/2026/07/uk-cybercrime-journal-argos-account.html
source: Over Security
date: 2026-07-01
fetch_date: 2026-07-02T05:58:13.078509
---

# UK Cybercrime Journal: Argos Account Takeover Fraud

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: Argos Account Takeover Fraud

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[July 01, 2026](https://blog.bushidotoken.net/2026/07/uk-cybercrime-journal-argos-account.html "permanent link")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjvTLBe45bDvwqP9X85tdOgKqSCKIUZlcJsVGNw8Zfnd1ATMIve2xnl5mIE46fTawt8NljnfXRzNCuAgJvL2WmQN20hazUnvFK3WsskGAR9W0wkUwuwRDuLR56k30P0lPV8OSEt8ddvxR9kP9mlTZOy4Ls2Haup9_furaeRUHFnYmFwvGXsPKRA88S4JbQB=w640-h312)](https://blogger.googleusercontent.com/img/a/AVvXsEjvTLBe45bDvwqP9X85tdOgKqSCKIUZlcJsVGNw8Zfnd1ATMIve2xnl5mIE46fTawt8NljnfXRzNCuAgJvL2WmQN20hazUnvFK3WsskGAR9W0wkUwuwRDuLR56k30P0lPV8OSEt8ddvxR9kP9mlTZOy4Ls2Haup9_furaeRUHFnYmFwvGXsPKRA88S4JbQB)

What Happened

* On 3 June 2026, the City of London Police issued a [warning](https://www.cityoflondon.police.uk/news/city-of-london/news/2026/june/report-fraud-alert-warning-for-argos-shoppers-after-323-per-cent-spike-in-fraud-reports-mentioning-the-retailer/report-fraud-alert-warning-for-online-shoppers-after-spike-in-criminals-gaining-unauthorised-access-to-retailer-accounts/) stating Report Fraud has seen a significant increase in cases mentioning the retailer, reflecting how criminals are targeting well-known brands.
* Report Fraud, which is run by the City of London Police, warned that cybercriminals are using leaked credentials from historical data breaches to hijack Argos user accounts.
* Once on the account, the fraudsters order and then collect the goods in-person at a physical store. In some instances, the goods are paid for using payment details not connected to the victim of the compromised account.
* Notably, the goods from fraudulent orders are often claimed via Click & Collect option that Argos allows, enabling the threat actors to retrieve goods in store.
* In May, Report Fraud received 652 reports which mention Argos, a 323% increase compared to April, when 154 reports mentioning the retailer were made. Since the start of 2026, there have been 1,175 reports mentioning the retailer, with May seeing the highest number to date.
* This alert is also not the first raised about Argos. On 18 November 2025, the East Midlands Cyber Resilience Center issued a [warning](https://www.emcrc.co.uk/post/currys-and-argos-account-warning-issued-by-police) about Argos and Currys accounts getting compromised and unauthorised purchases being made. In some instances, particularly with Currys, the Buy Now Pay Later (BNPL) option was used, leaving the account holder with finance plans in their names.

Analyst Comment

For both everyday UK consumers and UK retail risk teams, these alerts provide several layered insights. Retailers have spent years optimising Click & Collect to be as frictionless as possible to compete with online shopping giants like Amazon. However, this alert shows how Click & Collect can be a security liability. As Argos allows quick collections, criminals can buy an item online and pick it up at a local store before the real account owner notices an order confirmation email.

The police alerts also note that the items may even be paid for using payment details not connected to the victim. Criminals are mixing stolen accounts with stolen credit cards. This is likely due to an established Argos account with a multi-year history buying expensive items would look pretty normal to a fraud detection engines.

The combination of an Account Takeover (ATO) and Buy Now Pay Later (BNPL) fraud creates a difficult scenario for retailers, credit providers, and consumers. The regulatory and reputational fallout for a retailer under the rules of the UK Financial Conduct Authority (FCA) could be severe. If a retailer's poor account security allows fraudsters to easily spin up a finance plan in a victim's name, the FCA will view this as a systemic failure to protect consumers, resulting in massive fines.

These attacks are possible due to the practice of Argos users who are reusing the same previously leaked password across multiple accounts, plus users not having multi-factor authentication (MFA) turned on in their account settings.

Campaigns like this can trigger a reputational hit to retailers as victims often do not suffer silently. They take to social media to share stories and the public narrative can shift to being about a retailer who is complicit in disrupting innocent people's financial lives.

Defensive Takeaways

* User Account Hygiene Best Practices: Standard practices such as rotating passwords, using complex password, using a different password per service, using a password manager, using passkeys, and turning on MFA would all help mitigate this type of threat for users.
* Credit Monitoring: If a user suspects their account has been compromised, they should consider using a credit monitoring service to help prevent unauthorised loans taken out in their name.
* Cancel and Replace Payment Cards: If a user suspects their payment card data has been stolen, then they should contact their financial institution and have it cancelled and replaced.
* Implement Click-and-Collect Controls: Retailers with click-and-click options should introduce controls such as requiring ID of the account owner or a single-use QR code or PIN via SMS/Email at the point of collection for high-value items to prevent this type of fraud.
* Detecting Credential Stuff Attacks: If the cybercriminals were using credential stuffing attacks, then retailers should be able to detect unauthorised password guessing attempts against their online portals. It is recommended to use IP context analysis and perform source IP correlation. If one IP address tagged as a proxy or VPN is observed attempting to login to dozens of accounts simultaneously, then there’s an issue.
* Leverage Stripe’s FT3 framework: If your organisation or team is tasked with combating fraud, then categorising these scammers TTPs is crucial. That’s why Stripe has [developed](https://github.com/stripe/ft3) the Fraud Tools, Tactics, and Techniques (FT3) framework. It’s designed to help security teams understand the landscape, spot gaps, develop detections, improve incident response, and foster collaboration.

Relevant Sources

1. <https://www.cityoflondon.police.uk/news/city-of-london/news/2026/june/report-fraud-alert-warning-for-argos-shoppers-after-323-per-cent-spike-in-fraud-reports-mentioning-the-retailer/report-fraud-alert-warning-for-online-shoppers-after-spike-in-criminals-gaining-unauthorised-access-to-retailer-accounts/>
2. <https://www.emcrc.co.uk/post/currys-and-argos-account-warning-issued-by-police>

Social Media Intelligence (SOCMINT)

1. <https://www.reddit.com/r/LegalAdviceUK/s/NbOWRfzvgm>
2. <https://www.reddit.com/r/Argos/s/6uOo52UpHf>
3. <https://www.reddit.com/r/Argos/s/eZTgBhhNzp>
4. [https://x.com/donnaeenichols1/status/2060321697996161165](https://x.com/donnaeenichols1/status/2060321697996161165?s=46&t=-dkNDSDHEzyAagaVN0SDgA)
5. [https://x.com/lottyburns/status/1983581827127259558](https://x.com/lottyburns/status/1983581827127259558?s=46&t=-dkNDSDHEzyAagaVN0SDgA)

Relevant CTI Resources

1. <https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/>

[Argos](https://blog.bushidotoken.net/search/label/Argos)
[ATO](https://blog.bushidotoken.net/search/label/ATO)
[City of London Police](https://blog.bushidotoken.net/search/label/City%20of%20London%20Police)
[Click-and-collect](https://blog.bushidotoken.net/search/label/Click-and-collect)
[fraud](https://blog.bushidotoken.net/search/label/fraud)
[Report Fraud](https://blog.bushidotoken.net/search/label/Report%20Fraud)
[retail](https://blog.bushidotoken.net/search/label/retail)
[scams](https://blog.bushidotoken.net/search/label/scams)
[UK Cybercrime Journal](https://blog.bushidotoken.net/search/label/UK%20Cybercrime%20Journal)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular p...