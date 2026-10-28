---
title: Keystone to Destroy 18,835 Hardware Wallets After Hackers Steal Device Verification Key
url: https://thehackernews.com/2026/10/keystone-to-destroy-18835-hardware.html
source: The Hacker News
date: 2026-10-27
fetch_date: 2026-10-28T07:49:45.879027
---

# Keystone to Destroy 18,835 Hardware Wallets After Hackers Steal Device Verification Key

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Keystone to Destroy 18,835 Hardware Wallets After Hackers Steal Device Verification Key](https://thehackernews.com/2026/10/keystone-to-destroy-18835-hardware.html)

**Swati Khandelwal**Oct 27, 2026Cryptocurrency / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkvGXPUhZZjWBsYYBAx8KeJ8WilsBMLE-JhqfNAEyCOPuxs6-4VIF1e77IHR5zVdGfRsjJkSOfUVE1JaEmKe0mSAVM-ha4SeROxEGAdkLY5n5rBqx1LBSm6UVxA167sJYZEJTRra7BSipFtdlw2S-kFCUOSa9n70NbfSka3zRNVHd0D69qbVpSGIOnuAU/s1700-nu-rw-lo-l85-e365/keystone.jpg)

An attacker who gained access to Keystone's website obtained the key that its hardware wallets use to prove they are genuine, the company said in a [statement](https://x.com/KeystoneWallet/article/2114719318722404578) on October 26.

Someone with that key could build counterfeit devices that pass the online check owners use to verify a Keystone. A buyer who trusted a counterfeit could have their crypto stolen, but the incident did not involve owners' recovery phrases or wallet private keys.

Keystone will destroy 18,835 unsold devices that carry the key, and all new devices will get a new one.

Keystone found the unauthorized access on October 20, and its advice to owners depends on when a device arrived. For a device received after that date with the old key, the company said: "Even if such a device passes authentication, we cannot completely rule out the possibility that it is counterfeit."

Owners of such a device should contact Keystone support and use it only after the company confirms it is genuine.

A device delivered before October 20 that passes the check can be considered genuine and used normally, according to Keystone. The company has not said when the attacker first got in.

The attacker exploited a vulnerability in a third-party data monitoring tool used by Keystone's website to escalate privileges, according to the company. That let the attacker obtain customer data and the key.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Keystone blocked the attacker's access on October 20 and has since fixed the vulnerability. It has not said where the key was stored.

### How the Device Check Works

The owner scans a QR code on Keystone's verification page with the device, then enters the code the device displays on the page.

In [Keystone's open-source firmware](https://github.com/KeystoneHQ/keystone3-firmware/blob/3690bf1f36cb9e817f9a2412a9fc7560c08953f0/rust/rust_c/src/common/web_auth.rs), the QR code carries that code in encrypted form, and the device decrypts it with its stored key. So a correct code shows that the device holds the key.

The key is used only for this check. It plays no part in creating recovery phrases, deriving private keys, or signing transactions.

Anyone with a copy of the key could produce the right codes, so a counterfeit device carrying it could pass the check. Such devices could be sold or shipped to customers, leading to the theft of their crypto, Keystone said. The company has not reported any counterfeit devices or thefts.

The key is written into each device during manufacturing and cannot be erased or rewritten. The firmware keeps it in memory, which can be written only once, and [refuses to accept a second key](https://github.com/KeystoneHQ/keystone3-firmware/blob/3690bf1f36cb9e817f9a2412a9fc7560c08953f0/src/presetting.c). So devices already made cannot be switched to the new key.

### Customer Records

Keystone first [disclosed the breach](https://x.com/KeystoneWallet/status/2114054080754770137) on October 24, saying a third party had obtained customers' shipping information.

The incident affected 25,964 buyer records from purchases on Keystone's website between 2024 and 2026, the company said on October 26. The records hold names, contact details, shipping addresses, and order details. Keystone's online store runs on Shopify, which stored and managed the records.

Payment card and bank details and government ID numbers were not involved, Keystone said. Purchase records from Amazon and Keystone's other sales channels were not affected.

Keystone has also included 12,873 unpaid checkout records in its response as a precaution. These hold names, contact details, and shipping information from purchases that were never completed.

Some of the affected data should already have been deleted. Keystone had [promised to delete shipping information](https://keyst.one/privacy-promises) 180 days after each order.

An automated tool Keystone built to erase records in bulk did not work reliably. Some deletions failed, and Keystone did not catch the failures in time.

Keystone is shortening the period it retains customers' personal data from 180 days to 90 days, effective immediately. It has asked Shopify to delete buyers' personal data older than 90 days and expects that to be done on November 3. As of October 27, its [privacy policy](https://keyst.one/privacy-policy) still listed 180 days.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Keystone is emailing affected customers and plans a page where people can check whether their information was affected.

### What Keystone Owners Should Do

Keystone's guidance covers these situations:

* **Delivered before October 20:** A device that passes the check can be used normally.
* **Received after October 20 with the old key:** Do not use the device until Keystone support, at support@keyst.one, confirms it is genuine. Keystone told these owners to follow instructions on its [device verification page](https://keyst.one/authentication), but the page showed no such instructions as of October 27. Keystone has not said how to tell which key a device carries, or what owners who have already sent crypto to such a device should do.
* **Waiting on an order from Keystone's website:** Shipping is paused until devices with the new key are ready. As of October 27, the store listed the Keystone 3 Pro as a pr...