---
title: Uncovering a Stalker with Breach Data
url: https://inteltechniques.com/blog/2022/12/12/uncovering-a-stalker-with-breach-data/
source: Instapaper: Unread
date: 2022-12-14
fetch_date: 2025-10-04T01:27:51.709787
---

# Uncovering a Stalker with Breach Data

[Skip to content](#main)

[# IntelTechniques](https://inteltechniques.com)

[IntelTechniques Blog](https://inteltechniques.com/blog/)

* [Training](https://inteltechniques.com/training.html)
* [Services](https://inteltechniques.com/services.html)
* [Resources](https://inteltechniques.com/links.html)
* [Tools](https://inteltechniques.com/tools/)
* [Blog](https://inteltechniques.com/blog/)
* [Podcast](https://inteltechniques.com/podcast.html)
* [Magazine](https://inteltechniques.com/magazine.html)
* [Books](https://inteltechniques.com/books.html)
* [Contact](https://inteltechniques.com/contact.html)

# Uncovering a Stalker with Breach Data

* [Posted on
  December 12, 2022](https://inteltechniques.com/blog/2022/12/12/uncovering-a-stalker-with-breach-data/)
* Posted in
  [OSINT](https://inteltechniques.com/blog/category/osint/), [Privacy](https://inteltechniques.com/blog/category/privacy/), [Security](https://inteltechniques.com/blog/category/security/)

In 2019, a client of mine suffered a terrifying case of harassment which lasted many months. It included numerous threatening text messages, countless emails, and two physical package deliveries. It caused her to embrace an anonymous life with a full privacy reboot. She now lives in an anonymous home, and sleeps well at night knowing that no one can find her. However, it understandably has bothered her to not know the identity of her adversary. Today, she knows, and has allowed me to share redacted details about the investigation.

A website called "Get Revenge On Your Ex" (https://www.getrevengeonyourex.com) has been around for over a decade. It is one of many services which will blast text messages and emails to any victim for a small fee. With so many ways to harass people anonymously today, I don't think it is used as much as previous years. However, it has been on my radar for some time. I previously had no evidence this service was used as part of the harassment campaign targeting my client, but I do now. In September 2022, the site was breached and all user data was stolen. The post is below.

![](https://inteltechniques.com/blog/wp-content/uploads/Capture-2-620x321.png)

Below is the current view of the breached website.

![](https://inteltechniques.com/blog/wp-content/uploads/Capture-620x225.png)

![](https://inteltechniques.com/blog/wp-content/uploads/Capture-1-620x154.png)

When we digest data breaches, leaks, logs, and ransomware, our offline system immediately queries various client data to identify any new exposure. This new data set hit on my client's cellular telephone number. This breach included a file titled "v2ordersms.txt", which appears to contain every outgoing message sent by this service since 2009. This file includes entries for "phone", "message", and "timestamp". A fictitious entry would appears as follows.

"2025551212,I'm going to kill you,2021-01-01 00:11:49"

I will only display fictitious details throughout this post, but I will include the proper format of data in order to follow along with the investigation. I reviewed our internal reports and verified that the text message from this file matched the threat received by my client, as well as the cellular number associated with the message. This breach included numerous files extracted from the service, but it was difficult to associate a specific message with the suspect who purchased the harassment. While there were files which included the email addresses and plain-text passwords of all customers of this service, I could not immediately tie one account to the threatening texts, emails, or packages received by my client. Therefore, I began analyzing the timestamps.

In the previous example, the message was sent on 2021-01-01 at 00:11:49. I do not know which time zone this was, but I do know the date(s). I also acquired the dates of other messages sent to my client by the unknown suspect. I then opened a file called "v2rawpaypal.txt" from this breach. It contained all PayPal transactions in chronological order. I immediately noticed the following record (modified for privacy).

"2xxxx, "Thu, 01 Jan 2021 13:", Sale value: USD 2.96, Jon Doe, 111 south main, Apt 200, Los Angeles, California, 90000, 717.115.134.94, [[email protected]](/cdn-cgi/l/email-protection), The above payment has been processed. security code comparison - matched postcode comparison"

I immediately accessed the file titled "v2paypal.txt" to compare the purchase with PayPal details from another view, and they matched:

"717.115.134.94, Anonymous SMS, [[email protected]](/cdn-cgi/l/email-protection), 2021-01-01 at 00:17:42"

NOTE: These modified examples simply show the structure. The data I discovered included what appeared to be a real name, email address, and IP address. These entries identified that "[[email protected]](/cdn-cgi/l/email-protection)" from IP Address "717.115.134.94" ordered a fake SMS from this service and paid via PayPal the amount of $2.96. I then compared the orders from additional dates to my report and saw the same person's details each time.  This was much more than a coincidence.

Surely they used a VPN, right? Nope:

"OrgName: Charter Communications Inc Comment: Legacy Time Warner Cable IP Assets"

This doesn't tell me anything about the suspect, but a subpoena would. Unfortunately, I no longer have that power. However, I now have a suspect. I contacted my client and offered the details. She did not recognize the name and email at first, but called me later after she realized it was a man she worked with for a short period of time in 2020. I now feel confident that we know the identity of the suspect. I now let her decide how we proceed.

**I post this to highlight the benefits of breach data. While most breaches include damaging details which could harm innocent victims, we occasionally encounter a breach which shares the exposure with criminals who think they are anonymous. I believe these are the successes which should be discussed when the ethics of data access are debated.**

Oh, and if you are one of the 71,000 customers of "Get Revenge On Your Ex" who used PayPal to pay for the service, you are extremely exposed. Once online investigators start digging into this data, you may be the one who feels harassed.

* [« Previous Post](https://inteltechniques.com/blog/2022/12/02/the-privacy-security-osint-show-episode-285/)
* [Next Post »](https://inteltechniques.com/blog/2022/12/16/the-privacy-security-osint-show-episode-286/)

The RSS feed for this blog is at
<https://inteltechniques.com/blog/feed/>.

#### Recent Posts

* [UNREDACTED Magazine Issue 008](https://inteltechniques.com/blog/2025/09/05/unredacted-magazine-issue-008/)
* [Extreme Privacy Update: E2EE Email Guide](https://inteltechniques.com/blog/2025/07/12/extreme-privacy-update-e2ee-email-guide/)
* [Virtual Currency Payments Return](https://inteltechniques.com/blog/2025/07/11/virtual-currency-payments-return/)
* [Extreme Privacy Update: Self-Hosted SearXNG Guide](https://inteltechniques.com/blog/2025/07/11/extreme-privacy-update-self-hosted-searxng-guide/)
* [Extreme Privacy Update: Windows 10 EOL](https://inteltechniques.com/blog/2025/07/08/extreme-privacy-update-windows-10-eol/)
* [Extreme Privacy Update: KnockKnock Script](https://inteltechniques.com/blog/2025/07/05/extreme-privacy-update-knockknock-script/)
* [OSINT Techniques Updates: inurl & Amass path](https://inteltechniques.com/blog/2025/07/05/osint-techniques-updates-inurl-amass-path/)
* [New Digital Book Provider](https://inteltechniques.com/blog/2025/04/02/new-digital-book-provider/)
* [New Ebook Updates](https://inteltechniques.com/blog/2025/04/02/new-ebook-updates/)
* [Executive EDC Bags](https://inteltechniques.com/blog/2025/01/05/executive-edc-bags/)
* [Books Updated](https://inteltechniques.com/blog/2024/11/29/books-updated/)
* [OSINT Techniques 11th Edition Now Available](https://inteltechniques.com/blog/2024/11/10/osint-techniques-11th-edition-now-available/)
* [Digital Guide Updates 2024.11.01]...