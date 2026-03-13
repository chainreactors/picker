---
title: ThreatsDay Bulletin: OAuth Trap, EDR Killer, Signal Phishing, Zombie ZIP, AI Platform Hack & More
url: https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html
source: The Hacker News
date: 2026-03-12
fetch_date: 2026-03-13T04:08:03.984290
---

# ThreatsDay Bulletin: OAuth Trap, EDR Killer, Signal Phishing, Zombie ZIP, AI Platform Hack & More

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

# [ThreatsDay Bulletin: OAuth Trap, EDR Killer, Signal Phishing, Zombie ZIP, AI Platform Hack & More](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html)

**Ravie Lakshmanan**Mar 12, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXV4c7kTpbuiCqYlpV1_7JzOZ3Pz-M51G5q4u6vUoAjUZF32E3z0pJ7mNpG3gz4N9ai7SaQ-nDNpYJWfLc7e8CeYKCeNJQH8OAljb8V6HB_r4s1MWBYCoduTSf4iPbtpSqnIxpp2uXGGikUKEXUVlhEtFeB_Ddaw83fcaC9tmy-mBCWNRBzNnFoNyJTxDV/s1700-e365/tday.jpg)

Another Thursday, another pile of weird security stuff that somehow happened in just seven days. Some of it is clever. Some of it is lazy. A few bits fall into that uncomfortable category of “yeah… this is probably going to show up in real incidents sooner than we’d like.”

The pattern this week feels familiar in a slightly annoying way. Old tricks are getting polished. New research shows how flimsy certain assumptions really are. A couple of things that make you stop mid-scroll and think, “wait… people are actually pulling this off?”

There’s also the usual mix of strange corners of the ecosystem doing strange things — infrastructure behaving a little too professionally for comfort, tools showing up where they absolutely shouldn’t, and a few cases where the weakest link is still just… people clicking stuff they probably shouldn’t.

Anyway. If you’ve got five minutes and a mild curiosity about what attackers, researchers, and the broader internet gremlins were up to lately, this week’s ThreatsDay Bulletin on The Hacker News has the quick hits. Scroll on.

1. OAuth consent abuse

   [The Dangers of Malicious OAuth Applications](https://www.wiz.io/blog/detecting-malicious-oauth-applications)

   Cloud security firm Wiz has warned of the dangers posed by [malicious OAuth applications](https://thehackernews.com/2026/03/microsoft-warns-oauth-redirect-abuse.html), highlighting how "consent fatigue" could open the door for attackers to gain access to a victim's sensitive data by giving their malicious apps a legitimate-looking name. By accepting the permissions requested by a rogue OAuth application, the user is "adding" the attacker's app into their company's tenant. "Once 'Accept' is clicked, the sign-in process is complete," Wiz [said](https://www.wiz.io/blog/detecting-malicious-oauth-applications). "But instead of going to a normal landing page, the access token is sent to the attacker's Redirect URL. With that token, the attacker now has access to the user's files or emails without ever needing to know their password." The Google-owned company also said it detected a large-scale campaign active in early 2025 that involved 19 distinct OAuth applications impersonating well-known brands such as Adobe, DocuSign, and OneDrive, and targeted multiple organizations. Details of the activity were [documented](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html) by Proofpoint in August 2025.
2. Messaging account takeover

   [Russian Hackers Target Signal and WhatsApp Accounts](https://english.aivd.nl/documents/2026/03/09/cybersecurity-advisory.-phishing-via-messaging-apps-signal-and-whatsapp)

   Russian-linked hackers are trying to [break into](https://english.aivd.nl/documents/2026/03/09/cybersecurity-advisory.-phishing-via-messaging-apps-signal-and-whatsapp) the Signal and WhatsApp accounts of government officials, journalists, and military personnel globally with an aim to get unauthorized access – not by breaking encryption, but by simply tricking people into handing over the security verification codes or PINs. "The most frequently observed method used by the Russian hackers is to masquerade as a Signal Support chatbot in order to induce their targets to divulge their codes," the Netherlands Defence Intelligence and Security Service (MIVD) and the General Intelligence and Security Service (AIVD) [said](https://english.aivd.nl/latest/news/2026/03/09/russia-targets-signal-and-whatsapp-accounts-in-cyber-campaign). "The hackers can then use these codes to take over the user's account. Another method used by the Russian actors takes advantage of the 'linked devices' function within Signal and WhatsApp." It's worth noting that a similar warning was [issued](https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html) by Germany last month. "These attacks were executed via sophisticated phishing campaigns, designed to trick users into sharing information – SMS codes and/or Signal PIN – to gain access to users' accounts," Signal [said](https://x.com/i/status/2031038277604585785). Google warned last year that Signal's widespread use among Ukrainian soldiers, politicians, and journalists had made it a frequent target for Russian espionage operations.
3. Cloud breach via software flaws

   [Threat Actors Exploit Flaws in Third-Party Software to Breach Cloud](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026)

   Google has revealed that threat actors are increasingly exploiting vulnerabilities in third-party software to breach cloud environments. "The window between vulnerability disclosure and mass exploitation collapsed by an order of magnitude, from weeks to days," the tech giant's cloud division [said](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026). "While software-based exploits increased, initial access by threat actors using misconfiguration, which accounted for 29.4% of incidents in the first half of 2025, dropped to 21% in H2 2025. Similarly, exposed sensitive UI or APIs continued a downward trend, falling from 11.8% in H1 to 4.9% in H2. This decline suggests that automated guardrails are making identity and configuration errors harder to exploit and that threat actors are being driven toward more sophisticated and costly vectors that specifically target software vulnerabilities to gain a foothold." In most attacks investigated by Go...