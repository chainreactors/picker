---
title: An AI Agent Found a Critical OTP Bypass in Production. The Attack Was the Easy Part.
url: https://thehackernews.com/2026/10/an-ai-agent-found-critical-otp-bypass.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:39.726081
---

# An AI Agent Found a Critical OTP Bypass in Production. The Attack Was the Easy Part.

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

# [An AI Agent Found a Critical OTP Bypass in Production. The Attack Was the Easy Part.](https://thehackernews.com/2026/10/an-ai-agent-found-critical-otp-bypass.html)

**The Hacker News**Oct 14, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_bop9V2vtfHPW4Obd0zupOPpNFCd9N5HtVwWVs9u-njx8RuEgOkAh75uRjWLS_h3zHQ847m7xc01PkVAdKhyphenhyphen5Pkg2Pb_qthWVQe-9lcpKclCOq3ZDpQ2iSfRSFCQQU8gxyBl6lWEjTKWZHn9LiNSq2rQ4_nUIM6Sjcqv5fwgVRnFpiuxpYDfhrkbikLE/s1700-nu-rw-lo-l85-e365/case.jpg)

*The bug was simple: the login let you choose where your sign-in code went. Proving it on a live website was the hard part.*

## **TL;DR**

* During an authorized assessment, an AI pentesting agent found a critical authentication bypass on a major insurer's production website, on its own.
* One login request let the user choose where the one-time passcode went.
* The attack was the easy part. Proving it on a live site took web context built over a decade.

## **The Login Worked. Then the Agent Stopped.**

Reflectiz's [AI pentesting agent](https://www.reflectiz.com/lp/agentic-pentesting/?utm_source=thehackernews&utm_medium=sponsored&utm_campaign=otp-case-study&utm_content=intro) was mapping the login flow of a major insurer's production website, which has millions of users.

The agent requested a login code and directed it to an email inbox it controlled. The code arrived. The login went through. Its guardrails halted the test after the login succeeded.

The agent had discovered a critical-severity authentication bypass on its own. Reflectiz reported it to the insurer.

## **The Flaw: The Request Chose Where the Code Went**

A one-time passcode (OTP) only proves who you are if it goes somewhere already linked to the account. Here, that link was broken.

The login request carried two fields that decided delivery: the channel and the address. Normally, the code went by text to the phone number on the account. But the request could change the channel. Switch it to email, and the server sent the code to whatever address the request named, not the address registered to the account.

Simplified, the request looked like this:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijgI_rdPwvRTCShUgC6caWgYK9d_Ie2xE1COPSv58ic2qYIc7cSLF3JcZ_w-M-rNnkVQjCQOYdSVeZjDrSyaQtZog9XqeXT1XN4zem1MVRn5DDR7XIldx5a3n7Te1ociujNbpP8gPHTAXpEfp2Wq3LW-nd0W2XJvrPJ3AtTPfKtZ_vEmdEDBRODxeW3ws/s1700-nu-rw-lo-l85-e365/1.png)

The server never checked that the address belonged to the account.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqNH_rsJIqXSRoPk8jocJBj-sd0KhsKwl3qlwjwAg0Hg_FmRTDCYtQbR51PE_QN1FlRCbszeG_YlR1kreXj8gIg93keBKir4nKGrcpi3tRrPlJn5IkRbu4BARhQ50EaICEfsMCueRF00s_iWtvlhRFjbKEmwHEobbnTDydh8eWEAx4tvd8fzyUTpcFU50/s1700-nu-rw-lo-l85-e365/2.png)

Binding a code to its account is one of the most basic checks in authentication. OWASP's testing guide asks this in plain words: "Are the OTPs tied to the correct user account...?"

An attacker with the required customer identifiers could potentially use the flaw to access that customer's account.

## **From a Suspicious Field to a Proven Bypass**

The agent began with reconnaissance, looking at the site's JavaScript and the API calls behind its pages. That analysis surfaced the OTP request and two values that appeared to control how and where the code was sent. Values like those can suggest a hypothesis, but they’re not a finding, since the server might reject the changes or block them later in the login. So the agent built a targeted test around both values and ran it through the live login flow, which confirmed the bypass.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEht3rpoINCL5nqrkfJGHFlUJz0zvzPP1Lndk_vG6-aMlP8jYQsHvyLYAeT8SJ9v7gt7Knuzgdzdli7c1eK3MZ3wePUt68ocfcJ4G3XcxDe1si-6j2sdImkPAsOasLGV2FalOui5wNRkUZdNtx1cawh93dLhyphenhyphensxo3U5rP18GhXF7G27fU0x-SyWDvjNItd8/s1700-nu-rw-lo-l85-e365/3.png) |
| Illustration of the authenticated state the agent reached before stopping. Recreated and anonymized. |

**Want to see how that testing process works?** [Book a technical demo](https://www.reflectiz.com/lp/agentic-pentesting/?utm_source=thehackernews&utm_medium=sponsored&utm_campaign=otp-case-study&utm_content=mid) to examine how Reflectiz investigates website workflows, validates findings, and controls execution.

## **Web Context Is the Hard Part**

Plenty of automated testing stops at the login gate, but much of what matters sits behind it. A testing system that cannot reach a workflow cannot assess what happens inside it.

Reflectiz solved that problem long before the agent existed. The company has spent more than a decade scanning thousands of production websites, which meant logging in, receiving verification codes, and navigating multi-step flows. So, on sites the company already monitors, the agent starts with that context instead of a blank URL.

Reflectiz's agentic pentesting puts that web context to work. It drives a real browser through the flows a customer follows, including one-time passcodes and 2FA.

Reflectiz CTO and co-founder Ysrael Gurt, a longtime ethical hacker, built the agent on that foundation.

## **One Finding Is Not a Coverage Report**

A confirmed vulnerability may show what failed, but it doesn’t show how much of the application was tested.

The OTP test ran alongside other attack plans on the same site. Reflectiz's agentic pentesting pairs that open-ended investigation with a structured plan: test every discovered endpoint against every applicable attack category. A separate validator agent reproduces each suspected finding with the same payload and context before it is reported.

The output is a coverage record of which tests ran, their recorded outcomes, and any exclusions.

## **Pentested Is Not the Same as Secure**

The ...