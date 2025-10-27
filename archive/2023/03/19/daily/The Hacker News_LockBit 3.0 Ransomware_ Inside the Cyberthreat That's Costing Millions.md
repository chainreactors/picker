---
title: LockBit 3.0 Ransomware: Inside the Cyberthreat That's Costing Millions
url: https://thehackernews.com/2023/03/lockbit-30-ransomware-inside.html
source: The Hacker News
date: 2023-03-19
fetch_date: 2025-10-04T10:03:35.142901
---

# LockBit 3.0 Ransomware: Inside the Cyberthreat That's Costing Millions

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

# [LockBit 3.0 Ransomware: Inside the Cyberthreat That's Costing Millions](https://thehackernews.com/2023/03/lockbit-30-ransomware-inside.html)

**Mar 18, 2023**Ravie LakshmananEndpoint Security / Encryption

[![lockbit-ransomware](data:image/png;base64... "lockbit-ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiq79HBBA8LS8E2xr4gPiDnGScNC4jYO-4A8gPKFqegEOWp_bsuoDvbWN2s0UKQiqwmEzw1hlGrvLcO82M4GuBfsiXYaVatejI5H45L1Nfzze6fbQAES1cPA2B4Tngk76-gmvC7gynFpA8eZdr0Z5HE7ZJlGPph8PdwvQwQcOq4YnGYcY_SYUktLrUN/s790-rw-e365/lockbit-ransomware.png)

U.S. government agencies have released a joint cybersecurity advisory detailing the indicators of compromise (IoCs) and tactics, techniques, and procedures (TTPs) associated with the notorious [LockBit 3.0 ransomware](https://thehackernews.com/2022/11/amadey-bot-spotted-deploying-lockbit-30.html).

"The LockBit 3.0 ransomware operations function as a Ransomware-as-a-Service (RaaS) model and is a continuation of previous versions of the ransomware, LockBit 2.0, and LockBit," the authorities [said](https://www.cisa.gov/news-events/alerts/2023/03/16/fbi-cisa-and-ms-isac-release-stopransomware-lockbit-30).

The alert comes courtesy of the U.S. Federal Bureau of Investigation (FBI), the Cybersecurity and Infrastructure Security Agency (CISA), and the Multi-State Information Sharing & Analysis Center (MS-ISAC).

Since emerging in late 2019, the [LockBit actors](https://www.wired.com/story/lockbit-ransomware-attacks/) have invested significant [technical efforts](https://thehackernews.com/2022/07/researchers-detail-techniques-lockbit.html) to develop and fine-tune its malware, issuing two major updates — LockBit 2.0, released in mid-2021, and [LockBit 3.0](https://thehackernews.com/2022/07/experts-find-similarities-between.html), released in June 2022. The two versions are also known as LockBit Red and LockBit Black, respectively.

"LockBit 3.0 accepts additional arguments for specific operations in lateral movement and rebooting into Safe Mode," according to the [alert](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a). "If a LockBit affiliate does not have access to passwordless LockBit 3.0 ransomware, then a password argument is mandatory during the execution of the ransomware."

The ransomware is also designed to infect only those machines whose language settings do not overlap with those specified in an exclusion list, which includes Romanian (Moldova), Arabic (Syria), and Tatar (Russia).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Initial access to victim networks is obtained via remote desktop protocol (RDP) exploitation, drive-by compromise, phishing campaigns, abuse of valid accounts, and weaponization of public-facing applications.

Upon finding a successful ingress point, the malware takes steps to establish persistence, escalate privileges, carry out lateral movement, and purge log files, files in the Windows Recycle Bin folder, and shadow copies, before initiating the encryption routine.

"LockBit affiliates have been observed using various freeware and open source tools during their intrusions," the agencies said. "These tools are used for a range of activities such as network reconnaissance, remote access and tunneling, credential dumping, and file exfiltration."

One defining characteristic of the attacks is the use of a custom exfiltration tool referred to as [StealBit](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool), which the LockBit group provides to affiliates for double extortion purposes.

In November, the U.S. Department of Justice [reported](https://thehackernews.com/2022/11/russian-canadian-national-charged-over.html) that the LockBit ransomware strain has been used against at least 1,000 victims worldwide, netting the operation over $100 million in illicit profits.

Industrial cybersecurity firm Dragos, earlier this year, [revealed](https://www.dragos.com/blog/industry-news/dragos-industrial-ransomware-analysis-q4-2022/) that LockBit 3.0 was responsible for 21% of 189 ransomware attacks detected against critical infrastructure in Q4 2022, accounting for 40 incidents. A majority of those attacks impacted food and beverage and manufacturing sectors.

The FBI's Internet Crime Complaint Center (IC3), in its latest [Internet Crime Report](https://www.ic3.gov/Home/AnnualReports), listed LockBit (149), [BlackCat](https://thehackernews.com/2022/09/blackcat-ransomware-attackers-spotted.html) (114), and [Hive](https://thehackernews.com/2023/01/hive-ransomware-infrastructure-seized.html) (87) as the top three ransomware variants victimizing critical infrastructure in 2022.

Despite LockBit's prolific attack spree, the ransomware gang [suffered a huge blow](https://intel471.com/blog/lockbit-3-0-builder-code-leak-points-to-another-disgruntled-criminal-employee) in late September 2022 when a disgruntled LockBit developer released the builder code for LockBit 3.0, raising concerns that other criminal actors could take advantage of the situation and spawn their own variants.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The advisory comes as the [BianLian](https://thehackernews.com/2022/09/researchers-detail-emerging-cross.html) ransomware group has [shifted its focus](https://redacted.com/blog/bianlian-ransomware-gang-continues-to-evolve/) from encrypting its victims' files to pure data-theft extortion attacks, months after cybersecurity company Avast [released](https://thehackernews.com/2023/02/bitdefender-releases-free-decryptor-for.html) a free decryptor in January 2023.

In a related development, Kaspersky has [published](https://usa.kaspersky.com/about/press-releases/2023_kaspersky-releases-tool-for-decrypting-conti-based-ransomware) a free decryptor to help victims who have had their data locked down by a version of ransomware based on the [Conti source code](https://theha...