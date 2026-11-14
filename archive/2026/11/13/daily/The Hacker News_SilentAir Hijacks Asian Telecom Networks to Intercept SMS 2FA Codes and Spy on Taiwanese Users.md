---
title: SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and Spy on Taiwanese Users
url: https://thehackernews.com/2026/11/silentair-hijacks-asian-telecom.html
source: The Hacker News
date: 2026-11-13
fetch_date: 2026-11-14T08:21:56.746038
---

# SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and Spy on Taiwanese Users

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and Spy on Taiwanese Users](https://thehackernews.com/2026/11/silentair-hijacks-asian-telecom.html)

**Swati Khandelwal**Nov 13, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjskRPNlV_kYE1N2eF2J_J0fBvF_nQxnvtaS78Grj04KqkEauvr-R5jO-ynD9nm51SgF2XtCCAsWUbJrHU0wGRnXC9yHmblhNCF8Jt9NdVahMju3voR2z9xb2uqoSi7Nc085UqDBelqg4XDRdjJ2lsF7EeN28rjq7oBc_NpBUWRqLWXiOh9FBRIH28teHM/s1700-nu-rw-lo-l85-e365/telecom-hack.jpg)

A newly identified spying group used hacked equipment inside Asian mobile operators to intercept the calls and texts of selected people, mostly in Taiwan.

**Enea**, a telecom and cybersecurity software company based in Stockholm, found the group's attack sources in at least six Asian countries and named it SilentAir this week. It assessed with high confidence that **SilentAir** is a state-level actor, but linked its activity to China only with low confidence.

The company has told the operators where it found SilentAir sources. It said SilentAir has been disrupted for now but could return. The report does not say whether those operators have cleaned up the hacked equipment.

Mobile operators use the SS7 and Diameter protocols to exchange signaling messages that route calls and texts and enable roaming. This traffic crosses a shared network called the **IPX**, which runs on a high level of trust between operators. SilentAir sent its attacks into the IPX from the hacked equipment.

For interception, SilentAir sent the target's home network an UpdateLocation message, or its Diameter equivalent. The message claimed that the hacked equipment was now serving the target's phone. If the home network accepted it, calls and texts for that person would be diverted to the attackers.

Some of these attacks worked. For some targets, the company observed two-factor authentication (2FA) codes being intercepted immediately after the diversion took effect. That points to an attempt to break into other accounts registered to those people.

The report gives no similar evidence for voice calls, and it does not say whether any account was taken over.

Interception made up 18.3% of the attacks the company saw from SilentAir. For a typical surveillance company, the kind of firm behind most signaling attacks, the share was 2.1% in the company's earlier research.

Some targets were political and government VIPs in their own countries. In rare cases, SilentAir equipment in several countries worked together against such targets, which the company said points to a single controller.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The attacks came in bursts, from one or a few subscribers to several thousand over a month, with gaps of up to several months or longer between bursts.

Outside Taiwan, targets were mostly in other Southeast and East Asian networks, and at times in East Africa, Central Asia, the Middle East, and Europe. People using the hacked operators' own networks may also have been targeted, but the company could not see that traffic.

The company spotted SilentAir by studying attacks on the links between operators. Since early 2025, it has tracked unusual attacks, mostly over SS7 and sometimes Diameter, from some Asian operators that would not normally send attacks. Later analysis found suspicious activity even earlier.

The networks hosting SilentAir handled follow-up messages for diverted targets in odd and inconsistent ways, according to the company's [technical report](https://www.enea.com/insights/the-enemy-within-tracking-liminal-panda-and-silentair-through-mobile-networks/). That left two explanations: someone outside was faking those networks' signaling addresses, or equipment inside each network had been taken over.

The company then saw equipment inside one operator both send and receive attack commands, which confirmed the second explanation. That equipment behaved exactly like SilentAir sources in other networks.

Detecting and blocking the attacks was hard at first because the attackers understood mobile networks and signaling defenses well. After the attacks were contained, the company recovered traces of unauthorized access. It could not analyze the malware it believes SilentAir used.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFMhT7ce7NKYGnmqLW5ic51dTUbeKkAAJUIzDmPeJJslXxPI1SeslE70rc0v6Na_ddq62vcLZSCY9_G159fXchXdCIC23TIh19QyToZW9GAYRQCmFPUnYpBzF2hRp9SK4G39OApsHOtdyWgQFsr3KH3rtp-MtMuRuGOnS5bp1p93KB48WoGoNtw7p57Hs/s1700-nu-rw-lo-l85-e365/sms.jpg)

The report does not name the countries, the operators, or any of the targets. In some countries, SilentAir attacks came from more than one operator.

SilentAir also sent silent SMS on a very large scale, mainly to subscribers in Taiwan. These are texts that the phone does not display or alert on.

During the day, most silent SMS went to subscribers on other networks, such as Southeast Asian networks. One of their main uses appears to have been checking whether a diversion had worked, the company said.

If the test text reached the hacked equipment instead of the phone, the attackers knew they were getting that person's texts.

Most silent SMS went out at night, and most of those went to people in Taiwan. The company said the purpose of those messages is not confirmed. They may be a bulk check that earlier diversions were still in place, since phones are least likely to re-register to their real location at night.

The silent texts carried spam-like motivational or promotional lines, often in English. The company believes the text was a disguise. If an operator along the way stripped a message's silent setting, the recipient would see it as spam and ignore it.

The company's low-confidence link to China rests on several signs. SilentAir focused on Taiwan and did not target Chinese networks or subscribers.

Its...