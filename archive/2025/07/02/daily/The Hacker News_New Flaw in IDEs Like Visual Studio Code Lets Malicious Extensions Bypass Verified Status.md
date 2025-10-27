---
title: New Flaw in IDEs Like Visual Studio Code Lets Malicious Extensions Bypass Verified Status
url: https://thehackernews.com/2025/07/new-flaw-in-ides-like-visual-studio.html
source: The Hacker News
date: 2025-07-02
fetch_date: 2025-10-07T00:02:02.793730
---

# New Flaw in IDEs Like Visual Studio Code Lets Malicious Extensions Bypass Verified Status

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New Flaw in IDEs Like Visual Studio Code Lets Malicious Extensions Bypass Verified Status](https://thehackernews.com/2025/07/new-flaw-in-ides-like-visual-studio.html)

**Jul 01, 2025**Ravie LakshmananDeveloper Security / Software Development

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimmTyPLNXT22n5xKTUHUryWdPGKcHESq4LSakTAj8hJDBb6I4Ct9IMqpiclJ8xxQf8Fo_OJgYct487b7rPGT0GtxGLX3_8jkdWUwEU8R3AK1Oz94s3OobhwKWz6fYjXBd3I8hbn3Ah0tMZ-OUaNo6oESMqKnflTJ07z_thTjekqJKxj97g-VmFAm9e8h5V/s790-rw-e365/IDE-code.jpg)

A new study of integrated development environments (IDEs) like Microsoft Visual Studio Code, Visual Studio, IntelliJ IDEA, and Cursor has revealed weaknesses in how they handle the extension verification process, ultimately enabling attackers to execute malicious code on developer machines.

"We discovered that flawed verification checks in Visual Studio Code allow publishers to add functionality to extensions while maintaining the verified icon," OX Security researchers Nir Zadok and Moshe Siman Tov Bustan [said](https://www.ox.security/can-you-trust-that-verified-symbol-exploiting-ide-extensions-is-easier-than-it-should-be/) in a report shared with The Hacker News. "This results in the potential for malicious extensions to appear verified and approved, creating a false sense of trust."

Specifically, the analysis found that Visual Studio Code sends an HTTP POST request to the domain "marketplace.visualstudio[.]com" to determine if an extension is verified or otherwise.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The exploitation method essentially involves creating a malicious extension with the same verifiable values as an already verified extension, such as that of Microsoft, and bypassing trust checks.

As a result, it allows rogue extensions to appear verified to unsuspecting developers, while also containing code capable of executing operating system commands.

From a security standpoint, this is a classic case of extension sideloading abuse, where bad actors distribute plugins outside the official marketplace. Without proper code signing enforcement or trusted publisher verification, even legitimate-looking extensions can hide dangerous scripts.

For attackers, this opens up a low-barrier entry point to achieve remote code execution—a risk that's especially serious in development environments where sensitive credentials and source code are often accessible.

In a proof-of-concept (PoC) demonstrated by the cybersecurity company, the extension was configured to open the Calculator app on a Windows machine, thereby highlighting its ability to execute commands on the underlying host.

By identifying the values used in verification requests and modifying them, it was found that it's possible to create a VSIX package file such that it causes the malicious extension to appear legitimate.

OX Security said it was able to reproduce the flaw across other IDEs like IntelliJ IDEA and Cursor by modifying the values used for verification without making them lose their verified status.

In response to responsible disclosures, Microsoft said the behavior is by design and that the changes will prevent the VSIX extension from being published to the Marketplace owing to extension signature verification that's enabled by default across all platforms.

However, the cybersecurity company found the flaw to be exploitable as recently as June 29, 2025. The Hacker News has reached out to Microsoft for comment, and we will update the story if we hear back.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings once again show that relying solely on the verified symbol of extensions can be risky, as attackers can trick developers into running malicious code without their knowledge. To mitigate such risks, it's advised to install extensions directly from official marketplaces as opposed to using VSIX extension files shared online.

"The ability to inject malicious code into extensions, package them as VSIX/ZIP files, and install them while maintaining the verified symbols across multiple major development platforms poses a serious risk," the researchers said. "This vulnerability particularly impacts developers who install extensions from online resources such as GitHub."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Developer Security](https://thehackernews.com/search/label/Developer%20Security)[Microsoft](https://thehackernews.com/search/label/Microsoft)[software development](https://thehackernews.com/search/label/software%20development)[Software Integrity](https://thehackernews.com/search/label/Software%20Integrity)[Visual Studio Code](https://thehackernews.com/search/label/Visual%20Studio%20Code)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](htt...