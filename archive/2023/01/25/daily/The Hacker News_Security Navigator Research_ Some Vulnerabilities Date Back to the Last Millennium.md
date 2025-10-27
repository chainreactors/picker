---
title: Security Navigator Research: Some Vulnerabilities Date Back to the Last Millennium
url: https://thehackernews.com/2023/01/security-navigator-research-some.html
source: The Hacker News
date: 2023-01-25
fetch_date: 2025-10-04T04:49:00.783283
---

# Security Navigator Research: Some Vulnerabilities Date Back to the Last Millennium

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

# [Security Navigator Research: Some Vulnerabilities Date Back to the Last Millennium](https://thehackernews.com/2023/01/security-navigator-research-some.html)

**Jan 24, 2023**The Hacker NewsVulnerability Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinBaU4o4pRLeqvHi-7U1D2KX-Z0zzIzedDaeAIb-SZjxwp5TX4iSiHJTy5k2B1csgd7M_Wt9C1yE4u63e8nU_oIlNacJiX1QRnsiDP60hgpYakWQggUSPpYDkUbhYjlj9itb4bAdg1l1DwjCd3u09Sc2Qu9fGnY3kEWx8YLpnKTyHg1VWllH0w-D5w/s790-rw-e365/main.jpg)

Vulnerability analysis results in [Orange Cyberdefenses' Security Navigator](https://www.orangecyberdefense.com/global/security-navigator?utm_source=hackernews&utm_medium=media&utm_campaign=sn2023) show that some vulnerabilities first discovered in 1999 are still found in networks today. This is concerning.

## **Age of VOC findings**

Our Vulnerability Scans are performed on a recurring basis, which provides us the opportunity to examine the difference between when a scan was performed on an Asset, and when a given finding on that Asset was reported. We can call that the finding 'Age'. If the findings first reported are not addressed, they will occur in more scans over time with increasing Age, and so we can track how the Age of reported findings changes over time.

As the chart below clearly illustrates, the majority of real findings in our dataset, across all Severity levels, are between 75 and 225 days old. There is a second 'peak' at around 300 days, which we suspect has more to do with the age of the data in the dataset and can therefore be ignored. Finally, there is a fascinating 'bump' at around 1,000 days, which we believe represents the 'long tail' of findings in the dataset that will simply never be addressed.

75% of the findings in the 1000-days 'bump' are Medium Severity, but 16% are classified as High or Critical Severity.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6Y3SdPYLog_Kt7ZDRNBNRNrB-qEo-pGm8hF8bHBm5knhUt9oPxHbQSgjK0nB135tyqJijR34_CTQw_AlMQQ44iX3OKIm603THlbQGXY1wF7s26vx1dOg0NDkr9aFS3PvnkuopOOJrrudD4bEYcSK-pmtZx7S2zCuoGoswYBDi3yeTOlw9IkmUh9VQ/s790-rw-e365/4.jpg)

The Average Age of findings in our dataset is impacted as much by changes in our Customer and Assets set as any external factor, as can be seen in the high degree of variation. Yet, there is a clear increase in the Average Age of findings of 241% from 63 to 215 days over the 24 months since we've been onboarding clients onto this platform.

**Roughly grouping confirmed findings from our Vulnerability Scan data by 'Age Group' reveals the following:**

* Only 20% of all findings are addressed in under 30 days
* 80% all findings take 30 days or more to patch
* 57% of all findings take 90 days or more to patch.
* 215 days Average

## **Average/max age of findings by severity**

The chart below suggests that even Critical Vulnerabilities are taking around 6 months on average to resolve, but that is encouragingly at least 36% faster than the time for low-severity issues.

Taking a closer look at the readings of average vs. maximum time for different ratings of criticality we end up with the chart below.

While our conclusion of critical issues being resolved faster stands for the average mitigation time, the maximum time is consistently high regardless of criticality.

We will have to watch this metric more as the dataset grows in the future.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZXX8uuFcQlRFb0L5Sf1B3Z2my7mh0-2ieadROJCuBaU6-6kXQiyvlXaqvw6NK2AFhJiVvKSplMLtb-UQx5dnAvbMpkh5HpeFkPsNWl7iPL9qdBXyHpJpCHSuC01AAVQoWOKkcEX14bbUZNX1lFhK5kPHzM5DoBdulgwVFvr6op_UAokbgH3yG-w6U/s790-rw-e365/2.jpg)

## **Industry Comparison**

The maximum age of findings in the view below serves as much as an indication of how long customers from that Industry have been present in our dataset as anything else, while the average age is a better proxy for how well customers are doing at addressing the issues we report. Industries with high maximums and low averages would therefore be doing the best, high maximum and high average… the 'worst.' Industries with very low maximum ages have probably not been in the dataset for very long and should, therefore, perhaps not be included in comparisons on this metric.

**However these Industries are compared, the finding Age is a concerning metric.**

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNX4FK85K19O2u82TnvUwFw9C7TKUKFTCe-1Z1Wh-r7glx6Vdi5M_SlTi5IwSf62QSy-L7myljD03zZdrHkw7Pel5CXNdY7dmSY-6r0-UZuuOZxxM6gg8akFW4aukrD5-Yd6LEaV8HUP03LwhWEkGydawed5jjHsZjkrjbUiBEjNkq-_HgKL4LbZXh/s790-rw-e365/3.jpg)

## **How old are those vulnerabilities really?**

So far we have only looked at the relative time, from when we first found a vulnerability in an asset up until now (if still present). However, that does not give us any information on how old those vulnerabilities really are. Taking a closer look at the found CVEs we can analyze their publishing dates. The results are somewhat baffling, but seem to fit the picture that emerges: for one reason or another, some vulnerabilities are just not fixed, ever. They become part of the security debt that businesses accumulate.

* 0.5% of CVEs reported are 20 years old or more
* 13% of CVEs reports are 10 years old or more
* 47% of CVEs are 5 years old or more

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjWYEsL31ruQyv0Sxp_3ia9VGz5sCXw-I7P7Yp72T9V6OtLg7p5Ybgb86FbkYhf7SbZ9XtOxCpIsRYwFUMlft8cadAZPdKAuLfoCyuyjK26bayOaralh1MsswuF2Fh298Hwc8iSE0x8tgf_LIwEO7VBDPzffwQWXlnDOCWKMrESlLG2xd6i-e5pfDI/s790-rw-e365/1.jpg)

## **Conclusion**

More than 22 vulnerabilities with assigned CVEs are published each day. With an average CVSS score above 7 (High Severity), each of these disclosed vulnerabilities is a significant datapoint that affects our risk equations and our real exposure to threats.

Vulnerability Scanning and Penetra...