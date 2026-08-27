---
title: NovaCookies Campaigns Abuse Genuine Docusign Notifications to Steal Microsoft 365 Sessions
url: https://thehackernews.com/2026/08/novacookies-campaigns-abuse-genuine.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:29.501678
---

# NovaCookies Campaigns Abuse Genuine Docusign Notifications to Steal Microsoft 365 Sessions

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [NovaCookies Campaigns Abuse Genuine Docusign Notifications to Steal Microsoft 365 Sessions](https://thehackernews.com/2026/08/novacookies-campaigns-abuse-genuine.html)

**Ravie Lakshmanan**Aug 26, 2026Phishing / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiz4GD3giiT1DIPT5Q13XvCZcwC8-STaGCZ3KbqUzQ5Q9oniGfA0Odbqfmwva6B-xSSTD2QG1wdqu5fFOleaBVFSA-t3ZfeqpcrYOEomdygWsZOONJXYcpxhRdT-EbTS_DZ0zYLrH_-1YN7TjXCsDuIj0I2G53mFT0df1HC3tjUdUQ5MCdHdEo27rDE2QEm/s1700-e365/docusign.jpg)

Cybersecurity researchers have disclosed details of a new adversary-in-the-middle ([AitM](https://thehackernews.com/2026/08/microsoft-365-aitm-phishing-hijacks.html)) phishing toolkit called **NovaCookies** that's used as a proxy to redirect Microsoft 365 sign-ins, while capturing authenticated sessions in the process.

In a [report](https://www.island.io/blog/novacookies-at-scale-inside-the-320-phishing-service-targeting-hundreds-of-organizations) shared with The Hacker News ahead of publication, Island characterized the $320/month service as a subscription-based phishing platform that facilitates real-time Microsoft 365 session theft. The kit has been used to target hundreds of organizations across multiple sectors in the U.S., the U.K., Canada, Germany, Israel, and the U.A.E. to date.

"Observed campaigns used genuine Docusign envelopes to carry counterfeit document-share lures, with some clicks routed through legitimate Microsoft or Google sign-in endpoints as redirect hops before reaching the kit," Island said. "The message, document service and redirect can therefore appear trustworthy until the browser reaches attacker-controlled infrastructure."

Like other AitM phishing kits, NovaCookies is designed to relay Microsoft 365 authentication through attacker-controlled infrastructure, allowing it to act as a proxy and harvest the resulting session after victims enter their passwords and multi-factor authentication (MFA) codes.

Evidence indicates that NovaCookies is advertised via Telegram, with the messaging service also used as infrastructure to manage customer profiles, configure redirect services, and contact support. According to Proofpoint, NovaCookies is assessed to be a variant of the [Sneaky 2FA](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html) phishing kit.

"While the original Sneaky2FA appeared to focus mainly on Microsoft accounts, the NovaCookies variant includes dedicated flows for other identity providers, including Okta, and Entra domains federated to GoDaddy," Proofpoint [noted](https://x.com/threatinsight/status/2072338466076033073) in an X post last month.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"Unlike Sneaky2FA, NovaCookies uses a fully managed phishing-as-a-service (PhaaS) model where affiliates pay to use a PhaaS platform, and the infrastructure is hosted centrally by the PhaaS operator rather than by each affiliate."

Many NovaCookies lure domains have been found to be hosted on the ".vu" domain (e.g., "fordmotbvmorcompany[.]vu"), with the phishing URLs featuring alternating-case labels such as PwPt-sHaRe, Ms36-AcCeSs, and ClOd-ViEw in an attempt to masquerade as legitimate Microsoft services.

One of the attack chains employs Docusign notifications as decoys to lead victims to the phishing pages, while bypassing sender-authentication and reputation checks by taking advantage of the fact that the email is a genuine Docusign notification. What's malicious is the document shared via the service.

"Styled as a Docusign share notice, it claimed that an accounting department had shared a remittance-advice PDF and invited the recipient to open it," Island said. "The malicious destination sat inside the document, below the layer most mail security products inspect."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWNhR2jtw9Qhs7nLKrlhyphenhyphenHCI2nDNTo_HH7r9Omwu3majfyuvm-mhXtl0zsU9eCS5vb9beXKm0XsfanPpPHICqekd6NfCkXV_UNiD_blqiWPgzU2whzw-HEweok9x8JJwhzvyCozxPu3eZho8_q31rpNMq4d5jGwiqAKZouF6yTtNcwKMCPDm0M83TMA6k1/s1700-e365/island-flow.jpg)

The attack then employs an OAuth error-redirect technique [detailed](https://thehackernews.com/2026/03/microsoft-warns-oauth-redirect-abuse.html) by Microsoft earlier this March to lead victims to attacker-controlled infrastructure. The phishing infrastructure operated by NovaCookies is a live AitM relay designed to capture credentials and session information, and relay it to Microsoft in real time.

The commercial offering also boasts of various anti-analysis checks to evade security scanners before serving the bogus login form impersonating Microsoft 365. This includes a Cloudflare gate and a mechanism to detect execution passes associated with debugging tools.

"NovaCookies is built so each hop can look legitimate on its own: a trusted delivery service, an identity-provider redirect, then a familiar sign-in page," Island said. "Those pieces often land in different tools. The browser is where they become a single event."

The disclosure comes as [PhaaS toolkits](https://thehackernews.com/2026/04/weekly-recap-fast16-malware-xchat.html#:~:text=New%20Phishing%20Toolkits%20Discovered) continue to be a lucrative subscription service in the cybercrime underground, allowing cybercriminals with little to no technical expertise to mount phishing campaigns at scale. Some of the new services that have emerged in recent months include -

* **[AnonyMousKIT](https://socradar.io/blog/anonymouskit-ai-phaas-supply-chain/)**, which has been active since early 2024 and uses artificial intelligence (AI)-powered vishing tactics to target stolen device owners by posing as Apple Support and asking them to provide their device passcode, Apple ID, and 6-digit 2FA code on fake domains embedded in emails with the end goal of disabling Activation Lock on the device and reselling it. The service obtains the owner's ...