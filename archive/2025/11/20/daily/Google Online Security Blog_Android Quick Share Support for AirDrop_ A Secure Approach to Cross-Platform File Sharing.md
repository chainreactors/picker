---
title: Android Quick Share Support for AirDrop: A Secure Approach to Cross-Platform File Sharing
url: http://security.googleblog.com/2025/11/android-quick-share-support-for-airdrop-security.html
source: Google Online Security Blog
date: 2025-11-20
fetch_date: 2025-11-21T03:12:15.372609
---

# Android Quick Share Support for AirDrop: A Secure Approach to Cross-Platform File Sharing

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Android Quick Share Support for AirDrop: A Secure Approach to Cross-Platform File Sharing](https://security.googleblog.com/2025/11/android-quick-share-support-for-airdrop-security.html "Android Quick Share Support for AirDrop: A Secure Approach to Cross-Platform File Sharing")

November 20, 2025

Posted by Dave Kleidermacher, VP, Platforms Security & Privacy, Google

Technology should bring people closer together, not create walls. Being able to communicate and connect with friends and family should be easy regardless of the phone they use. That’s why Android has been building experiences that help you stay connected across platforms.

As part of our efforts to continue to make cross-platform communication more seamless for users, we've made Quick Share interoperable with AirDrop, allowing for two-way file sharing between Android and iOS devices, starting with the Pixel 10 Family. This new feature makes it possible to quickly share your photos, videos, and files with people you choose to communicate with, without worrying about the kind of phone they use.

Most importantly, when you share personal files and content, you need to trust that it stays secure. You can share across devices with confidence knowing we built this feature with security at its core, protecting your data with strong safeguards that have been tested by independent security experts.

### Secure by Design

We built Quick Share’s interoperability support for AirDrop with the same rigorous security standards that we apply to all Google products. Our approach to security is proactive and deeply integrated into every stage of the development process. This includes:

* **Threat Modeling:** We identify and address potential security risks before they can become a problem.
* **Internal Security Design and Privacy Reviews:** Our dedicated security and privacy teams thoroughly review the design to ensure it meets our high standards.
* **Internal Penetration Testing:** We conduct extensive in-house testing to identify and fix vulnerabilities.

This [Secure by Design](https://blog.google/technology/safety-security/tackling-cybersecurity-vulnerabilities-through-secure-by-design/) philosophy ensures that all of our products are not just functional but also fundamentally secure.

This feature is also protected by a multi-layered security approach to ensure a safe sharing experience from end-to-end, regardless of what platform you’re on.

* **Secure Sharing Channel:** The communication channel itself is hardened by our use of Rust to develop this feature. This memory-safe language is the industry benchmark for building secure systems and provides confidence that the connection is protected against buffer overflow attacks and other common vulnerabilities.
* **Built-in Platform Protections:** This feature is strengthened by the robust built-in security of both Android and iOS. On Android, security is built in at every layer. Our deep investment in Rust at the OS level hardens the foundation, while proactive defenses like [Google Play Protect](https://support.google.com/googleplay/answer/2812853?hl=en) work to keep your device safe. This is complemented by the security architecture of iOS that provides its own strong safeguards that mitigate malicious files and exploitation. These overlapping protections on both platforms work in concert with the secure connection to provide comprehensive safety for your data when you share or receive.
* **You’re in Control:** Sharing across platforms works just like you're used to: a file requires your approval before being received, so you're in control of what you accept.

### The Power of Rust: A Foundation of Secure Communication

A key element of our security strategy for the interoperability layer between Quick Share and AirDrop is the use of the memory-safe Rust programming language. Recognized by security agencies around the world, including the [NSA](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/article/3608324/us-and-international-partners-issue-recommendations-to-secure-software-products/) and [CISA](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF), Rust is widely considered the industry benchmark for building secure systems because it eliminates entire classes of memory-safety vulnerabilities by design.

[Rust is already a cornerstone](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html) of our broader initiative to eliminate memory safety bugs across Android. Its selection for this feature was deliberate, driven by the unique security challenges of cross-platform communication that demanded the most robust protections for memory safety.

The core of this feature involves receiving and parsing data sent over a wireless protocol from another device. Historically, when using a memory-unsafe language, bugs in data parsing logic are one of the most common sources of high-severity security vulnerabilities. A malformed data packet sent to a parser written in a memory-unsafe language can lead to buffer overflows and other memory corruption bugs, creating an opportunity for code execution.

This is precisely where Rust provides a robust defense. Its compiler enforces strict ownership and borrowing rules at compile time, which guarantees memory safety. Rust removes entire classes of memory-related bugs. This means our implementation is inherently resilient against attackers attempting to use maliciously crafted data packets to exploit memory errors.

### Secure Sharing Using AirDrop's "Everyone" Mode

To ensure a seamless experience for both Android and iOS users, Quick Share currently works with AirDrop's "Everyone for 10 minutes" mode. This feature does not use a workaround; the connection is direct and peer-to-peer, meaning your data is never routed through a server, shared content is never logged, and no extra data is shared. As with "Everyone for 10 minutes" mode on any device when you’re sharing between non-contacts, you can ensure you're sharing with the right person by confirming their device name on your screen with them in person.

This implementation using "Everyone for 10 minutes” mode is just the first step in seamless cross-platform sharing, and we welcome the opportunity to work with Apple to enable “Contacts Only” mode in the future.

### Tested by Independent Security Experts

After conducting our own secure product development, internal threat modeling, privacy reviews, and red team penetration tests, we engaged with **[NetSPI](https://www.netspi.com/)**, a leading third-party penetration testing firm, to further validate the security of this feature and conduct an [independent security assessment](https://www.netspi.com/wp-content/uploads/2025/11/google-feature-review-report.pdf). The assessment found the interoperability between Quick Share and AirDrop is secure, is “notably stronger” than other industry implementations and does not leak any information.

Based on these internal and external assessments, we believe our implementation provides a strong security foundation for cross-platform file sharing for both Android and iOS users. We will continue to evaluate and enhance the implementation’s security in collaboration with additional third-party partners.

To complement this deep technical audit, we also sought expert third-party perspective on our approach from [Dan Boneh](https://crypto.stanford.edu/~dabo/), a renowned security expert and professor at Stanford University:

“Google’s work on this feature, including the use of memory safe Rust for the core co...