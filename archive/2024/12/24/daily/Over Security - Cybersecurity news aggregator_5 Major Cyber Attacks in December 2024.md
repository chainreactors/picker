---
title: 5 Major Cyber Attacks in December 2024
url: https://any.run/cybersecurity-blog/cyber-attacks-december-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-24
fetch_date: 2025-10-06T19:41:55.384477
---

# 5 Major Cyber Attacks in December 2024

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![5 Major Cyber Attacks in December 2024](/cybersecurity-blog/wp-content/uploads/2024/12/dec_attacks_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# 5 Major Cyber Attacks in December 2024

December 23, 2024

[Add comment](#comments-10604)
5308 views
6 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

5 Major Cyber Attacks in December 2024

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1418
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3028
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3063
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

5 Major Cyber Attacks in December 2024

The cybersecurity research team of [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyber_attacks_december_24&utm_term=231224&utm_content=linktolanding) found and analyzed a bunch of emerging threats with the help of our mighty [Interactive Sandbox](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyber_attacks_december_24&utm_term=231224&utm_content=linktoregistration#register/) and [Threat Intelligence Lookup](https://intelligence.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyber_attacks_december_24&utm_term=231224&utm_content=linktotilookup).

We’ve been sharing their findings [via X](https://x.com/anyrun_app) and in [our blog](https://any.run/cybersecurity-blog/). Here is a summary on the most interesting insights from December 2024.

## Phishing Campaigns targeting Microsoft’s Azure Blob Storage

[*Original post on X*](https://x.com/anyrun_app/status/1863568916573827099)

![](/cybersecurity-blog/wp-content/uploads/2024/12/image9-2.png)

Cyber criminals are abusing Microsoft’s cloud-based file storage solution by hosting phishing pages on the service, employing techniques like HTML smuggling.

The phishing pages are HTML documents that contain a block input element with the ID attribute “doom”. The pages include information about users’ software obtained via JScript (OS and browser), to make them more convincing.

Phishing pages on Azure Blob Storage typically have a short lifespan. Attackers may host pages with redirects to phishing sites. With minimal suspicious content, these pages can evade detection slightly longer.

[See the analysis session](https://app.any.run/tasks/60157f76-92ec-463e-a1d0-c17930af3da6/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyber_attacks_december_24&utm_term=231224&utm_content=linktoservice) in the ANY.RUN sandbox.

![](/cybersecurity-blog/wp-content/uploads/2024/12/image6-1-1024x512.png)

* Threat actors leverage the \*.blob.core.windows[.]net subdomain to store documents.
* Company logos are extracted using email address parsing and loaded from the logo[.]clearbit[.]com service.
* To collect and store stolen data, an HTTP POST request is sent to nocodeform[.]io for collecting form submissions.

![](/cybersecurity-blog/wp-content/uploads/2024/12/image7-2-1024x634.png)

Use the following [Threat Intelligence Lookup](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/) query to find threats targeting the set of requested domains:

|  |
| --- |
| [domainName:".blob.core.windows.net" and domainName:"aadcdn.msauth.net" and domainName:"cdnjs.cloudflare.com" and domainName:"www.w3schools.com"](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyber_attacks_december_24&utm_term=231224&utm_content=linktotilookup#%257B%2522query%2522:%2522domainName:%255C%2522.blob.core.windows.net%255C%2522%25C2%25A0and%25C2%25A0%25C2%25A0domainName:%255C%2522aadcdn.msauth.net%255C%2522%2520and%2520domainName:%255C%2522cdnjs.cloudflare.com%255C%2522%2520and%2520domainName:%255C%2522www.w3schools.com%255C%2522%2522,%2522dateRange%2522:180%257D) |

![](/cybersecurity-blog/wp-content/uploads/2024/12/image8-1-1024x690.png)

And [this search request](https://intelligence.any.run/analysis/lookup#%257B%2522query%2522:%2522commandLine:%255C%2522https:/*.blob.core.windows.net/*.html%255C%2522%2522,%2522dateRange%2522:180%257D) to find links to HTML pages hosted on Azure Blob Storage.

Get 20 free requests in TI Lookup
to enrich your threat investigations

[Contact us](https://intelligence.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyber_attacks_december_24&utm_term=231224&utm_content=linktotiplans/)

## Microsoft’s OneDrive also fell victim to HTML Blob Smuggling Campaign

[The original post on X](https://x.com/anyrun_app/status/1869379428477735197)

As in the attack above, threat actors make victims believe they are logging into a legitimate platform.

![](/cybersecurity...