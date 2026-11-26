---
title: Com-Affiliated Hackers Hijack Cloud Accounts via Vishing for Data Theft and Extortion
url: https://thehackernews.com/2026/11/com-affiliated-hackers-hijack-cloud.html
source: The Hacker News
date: 2026-11-25
fetch_date: 2026-11-26T10:15:12.854838
---

# Com-Affiliated Hackers Hijack Cloud Accounts via Vishing for Data Theft and Extortion

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Com-Affiliated Hackers Hijack Cloud Accounts via Vishing for Data Theft and Extortion](https://thehackernews.com/2026/11/com-affiliated-hackers-hijack-cloud.html)

**Ravie Lakshmanan**Nov 25, 2026Social Engineering / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoCQn2zL8-RpfdhDeb1Zmyn46vLk1s9lerpXtGlcMkN5IGF9nlhEejtwoOXwhznjS7JVrix_FeG_G6yJ6Jb8mI31CU4Mi2dndKvLp-4nG4wWsqMaBpI60HFIk5d8_5uIxj6XEjSt4sixJYkJN8Xeqs4OrgSzOPK48esNtXbQ_FgtVe67B_WZkfpuUSEiD7/s1700-nu-rw-lo-l85-e365/vishing.jpg)

Palo Alto Networks Unit 42 has disclosed that it's tracking and has responded to "numerous waves of vishing attacks" orchestrated by Com-affiliated threat actors since August 2026 that have led to data theft and extortion attempts.

The attacks have targeted financial services, healthcare, and legal services located in the U.S., the U.K., and Australia. Other targets include construction, high-technology, transportation, manufacturing, pharmaceuticals, insurance, and real estate sectors.

"The victims share a common profile: they hold large volumes of high-impact corporate data where exposure carries severe regulatory, legal, or market consequences," Unit 42 [said](https://unit42.paloaltonetworks.com/com-affiliate-vishing-attacks/). "These attackers targeted financial services organizations about twice as often as healthcare organizations in August 2026, but healthcare overtook financial services in September."

The activity has been attributed to a [number of threat clusters](https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html), including -

* Bling Libra (aka ShinyHunters)
* CL-CRI-1116 (aka Redact, formerly BlackFile), first observed in January 2026
* CL-CRI-1147 (aka Pink), first observed in May 2026
* CL-CRI-1182 (aka Falcon), first observed in mid-2026
* CL-CRI-1192 (aka Helix and UNC6671), first observed in June 2026
* CL-CRI-1264 (aka Vortex), first observed in September 2026
* CL-CRI-1274 (aka Cinder), first observed in September 2026

Intrusions typically commence with voice phishing, with the attackers posing as IT staff to resolve a purported authentication issue and direct the victim to a phishing page personalized to their organization.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Once the AiTM kit captures credentials and session tokens, the attackers quickly enroll their own multi-factor authentication (MFA) devices, abuse cloud utilities and, in a few instances, deploy malicious browser extensions to exfiltrate data and extort victims.

The harvested authentication data is used to authenticate to victim environments, typically by routing such requests through residential proxy networks and commercial VPNs. The adversaries then seek to establish multi-layered persistence by registering their MFA devices, generating cloud infrastructure temporary credentials, authorizing unapproved third-party OAuth applications; enumerate sensitive data; evade defenses by modifying mailbox rules and clearing security alert events; and harvest data from cloud platforms.

"Attackers associated with CL-CRI-1264 establish initial access through vishing, where they pose as internal IT support and direct employees to servers using subdomains tailored to each targeted organization," Unit 42 said.

"These servers act as adversary-in-the-middle (AitM) proxies that pass user credentials and multi-factor authentication (MFA) approvals to the attackers in real time. Attackers have targeted employees on both their corporate workstations and personal mobile devices."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-rBOP6kzc-DbB8LzHGHUt7034hmOyCtuN7IJ3LKfmVZfwguQ5Fg4a7QcafXwJ8oLIjm-o5pqrFDnh5skBUZkXkPBhOjwvzMXz3opFPyLCW26TlWRER4T59AMNKHr71SA8D1qqhi8-eswCvOh841Kv-oyyYHuIDiEmQpg0IrYDMT1cQiGt6wC34CUSo5kU/s1700-nu-rw-lo-l85-e365/cloud.png)

CL-CRI-1264 has also been observed enrolling unauthorized MFA devices within minutes of authenticating to establish persistence, often reusing a single device named Pixel 10a across compromised accounts. The attack chains involve automated data exfiltration using Python scripts to harvest information from Microsoft 365 mailbox, OneDrive, and SharePoint.

Once data is exfiltrated, the threat actor sends Microsoft Teams messages directly to employees at victim organizations, claiming data theft and instructing them to visit a TOR-hosted ransom negotiation site.

The second new cluster to emerge around the same time is CL-CRI-1274, which has also leaned on vishing for initial access and leveraged the Microsoft Graph software development kit (SDK) to collect and exfiltrate data from the victim's SharePoint and OneDrive environments.

"Afterwards, the attackers used a compromised account to send extortion messages internally via email and Microsoft Teams, ultimately directing recipients to a Tor-hosted negotiation site," Unit 42 said.

The cybersecurity company said it also observed the CL-CRI-1192 attackers using a [malicious browser extension](https://deoxy.net/blog/inside-unc6671s-browser-implant/) named "Google Chrome" that's said to have been sideloaded onto the browser after enabling Developer Mode. The add-on performs a number of malicious actions, such as -

* Installing global keyloggers
* Stealing local/session storage and authentication cookies for Microsoft and Google accounts
* Scanning pages for QR codes to capture login/MFA tokens
* Streaming webcam feeds
* Implementing a command-and-control (C2) remote control module via Chrome DevTools Protocol to capture screenshots, dispatch input events, steal clipboard contents, and allow remote site navigation.

"We assess with moderate confidence that the attackers associated with CL-CRI-1192 developed this malicious browser extension as an alternative method to extract credentials from desktop and laptop devices running Chromium-based browsers such as Google Chrome and Microso...