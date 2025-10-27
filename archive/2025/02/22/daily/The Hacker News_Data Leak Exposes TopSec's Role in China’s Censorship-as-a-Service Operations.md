---
title: Data Leak Exposes TopSec's Role in China’s Censorship-as-a-Service Operations
url: https://thehackernews.com/2025/02/data-leak-exposes-topsecs-role-in.html
source: The Hacker News
date: 2025-02-22
fetch_date: 2025-10-06T20:47:04.890042
---

# Data Leak Exposes TopSec's Role in China’s Censorship-as-a-Service Operations

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

# [Data Leak Exposes TopSec's Role in China's Censorship-as-a-Service Operations](https://thehackernews.com/2025/02/data-leak-exposes-topsecs-role-in.html)

**Feb 21, 2025**Ravie LakshmananSurveillance / Content Monitoring

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTyrubLjPcxIr9-1cwuxi_EZfyfrnjYzzPKQEUiTD1D9RDyOGRS82m4mJUAe0T7w0VTKkKk-KzHsYffcKu4-Orw7oi4Soars_chNCPL8XEgOElllK-UoNQUjS-CE0KNusT73NjdfZ7EHrJuqfd8NwwXgHxsAKSfhOz3TXto_Z2LE_-xW0RtdGNnK-plIml/s790-rw-e365/china.png)

An analysis of a data leak from a Chinese cybersecurity company TopSec has revealed that it likely offers censorship-as-a-service solutions to prospective customers, including a state-owned enterprise in the country.

Founded in 1995, TopSec ostensibly offers services such as Endpoint Detection and Response (EDR) and vulnerability scanning. But it's also providing "boutique" solutions in order to align with government initiatives and intelligence requirements, SentinelOne researchers Alex Delamotte and Aleksandar Milenkoski [said](https://www.sentinelone.com/labs/censorship-as-a-service-leak-reveals-public-private-collaboration-to-monitor-chinese-cyberspace/) in a report shared with The Hacker News.

The data leak contains infrastructure details and work logs from employees, as well as references to web content monitoring services used to enforce censorship for public and private sector customers.

It's believed that the company provided bespoke monitoring services to a state-owned enterprise hit by a corruption scandal, indicating that such platforms are being used to monitor and control public opinion as necessary.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Present among the data leak is a contract for a "Cloud Monitoring Service Project" announced by the Shanghai Public Security Bureau in September 2024.

The project, the document reveals, involves continuous monitoring of websites within the Bureau's jurisdiction with the goal of identifying security issues and content changes, and providing incident alerts.

Specifically, the platform has been designed to look for the presence of hidden links in web content, along with those containing [sensitive words](https://www.sciencedirect.com/science/article/abs/pii/S2211695822000897) related to political criticism, violence, or pornography.

While the exact goals are unclear, it's suspected that such alerts could be used by customers to take follow-on actions, such as issuing warnings, deleting content, or restricting access when sensitive words are detected. That said, Shanghai Anheng Smart City Security Technology Co. Ltd. won the contract, per public documents analyzed by SentinelOne.

The cybersecurity firm said the leak was detected after it analyzed a text file that was [uploaded](https://www.virustotal.com/gui/file/026281c7651d49c77c597d1843578b4578deac3fb8c10be3977371f140b54690/details) to the VirusTotal platform on January 24, 2025. The manner in which the data was leaked remains unclear.

"The main file we analyzed contains numerous work logs, which are a description of the work performed by a TopSec employee and the amount of time the task took, often accompanied by scripts, commands, or data related to the task," the researchers noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"In addition to work logs, the leak contains many commands and playbooks used to administrate TopSec's services via multiple common DevOps and infrastructure technologies that are used worldwide, including Ansible, Docker, ElasticSearch, Gitlab, Kafka, Kibana, Kubernetes, and Redis."

Also found are references to another framework named Sparta (or Sparda) that's supposedly designed to handle sensitive word processing by receiving content from downstream web applications via GraphQL APIs, once again suggestive of censorship keyword monitoring.

"These leaks yield insight into the complex ecosystem of relationships between government entities and China's private sector cybersecurity companies," the researchers said.

"While many countries have significant overlap between government requirements and private sector cybersecurity firms, the ties between these entities in China are much deeper and represent the state's grasp on managing public opinion through online enforcement."

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

[censorship](https://thehackernews.com/search/label/censorship)[china](https://thehackernews.com/search/label/china)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Content Monitoring](https://thehackernews.com/search/label/Content%20Monitoring)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Leak](https://thehackernews.com/search/label/Data%20Leak)[DevOps](https://thehackernews.com/search/label/DevOps)[Digital Rights](https://thehackernews.com/search/label/Digital%20Rights)[surveillance](https://thehackernews.com/search/label/surveillance)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending ...