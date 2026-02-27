---
title: Malicious StripeApi NuGet Package Mimicked Official Library and Stole API Tokens
url: https://thehackernews.com/2026/02/malicious-stripeapi-nuget-package.html
source: The Hacker News
date: 2026-02-26
fetch_date: 2026-02-27T04:08:49.825140
---

# Malicious StripeApi NuGet Package Mimicked Official Library and Stole API Tokens

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

# [Malicious StripeApi NuGet Package Mimicked Official Library and Stole API Tokens](https://thehackernews.com/2026/02/malicious-stripeapi-nuget-package.html)

**Ravie Lakshmanan**Feb 26, 2026Malware / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOOA0ov4ywkdj7FrYHif0WbJFrQ04THhkLcOL83R7ggXvtpTTMUeO8-3e-YOobbh_5hGpdNbnXr1pbeU4Uj1DfBd7HLLefvr3fbmKeNnmxknerJm4TDUvvNUL1uJT0MN5frpDoVizcBh5KuEtiU-zq2rhZhZmLJ3iVOauRaHqBUf3k5DnZU8MUq7WHE8fX/s1700-e365/Stripe-malware.jpg)

Cybersecurity researchers have disclosed details of a new malicious package discovered on the NuGet Gallery, impersonating a library from financial services firm Stripe in an attempt to target the financial sector.

The package, codenamed StripeApi.Net, attempts to masquerade as [Stripe.net](https://www.nuget.org/packages/Stripe.net), a legitimate library from Stripe that has over 75 million downloads. It was uploaded by a user named StripePayments on February 16, 2026. The package is no longer available.

"The NuGet page for the malicious package is set up to resemble the official Stripe.net package as closely as possible," ReversingLabs Petar Kirhmajer [said](https://www.reversinglabs.com/blog/malicious-nuget-package-targets-stripe). "It uses the same icon as the legitimate package and contains a nearly identical readme, only swapping the 'Stripe.net' references to read 'Stripe-net.'"

In a further effort to lend credibility to the typosquatted package, the threat actor behind the campaign is said to have artificially inflated the download count to more than 180,000. But in an interesting twist, the downloads were split across 506 versions, with each version recording about 300 downloads on average.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The package replicates some of the legitimate Stripe package's functionality, but also modifies certain critical methods to collect and transfer sensitive data, including the user's Stripe API token, back to the threat actor. With the rest of the codebases remaining fully functional, it's unlikely to attract any suspicion from unsuspecting developers who may have inadvertently downloaded it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbROWVosq-ggoRuYIJWpLozaQMgJDHVsecZlsLbWWqOkwSo9tuf2wPuM0sv9eNOXQdzlTOh23TigMEW_cleAnk1zC8hhL2JMjBEwu5rRBQttUwQrmzWv3LoJn15NlmmNI550JbUjH6-W4YJExodZjsdJeOYWm3t1afLRMZKILrUEFyc7OyH7k3MmfCb047/s1700-e365/Stripe.jpg)

ReversingLabs said it discovered and reported the package "relatively soon" after it was initially released, causing it to be taken before it could inflict any serious damage.

The software supply chain security company also noted that the activity marks a shift from [prior campaigns](https://thehackernews.com/2025/10/fake-nethereum-nuget-package-used.html) that have leveraged [bogus NuGet packages](https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html) to target the cryptocurrency ecosystem and facilitate wallet key theft.

"Developers who mistakenly download and integrate a typosquatted library like StripeAPI.net will still have their applications compile successfully and function as intended," Kirhmajer said. "Payments would process normally and, from the developer’s perspective, nothing would appear broken. In the background, however, sensitive data is being secretly copied and exfiltrated by malicious actors."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Malware](https://thehackernews.com/search/label/Malware), [NuGet](https://thehackernews.com/search/label/NuGet), [Open Source](https://thehackernews.com/search/label/Open%20Source), [software security](https://thehackernews.com/search/label/software%20security), [Stripe](https://thehackernews.com/search/label/Stripe), [supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack), [typosquatting](https://thehackernews.com/search/label/typosquatting)

Trending News

[![OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](data:image/svg+xml;base64... "OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond")

OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](https://thehackernews.com/expert-insights/2026/01/ot-security-in-practice-4-crossindustry.html)

[![Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools](data:image/svg+xml;base64... "Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools")

Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools](https://thehackernews.com/2026/02/reynolds-ransomware-embeds-byovd-driver.html)

[![Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days](data:image/svg+xml;base64... "Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days")

Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days]...