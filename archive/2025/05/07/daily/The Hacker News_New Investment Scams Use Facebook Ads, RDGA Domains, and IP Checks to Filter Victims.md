---
title: New Investment Scams Use Facebook Ads, RDGA Domains, and IP Checks to Filter Victims
url: https://thehackernews.com/2025/05/new-investment-scams-use-facebook-ads.html
source: The Hacker News
date: 2025-05-07
fetch_date: 2025-10-06T22:30:53.398848
---

# New Investment Scams Use Facebook Ads, RDGA Domains, and IP Checks to Filter Victims

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

# [New Investment Scams Use Facebook Ads, RDGA Domains, and IP Checks to Filter Victims](https://thehackernews.com/2025/05/new-investment-scams-use-facebook-ads.html)

**May 06, 2025**Ravie LakshmananDeepfake / Online Fraud

[![New Investment Scams](data:image/png;base64... "New Investment Scams")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieSsP9cLL2nqy5d-ow2xBTm3tn-0WNPg1jPMHyrVfv0FaCTG1mAe2d-OUhNyGKFwwgQNYsaZjN88V31UGCeKAFU7Iv4ejlC2Qx7WRthoD0bhXOa9-PVmLgdpQbmFOmJnxGx5bgu7DRmrDJvKDFEHkr67VW1fBZPF2HPzw4ZXGUyWN4_KnN__pwqVa_WSFW/s790-rw-e365/scams.jpg)

Cybersecurity researchers have lifted the lid on two threat actors that orchestrate investment scams through spoofed celebrity endorsements and conceal their activity through traffic distribution systems (TDSes).

The activity clusters have been codenamed Reckless Rabbit and Ruthless Rabbit by DNS threat intelligence firm Infoblox.

The attacks have been observed to lure victims with bogus platforms, including cryptocurrency exchanges, which are then advertised on social media platforms. An important aspect of these scams is the use of web forms to collect user data.

"Reckless Rabbit creates ads on Facebook that lead to fake news articles featuring a celebrity endorsement for the investment platform," security researchers Darby Wise, Piotr Glaska, and Laura da Rocha [said](https://blogs.infoblox.com/threat-intelligence/uncovering-actor-ttp-patterns-and-the-role-of-dns-in-investment-scams/). "The article includes a link to the scam platform which contains an embedded web form persuading the user to enter their personal information to 'register' for the investment opportunity."

Some of these forms, besides requesting users' names, phone numbers, and email addresses, offer the ability to auto-generate a password, a key piece of information that's used to progress to the next phase of the attack -- validation checks.

The threat actors perform HTTP GET requests to legitimate IP validation tools, such as ipinfo[.]io, ipgeolocation[.]io, or ipapi[.]co, in order to filter out traffic from countries that they are not interested in. Checks are also carried out to ensure that the provided numbers and email addresses are authentic.

Should the user be deemed worthy of exploitation, they are subsequently routed through a TDS that either takes them directly to the scam platform where they are coaxed into parting with their funds by promising high returns, or to a different page that instructs them to wait for a call from their representative.

"Some campaigns use call centers to provide the victims with instructions on how to set up an account and transfer money into the fake investment platform," the researchers explained. "For users who do not pass the validation step, many campaigns will simply display a 'thank you' landing page."

An important aspect of the activity is the use of a registered domain generation algorithm ([RDGA](https://thehackernews.com/2024/07/new-linux-variant-of-play-ransomware.html)) to set up domain names for the sketchy investment platforms, a technique also adopted by other threat actors like Prolific Puma, Revolver Rabbit, and VexTrio Viper.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Unlike traditional domain generation algorithms (DGAs), RDGAs make use of a secret algorithm to register all the domain names. Reckless Rabbit is said to have been creating domains as far back as April 2024, primarily targeting users in Russia, Romania, and Poland, while excluding traffic from Afghanistan, Somalia, Liberia, Madagascar, and others.

The Facebook ads used to direct users to the fake news articles are interspersed with advertising content related to items listed for sale on marketplaces like Amazon in a bid to evade detection and enforcement action.

What's more, the ads contain unrelated images and display a decoy domain (e.g., "amazon[.]pl") that's different from the actual domain the user will be redirected to once they click on the link (e.g., "tyxarai[.]org").

Ruthless Rabbit, on the other hand, is believed to have been actively running investment scam campaigns since at least November 2022 that are aimed at Eastern European users. What sets this threat actor apart is that they run their own cloaking service ("mcraftdb[.]tech") to perform validation checks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvhjP4LH_i9LR6I0zNq9C2VVMbgFZci1zApOCoUSeAn_KyF5wVBjs8kSUmpQaS6xMt-iO57jfTcJqh9mCqv7tatHnUfXNm-iFhQAdwkub9Mm4wUNHM3mYqBPo4rZbwC-AUFDj8ddvxh5nDqPz4upTugYrr55DpCq-W6DDOIOjw48KUI8poEe4AXsyExdVi/s790-rw-e365/facebook.png)

Users who get past the verification checks are subsequently routed to an investment platform where they are urged to enter their financial information to complete the registration process.

"A TDS enables threat actors to strengthen their infrastructure, making it more resilient by providing the ability to hide malicious content from security researchers and bots," Infoblox said.

This is not the first time such fraudulent investment scam campaigns have been discovered in the wild. In December 2024, ESET [exposed](https://thehackernews.com/2024/12/new-investment-scam-leverages-ai-social.html) a similar scheme dubbed Nomani that uses a combination of social media malvertising, company-branded posts, and artificial intelligence (AI) powered video testimonials featuring famous personalities.

Then last month, Spanish authorities [revealed](https://thehackernews.com/2025/04/weekly-recap-windows-0-day-vpn-exploits.html) they have arrested six individuals aged between 34 and 57 for allegedly running a large-scale cryptocurrency investment scam that used AI tools to generate deepfake ads featuring popular public figures to deceive people.

Renee Burton, vice president of threat intelligence at Infoblox, told The Hacker News that they "would have to take a closer look to see if there is any evidence" to ascertain if there are any connections ...