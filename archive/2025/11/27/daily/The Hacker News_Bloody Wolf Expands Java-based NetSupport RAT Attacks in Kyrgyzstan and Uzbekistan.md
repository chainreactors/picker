---
title: Bloody Wolf Expands Java-based NetSupport RAT Attacks in Kyrgyzstan and Uzbekistan
url: https://thehackernews.com/2025/11/bloody-wolf-expands-java-based.html
source: The Hacker News
date: 2025-11-27
fetch_date: 2025-11-28T03:13:18.814143
---

# Bloody Wolf Expands Java-based NetSupport RAT Attacks in Kyrgyzstan and Uzbekistan

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

# [Bloody Wolf Expands Java-based NetSupport RAT Attacks in Kyrgyzstan and Uzbekistan](https://thehackernews.com/2025/11/bloody-wolf-expands-java-based.html)

**Nov 27, 2025**Ravie LakshmananMalware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjF1NjcNl0amY7zxe4zJ58EcQQ7cm-HPNA2F3qrnTLAeF1lyBNGx1SvEnmz0Ok5DUV8ZRiOZP0fDBf_tP0LIZRcShjLexQJ6nbXiQsFaBEXc8bSHuTmGjKGscfYjGahNnvbk7Vf0hmdHX5Gca9LrWUwPwIl10Q5qzaPbH6BNHIJNg1s79QJ4BMLD4z6hhN3/s790-rw-e365/gib.jpg)

The threat actor known as **Bloody Wolf** has been attributed to a cyber attack campaign that has targeted Kyrgyzstan since at least June 2025 with the goal of delivering NetSupport RAT.

As of October 2025, the activity has expanded to also single out Uzbekistan, Group-IB researchers Amirbek Kurbanov and Volen Kayo said in a report published in collaboration with Ukuk, a state enterprise under the Prosecutor General's office of the Kyrgyz Republic. The attacks have targeted finance, government, and information technology (IT) sectors.

"Those threat actors would impersonate the [Kyrgyzstan's] Ministry of Justice through official looking PDF documents and domain names, which in turn hosted malicious Java Archive (JAR) files designed to deploy the NetSupport RAT," the Singapore-headquartered company [said](https://www.group-ib.com/blog/bloody-wolf/).

"This combination of social engineering and accessible tooling allows Bloody Wolf to remain effective while keeping a low operational profile."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

[Bloody Wolf](https://thehackernews.com/2024/08/kazakh-organizations-targeted-by-bloody.html) is the name assigned to a [hacking group](https://thehackernews.com/2025/03/kaspersky-links-head-mare-to-twelve.html) of unknown provenance that has used spear-phishing attacks to target entities in Kazakhstan and Russia using tools like STRRAT and NetSupport. The group is assessed to be active since at least late 2023.

The targeting of Kyrgyzstan and Uzbekistan using similar initial access techniques marks an expansion of the threat actor's operations in Central Asia, primarily impersonating trusted government ministries in phishing emails to distribute weaponized links or attachments.

The attack chains more or less follow the same approach in that the message recipients are tricked into clicking on links that download malicious Java archive (JAR) loader files along with instructions to install Java Runtime.

While the email claims the installation is necessary to view the documents, the reality is that it's used to execute the loader. Once launched, the loader then proceeds to fetch the next-stage payload (i.e., NetSupport RAT) from infrastructure that's under the attacker's control and set up persistence in three ways -

* Creating a scheduled task
* Adding a Windows Registry value
* Dropping a batch script to the folder "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

The Uzbekistan phase of the campaign is notable for incorporating geofencing restrictions, thereby causing requests originating outside of the country to be redirected to the legitimate data.egov[.]uz website. Requests from within Uzbekistan have been found to trigger the download of the JAR file from an embedded link within the PDF attachment.

Group-IB said the JAR loaders observed in the campaigns are built with Java 8, which was released in March 2014. It's believed that the attackers are using a bespoke JAR generator or template to spawn these artifacts. The NetSupport RAT payload is a old version of NetSupport Manager from October 2013.

"Bloody Wolf has demonstrated how low-cost, commercially available tools can be weaponized into sophisticated, regionally targeted cyber operations," it said. "By exploiting trust in government institutions and leveraging simple JAR-based loaders, the group continues to maintain a strong foothold across the Central Asian threat landscape."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[finance](https://thehackernews.com/search/label/finance)[information technology](https://thehackernews.com/search/label/information%20technology)[Malware](https://thehackernews.com/search/label/Malware)[Phishing](https://thehackernews.com/search/label/Phishing)[remote access tool](https://thehackernews.com/search/label/remote%20access%20tool)[social engineering](https://thehackernews.com/search/label/social%20engineering)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Fortinet Exploited, China's AI Hacks, PhaaS Empire Falls and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploited, China's AI Hacks, PhaaS Empire Falls and More")

⚡ Weekly Recap: Fortinet Exploited, China's AI Hacks, PhaaS Empire Falls and More](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploited-chinas.html)

[![Google Issues Security Fix for Actively Exploited Chrome V8 Zero-Day Vulnerability](data:image/svg+xml;base64... "Goo...