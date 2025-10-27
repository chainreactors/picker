---
title: Gophish Framework Used in Phishing Campaigns to Deploy Remote Access Trojans
url: https://thehackernews.com/2024/10/gophish-framework-used-in-phishing.html
source: The Hacker News
date: 2024-10-23
fetch_date: 2025-10-06T18:56:19.827290
---

# Gophish Framework Used in Phishing Campaigns to Deploy Remote Access Trojans

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

# [Gophish Framework Used in Phishing Campaigns to Deploy Remote Access Trojans](https://thehackernews.com/2024/10/gophish-framework-used-in-phishing.html)

**Oct 22, 2024**Ravie LakshmananMalware / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyh219oGnY3AKVBPBCJm09TzH8EYdx_66SeJHCEn8FaubuYPzBFbrkbmyNaE01-CpVSPtfK7K0qr8cBe-MPp-1BPVA-CZ6F9g_MFU8B6g7BfkI4ol8BtJ2lVrFwQdSIJLdPk4TVPz1h3nVJ9dHkoMrY5ldZj5KESGl_gDEN8Fk0wy_F62GPm-wKbwKd9Cy/s790-rw-e365/cisco.png)

Russian-speaking users have become the target of a new phishing campaign that leverages an open-source phishing toolkit called Gophish to deliver [DarkCrystal RAT](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html) (aka DCRat) and a previously undocumented remote access trojan dubbed PowerRAT.

"The campaign involves modular infection chains that are either Maldoc or HTML-based infections and require the victim's intervention to trigger the infection chain," Cisco Talos researcher Chetan Raghuprasad [said](https://blog.talosintelligence.com/gophish-powerrat-dcrat/) in a Tuesday analysis.

The targeting of Russian-speaking users is an assessment derived from the language used in the phishing emails, the lure content in the malicious documents, links masquerade as Yandex Disk ("disk-yandex[.]ru"), and HTML web pages disguised as VK, a social network predominantly used in the country.

[Gophish](https://getgophish.com) refers to an open-source phishing framework that allows organizations to test their phishing defenses by leveraging easy-to-use templates and launch email-based campaigns that can then be tracked in near real-time.

The unknown threat actor behind the campaign has been observed taking advantage of the toolkit to send phishing messages to their targets and ultimately push DCRat or PowerRAT depending on the initial access vector used: A malicious Microsoft Word document or an HTML embedding JavaScript.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

When the victim opens the maldoc and enables macros, a rogue Visual Basic (VB) macro is executed to extract an HTML application (HTA) file ("UserCache.ini.hta") and a PowerShell loader ("UserCache.ini").

The macro is responsible for configuring a Windows Registry key such that the HTA file is automatically launched every time a user logs into their account on the device.

The HTA file, for its part, drops a JavaScript file ("UserCacheHelper.lnk.js") that's responsible for executing the PowerShell Loader. The JavaScript is executed using a legitimate Windows binary named "cscript.exe."

"The PowerShell loader script masquerading as the INI file contains base64 encoded data blob of the payload PowerRAT, which decodes and executes in the victim's machine memory," Raghuprasad said.

The malware, in addition to performing system reconnaissance, collects the drive serial number and connects to remote servers located in Russia (94.103.85[.]47 or 5.252.176[.]55) to receive further instructions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEil0xOcWVavw4R8W4ERayWQjKdDs5IXUPy1i4OrY_UKUwJjdYIPSGNQoHiqwXfkF2U6d9aQIAFCUkB8iJ1yWbTixfwoHNiXXxy0bdo4QPZ62RUF8DwhisPH5FZ6vp6NMhUlNRoLP_oH2nrSF9BMIeEBShnrlG2boHLGXNXpYmKsX6B_ZsHnHnEJKmKO85X9/s790-rw-e365/1.jpeg)

"[PowerRAT] has the functionality of executing other PowerShell scripts or commands as directed by the [command-and-control] server, enabling the attack vector for further infections on the victim machine."

In the event no response is received from the server, PowerRAT comes fitted with a feature that decodes and executes an embedded PowerShell script. None of the analyzed samples thus far have Base64-encoded strings in them, indicating that the malware is under active development.

The alternate infection chain that employs HTML files embedded with malicious JavaScript, in a similar vein, triggers a multi-step process that leads to the deployment of DCRat malware.

"When a victim clicks on the malicious link in the phishing email, a remotely located HTML file containing the malicious JavaScript opens in the victim machine's browser and simultaneously executes the JavaScript," Talos noted. "The JavaScript has a Base64-encoded data blob of a 7-Zip archive of a malicious SFX RAR executable."

Present within the archive file ("vkmessenger.7z") – which is downloaded via a technique called HTML smuggling – is another password-protected SFX RAR that contains the RAT payload.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's worth noting that the exact infection sequence was [detailed](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html) by Netskope Threat Labs in connection with a campaign that leveraged fake HTML pages impersonating TrueConf and VK Messenger to deliver DCRat. Furthermore, the use of a nested self-extracting archive has been [previously observed](https://hunt.io/blog/spotting-sparkrat-detection-tactics-and-sandbox-findings) in campaigns delivering SparkRAT.

"The SFX RAR executable is packaged with the malicious loader or dropper executables, batch file, and a decoy document in some samples," Raghuprasad said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfWHDJit4z2Ek6vDs_B-vUKD-cFLBr3Xdhr7DSrR3nCyr96Fz1D5SK42SsGLUHyWmYbnY71Y1WJom9XAh3XALatkFUwWt_WQPp0nmbX7KXSAAVjICuwZusRvaEWA0Xwg_wQo_2TQQWB0rLKuz_JrzqEZW255K3sb0afzRhjeDwKYeo2e_9qoBMDzzV_EhF/s790-rw-e365/2.jpeg)

"The SFX RAR drops the GOLoader and the decoy document Excel spreadsheet in the victim machine user profile applications temporary folder and runs the GOLoader along with opening the decoy document."

The Golang-based loader is also designed to retrieve the DCRat binary data stream from a remote location through a hard-coded URL that points to a now-removed [GitHub repository](https://github.com/mrbrounr) and save it...