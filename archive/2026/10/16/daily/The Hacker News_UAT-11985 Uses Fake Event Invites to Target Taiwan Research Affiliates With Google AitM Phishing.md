---
title: UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates With Google AitM Phishing
url: https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html
source: The Hacker News
date: 2026-10-16
fetch_date: 2026-10-17T06:39:13.743524
---

# UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates With Google AitM Phishing

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates With Google AitM Phishing](https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html)

**Ravie Lakshmanan**Oct 16, 2026Phishing / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPclyw7bJ19im5Qmzj9jgFlsM4XJqPK6hyphenhyphenRDCcQ0bnpWrteeTWgPNlip5T0P_oj_AC6V3osZ2xIpYipKjXWQw3BfFEQ1n28dleNCLRi7difLnPLY8Yc-oJ6BCVZ1V0VBpF_ZNu36qM_yCvyvbgBsSfh2AXq-IBIk7QjnBSR_T7s8ajMCOkIEhA5YGeYWg4/s1700-nu-rw-lo-l85-e365/google-phish.jpg)

Cybersecurity researchers have disclosed details of an advanced persistent threat (APT) spear-phishing campaign that has targeted individuals affiliated with Taiwan research organizations to direct victims to an adversary-in-the-middle (AitM) phishing framework designed to harvest their Google account credentials and multi-factor authentication (MFA) codes.

The activity is being tracked by Cisco Talos under the moniker **UAT-11985**, describing it as likely fueled by artificial intelligence (AI)-assisted content generation so as to quickly craft bespoke lures aimed at different targets within the confines of a common social engineering framework. The campaign was first observed in mid-2026.

"The operation leveraged legitimate public event themes and impersonated reputable academic and policy institutions to establish credibility," Talos researcher Joey Chen [said](https://blog.talosintelligence.com/uat-11985/) in an analysis.

"Beyond traditional email phishing, the actor incorporated QR code phishing (quishing) techniques by modifying legitimate event posters with malicious QR codes, expanding the attack surface beyond email recipients to secondary victims who may encounter printed materials."

Central to the operation is the use of legitimate or plausible public event information in spear-phishing emails and embedding within them a URL that points to attacker-controlled infrastructure, while hovering over the hyperlink displays a legitimate-looking Google Forms URL.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

These invitation emails feature nearly identical syntactic structures despite the breadth of geopolitical topics being discussed, indicating the content was mass-produced from a reusable prompt template rather than painstakingly crafted for each target.

Specifically, the emails follow a three-part structure -

* The opening section offers a "polished (but overly elaborate) description" of the geopolitical or policy context.
* The second section is tailored to the recipient and paints them in a flattering light in an attempt to trigger engagement.
* The third and final section provides details of event logistics, including the topic, date, venue, and registration instructions.

The threat actor has been found to impersonate legitimate Taiwan-based institutions like the Taiwan European Union Centre, NCCU Institute of International Relations, and Taiwan Research Institute, fabricating the sender identities to make the messages appear more convincing.

"Taken together, the reuse of an almost-identical narrative structure, rhetorical style, personalized flattery, institutional impersonation, and deceptive registration mechanism strongly suggests a coordinated and carefully targeted spear-phishing campaign rather than three independent invitations," Talos said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdHO3Er0XfVtdn3shorgjgruguA7DkP828B1DJBSX4Xr3mpLtWO2agxZ6EuPbQEYw-SgiyeRkqfiqEaEG-UHFDrsoj7_TAyODnzZzX5XoEXrlVyCgBLt-xfGVMevpez2agga-8C4nzORFK8GHap1izR8y37YKRQunLLts7YSyHvR6f_8oPbg8P1Wg77hoG/s1700-nu-rw-lo-l85-e365/flow.jpg)

In a subset of cases, the phishing emails incorporate legitimate event posters scraped from legitimate websites, but with the QR codes modified to trick victims into scanning the malicious QR code to "register" for the event.

The phishing site imitates the look of a legitimate Google Form, but the primary goal of the site is to serve a pop-up that prompts the victim to sign-in with their Google account to complete the form. Doing so takes them to a bogus site featuring a spoofed Google login panel to capture their credentials and authentication challenges.

The pixel-perfect replica site is an adversary-in-the-middle (AitM) proxy that uses obfuscated JavaScript to gather and exfiltrate the entered information in real-time over a WebSocket connection, while simultaneously forwarding it to legitimate Google authentication servers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Prior to establishing the WebSocket connection, the JavaScript payload collects device and browser information, including the locale, user agent, screen dimensions, and mobile-device status, which are then reported to the command-and-control (C2) server via a "google\_login\_start" request.

When the victim submits the password, the phishing page transmits the password, along with the account identifier and browser user-agent information, to the actor's HTTP C2 server through a "google\_login\_check" request. The threat actor's server, placed in an AitM position, then forwards the credentials to the actual Google authentication service.

"The spoofed Google login panels only support Simplified Chinese (zh-CN), Traditional Chinese (zh-TW), and English locales, with region detection based on the victim's browser 'navigator.languages,' strongly suggesting targeting of Chinese-speaking users," Chen explained.

"By deliberately splitting one-shot uploads with POST requests from low-latency state updates with WebSocket connection, the threat actor has engineered a seamless credential-harvesting relay. This allows the threat actor to mirror Google's dynamic authentication state in real time, ultimately achieving full account takeover without raising the victim's ...