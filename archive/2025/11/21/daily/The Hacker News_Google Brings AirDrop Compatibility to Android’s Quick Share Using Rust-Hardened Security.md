---
title: Google Brings AirDrop Compatibility to Android’s Quick Share Using Rust-Hardened Security
url: https://thehackernews.com/2025/11/google-adds-airdrop-compatibility-to.html
source: The Hacker News
date: 2025-11-21
fetch_date: 2025-11-22T03:08:59.625198
---

# Google Brings AirDrop Compatibility to Android’s Quick Share Using Rust-Hardened Security

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Google Brings AirDrop Compatibility to Android's Quick Share Using Rust-Hardened Security](https://thehackernews.com/2025/11/google-adds-airdrop-compatibility-to.html)

**Nov 21, 2025**Ravie LakshmananData Protection / Technology

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiId5Cf7YMovzRkPOI6S1tm4fgDKNLcFvdg3ASml-f-mWCwj0rtSAZJ-P4jmORklaJoflcXdYLEVk_EjwXMqcoy7e0c_-fAPSpE_8R5Nvt5cc4VTxf-D1Nh-8qXuAeFjKR6-TcLvZxT1o2D46Iv9dGvkNNWv79ce2E-DzN4FC6XSsQM1QxgylI1fmDMhU4E/s790-rw-e365/android.jpg)

In a surprise move, Google on Thursday [announced](https://blog.google/products/android/quick-share-airdrop/) that it has updated Quick Share, its peer-to-peer file transfer service, to work with Apple's equipment AirDrop, allowing users to more easily share files and photos between Android and iPhone devices.

The cross-platform sharing feature is currently limited to the Pixel 10 lineup and works with iPhone, iPad, and macOS devices, with plans to expand to additional Android devices in the future.

In order to transfer a file from a Pixel 10 phone over AirDrop, the only caveat is that the owner of the Apple device is required to make sure their iPhone (or iPad or Mac) is discoverable to anyone – which can be enabled for 10 minutes.

Likewise, to receive content from an Apple device, Android device users will need to adjust their Quick Share visibility settings to Everyone for 10 minutes or be in Receive mode on the Quick Share page, according to a [support document](https://support.google.com/android/answer/9286773#zippy=%2Csend-content-to-an-iphone-ipad-or-macos-device%2Creceive-content-through-quick-share) published by Google.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"We built Quick Share's interoperability support for AirDrop with the same rigorous security standards that we apply to all Google products," Dave Kleidermacher, vice president of Platforms Security and Privacy at Google, [said](https://security.googleblog.com/2025/11/android-quick-share-support-for-airdrop-security.html).

At the heart of the future is a multi-layered security approach that's powered by the [memory-safe Rust](https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html) programming language to create a secure sharing channel that Google said eliminates entire classes of memory safety vulnerabilities, making its implementation resilient against attacks that attempt to exploit memory errors.

The tech giant also noted that the feature does not rely on any workaround and that the data is not routed through a server, adding it's open to working with Apple to enable "Contacts Only" mode in the future.

"Google's implementation of its version of Quick Share does not introduce vulnerabilities into the broader protocol's ecosystem," NetSPI, which carried out an independent assessment in August 2025, said.

"While it shares specific characteristics with implementations made by other manufacturers, this implementation is reasonably more secure. In fact, the process of file exchange is notably stronger, as it doesn't leak any information, which is a common weakness in other manufacturers' implementations."

That said, its analysis uncovered a low-severity information disclosure vulnerability (CVSS score: 2.1) that could permit an attacker with physical access to the device to access information, such as image thumbnails and SHA256 hashes of phone numbers and email addresses. It has since been addressed by Google.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

The development comes as Google said it blocked in India more than 115 million attempts to install sideloaded apps that request access to sensitive permissions for financial fraud. The company also said it's piloting a new feature in the country in collaboration with financial services like Google Pay, Navi, and Paytm to combat scams that trick users into opening the apps when sharing their screens.

"Devices running Android 11+ now show a prominent alert if a user opens one of these apps while screen sharing on a call with an unknown contact," Evan Kotsovinos, vice president of privacy, safety, and security at Google, [said](https://blog.google/intl/en-in/company-news/protecting-vulnerable-audiences-is-at-the-heart-of-ai-safety-efforts/). "This feature provides a one-tap option to end the call and stop screen sharing, protecting users from potential fraud.

Lastly, Google said it's also developing Enhanced Phone Number Verification (ePNV), which it described as a new Android-based security protocol that replaces SMS OTP flows with SIM-based verification to improve sign-in security.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Android](https://thehackernews.com/search/label/Android)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[Fraud Prevention](https://thehackernews.com/search/label/Fraud%20Prevention)[iOS](https://thehackernews.com/search/label/iOS)[mobile security](https://thehackernews.com/search/label/mobile%20security)[Vulnerability](https://thehackernews.com/sear...