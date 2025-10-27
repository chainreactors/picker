---
title: AI Tools Fuel Brazilian Phishing Scam While Efimer Trojan Steals Crypto from 5,000 Victims
url: https://thehackernews.com/2025/08/ai-tools-fuel-brazilian-phishing-scam.html
source: The Hacker News
date: 2025-08-09
fetch_date: 2025-10-07T00:49:50.658948
---

# AI Tools Fuel Brazilian Phishing Scam While Efimer Trojan Steals Crypto from 5,000 Victims

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [AI Tools Fuel Brazilian Phishing Scam While Efimer Trojan Steals Crypto from 5,000 Victims](https://thehackernews.com/2025/08/ai-tools-fuel-brazilian-phishing-scam.html)

**Aug 08, 2025**Ravie LakshmananCryptocurrency / SEO Poisoning

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggchS-BbVWHLvBpjp1ksu2Qo6nqMJ8eVIVjlkVd0U2It_w6C84pLdDo09r3D5nXjNqJ6_vZSmIxXdP95RsxSiBGmxHD6rcNgAF-pOFaF9kXWpFIppbjhvavwPVEbO214f41PE-6s-VIjZHBZBNLlf2LIoCS5MuzgCroaCTRkeKPsg6MzQxeNCkVdPHsBFi/s790-rw-e365/brazil-malware.jpg)

Cybersecurity researchers are drawing attention to a new campaign that's using legitimate generative artificial intelligence (AI)-powered website building tools like DeepSite AI and BlackBox AI to create replica phishing pages mimicking Brazilian government agencies as part of a financially motivated campaign.

The activity involves the creation of lookalike sites imitating Brazil's State Department of Traffic and Ministry of Education, which then trick unsuspecting users into making unwarranted payments through the country's PIX payment system, Zscaler ThreatLabz said.

These fraudulent sites are artificially boosted using search engine optimization (SEO) poisoning techniques to enhance their visibility, thereby increasing the likelihood of success of the attack.

"Source code analysis reveals signatures of generative AI tools, such as overly explanatory comments meant to guide developers, non-functional elements that would typically work on an authentic website, and trends like TailwindCSS styling, which is different from the traditional phishing kits used by threat actors," Zscaler's Jagadeeswar Ramanukolanu, Kartik Dixit, and Yesenia Barajas [said](https://www.zscaler.com/blogs/security-research/genai-used-phishing-websites-impersonating-brazil-s-government).

The end goal of the attacks is to serve bogus forms that collect sensitive personal information, including Cadastro de Pessoas Físicas (CPF) numbers, Brazilian taxpayer identification numbers, residential addresses, and convince them to make a one-time payment of 87.40 reals ($16) to the threat actors via PIX under the guise of completing a psychometric and medical exam or securing a job offer.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

To further increase the legitimacy of the campaign, the phishing pages are designed such that they employ staged data collection by progressively requesting additional information from the victim, mirroring the behavior of the authentic websites. The collected CPF numbers are also validated on the backend by means of an API created by the threat actor.

"The API domain identified during analysis is registered by the threat actor," Zscaler said. "The API retrieves data associated with the CPF number and automatically populates the phishing page with information linked to the CPF."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiupbX8uvEQ3e9-qI1B_sBFc8EgCdqGho-gIgFRBIiIYU35m6viyyzC3axb0FB2ZTBtsrhPWMYDw6UgyWA9UYuFWPZsKsmN6ilw1wceO6aQ9vomquCLHhFk3hnwIJcqum7_tf2CT2iyNUMJv_3HPx-i4mWeG214WiHghjV88PtWanD-oS7Ls60QyVyGeEha/s790-rw-e365/ai-zz.jpg)

That said, the company noted that it's possible the attackers may have acquired CPF numbers and user details through data breaches or by leveraging publicly exposed APIs with an authentication key, and then used the information to increase the credibility of their phishing attempts.

"While these phishing campaigns are currently stealing relatively small amounts of money from victims, similar attacks can be used to cause far more damage," Zscaler noted.

## Mass Mailing Campaign Distributes Efimer Trojan to Steal Crypto

Brazil has also become the focus of a malspam campaign that impersonates lawyers from a major company to deliver a malicious script called Efimer and steal a victim's cryptocurrency. Russian cybersecurity company Kaspersky said it detected the mass mailing campaign in June 2025, with early iteration of the malware dating all the way back to October 2024 and spread via infected WordPress websites.

"These emails falsely claimed the recipient's domain name infringed on the sender's rights," researchers Vladimir Gursky and Artem Ushkov [said](https://securelist.com/efimer-trojan/117148/). "This script also includes additional functionality that helps attackers spread it further by compromising WordPress sites and hosting malicious files there, among other techniques."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigLyThAKL0ODA_j__9ZhUZIz9Sqdb2DVYgYwkaYeno4ZWkrM6L1T4crpwnYJuW3gcJ3hrpsZ-OzxPwKeuY6qmH7UuZImSlDz77rUCkLrmHxHMaHSjTGWdBwv4k4TZUnbOeLJKVkRf3gwywPdLgcG2z-fDMUhm98Q76aLEooSZY2kQ9yyrV91ukR6qmAmNo/s790-rw-e365/zzz.png) |
| Number of users who encountered Efimer |

Efimer, besides propagating via compromised WordPress sites and email, leverages malicious torrents as distribution vector, while communicating with its command-and-control (C2) server via the TOR network. Furthermore, the malware can extend its capabilities with additional scripts that can brute-force passwords for WordPress sites and harvest email addresses from specified websites for future email campaigns.

"The script receives domains [from the C2 server] and iterates through each one to find hyperlinks and email addresses on the website pages," Kaspersky said, noting it also serves as a spam module engineered to fill out contact forms on target websites.

In the attack chain documented by Kaspersky, the emails come fitted with ZIP archives containing another password-protected archive and an empty file with a name specifying the password to open it. Present within the second ZIP file is a malicious Windows Script File (WSF) that, when launched, infects the machine with Efimer.

At the same time, the victim is displayed an error message stating the document cannot be opened on the device as a distraction mechanism. In ...