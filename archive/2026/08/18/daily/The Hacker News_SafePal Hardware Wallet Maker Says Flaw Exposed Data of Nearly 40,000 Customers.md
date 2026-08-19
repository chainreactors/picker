---
title: SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers
url: https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html
source: The Hacker News
date: 2026-08-18
fetch_date: 2026-08-19T03:00:29.539397
---

# SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers

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

# [SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers](https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html)

**Swati Khandelwal**Aug 18, 2026Vulnerability / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFTKWlpW6A2F_jXpwDsCbJmaJ7-TnZPoCNsW0BG5pa4F8X8I1zzCRAMefU00NEQHKlqdqGchFbSTQ_aADgjlJeIHpUKswwnwNiP7WnbAftpciT_4FAFzPKi5NYnBtI0R0VEhP4JIHXFpm6hhyQFASu7IP1kFP2FmlLVejJDiG3Tgxf2ofz-J0Aq02AoF8/s1700-e365/safe.jpg)

SafePal has disclosed that an authorization flaw in an order-tracking plug-in exposed the names, email addresses, shipping addresses, phone numbers, and purchase details of approximately 39,798 customers.

The hardware wallet maker said all affected customers were notified individually by email on August 16 from security@safepal.com, with the subject line "[Important] Your SafePal Order Information Has Been Affected."

The exposed records did not include wallet credentials or financial information, according to SafePal, which said it has found no evidence that the incident itself compromised access to SafePal wallets or funds.

"This incident did not involve your seed phrase, private keys, wallet password, or other wallet credentials, bank account information, payment card numbers, or government-issued identification numbers," SafePal [said](https://www.safepal.com/en/blog/security-update).

Under certain conditions, the flaw allowed unauthorized access to another customer's order information, the company said, without naming the plug-in, its vendor, or the version affected. No CVE identifier has been assigned to the issue.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The affected orders were placed between March 2, 2025, and April 11, 2026. Those dates describe when the orders were placed rather than the period over which the flaw was exploitable, and SafePal has not said when the unauthorized access began or ended, how many parties reached the records, or how the flaw was originally found.

Because the records tie a named individual to a home address and a purchase, SafePal warned that affected customers may face "fraudulent phone calls, emails, text messages, letters, refund offers, firmware-update requests, fake customer-support communications." The data does not include wallet addresses, balances, or any indication of what a customer holds.

"Treat any unexpected contact or hardware delivery referencing your SafePal purchase as suspect, whether it arrives by phone, in the post, or in person," SafePal said.

Blockchain analytics firm Chainalysis counted [46 violent incidents documented globally through late June](https://www.chainalysis.com/blog/violent-crypto-wrench-attacks-2026/) and over $30 million stolen, tying a jump in French cases from a handful before 2025 to 30 by mid-2026 to stolen tax records on crypto holders. Only 12 of the 46 attempts produced a payment, a rate of 26%, down from 49% in 2025.

"Criminals have recognized that crypto holders are high-value targets because they possess wealth in an instantly and irreversibly transferrable form," Chainalysis said.

Separately, SafePal said it found that a [scheduled data-cleanup process](https://www.safepal.com/scam-protection) had stopped working correctly between September 2025 and April 2026 because of a configuration error, leaving older order records in the system longer than intended.

"That issue did not cause the unauthorized access itself, but it is why the affected range extends back to March 2025," SafePal said.

Trezor, which [disclosed a breach at shipping provider ShipMonk](https://thehackernews.com/2026/08/threatsday-ghostjacking-ai-attacks.html) three days earlier, credited a 90-day data storage policy already in force with limiting its own exposure.

SafePal said the first report consistent with the issue reached it in early May 2026. "We first received a report consistent with this issue in early May, and treated it as an isolated case at the time, but escalated it into a formal security investigation and introduced additional protections," SafePal said.

The incident FAQ puts the delay in a question of its own, asking why phishing emails received in May took until August to confirm the cause. One customer wrote on X about receiving a suspicious email, a letter, and a phone call that month from someone claiming to represent SafePal, Help Net Security reported, although there is no confirmed connection between the exposure and the phishing attempt.

The company said it began a full review and rebuild of its order-processing pipeline in July and confirmed the root cause during that work.

A threat actor has since advertised a dataset on a cybercrime forum that cites the same order window and the same customer count. The listing was [surfaced](https://x.com/DarkWebInformer/status/2089052501492236328) by DarkWebInformer on August 16, and the seller offered to share order IDs and shipping countries so prospective buyers could check them against SafePal's own verification tool.

SafePal has published no statement on the listing on its blog, its incident page, or its X account as of writing. The company did not immediately respond to a request for comment.

SafePal listed the following measures -

* The flaw has been fixed and additional security measures introduced.
* Retention of personal information in the relevant order-processing environment has been cut to 90 days, subject to applicable legal requirements.
* Affected records have been purged from active servers, with a secured offline backup kept solely to support potential investigations.
* An independent third-party security firm is being engaged to validate the fix and review order-processing systems more broadly.
* Third-party logistics and fulfillment partners have been contacted to confirm the issue had not spread within their systems.
* Over 30 fraudulent websites and phishing links "tied to the sc...