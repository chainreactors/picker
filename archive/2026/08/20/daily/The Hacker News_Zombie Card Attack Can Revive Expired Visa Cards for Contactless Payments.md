---
title: Zombie Card Attack Can Revive Expired Visa Cards for Contactless Payments
url: https://thehackernews.com/2026/08/zombie-card-attack-can-revive-expired.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:09.359878
---

# Zombie Card Attack Can Revive Expired Visa Cards for Contactless Payments

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

# [Zombie Card Attack Can Revive Expired Visa Cards for Contactless Payments](https://thehackernews.com/2026/08/zombie-card-attack-can-revive-expired.html)

**Swati Khandelwal**Aug 20, 2026Vulnerability / Financial Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsJMUJluWegBU4C6RiZ4QHg6rTqhFHMt5JJt3RR2K7l06c3FOFlnq8gIVuBqVUX8qsJFiAh6KKAlDXpVAydAoC2rM0dUKUayta50sqRXoW36_V2OgSXJBKaaAFY4boBYhtHkqeyBaBZavbo7bz3S8otNwyb3NUmW9j88edph6zAfnyJikYhLBrAHuCdBA/s1700-e365/visa.jpg)

Researchers at the University of Massachusetts Amherst have demonstrated an attack that revives expired Visa contactless credit cards for real in-store purchases by rewriting the expiration date a point-of-sale (POS) terminal reads over near-field communication (NFC), without breaking any of the card's cryptography.

The attack, which the researchers named "**Zombie Card**," requires physical possession of the expired card or sustained NFC proximity to it, plus a man-in-the-middle (MitM) relay positioned between the card and the terminal.

It also requires that the account remain open under the same primary account number (PAN), which is standard practice when an issuer sends a replacement card, and that the issuing bank not independently re-check the expiry during authorization.

The paper's preliminary study spans five major US banks and tests general tampering with Europay, Mastercard, and Visa (EMV) transactions. Raja Hasnain Anwar, the lead author, told The Hacker News that transactions succeeded at most of those banks when the team modified the Consumer Device Cardholder Verification Method (CDCVM) flag, a result he called alarming because it rests on the same weakness the expiry attack relies on, that transaction modifications go undetected.

Three of the five banks were then tested with expired and replaced physical cards, and Anwar said they showed three distinct policies rather than a straightforward pass or fail. Bank A allowed the expiration date to be modified and accepted transactions from more than one card at a time. Bank B detected the modification and accepted transactions from only one active card. Bank D, whose cards ran Discover's kernel, detected the modification but still accepted transactions from more than one card.

The [work was presented](https://www.usenix.org/system/files/usenixsecurity26-anwar.pdf) at the 35th USENIX Security Symposium in Baltimore from August 12 to 14, 2026. Anwar, Gerard DeCunha, and Muhammad Taqi Raza disclosed the findings to Visa and the affected banks in May 2025 and made contact again in December 2025. No CVE has been assigned and no exploitation of the technique has been reported.

The Hacker News found no advisory, specification bulletin, or mitigation guidance published by Visa, EMVCo, Mastercard, Discover, American Express, or terminal vendor SumUp as of August 20, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Card expiry appears twice in a [Visa contactless transaction](https://thehackernews.com/2020/09/emv-payment-card-pin-hacking.html), and the two representations are consumed by different parties. The terminal evaluates its processing restrictions against the Application Expiration Date, carried in Tag-Length-Value (TLV) tag 5F24. The issuer derives the expiry from Track 2 Equivalent Data, tag 57, which travels in the online authorization request.

According to the paper, Visa's Kernel 3 does not require the two to be consistently bound, and the fast Dynamic Data Authentication (fDDA) signature the terminal verifies excludes 5F24 entirely. The relay rewrites the terminal-facing date to any future value and leaves Track 2 untouched, so the card's signature and its issuer-verified cryptogram both still validate.

"Yet it is not cryptographically protected. So we can easily modify it to fool the POS," Anwar, a doctoral candidate with the Khwarizmi Lab at UMass Amherst, [said of the expiration date](https://www.umass.edu/news/article/when-zombie-credit-cards-attack-umass-researchers-discover-loophole-can-reanimate) in a university release.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyUBvIm3NVkSczYEtHNP8P6xUXieDDAeTEo5AzoVo-fVMtvEGIhx9u_Bx8cgM6LTOMdnQ0jmZOl_ADDNLXxe6-cab82EBaiJe_cp09cOT0r3fGCwpgErZ8L_440tsgSfHm9RK7LRyM8LWAzvtXQ9CwLTCJsiRsa2TQWSRjodLNZkF2RDoKAzp6DRghREI/s1700-e365/cards.jpg)

An expired card still passes offline data authentication because issuer and integrated circuit card certificate lifetimes are set independently of application expiry and routinely outlast the printed date.

The card's private key encodes no notion of expiry at all. Kernel 3 also specifies that the Terminal Verification Results forwarded to the issuer are set to all zeros, so a bank cannot see whether the terminal ran or failed its local expiry check.

The attacker does not need to know the replacement card's real expiration date. Any date later than the transaction date is sufficient.

The team ran the same modification against four [EMV contactless kernels](https://thehackernews.com/2021/02/new-hack-lets-attackers-bypass.html), the per-network implementations of the protocol, with the following outcomes -

* **Visa (Kernel 3).** The edit passed the terminal's processing restrictions and did not invalidate the signature, because 5F24 is not among the signed data.
* **Mastercard (Kernel 2).** The terminal performs a consistency check between the two expiry representations during READ RECORD parsing and treats a mismatch as a card data error, declining rather than falling back online.
* **American Express (Kernel 4).** The expiration date is a mandatory record element bound into the static data covered by offline data authentication, producing a hash mismatch during signature validation.
* **Discover (Kernel 6).** Combined Dynamic Data Authentication binds the card-returned TLV objects into the verified transaction hash, and modified transa...