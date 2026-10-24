---
title: Does opting out of smart TV tracking work Research finds “suspicious” traffic.
url: https://arstechnica.com/gadgets/2026/10/does-opting-out-of-smart-tv-tracking-work-research-finds-suspicious-traffic/
source: Instapaper: Unread
date: 2026-10-23
fetch_date: 2026-10-24T06:48:05.733943
---

# Does opting out of smart TV tracking work Research finds “suspicious” traffic.

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

[Search](/search/ "Search")

Sign In

Sign in dialog...

Sign in

privacy

# Does opting out of smart TV tracking work? Research finds “suspicious” traffic.

OS operators throwing out that data is “unlikely,” research author tells Ars.

[Scharon Harding](https://arstechnica.com/author/scharonharding/)
–

Oct 21, 2026 2:00 pm
| [90](https://arstechnica.com/gadgets/2026/10/does-opting-out-of-smart-tv-tracking-work-research-finds-suspicious-traffic/#comments "90 comments")

[![Smart TV is mounted on the wall in a contemporary living room while a person holds a remote control .](https://cdn.arstechnica.net/wp-content/uploads/2026/10/GettyImages-2226225055-640x427.jpg)
![Smart TV is mounted on the wall in a contemporary living room while a person holds a remote control .](https://cdn.arstechnica.net/wp-content/uploads/2026/10/GettyImages-2226225055-1152x648.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2026/10/GettyImages-2226225055.jpg)

Credit:
[https://www.gettyimages.com/detail/photo/modern-living-room-with-smart-tv-and-remote-control-royalty-free-image/2226225055](Getty)

Credit:
[https://www.gettyimages.com/detail/photo/modern-living-room-with-smart-tv-and-remote-control-royalty-free-image/2226225055](Getty)

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

Smart TVs running operating systems from Samsung, Vizio, and Roku continue sending data to automatic content recognition (ACR) endpoints after users opt out of tracking in the devices’ settings, according to research published on Monday. The paper from Northeastern University researchers points to potential privacy violations from some of the biggest TV brands.

ACR captures video screenshots or audio clips from smart TVs and sends the data to remote servers, where it’s used for things like measuring content viewership and serving targeted ads.

The paper, [“Watching the Watchers: Privacy Analysis of US Smart TV Automatic Content Recognition,”](https://watchingthewatchers.github.io/watchingthewatchers/paper.html) examined eight smart TV OSes across 12 smart TVs from 10 manufacturers (Amazon, Hisense, LG, Roku, Samsung, Sony, Supersonic, TCL, Vizio, and Westinghouse) to examine when smart TVs use ACR and how effective opting out of user tracking is.

Regarding the relatively small number of TVs studied, Ilgar Mammadov, the report’s lead author and a research assistant at Northeastern, told Ars Technica:

> Together, the smart TV operating systems we tested cover approximately 95 percent of those used in the United States. Because ACR is implemented at the OS level, we expect that adding more TVs running the same operating systems would largely repeat our existing findings rather than reveal new behavior.

The researchers made OS-specific control scripts and delivered them over Wi-Fi, while Mon(IoT)r and SPHERE Research Infrastructure software captured network traffic coming to and from each TV. The research included identifying each OS’s ACR endpoint. Some of the OSes, including Samsung’s Tizen, “expose self-disclosing ACR domains containing keywords such as ‘acr’ and ACR provider names,” the paper said. The researchers conducted 5,943 controlled experiments for the report.

The report’s findings have their limits, of course. Mammadov noted that each ACR provider and OS studied implemented ACR differently, adding:

> They differed in the scenarios that trigger ACR, in how effective the opt-out is, and in the ACR modalities used. We would therefore expect TVs using ACR providers outside our study to behave differently as well, and our results should not be generalized to them. That said, our methodology is designed to be reusable.

## Ongoing network traffic after user tracking is disabled

The researchers found that the TVs running Samsung Tizen, Vizio OS (which the report refers to by its former name, SmartCast), and Roku OS continued to send network traffic to the respective ACR endpoints when user tracking was disabled in settings and when tested for specific usage scenarios, including using a first-party streaming app.

In Roku OS’ case, the tested TVs exhibited this ACR-like behavior only when using the operating system’s integrated streaming app, The Roku Channel. Further, that behavior is expected and disclosed in Roku’s terms of service and, according to the report, in the TV’s settings on TCL-branded TVs.

That’s not the case for Tizen and Vizio OS TVs, which exhibited ACR-like behavior across additional usage scenarios, as shown in the table from the report below.

[[![](https://cdn.arstechnica.net/wp-content/uploads/2026/10/report.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2026/10/report.jpg)

Credit:
[Creative Commons Attribution 4.0 International License](https://watchingthewatchers.github.io/watchingthewatchers/paper.html)

Credit:
[Creative Commons Attribution 4.0 International License](https://watchingthewatchers.github.io/watchingthewatchers/paper.html)](https://cdn.arstechnica.net/wp-content/uploads/2026/10/report.jpg)

Ars contacted Samsung and Vizio to ask why TVs running their OSes send network traffic to ACR endpoints when tracking is disabled. We’ll update this story if we get answers.

Critically, encryption prevented the report’s authors from determining what the network traffic contained. However, they view the “continued presence of traffic consistent with ACR tracking after opt-out as suspicious.”

“These behaviors indicate potential privacy violations; however, we cannot know for certain without access to payload content,” the report reads.

### Samsung

Researchers found that “traffic consistent with ACR tracking” remained present in all 30 of Tizen’s first-party streaming app measurements and 41 out of 60 of its “antenna” measurements, specifically when they used a radio frequency (RF) modulator “to deliver custom broadcast TV content with both dynamic video and audio” and to “deliver simulated content with dynamic video but no audio.”

Network traffic also continued after opt-out during 18 of 30 HDMI measurements on Tizen.

The researchers also recorded traffic to ACR endpoints in more than half the tests in which the researchers displayed “dynamic video with audio via HDMI from an external source” on a Tizen TV.

### Vizio OS

The report’s authors determined that Amazon Kinesis is “the endpoint most consistent with ACR behavior for” Vizio OS and noted that traffic to the domain stops whe...