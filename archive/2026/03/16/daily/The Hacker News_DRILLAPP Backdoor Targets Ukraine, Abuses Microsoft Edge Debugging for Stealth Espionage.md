---
title: DRILLAPP Backdoor Targets Ukraine, Abuses Microsoft Edge Debugging for Stealth Espionage
url: https://thehackernews.com/2026/03/drillapp-backdoor-targets-ukraine.html
source: The Hacker News
date: 2026-03-16
fetch_date: 2026-03-17T04:17:12.291534
---

# DRILLAPP Backdoor Targets Ukraine, Abuses Microsoft Edge Debugging for Stealth Espionage

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [DRILLAPP Backdoor Targets Ukraine, Abuses Microsoft Edge Debugging for Stealth Espionage](https://thehackernews.com/2026/03/drillapp-backdoor-targets-ukraine.html)

**Ravie Lakshmanan**Mar 16, 2026Cyber Espionage / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLAzfBgcfc_bSkMovfPss0X0ONO4MhDVIOKyB_FgCnAZ4NOfVM3MdIMfIr0QMDCqKBvJaAz0mRIPYV075qfnurW27qWCCmjlcnDX-DOnb-kHulHrvk-k_cZCchJfEfxBdhkUf3GCbboHdQzxOCv3sEzSvgKaOoCNRgD20y7ZywYWsYtjjnh8dDLMbqJnvr/s1700-e365/uk-cyberattacks.jpg)

Ukrainian entities have emerged as the target of a new campaign likely orchestrated by threat actors linked to Russia, according to a report from S2 Grupo's LAB52 threat intelligence team.

The campaign, [observed](https://lab52.io/blog/drillapp-new-backdoor-targeting-ukrainian-entities-with-possible-links-to-laundry-bear/) in February 2026, has been assessed to share overlaps with a prior campaign mounted by [Laundry Bear](https://thehackernews.com/2026/01/pluggyape-malware-uses-signal-and.html) (aka UAC-0190 or Void Blizzard) aimed at Ukrainian defense forces with a malware family known as PLUGGYAPE.

The attack activity "employs various judicial and charity themed lures to deploy a JavaScript‑based backdoor that runs through the Edge browser," the cybersecurity company said. Codenamed **DRILLAPP**, the malware is capable of uploading and downloading files, leveraging the microphone, and capturing images through the webcam by taking advantage of the web browser's features.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Two different versions of the campaign have been identified, with the first iteration detected in early February by making use of a Windows shortcut (LNK) file to create an HTML Application (HTA) in the temporary folder, which then loads a remote remote script hosted on Pastefy, a legitimate paste service.

To establish persistence, the LNK files are copied to the Windows Startup folder so that they are automatically launched following a system reboot. The attack chain then displays a URL containing lures related to installing Starlink or a Ukrainian charity named Come Back Alive Foundation.

The HTML file is eventually executed via the Microsoft Edge browser in [headless mode](https://en.wikipedia.org/wiki/Headless_browser), which then loads the remote obfuscated script hosted on Pastefy.

The browser is executed with additional parameters like –no-sandbox, –disable-web-security, –allow-file-access-from-files, –use-fake-ui-for-media-stream, –auto-select-screen-capture-source=true, and –disable-user-media-security, granting it access to the local file system, as well as camera, microphone, and screen capture without requiring any user interaction.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1aAJG38sglu5mCXzEeN4sPJuXRmQmzD0hAacZH8ZLmMj91KNzfkY277d7-IUBApMShbNfKhAh3VkWby75Ewd-GrKypXi9HdvUctBGPy6wbtc2O0NWMgdr1mLEEkg4us70GK70YTJosE16KL8iC6PI3mEzYZyTbPz5FZnmwft0iizYqY6U0_0iwn9VqCGC/s1700-e365/camera.png)

The artifact essentially functions as a lightweight backdoor to facilitate file system access and capture audio from the microphone, video from the camera, and images of the device's screen all through the browser. It also generates a device fingerprint using a technique called [canvas fingerprinting](https://en.wikipedia.org/wiki/Canvas_fingerprinting) when run for the first time and uses Pastefy as a dead drop resolver to fetch a WebSocket URL used for command‑and‑control (C2) communications.

The malware transmits the device fingerprint data along with the victim's country, which is determined from the machine's time zone. It specifically checks if the time zones correspond to the U.K., Russia, Germany, France, China, Japan, the U.S., Brazil, India, Ukraine, Canada, Australia, Italy, Spain, and Poland. If that's not the case, it defaults to the U.S.

The second version of the campaign, spotted in late February 2026, eschews LNK files for Windows Control Panel modules, while keeping the infection sequence largely intact. Another notable change involves the backdoor itself, which has now been upgraded to allow recursive file enumeration, batch file uploads, and arbitrary file download.

"For security reasons, JavaScript does not allow the remote downloading of files," LAB52 said. "This is why the attackers use the Chrome DevTools Protocol (CDP), an internal protocol of Chromium‑based browsers that can only be used when the –remote-debugging-port parameter is enabled."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

It's believed that the backdoor is still in the initial stages of development. An early variant of the malware detected in the wild on January 28, 2026, has been observed just communicating with the domain "gnome[.]com" instead of downloading the primary payload from Pastefy.

"One of the most notable aspects is the use of the browser to deploy a backdoor, which suggests that the attackers are exploring new ways to evade detection," the Spanish security vendor said.

"The browser is advantageous for this type of activity because it is a common and generally non‑suspicious process, it offers extended capabilities accessible through debugging parameters that enable unsafe actions such as downloading remote files, and it provides legitimate access to sensitive resources such as the microphone, camera, or screen recording without triggering immediate alerts."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_sha...