---
title: Agile Approach to Mass Cloud Credential Harvesting and Crypto Mining Sprints Ahead
url: https://thehackernews.com/2023/08/agile-approach-to-mass-cloud-credential.html
source: The Hacker News
date: 2023-08-24
fetch_date: 2025-10-04T12:04:00.760283
---

# Agile Approach to Mass Cloud Credential Harvesting and Crypto Mining Sprints Ahead

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

# [Agile Approach to Mass Cloud Credential Harvesting and Crypto Mining Sprints Ahead](https://thehackernews.com/2023/08/agile-approach-to-mass-cloud-credential.html)

**Aug 23, 2023**The Hacker NewsMalware / Cybersecurity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPZnxLTy-yqlT98teGPo2pJKoP7jkuxfMVaVJU1Nkwh7jB-Twl1EAeOAAVwg3HBF4i7iBWzniTO3zBgUvz7NqZcgTb-RRb8hjisiG5PjZy6aRKrfrInW8wOdPfddG93RMBMEFchSk-t_ibj-CPSj58ETrgLmP_jg_4Bu_3JaUm081_K8qMTA4KgXNzMqA/s790-rw-e365/main.jpg)

Developers are not the only people who have adopted the agile methodology for their development processes. From 2023-06-15 to 2023-07-11, Permiso Security's p0 Labs team identified and tracked an attacker developing and deploying eight (8) incremental iterations of their credential harvesting malware while continuing to develop infrastructure for an upcoming (spoiler: now launched) campaign targeting various cloud services.

While last week Aqua Security [published](https://blog.aquasec.com/threat-alert-anatomy-of-silentbobs-cloud-attack) a blog detailing this under-development campaign's stages related to infected Docker images, today [Permiso p0 Labs](https://permiso.io/p0-labs/) and [SentinelLabs](https://s1.ai/cloudcreds) are releasing joint research highlighting the incremental updates to the cloud credential harvesting malware samples systematically collected by monitoring the attacker's infrastructure. So get out of your seats and enjoy this scrum meeting stand-up dedicated to sharing knowledge about this actors campaign and the tooling they will use to steal more cloud credentials.

If you like IDA screenshots in your analysis blogs, be sure to check out [SentinelLabs](https://s1.ai/cloudcreds)' take on this campaign!

## Previous Campaigns

There have been many campaigns where actors have used similar tooling to perform cloud credential scraping while also mass deploying crypto mining software. As a refresher, in December, the Permiso team reported the details of an actor [targeting public facing Juptyer Notebooks](https://permiso.io/blog/s/christmas-cloud-cred-harvesting-campaign/) with this toolset.

Our friends over at Cado have also reported extensively on [previous campaigns](https://www.cadosecurity.com/team-tnt-the-first-crypto-mining-worm-to-steal-aws-credentials/).

## Active Campaign

On 2023-07-11, while we were preparing the release of this blog about the in-development toolset, the actor kicked off their campaign.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisMKofQQhOFAsBts84YvHmRODnldseynIB5vHs663psr6T1gJ5C_Bh42-cJ1eDT_hOczX9ua61ptk21rK_2OgB2mrTZO5ty7LEnez5KNh5q6qS4ymrpvF1iVs4NPlf8Eezbm8WKPodTe69-hG2HP6UW8lX0bsPi75_4mCTlSjopBiCybvqksi48l70TFo/s790-rw-e365/2.jpg)

The file b.sh is the initializing script that downloads and deploys the full tool suite functionality. The main features are to install a backdoor for continued access, deploy crypto mining utilities, and search for and spread to other vulnerable systems.

Currently (2023-07-12), there are 39 compromised systems in this campaign:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHipqXujp9gNC2_68KnAsz2KrEgrBj_QzrX9Y-YCn6Vmsp3VWlKvc2VdF1IOERrcIrCaZlPQAt4-tTAqdBeugJL1nYhNViMcxEYoBpLRIWfB_CiRzyiQzAQ6eFvTMnpz6fjnkMSPihufu0AoVVouDPHoFE8g8uyRUAG5C8HCoDxwLsXl4sJR5dqtjnFJc/s790-rw-e365/1.jpg)

## What's New?

The cloud credential harvesting utilities in this campaign have some notable differences from previous versions. The following are the highlights of the modifications:

* **Multi-cloud Support**:

+ GCP support added
+ GCLOUD\_CREDS\_FILES=("config\_sentinel" "gce" ".last\_survey\_prompt.yaml" "config\_default" "active\_config" "credentials.db" "access\_tokens.db" ".last\_update\_check.json" ".last\_opt\_in\_prompt.yaml" ".feature\_flags\_config.yaml" "adc.json" "resource.cache")

* Azure support added by looking for and extracting credentials from any files named azure.json
* Numerous structural and syntactical changes highlight the shift from AWS targeting to multi-cloud:

+ Sensitive file name arrays split by cloud service:

- CRED\_FILE\_NAMES → AWS\_CREDS\_FILES, AZURE\_CREDS\_FILES and GCLOUD\_CREDS\_FILES

+ Function names genericized:

- send\_aws\_data → send\_data

+ Output section headers modified:

- INFO → AWS INFO
- IAM → IAM USERDATA
- EC2 → EC2 USERDATA

* **Targeted Files**: Added "kubeconfig" "adc.json" "azure.json" "clusters.conf" "docker-compose.yaml" ".env" to the CRED\_FILE\_NAMES variable. redis.conf.not.exist added with a variable MIXED\_CREDFILES.
* **New Curl**: Shifted from dload function ("curl without curl") to downloading staged curl binary to eventually using the native curl binary.
* **AWS-CLI**: aws sts get-caller-identity for validating cloud credentials, and identity information

+ **Infrastructure**: Most previous campaigns hosted utilities and C2 on a single domain. In this campaign the actor is utilizing multiple FQDNs (including noteworthy masquerade as EC2 Instance: ap-northeast-1.compute.internal.anondns[.]net).

- Numerous elements of the actor's infrastructure and code give weight to the author being a native German speaker (in addition to the fact that the open source TeamTNT tooling already has many German elements in its code).

* One of the intermediate versions of aws.sh referenced the FQDN ap-northeast-1.compute.internal.anondns[.]net , which returned the German error message Fehler! vergleiche bitte die Authentifizierungsmerkmale in beiden Scripten!!! (which translates to Error! please compare the authentication features in both scripts!!) when visited by a VirusTotal scan on 2023-06-23:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFcQCqn-luTmW1BKvm32rh7IQ9jSH_VycDalOsr6dPStOR8cH2fJm2Db8IsNHj5xt00fJHjszlseR-fdQl3CyhK00ziULr3xBlImwCn7QhEJP5-i6yfxqU4uxXsFpjWPJkO4VyMkjTorfQwr66lrrdg3kih_q-DSgaMkDItf82bhX1u10hYuzn15q645s/s790-rw-e365/vt.jpg)

* A Go...