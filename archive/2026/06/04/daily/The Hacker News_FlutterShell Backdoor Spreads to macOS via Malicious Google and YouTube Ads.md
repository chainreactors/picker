---
title: FlutterShell Backdoor Spreads to macOS via Malicious Google and YouTube Ads
url: https://thehackernews.com/2026/06/fluttershell-backdoor-spreads-to-macos.html
source: The Hacker News
date: 2026-06-04
fetch_date: 2026-06-05T06:14:26.935563
---

# FlutterShell Backdoor Spreads to macOS via Malicious Google and YouTube Ads

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [FlutterShell Backdoor Spreads to macOS via Malicious Google and YouTube Ads](https://thehackernews.com/2026/06/fluttershell-backdoor-spreads-to-macos.html)

**Ravie Lakshmanan**Jun 04, 2026Malvertising / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwFQkJElJQpI5ODTBzh1EzrxsRYamFN0ntC9V6vF4b4FfEJ0svPhI_1TnKm960eIsewSFT-DR1RtNk3M511OQK6I-k3UQNNLut1f_fjM9wB4NHxdvJzJQ3VvhIGO9ja0hNIzRAOZLVMngS4R8hQxXfV-_DO71x0CU0YSnxpclCnV0DGX6TdNmr32ongewk/s1700-e365/macos.jpg)

Cybersecurity researchers have shed light on a macOS malvertising campaign codenamed Operation FlutterBridge that spreads a new backdoor called **FlutterShell**.

According to Palo Alto Networks Unit 42, the campaign is said to be the next stage of a previously reported activity cluster dubbed [JSCoreRunner](https://thehackernews.com/2025/09/weekly-recap-drift-breach-chaos-zero.html#:~:text=Fake%20PDF%20Converters%20Deliver%20JSCoreRunner%20macOS%20Malware) (aka [FileRipple](https://moonlock.com/jscorerunner-fake-pdf-converters)) in late August 2025. The cybercrime group behind the two attack chains is being tracked under the moniker CL-CRI-1089. The attackers are assessed to be active since at least 2023.

"Built using the Flutter framework, FlutterShell infects targets with adware via malicious desktop applications," Unit 42 [said](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/). "In addition to its adware functionality, the payload possesses backdoor capabilities, including shell command execution and file system manipulation."

Operations attributed to CL-CRI-1089 also include [Recipe Lister](https://www.bluevoyant.com/blog/recipelister-a-recipe-for-disaster) and [Calendaromatic](https://medium.com/%40rabbit_knight/when-your-calendar-wants-to-steal-your-tokens-a-look-at-calendaromatic-81c15bb7ed9e), both of which fall under a broader designation known as [TamperedChef](https://thehackernews.com/2026/05/threatsday-bulletin-linux-rootkits.html#trojanized-apps-cluster) (aka [EvilAI](https://thehackernews.com/2025/09/evilai-malware-masquerades-as-ai-tools.html)), an ongoing series of campaigns that involve using trojanized versions of productivity software to deliver potentially unwanted programs (PUPs) and adware.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

These campaigns distribute malicious Google and YouTube advertisements using a network of Google-verified shell companies, with the ads acting as a lure to trick targets into deploying malware that masquerades as legitimate desktop applications. Some of the front companies are [AdsParkPro LTD](https://find-and-update.company-information.service.gov.uk/company/15623150/officers), [Advantage Web Marketing LLC](https://youcontrol.com.ua/en/catalog/company_details/42303397/), and [SOFT WE ART LIMITED](https://find-and-update.company-information.service.gov.uk/company/15372588/officers) (now PACIFIC TRADE SOLUTIONS LTD).

Target audiences for these ads are macOS users in the U.S., Canada, Australia, France, and Germany. Although none of the Google Ads accounts are currently accessible via the Google Ads Transparency Center, records from YouControl and the U.K. government's Companies House register indicate that the firms all have links to Ukrainian individuals.

The latest iteration entails the deployment of FlutterShell, which supports arbitrary command execution, file system interaction, and environment variables exfiltration. These efforts have been detected as recently as March 2026.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRaLMt1LGvxqD0cbhT30RVO_h_r97NYF59qcHQOxSqZzy2VW6k6Z8NBs2VoijB0n3_z-xPiGq5ZkcpbcO_-fPOTK9nYjCEVa-XPxs2Y99kzbVsnNW_3Msg8olYlKYTftpKm1_y2cW0J1EK59jwmTCHF3MTsOqZHzIS0i41Btfz_a7aE5PJH8tUQr8FetYn/s1700-e365/macos.png)

"Upon execution, the malware modifies Google Chrome configuration files to hijack the browser, forcing all traffic through an attacker-controlled, ad-filled intermediary site," researchers Ido Asher, Noa Dekel, and Tom Fakterman said. "All observed samples were signed with valid Apple Developer IDs and successfully passed notarization, meaning Apple's automated security checks did not flag them as malicious at the time of submission."

What makes FlutterShell noteworthy is that it implements a WebView-based architecture that utilizes a JavaScript-to-native bridge, thereby allowing the adversary to host malicious logic on an external website, rather than embedding it into the binary. This, in turn, makes it possible to dynamically alter the malware's behavior in real time without having to recompile or push out an updated version to compromised hosts.

"In WebView-based architecture, a native application uses an embedded web browser component to display content," Unit 42 explained. "The JavaScript-to-native bridge acts as a communication channel between this web content and the host native application, allowing them to exchange data and cross-invoke functionality."

Three different variants of FlutterShell, viz., PodcastsLounge, PDF-Brain, and PDF-Ninja, have been identified. This, coupled with the presence of unfinished functions in the JavaScript logic hosted on the attackers' infrastructure, suggests the malware is likely under active development.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Some of the variants, PDF-Brain and PDF-Ninja, feature an artificial intelligence (AI)-powered summarization capability by relaying documents through an attacker-controlled server before processing them. In addition, the malware enables system fingerprinting and the theft of browser session data.

FlutterShell has also been found to share technical similarities with [Calendaromatic](https://www.kroll.com/en/publications/cyber/widespread-installation-calendaromatic-adware-homoglyph-channel) and Recipe Lister, the most obvious being the WebView...