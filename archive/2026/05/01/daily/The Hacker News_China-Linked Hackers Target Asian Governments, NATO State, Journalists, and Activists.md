---
title: China-Linked Hackers Target Asian Governments, NATO State, Journalists, and Activists
url: https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html
source: The Hacker News
date: 2026-05-01
fetch_date: 2026-05-02T05:00:27.937277
---

# China-Linked Hackers Target Asian Governments, NATO State, Journalists, and Activists

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [China-Linked Hackers Target Asian Governments, NATO State, Journalists, and Activists](https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html)

**Ravie Lakshmanan**May 01, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhD3mr1fHyy1yT3u6ebxE9skoiCRtBYdZnkvdputmKF0XgZW5BKeQKkvnYswwusYFG4tvzVeWOqP3wgGtqLA7Ds9I-PYlasFVkOmaClo8IIpRGtdvuFZuKzDgvktukM1YXbTDbBAZUfk1mtWx8lHFF8N_YZXRl0ncSWtGGkzXDkm5gWMovjixeiyh6w_64W/s1700-e365/chinese-hackers.jpg)

Cybersecurity researchers have disclosed details of a new China-aligned espionage campaign targeting government and defense sectors across South, East, and Southeast Asia, along with one European government belonging to NATO.

Trend Micro has attributed the activity to a threat activity cluster it tracks under the temporary designation **SHADOW-EARTH-053**. The adversarial collective is assessed to be active since at least December 2024, while sharing some level of network overlap with [CL-STA-0049, Earth Alux, and REF7707](https://thehackernews.com/2025/12/china-linked-ink-dragon-hacks.html).

"The group exploits N-day vulnerabilities in internet-facing Microsoft Exchange and Internet Information Services (IIS) servers (e.g., [ProxyLogon](https://thehackernews.com/2021/03/proxylogon-exchange-poc-exploit.html) chain), then deploys web shells ([Godzilla](https://thehackernews.com/2024/01/apache-activemq-flaw-exploited-in-new.html)) for persistent access and stages [ShadowPad](https://thehackernews.com/2025/11/shadowpad-malware-actively-exploits.html) implants via DLL sideloading of legitimate signed executables," security researchers Daniel Lunghi and Lucas Silva [said](https://www.trendmicro.com/en_us/research/26/d/inside-shadow-earth-053.html) in an analysis.

Targets of the campaigns include Pakistan, Thailand, Malaysia, India, Myanmar, Sri Lanka, and Taiwan. The lone European country that features in the threat actor's victimology footprint is Poland.

The cybersecurity vendor said it observed nearly half the SHADOW-EARTH-053 targets, particularly those in Malaysia, Sri Lanka, and Myanmar, also compromised earlier by a related intrusion set dubbed SHADOW-EARTH-054, although no evidence of direct operational coordination has been observed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The starting point of the attacks is the exploitation of known security flaws to breach unpatched systems and drop web shells like Godzilla to facilitate persistent remote access. The web shells function as a delivery vehicle for command execution, enabling reconnaissance and ultimately resulting in the deployment of the ShadowPad backdoor via AnyDesk. The malware is launched using DLL side-loading.

In at least one case, the weaponization of the [React2Shell](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html) (CVE-2025-55182) is said to have facilitated the distribution of a Linux version of [Noodle RAT](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html) (aka ANGRYREBEL and Nood RAT). It's worth mentioning here that the Google Threat Intelligence Group (GTIG) linked this attack chain to a group known as UNC6595.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo6Xzcsumywb12fXk_W9qHqQLb9CZgKdGfNsl7wa5B70N7oDXitV-ogJQAS4HlZ8TgMgALuYRBRYpp8GM5FhVdeb57eaWZ4h6BfrNs8_M08vy4MhLt0V9gwB0iwXGUdf1bHbpn-J2dKCUfhBids4nzmbht0YemDwI_L2LJZmk3UPuzmlsNPwa-E6agO4uR/s1700-e365/zimbra.png)

Also put to use are [open-source tunneling tools](https://thehackernews.com/2026/02/asian-state-backed-group-tgr-sta-1030.html) like the IOX, GO Simple Tunnel (GOST), and Wstunnel, as well as [RingQ](https://thehackernews.com/2024/08/new-windows-backdoor-bitsloth-exploits.html) to pack malicious binaries and evade detection. To facilitate privilege escalation, SHADOW-EARTH-053 has been found to use Mimikatz, while lateral movement is accomplished using a custom remote desktop protocol (RDP) launcher and C# implementation of SMBExec known as [Sharp-SMBExec](https://github.com/checkymander/Sharp-SMBExec/).

"The primary entry vector used in this campaign were vulnerabilities in internet-facing IIS applications," Trend Micro said. "Organizations should prioritize applying the latest security updates and cumulative patches to Microsoft Exchange and any web applications hosted on IIS."

"In scenarios where immediate patching is not feasible, we strongly recommend deploying Intrusion Prevention Systems (IPS) or Web Application Firewalls (WAF) with rulesets specifically tuned to block exploit attempts against these known CVEs (Virtual Patching)."

### GLITTER CARP and SEQUIN CARP Go After Activists and Journalists

The disclosure comes as the Citizen Lab flagged a new phishing campaign undertaken by two distinct China-affiliated threat actors targeting and impersonating journalists and civil society, including Uyghur, Tibetan, Taiwanese, and Hong Kong diaspora activists. The wide-ranging campaigns were first detected in April and June 2025, respectively.

The clusters have been codenamed **GLITTER CARP**, which has singled out the International Consortium of Investigative Journalists (ICIJ), and **SEQUIN CARP**, whose main target was ICIJ journalist Scilla Alecci and other international journalists writing about topics of critical interest to the Chinese government.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_Fc0xPrkWNd7XDFbELmF2VXPcImXiLqCTQHw__Egdgqo9VHWMGsqdWRp_lyEdlf9hhgIYirwghWKZ8aX8uuNS-iROUyyVyIG2W0_DrfQ-A_Cp4CPRz42YsqnfZVhLENBuqUt3PV1i3-7JGIbdV57XQiocrquUxsHr06_gCzygPCSDSELxb-6t-GLsxEmq/s1700-e365/pixel.png)

"The actor employs well-thought-out digital impersonation schemes in phishing emails, including impersonation of known individuals and tech company security alerts," the Citizen Lab [said](https://citizenlab.ca...