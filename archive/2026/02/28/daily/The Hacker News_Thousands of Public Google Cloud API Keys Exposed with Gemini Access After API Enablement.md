---
title: Thousands of Public Google Cloud API Keys Exposed with Gemini Access After API Enablement
url: https://thehackernews.com/2026/02/thousands-of-public-google-cloud-api.html
source: The Hacker News
date: 2026-02-28
fetch_date: 2026-03-01T04:28:18.474279
---

# Thousands of Public Google Cloud API Keys Exposed with Gemini Access After API Enablement

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Thousands of Public Google Cloud API Keys Exposed with Gemini Access After API Enablement](https://thehackernews.com/2026/02/thousands-of-public-google-cloud-api.html)

**Ravie Lakshmanan**Feb 28, 2026Generative AI / API Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1wA-JoARjvd0BYW-3G0XMdHXcWpWdkWk3bIkWV2myMGfRRsp4Dl8A24cpj8Elpe5lJO6KdyS36Nsts7_o0Xx70HSxwY3se4RuNPRzfFmodMhX-jU_lkCefaathP6uan4UGLWmuQvxjerq6_H-z16vFY3h4pCeVqDBGA13ne12uRZfuU7fHW2pQVAtuM4E/s1700-e365/gemini.jpg)

New research has found that Google Cloud API keys, typically designated as project identifiers for billing purposes, could be abused to authenticate to sensitive Gemini endpoints and access private data.

The findings come from Truffle Security, which discovered nearly 3,000 Google API keys (identified by the prefix "AIza") embedded in client-side code to provide Google-related services like embedded maps on websites.

"With a valid key, an attacker can access uploaded files, cached data, and charge LLM-usage to your account," security researcher Joe Leon [said](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules), adding the keys "now also authenticate to Gemini even though they were never intended for it."

The problem occurs when users enable the Gemini API on a Google Cloud project (i.e., Generative Language API), causing the existing API keys in that project, including those accessible via the website JavaScript code, to gain surreptitious access to Gemini endpoints without any warning or notice.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

This effectively allows any attacker who scrapes websites to get hold of such API keys and use them for nefarious purposes and quota theft, including accessing sensitive files via the /files and /cachedContents endpoints, as well as making Gemini API calls, racking up huge bills for the victims.

In addition, Truffle Security found that creating a new API key in Google Cloud defaults to "Unrestricted," meaning it's applicable for every enabled API in the project, including Gemini.

"The result: thousands of API keys that were deployed as benign billing tokens are now live Gemini credentials sitting on the public internet," Leon said. In all, the company said it found 2,863 live keys accessible on the public internet, including a website associated with Google.

The disclosure comes as Quokka published a similar report, finding over 35,000 unique Google API keys embedded in its scan of 250,000 Android apps.

"Beyond potential cost abuse through automated LLM requests, organizations must also consider how AI-enabled endpoints might interact with prompts, generated content, or connected cloud services in ways that expand the blast radius of a compromised key," the mobile security company [said](https://www.quokka.io/blog/google-gemini-api-key-mobile-app-security-risk).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5pyZ_EYzPi4PE_N1tIG2N9b99Jg124o2aWv5woBnHqP2Sf9hIs31_qfq16vyDDetDKx827vNWUBsSCoR7xOcyQMm1662CcUyILn6s876XZRaU2HW3ioLJls3SYAK6YJ1wtxhh4ivTIALyMf9FC3PirbRFLi_H0yWGo94tU9Qri8WHWNFYCPnLDYCXU4b_/s1700-e365/api.jpg)

"Even if no direct customer data is accessible, the combination of inference access, quota consumption, and possible integration with broader Google Cloud resources creates a risk profile that is materially different from the original billing-identifier model developers relied upon."

Although the behavior was initially deemed intended, Google has since stepped in to address the problem.

"We are aware of this report and have worked with the researchers to address the issue," a Google spokesperson told The Hacker News via email. "Protecting our users' data and infrastructure is our top priority. We have already implemented proactive measures to detect and block leaked API keys that attempt to access the Gemini API."

It's currently not known if this issue was ever exploited in the wild. However, in a [Reddit post](https://www.reddit.com/r/googlecloud/comments/1reqtvi/82000_in_48_hours_from_stolen_gemini_api_key_my/) published two days ago, a user claimed a "stolen" Google Cloud API Key resulted in $82,314.44 in charges between February 11 and 12, 2026, up from a regular spend of $180 per month.

We have reached out to Google for further comment, and we will update the story if we hear back.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Users who have set up Google Cloud projects are advised to check their APIs and services, and verify if artificial intelligence (AI)-related APIs are enabled. If they are enabled and publicly accessible (either in client-side JavaScript or checked into a public repository), make sure the keys are rotated.

"Start with your oldest keys first," Truffle Security said. "Those are the most likely to have been deployed publicly under the old guidance that API keys are safe to share, and then retroactively gained Gemini privileges when someone on your team enabled the API."

"This is a great example of how risk is dynamic, and how APIs can be over-permissioned after the fact," Tim Erlin, security strategist at Wallarm, said in a statement. "Security testing, vulnerability scanning, and other assessments must be continuous."

"APIs are tricky in particular because changes in their operations or the data they can access aren't necessarily vulnerabilities, but they can directly increase risk. The adoption of AI running on these APIs, and using them, only accelerates the problem. Finding vulnerabilities isn't really enough for APIs. Organizations have to profile behavior and data access, identifying anomalies and actively blocking malicious activity."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaF...