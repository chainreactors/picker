---
title: Chrome is Silently Installing 4GB AI Model on Your Device without Consent. Here’s how to find it and remove it.
url: https://securityuncorked.com/2026/05/how-to-stop-chrome-from-silently-installing-ai-model-on-your-device/
source: Security Uncorked
date: 2026-05-14
fetch_date: 2026-05-15T05:52:00.096988
---

# Chrome is Silently Installing 4GB AI Model on Your Device without Consent. Here’s how to find it and remove it.

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)* ···

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)* ···

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)

![](https://securityuncorked.com/wordpress/wp-content/uploads/2026/05/image-987x350.png)

[Next
The First Wi-Fi Training and Certification Mini-Event](https://securityuncorked.com/2024/10/the-first-wi-fi-training-and-certification-mini-event/)

[Random-izations](https://securityuncorked.com/category/random-izations/)

# Chrome is Silently Installing 4GB AI Model on Your Device without Consent. Here’s how to find it and remove it.

9 hours ago

2 min read

[Add comment](https://securityuncorked.com/2026/05/how-to-stop-chrome-from-silently-installing-ai-model-on-your-device/#respond)

Sometime we cover things on the [Packet Protector Podcast](https://www.youtube.com/playlist?list=PLtO_OYBiEo6lNaXQrwEqt4pwP7OX0GmLY) News Roundup episodes that need immediate attention. This is one.

**Chrome has been sneaking a local AI model on systems, possibly since 2024.**

* Across multiple platforms (MacOS, Windows, Linux, etc.) if the device is capable.
* No notice.
* No opt-in.
* No consent.
* Uses purposefully obscure and misleading naming conventions.
* Delete it… Chrome re-installs it.
* CONCERNS: Myriad – Privacy, resource impact, environmental, data exfil (there’s a Prompt API accessible).

## **How to Disable and Remove It**

Quick option..

1. **Browse** to **`chrome://flags`**
2. **Search** for `optimization-guide-on-device-model`
3. **Set** to `Disable` (to remove and restart Chrome)

## **See If It’s Installed Now**

**On Mac**

* **Run this in Terminal:** find ~/Library/Application\ Support/Google/Chrome -size +1G -ls 2>/dev/null

**On Windows**

* **Search your C: drive** for **`weights.bin`**  and/or
* **Look for a folder** named `OptGuideOnDeviceModel` under your Chrome user profile. Look in %LOCALAPPDATA%\Google\Chrome\User Data

## **Enterprise Centralized Removal Options**

* On Windows Registry key: navigate to **`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome`**, create a DWORD called **`GenAILocalFoundationalModelSettings`** and set it to 1
* Enterprise environments can also push policy via `GenAILocalFoundationalModelSettings` in Chrome’s enterprise policy framework

## More info and articles

* **Fantastic research and write-up on the issue by [Alexander Hanff (LLM, CIPPE, CIPT)](https://www.linkedin.com/in/alexanderhanff/)**
  Google Chrome silently installs a 4 GB AI model on your device without consent. At a billion-device scale the climate costs are insane <https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/>
* **Overview at the Register.**
  Chrome silently installs a 4 GB local LLM on your computer <https://www.theregister.com/ai-and-ml/2026/05/07/chrome-silently-installs-a-4-gb-local-llm-on-your-computer/5230893>

[![Looking for the Chrome://flags to find the sneaky AI model](https://securityuncorked.com/wordpress/wp-content/uploads/2026/05/image.png "Demonstrates steps of finding the software in question")](https://securityuncorked.com/wordpress/wp-content/uploads/2026/05/image.png)

[AI](https://securityuncorked.com/tag/ai/) [Endpoint Security](https://securityuncorked.com/tag/endpoint-security/)

FacebookXEmailLinkedIn

[![](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/ad-book-01.jpg)](https://www.amazon.com/Wireless-Security-Architecture-Maintaining-Enterprise/dp/1119883059)

[Next
The First Wi-Fi Training and Certification Mini-Event](https://securityuncorked.com/2024/10/the-first-wi-fi-training-and-certification-mini-event/)

![](https://secure.gravatar.com/avatar/fa111d40af5e09b5eb81e1cf04e7da362300537a4671e26ba28e97457a0b5a21?s=140&d=mm&r=g)

#### jj

Author, speaker, and recognized authority on network and wireless security architectures, Jennifer (JJ) Minella helps organizations solve technical problems and align teams.

[View all posts](https://securityuncorked.com/author/su-jj/)

#### You may also like

[![](https://securityuncorked.com/wordpress/wp-content/uploads/2023/03/blog-202302-askjjx-keepass-featured-232x130.png)

Video](https://securityuncorked.com/2023/03/ask-jjx-what-about-the-keepass-vulnerability/ "Ask JJX: What About the KeePass Vulnerability?")

[Random-izations](https://securityuncorked.com/category/random-izations/), [Zero Trust and NAC](https://securityuncorked.com/category/zero-trust-nac/)

## [Ask JJX: What About the KeePass Vulnerability?](https://securityuncorked.com/2023/03/ask-jjx-what-about-the-keepass-vulnerability/)

519 views

9 min read

[![](https://securityuncorked.com/wordpress/wp-content/uploads/2022/04/2202-Monthly-Book-Giveaway-feature-232x130.png)](https://securityuncorked.com/2022/04/april-book-giveaway/ "Monthl...