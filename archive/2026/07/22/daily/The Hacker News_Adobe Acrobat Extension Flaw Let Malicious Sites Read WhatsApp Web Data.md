---
title: Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data
url: https://thehackernews.com/2026/07/adobe-acrobat-extension-flaw-let.html
source: The Hacker News
date: 2026-07-22
fetch_date: 2026-07-23T05:11:47.495972
---

# Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data](https://thehackernews.com/2026/07/adobe-acrobat-extension-flaw-let.html)

**Ravie Lakshmanan**Jul 22, 2026Vulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhf4tAo-p42ED3dQRVz6O7qldcTuY-ztwtPbNnnJFBHd-yJDm2dJmYNPtprB3IFhF9-7xExM_6jzqElcEotSZPEXwVYoiqG7Wh6isEjRAZkqzIyL4TYXUL3pK8hp53PdCHotDcUAZ9LVCJLDPX3PPZqDKIaFDlTnB5MbaRH0-ohMCzBAmdRDC_E6O5rGUtd/s1700-e365/adobe.jpg)

Cybersecurity researchers have disclosed details of a [now-patched vulnerability chain](https://helpx.adobe.com/security/acknowledgements.html) in the Adobe Acrobat Chrome extension that has over 314 million users, which, if exploited, could facilitate a silent hijack of a user's WhatsApp data.

The shortcoming has been codenamed **[HermeticReader](https://guard.io/labs/hermeticreader---the-vulnerability-that-turned-adobe-300m-install-extension-into-a-full-whatsapp-takeover)** by Guardio Labs. It's officially tracked as [CVE-2026-48294](https://nvd.nist.gov/vuln/detail/CVE-2026-48294) (CVSS score: 7.4), with the vulnerability described as a case of universal cross-site scripting (UXSS)-class cross-origin data disclosure vulnerability. It affects all versions of the extension (ID: [efaidnbmnnnibpcajpcglclefindmkaj](https://chromewebstore.google.com/detail/adobe-acrobat-pdf-edit-co/efaidnbmnnnibpcajpcglclefindmkaj)) prior to and including 26.5.2.2.

Successful exploitation of the flaw can bypass the browser's same-origin policy and access data linked to the victim's session across origins. The only prerequisite is that it requires user interaction. A victim must be convinced into visiting a maliciously crafted URL or interact with a compromised web page that triggers the extension's vulnerable code path.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

In other words, an attacker can weaponize the flaw to obtain cross-origin read access to session-bound data. This can include authenticated content from third-party web applications loaded in the victim's browser.

"The setup is almost insultingly ordinary: an attacker-controlled page, dressed to look like the kind of page you land on via search results, marketing emails, etc.," Guardio Labs researcher Shaked Biner said in a report shared with The Hacker News. "The visitor, who already has the Adobe Acrobat extension installed, opens that page."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjV5x93BfMl_Y4aEIw0hipVIoutSTQvI2tjJ1QuTOB_G31vO4eqzAZMuVFw2FJwriQaPzh1KVoSKlweHPZ6Z8rFyTZn5F__id3NsOfFU27oVyjfmroYPEZAst-eOHbsMoUXUCNBj8R6cxre_YbWoz0VazGrBl0L4B1jcqrVWFil05dXRDPgZ196JrctfoXk/s1700-e365/whatsapp-chain.jpg)

"The page wakes up a dormant engine inside the extension, reaches directly into WhatsApp Web. Seconds later, the rendered WhatsApp Web view - the chat list, contact names, messages, the profile name, the text of whatever conversation is open - the whole WhatsApp in the attacker's hands."

What's notable about the flaw is that it does not require a bad actor to install malware through some other means, phish a user's credentials, or extract their session cookie. All it needs is for the victim to visit the crafted web page.

The entire sequence of actions is as follows -

* An attacker-controlled page calls an iframe element loaded from the extension resources.
* The iframe sends commands to alter settings to activate the Hermes engine, which handles WhatsApp integration in the extension only if a specific feature flag is enabled ("floodgate-add").
* The attacker page opens WhatsApp Web in a browser tab in the background.
* The iframe sends commands directly to the engine directed against the WhatsApp tab after obtaining the tab's numeric ID.
* The engine manipulates WhatsApp Web's by injecting a POST form into WhatsApp's DOM to steal WhatsApp data.

"Why does submitting a form carry chat text out of WhatsApp's origin? Two enablers deep from the HTML specifications: An option element with no value attribute submits its text content - and the text content of a node is the concatenation of everything rendered beneath it," Biner explained. "Move the live body in, and the option's submitted value becomes the entire rendered page text!"

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

"The second enabler is that WhatsApp Web's content security policy that ships no form-action directive, and per the spec that absence means a top-level form submission may navigate to any origin. So WhatsApp itself performs the navigation, POSTing its own rendered DOM to our controlled endpoint and then dutifully rendering whatever we send back."

As a result, a threat actor can exploit HermeticReader to capture the rendered chat list, contact names, message previews, the profile name, and the visible text of the open conversation.

"The industry pours its attention into the dramatic exploit classes and leaves the plumbing to the assumption that nobody will ever look hard at it," Guardio concluded. "Composition is the threat. Plumbing-level flaws compose into building-level collapse, and the bigger the install base, the longer the building stands before anyone checks the joints."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#li...