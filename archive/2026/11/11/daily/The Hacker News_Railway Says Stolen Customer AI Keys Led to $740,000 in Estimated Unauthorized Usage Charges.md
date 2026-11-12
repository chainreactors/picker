---
title: Railway Says Stolen Customer AI Keys Led to $740,000 in Estimated Unauthorized Usage Charges
url: https://thehackernews.com/2026/11/railway-says-stolen-customer-ai-keys.html
source: The Hacker News
date: 2026-11-11
fetch_date: 2026-11-12T09:02:55.582504
---

# Railway Says Stolen Customer AI Keys Led to $740,000 in Estimated Unauthorized Usage Charges

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Railway Says Stolen Customer AI Keys Led to $740,000 in Estimated Unauthorized Usage Charges](https://thehackernews.com/2026/11/railway-says-stolen-customer-ai-keys.html)

**Swati Khandelwal**Nov 11, 2026Data Breach / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheDP-YSdactqjEqKJOJEJulSVt5fmo134ko3-hE9dbQrLkrcIuhIkAOQDPe4eGS8WR6mLJs3urGqLpdi9erHsuLMAQ1t2saYXZAhnIRNqzliU3reOp2uPoKCRlpWBj8JQcyRIwo9eqK4AuSFcsB5XhIdLFzNYudzLlW_eHiZ094cCzg_gjihMTAZufcCc/s1700-nu-rw-lo-l85-e365/railway-ai.jpg)

AI provider keys that customers stored on Railway were stolen in an October breach and used to commit an estimated $740,000 in unauthorized spending, the platform-as-a-service provider said yesterday. It has promised to pay those charges itself when an AI provider will not refund them.

The company builds and runs apps for its customers and stores their secrets, such as API keys and database credentials, as environment variables. The attacker decrypted variables in at most 1.85% of workspaces, about 100,000, and its database queries looked for AI provider keys.

In an October 26 update, the company told customers asking about refunds for unauthorized AI spend that "Railway is unable to refund customers for spend performed with compromised API keys." It encouraged them to contact the AI providers directly and offered to escalate their requests.

According to the company's [incident report](https://blog.railway.com/p/incident-report-october-security-incident), the decrypted data also included linked-account tokens for 1,852 users: BYOK agent keys and GitHub OAuth tokens. All were reset, each user was notified, and no logins to customer accounts using stolen credentials were found.

In addition to AI keys, one of the attacker's database queries matched cloud, database, and payment service credentials. The company's forensics did not show any customer databases being accessed, and there was no indication that customers' code repositories were downloaded.

The attacker also read the stored histories of 353 builds, including the variables and secrets passed to those builds.

The company's logs show which environments were exposed but not which variables, so the figure of about 100,000 workspaces is an upper limit. It emailed customers it judged to be at high risk.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Any data the attacker copied but did not decrypt can no longer be decrypted, because the credential the attacker used has been disabled, according to the company.

### What Railway Customers Can Do

Refund terms differ by AI provider, according to the company's incident report:

* **AWS Bedrock**: AWS's existing refund policy covers fraud, and its account teams have started refunds.
* **Google Gemini**: Google's existing refund policy covers fraud, and its account teams have started refunds.
* **OpenAI**: Refunds are reviewed on a case-by-case basis. Customers file a claim with OpenAI, then pass the case ID to Railway's support team.
* **SpaceXSI**: Refunds are reviewed on a case-by-case basis, and customers submit their claims to the same support team.
* **Anthropic**: Talks are still underway, and the platform will cover costs from breached Anthropic keys in the meantime.
* **OpenRouter**: It maintains its no-refund policy in its terms of service, so the platform will cover all OpenRouter-related costs resulting from the breach.

Customers are asked to report charges they did not make through a [charge report form](https://docs.google.com/forms/d/e/1FAIpQLScoZrMclYiCD0mGxQ0Gf8spo-Brqn8nT6Vu7Ye9mRwQrCTz_A/viewform). The form says the company "is not responsible for usage of these keys" but is investigating the theft and working with the providers.

The report does not say how the $740,000 figure was estimated or what period it covers. Neither it nor the form sets a cap or a deadline for claims, or states whether customers must pay disputed charges while a claim is under review.

The company advises customers to revoke and replace any sensitive variable stored on the platform before October 21. Keys should be revoked or rotated with the provider that issued them, since filing a charge report does not revoke a key.

It also advises removing public network access to databases, checking GitHub audit logs and which apps can access the account, and checking audit logs in registries such as Docker Hub. Most of this advice dates from the company's [October disclosure](https://thehackernews.com/2026/10/railway-says-intruder-may-have-accessed.html) and a report it published the next day.

Out of caution, the company also gave some providers every key it held for their services, so reset requests reached more than 100,000 users. A revocation notice from a provider does not by itself mean a key was exposed.

### How the Railway Breach Happened

The attack began in the company's build system, according to its incident report. At 07:28 UTC on October 20, the attacker exploited a previously unknown flaw to partly escape the filesystem isolation around a build and read some files on the host virtual machine.

That gave the attacker a credential that build servers use to push finished images and reach some internal systems. The on-call engineer was paged at 13:58 UTC, about six and a half hours after the first exploit, when an alert flagged unusual calls to a registry service.

The credential was meant only for build work, but the company's internal Temporal system, which drives parts of the build process, accepted it as a trusted client. Through it, the attacker read some stored histories of other builds.

The same credential could also fetch cached snapshots of code. That gave the attacker a copy of the company's internal monorepo, the code base that many of its services deploy from. The company says the copy showed the attacker how the platform works and helped them find exploits and move quickly between systems.

After sc...