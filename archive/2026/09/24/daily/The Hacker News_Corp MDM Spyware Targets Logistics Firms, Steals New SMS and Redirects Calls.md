---
title: Corp MDM Spyware Targets Logistics Firms, Steals New SMS and Redirects Calls
url: https://thehackernews.com/2026/09/corp-mdm-spyware-targets-logistics.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:34.025422
---

# Corp MDM Spyware Targets Logistics Firms, Steals New SMS and Redirects Calls

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

# [Corp MDM Spyware Targets Logistics Firms, Steals New SMS and Redirects Calls](https://thehackernews.com/2026/09/corp-mdm-spyware-targets-logistics.html)

**Ravie Lakshmanan**Sep 24, 2026Artificial Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhitRqKj3-JlcQ69xxlsxJs80aq7MNxgAc_VrV-TCrHGTVEwdWKIdvAiwB4szXMT3cRKpkzCRVObZxAO47CLl3JWLRerxVSITKy9xorsP-XY212M07JzDkZ7VXOA-r0maycB0jMv0r5Kl3q0VgrxpoeYfHJ_gkeXbzXLKz_3gAhDGy1ML06lfta_5w8u_Xo/s1700-nu-rw-lo-l85-e365/1000110893.jpg)

The logistics sector has become the target of a new malicious cyber campaign that distributes an Android spyware codenamed **Corp MDM**.

According to Have I Been Squatted, the campaign uses fake Google Play pages branded as CEVA and TKW Logistics to distribute an Android Package Kit (APK) file that's dressed up as a system service. The delivered app has the package name "com.corp.mdm"

Corp MDM is a "compact surveillance implant designed to exfiltrate newly received SMS content, divert calls, and maintain a hidden foreground service," security researcher Ben Folland [said](https://haveibeensquatted.com/blog/inside-corp-mdm-android-spyware-targeting-logisitics).

The malware has been described as narrow by design, lacking in spyware functions typically observed in commercial Android spyware. It's suspected that the threat actor behind the campaign used artificial intelligence (AI) during the development phase, given the presence of bugs that interfere with its capabilities.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

In addition, the activity is said to be part of a broader campaign targeting the logistics sector using credential phishing and Windows-based malware.

The malicious packages are distributed via bogus Google Play Store pages such as below -

* playgoogle.logisticstkwcargo[.]com
* playgoogle.ceva-app[.]help

Both the artifacts use a hard-coded IP address ("69.55.61[.]82") for command-and-control (C2), as well as for hosting credential-phishing lures and serving additional Windows malware targeting the logistics sector.

Once sideloaded and installed, the malicious app requests SMS, telephony, and notification permissions, allowing it to intercept incoming SMS messages, enable call forwarding, and display notifications. The malware-laced app also removes its normal launcher, while ensuring background execution.

In the next stage, it registers an Android identifier with the C2 server, sends heartbeat telemetry every 30 seconds, and repeatedly polls for commands every seconds -

* /api/v1/devices/register, to register the device, along with basic information
* /api/v1/devices/heartbeat, to send heartbeat message
* /api/v1/devices/{ANDROID\_ID}/commands, to receive commands issued by the threat actor
* /api/v1/commands/result, to post the results of the command execution
* /api/v1/sms/report, to transmit SMS sender, message body, and received timestamp, along with the device identifier

The attacker-controlled infrastructure has been found to host a password-protected Corp MDM admin panel on port 3456 that allows the operator to commandeer infected devices and send commands. The list of supported commands is as follows -

* ping, to return "pong" through the command-result endpoint
* forward\_on, to issue unconditional call-forwarding code with an operator-selected number
* forward\_off, to request cancellation of unconditional forwarding with ##21#.
* sync\_sms, to report the initiation of the sync process without performing data collection
* self\_destroy, to disable the implant components, stop the service, and request app-data clearing
* get\_location (supported by the panel, but not by the malware)
* lock\_device (supported by the panel, but not by the malware)

Notably, Corp MDM's SMS stealing functionality is limited to new inbound messages after the permission is granted. It does not retroactively exfiltrate the SMS inbox contents.

"That limited collection path is sufficient to expose high-value content," Folland said. "SMS remains common for one-time passcodes, password resets, account recovery, transaction notifications, and dispatch or delivery updates. The sender, full body, and timestamp all leave the device over cleartext HTTP."

It's currently unclear who is behind the operation, but Have I Been Squatted said the activity likely has an Armenian or Russian nexus, citing localized artifacts in the panel user interface and source code associated with the wider campaign.

This is not the first time threat actors have gone after the logistics sector. In November 2025, Proofpoint [detailed](https://thehackernews.com/2025/11/cybercriminals-exploit-remote.html) a campaign that infected trucking and logistics companies with remote monitoring and management (RMM) software for financial gain and cargo theft.

Earlier this February, [Ctrl-Alt-Intel](https://ctrlaltintel.com/research/DieselVortex/) and [Have I Been Squatted](https://haveibeensquatted.com/blog/diesel-vortex-inside-the-russian-cybercrime-group-targeting-us-eu-freight) shed light on a threat cluster codenamed Diesel Vortex that singled out freight and logistics entities in the U.S. and Europe, including DAT Truckstop, TIMOCOM, Teleroute, Penske Logistics, Girteka, and Electronic Funds Source (EFS).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

A Russian-Armenian threat actor is behind a new phishing-as-a-service (PhaaS) platform codenamed Global Profit (aka MC Profit Always) that's specifically designed to target the freight and logistics sector via bogus emails and steal over 1,600 unique login credentials between September 2025 and February 2026.

"This operation was not the work of a lone actor," Have I Been Squatted said. "It was a structured, financially driven criminal service sold to other operators, with evidence suggesting the group was actively employing spear-phish...