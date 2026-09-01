---
title: ValleyRAT Backdoor Hides in Signed Adware That Users Add to Antivirus Exclusions
url: https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html
source: The Hacker News
date: 2026-08-31
fetch_date: 2026-09-01T07:01:28.609414
---

# ValleyRAT Backdoor Hides in Signed Adware That Users Add to Antivirus Exclusions

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [ValleyRAT Backdoor Hides in Signed Adware That Users Add to Antivirus Exclusions](https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html)

**Swati Khandelwal**Aug 31, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8OUY2TmBxA9RLM9yG0dnv8OShMmr_0KXcJUWtPvcTbFKQ-jmG4_6PyVNCNxQH9VacMVqmi3ZdmcHepDqoLT4XOl5AHZ6mnxmg_QrTUmK2D01fsjrBJKQ1KmlodLNjgbNp65TVoTslEHW5s1IqgFR8xYQWab9WQBvn30sYuM-xh7pSQfAKUOFi3v4q3Do/s1700-nu-rw-lo-l85-e365/adblock.jpg)

The threat actor known as **Silver Fox** has been observed distributing the **ValleyRAT** backdoor disguised as a signed Chinese adware application, running the malware under a trusted process to slip past users who add such software to their antivirus exclusions.

Russian cybersecurity vendor Kaspersky said the attackers built the disguise around **QN Wallpaper**, a genuine Chinese desktop-wallpaper tool that in its unmodified form is adware, bundling partner apps and displaying ad banners.

Once installed, ValleyRAT (also tracked as Winos 4.0) hands the operator full control of the compromised machine. Kaspersky said the attack's geography and payload point to Silver Fox as the likely group behind it, and urged users to avoid software of questionable reputation and to keep it away from security-tool exclusions.

"This case is a clear example of how adware and affiliate networks can turn out to be far more dangerous than they appear. ValleyRAT is a sophisticated backdoor capable of collecting sensitive data such as keystrokes and clipboard contents, taking screenshots, and delivering additional malicious modules," Kaspersky said in [its analysis](https://securelist.com/valleyrat-backdoor-adware/121175/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The disguise relies on DLL sideloading. The installer unpacks a modified copy of QN Wallpaper and runs its signed executable, `QnWallpaper.exe`, which loads a malicious `libcef.dll` planted in the same directory. With the library executing inside a legitimately signed process, the backdoor runs without triggering controls that trust the signature.

Before the adware component starts, the installer switches off Windows Defender through the `DisableAntiSpyware` registry key and adds the program to the system's autorun entries. When the logged-in user lacks administrator rights, the malware relaunches itself with `runas` to acquire them.

ValleyRAT can also flag its own process as critical, so that any attempt to terminate it triggers a blue screen of death.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtkJnSxq4tyrsThKNbj35jRVZF8gITCoJkNC6hyHZ9STZ1K8_t8rIvqb6P2WLcS76AglLMPt7FWr-bgVUHxPLUHc6zNFR7VqXu-TGcRaT5GCQYX0iNGhyphenhyphenBh1evZ4peXsRMIC_NVM58Yx33ipQhBo0ryQZHqnlyVpfzw61ELHhdhmAOtrfWDSth25IhTBU/s1700-nu-rw-lo-l85-e365/chinese.png)

Kaspersky shared the following indicators of compromise (IoCs) -

* **Hashes (MD5):** `c24e99f9437feacaa63766a3cde3fe3d` (the submitted installer), `07ddbbe2c71c45577a7a4fbcdba0df91` (the malicious `libcef.dll`), and `8a626d844943da3456b044f38deae3a2`
* **Command-and-control servers:** 103.45.66.18 on ports 441, 442 and 443, and 192.253.225.173 on ports 6666 and 8888
* **Domains in the chain:** qnwallpaper[.]keansoft[.]cn, the abused adware's download site, and meeting[.]tencent[.]com, a legitimate page opened as a decoy
* **Host artifacts:** the `DisableAntiSpyware` registry value and the install directory `C:\Program Files\QNWallpaper\5.4.0.1662\`

DLL sideloading through signed, legitimate software is an established part of Silver Fox's toolkit. In a campaign against a Japanese manufacturer about five weeks earlier, [Cato Networks documented](https://www.catonetworks.com/blog/cato-ctrl-silverfox-evolves/) what it called the group's "newly observed abuse of legitimate applications for DLL sideloading," and the same `libcef.dll` filename had already featured in [a 2025 ValleyRAT loader](https://thehackernews.com/2025/01/pngplug-loader-delivers-valleyrat.html).

Kaspersky itself tracked the group in [an earlier tax-themed campaign](https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html) against organizations in India and Russia.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Kaspersky's account is based on a single installer submitted by a customer; its advertising features stay inert while the infection chain runs, and the report stops short of attaching a victim count to the adware route.

Across 2026 the vendor recorded more than 100,000 detections of ValleyRAT and associated malware affecting over 1,500 unique users, mostly in China and India, a figure spanning all of the year's ValleyRAT activity rather than this campaign alone.

Kaspersky also urged organizations to set clear policies on third-party software on work devices and to keep staff aware of the threat.

"For individual users, we recommend avoiding the installation of software with a questionable reputation, and, even more importantly, never adding such software to your security solutions' exclusion lists," the company said.

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
[![Facebook Messen...