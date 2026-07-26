---
title: Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE
url: https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
source: The Hacker News
date: 2026-07-25
fetch_date: 2026-07-26T05:24:36.887312
---

# Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE

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

# [Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE](https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html)

**Ravie Lakshmanan**Jul 25, 2026Vulnerability / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIGAlXgFCqm8atTe__HpWBiCWISmrPOazxOVBMF-_YNrP2goBbW_4PSwGzw1Ndyue4qrnQnqrQyAR4DTaAdaiJPlVUZi7M_iceb4fqofWK0sGRLO9CHnj0lngtxdlC-tKqrppqFaKIkct2vOtGn_o5kbNa4fj-dutt8PMjiO5TVBw895aLg0TOJb8TKKtv/s1700-e365/cyberattack.jpg)

Threat actors linked to the Cl0p (aka Chubby Scorpius, FIN11, Graceful Spider, and Lace Tempest) ransomware campaign are exploiting flaws in internet-exposed PTC Windmill and FlexPLM deployments as part of a new data extortion campaign.

"Attackers chain a pre-authentication information disclosure in the FlexPLM WSDL endpoint with a server-side flaw in the Windchill login servlet, enabling unauthenticated remote code execution and deployment of hex-named JSP web shells under /Windchill/login/," according to a [new coordinated advisory](https://ransom-isac.org/blog/clop-windchill-flexplm-exploitation/) released by Ransom-ISAC along with eCrime.ch and DEFUSED.

Upon gaining an initial foothold, the attackers have been found to conduct file system enumeration, stage engineering/design data, and ultimately carry out double extortion data theft. Targets of the campaign include manufacturing, automotive, aerospace, and retail sectors.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

It's suspected that threat actors are exploiting [CVE-2026-12569](https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html) (CVSS score: 9.3), a critical security flaw in PTC Windmill that was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog late last month.

In an advisory, PTC warned customers that it had "received continued reports of heightened threat activity," adding that unknown attackers are exploiting the vulnerability to deploy JSP web shells against susceptible systems.

"In the observed intrusions, this RCE is chained with a separate pre-authentication information-disclosure defect in the FlexPLM WSDL endpoint (CVSS v3.1 7.5) to enable unauthenticated exploitation," researchers Brandon Parsons, Corsin Camichel, and Simo Kohonen said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9dZ5B11XJlJI6oMNpf8I9ElyXWaUM247KIe3hyphenhyphenS2QYRblxjZpmf7NNsmo4mBeEIK4KsaalynHmyDSZ-l7d4bQjJ_YuaqhHYhwUgvg4MpLofVUlUy7Sl2AGMtkQRWBRA9Ep_fi6wYMs9j03sL9oMKCSbsG1SULGvxWhCsr4Mf2jq0D7yOIdWormoiR-8D1/s1700-e365/data.png)

Ransom-ISAC has shared four IP addresses as indicators of compromise (IoCs), all of which match those shared by PTC -

* 216.152.148.54
* 216.152.151.204
* 104.243.35.63
* 5.180.41.35

The extortion emails appear to originate from previously compromised accounts and are sent to hundreds of users within an impacted organization, along with ways to contact the Cl0p ransomware crew.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

In a separate post on X, ReliaQuest said it observed threat actors actively exploiting CVE-2026-12569 to facilitate "unauthenticated remote code execution and JSP web shell deployment for remote command execution and sensitive product data exfiltration."

"The actor behind these attacks remains unconfirmed. However, the observed tradecraft shares characteristics with previous Cl0p campaigns targeting enterprise applications and high-value data repositories," it [added](https://x.com/ReliaQuestTR/status/2079963221365055890).

The Cl0p gang has a storied history of going after security flaws in widely-used enterprise products to break into target organizations for data theft and extortion attacks. Previous campaigns mounted by the group have weaponized [file transfer appliances](https://thehackernews.com/2025/10/cl0p-linked-hackers-breach-dozens-of.html), including those from Accellion FTA, GoAnywhere MFT, SolarWinds Serv-U FTP, Cleo, and MOVEit Transfer, as well as a vulnerability in [Oracle E-Business Suite](https://thehackernews.com/2025/10/oracle-ebs-under-fire-as-cl0p-exploits.html).

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Cyber Crime](https://thehackernews.com/search/label/Cyber%20Crime), [data breach](https://thehackernews.com/search/label/data%20breach), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Malware](https://thehackernews.com/search/label/Malware), [ransomware](https://thehackernews.com/search/label/ransomware), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Inte...