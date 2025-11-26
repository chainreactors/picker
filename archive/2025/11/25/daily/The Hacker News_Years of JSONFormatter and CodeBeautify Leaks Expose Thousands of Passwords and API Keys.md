---
title: Years of JSONFormatter and CodeBeautify Leaks Expose Thousands of Passwords and API Keys
url: https://thehackernews.com/2025/11/years-of-jsonformatter-and-codebeautify.html
source: The Hacker News
date: 2025-11-25
fetch_date: 2025-11-26T03:17:15.271899
---

# Years of JSONFormatter and CodeBeautify Leaks Expose Thousands of Passwords and API Keys

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Years of JSONFormatter and CodeBeautify Leaks Expose Thousands of Passwords and API Keys](https://thehackernews.com/2025/11/years-of-jsonformatter-and-codebeautify.html)

**Nov 25, 2025**Ravie LakshmananData Exposure / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMOKzumRIbT28KmhxEYK7XbBCh9DFCNL3o9nhJynO8qEPufvtFSaUZ410fDSym6bQyAxTbStDCFnOjDG4QwashtUee4Cclcfu6_MQ_pcWk_cjFhnlzNy_MDFLL4vwI5LOrJnuJUzt96Cdi3E6PevLQn33zrqYBicNRERNKDJ1DYW6JIOU879I4fCSv8NQp/s2600/json.jpg)

New research has found that organizations in various sensitive sectors, including governments, telecoms, and critical infrastructure, are pasting passwords and credentials into online tools like JSONformatter and CodeBeautify that are used to format and validate code.

Cybersecurity company watchTowr Labs [said](https://labs.watchtowr.com/stop-putting-your-passwords-into-random-websites-yes-seriously-you-are-the-problem/) it captured a dataset of over 80,000 files on these sites, uncovering thousands of usernames, passwords, repository authentication keys, Active Directory credentials, database credentials, FTP credentials, cloud environment keys, LDAP configuration information, helpdesk API keys, meeting room API keys, SSH session recordings, and all kinds of personal information.

This includes five years of historical JSONFormatter content and one year of historical CodeBeautify content, totalling over 5GB worth of enriched, annotated JSON data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Organizations impacted by the leak span critical national infrastructure, government, finance, insurance, banking, technology, retail, aerospace, telecommunications, healthcare, education, travel, and, ironically, cybersecurity sectors.

"These tools are extremely popular, often appearing near the top of search results for terms like 'JSON beautify' and 'best place to paste secrets' (probably, unproven) -- and used by a wide variety of organizations, organisms, developers, and administrators in both enterprise environments and for personal projects," security researcher Jake Knott said in a report shared with The Hacker News.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ22eyPZ9GPe46bubtp4PaDFE_IThd6eWYXIdCjHrCrZFJi01tPfYbtJzf1kh5zArIaebfWzwmAf0P7QDZ9W4B4_YdRd5LZHzse7iBCKAcFtG3MA-m1YqKKAjKBKQbFtfCuff5A3I8lWhFlCK-WCt4aR1HaVrEMAs4LU_2duuAr1IVo-rC2cLPnYX6TbDE/s2600/data.png)

Both tools also offer the ability to save a formatted JSON structure or code, turning it into a semi-permanent, shareable link with others – effectively allowing anyone with access to the URL to access the data.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtSzhUaNimaidu2yUM9J4u7t017tNo3lQoWVs0CHHQzejrRvijx5p-otayz0vqDCnyb_VJEeS2wCit5JM2r_bBjLpSwi30d_P2WBF-IbTKTwqxa-5EGvfmbm0YHt6_uk1YCpvHQsP04_142nskP1c_d_Vm8sn5Mg7VFU8vrqpd6L1tTogCXPAhM5Y1Keoc/s2600/here.jpg)

As it happens, the sites not only provide a [handy](https://jsonformatter.org/recentLinksPage/json) [Recent Links page](https://codebeautify.org/recentLinksPage) to list all recently saved links, but also follow a predictable URL format for the shareable link, thereby making it easier for a bad actor to retrieve all URLs using a simple crawler -

* https://jsonformatter.org/{id-here}
* https://jsonformatter.org/{formatter-type}/{id-here}
* https://codebeautify.org/{formatter-type}/{id-here}

Some examples of leaked information include Jenkins secrets, a cybersecurity company exposing encrypted credentials for sensitive configuration files, Know Your Customer (KYC) information associated with a bank, a major financial exchange's AWS credentials linked to Splunk, and Active Directory credentials for a bank.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

To make matters worse, the company said it uploaded fake AWS access keys to one of these tools, and found bad actors attempting to abuse them 48 hours after it was saved. This indicates that valuable information exposed through these sources is being scraped by other parties and tested, posing severe risks.

"Mostly because someone is already exploiting it, and this is all really, really stupid," Knott said. "We don't need more AI-driven agentic agent platforms; we need fewer critical organizations pasting credentials into random websites."

When checked by The Hacker News, both JSONFormatter and CodeBeautify have temporarily disabled the save functionality, claiming they are "working on to make it better" and implementing "enhanced NSFW (Not Safe For Work) content prevention measures."

watchTowr said that the save functionality was disabled by these sites likely in response to the research. "We suspect this change occurred in September in response to communication from a number of the affected organizations we alerted," it added.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Exposure](https://thehackernews.com/search/lab...