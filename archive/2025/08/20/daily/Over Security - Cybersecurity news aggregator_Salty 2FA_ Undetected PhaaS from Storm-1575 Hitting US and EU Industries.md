---
title: Salty 2FA: Undetected PhaaS from Storm-1575 Hitting US and EU Industries
url: https://any.run/cybersecurity-blog/salty2fa-technical-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-20
fetch_date: 2025-10-07T00:49:29.161062
---

# Salty 2FA: Undetected PhaaS from Storm-1575 Hitting US and EU Industries

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

![Salty 2FA: Undetected PhaaS from Storm-1575 Hitting US and EU Industries ](/cybersecurity-blog/wp-content/uploads/2025/08/Salty-2FA-cover.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Salty 2FA: Undetected PhaaS from Storm-1575 Hitting US and EU Industries

August 19, 2025

[Add comment](#comments-15459)
32609 views
12 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Salty 2FA: Undetected PhaaS from Storm-1575 Hitting US and EU Industries

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1969
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3195
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3302
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Salty 2FA: Undetected PhaaS from Storm-1575 Hitting US and EU Industries

Today, phishing accounts for the majority of all cyberattacks. The availability of low-cost, easy-to-use [Phishing-as-a-Service (PhaaS) platforms like Tycoon2FA](https://any.run/cybersecurity-blog/tycoon2fa-evasion-analysis/), EvilProxy, and Sneaky2FA only makes the problem worse.

These services are actively maintained by their operators; new evasion techniques are regularly added, and the multi-layered infrastructure behind the phishing kits continues to evolve and expand.

But beyond these established players in the PhaaS market, the [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=salty&utm_term=190825&utm_content=linktolanding) team sometimes comes across phishing campaigns that use tools unlike anything we’ve seen before.

One such example is a framework we’ve dubbed **Salty 2FA**, whose execution chain and infrastructure have not previously been documented.

Like other PhaaS platforms, Salty 2FA is mainly delivered via email and focuses on stealing Microsoft 365 credentials. It unfolds in multiple stages and includes several mechanisms designed to hinder detection and analysis.

Let’s dive deeper into how Salty 2FA works.

## Key Takeaways

* **Salty 2FA is a newly discovered PhaaS framework**, with overlaps to Storm-1575/1747 but distinct enough to stand apart.

* It uses a **unique domain pattern** (.com subdomains paired with .ru domains) and unfolds in a **multi-stage execution chain** designed to resist detection.

* The kit can **bypass multiple 2FA methods** (push, SMS, voice), giving attackers access beyond stolen credentials.

* **Victims span global industries** including finance, telecom, energy, consulting, logistics, and education.

* **Static IOCs are unreliable**; detection requires spotting **behavioral patterns** that persist across samples.

* **ANY.RUN’s interactive sandbox** was essential in mapping its execution flow and exposing its infrastructure in real time.

## Discovery of Salty 2FA

During phishing campaign hunting, several [ANY.RUN sandbox sessions](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=salty&utm_term=190825&utm_content=linktolanding) were identified that had not yet been flagged as malicious. At first glance, they showed familiar traits: Cloudflare Turnstile, a fake Microsoft login page, and unknown domains.

Check analysis sessions:

[Analysis session 1](https://app.any.run/tasks/91e777dd-603b-47e4-ad8f-96e8bddf2cba/?utm_source=anyrunblog&utm_medium=article&utm_campaign=salty&utm_term=190825&utm_content=linktoservice)

[Analysis session 2](https://app.any.run/tasks/7d8e3a4d-5226-40b9-9e94-0f833c784abc/?utm_source=anyrunblog&utm_medium=article&utm_campaign=salty&utm_term=190825&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2025/08/phishkit_salty-1024x580.png)

What stood out in these cases was the domain infrastructure. In the IOCs section of the sessions, a pattern became clear: the consistent use of compound domains in “.com” zones (e.g., .com.de, .it.com) in combination with domains registered under the .ru TLD. The phishing pages themselves also followed a recurring format, embedding “.com” subdomains within a pattern of <sub\_domain>.<main\_domain>.??.com.

![](/cybersecurity-blog/wp-content/uploads/2025/08/image1-1.png)

The URI paths hosting the phishing content also appeared unusual. While they initially looked randomly generated and unrelated, further inspection suggested they might share commonalities worth examining.

With this hypothesis in mind, a query was run in [Threat Intelligence Lookup](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=salty&utm_term=190825&utm_content=linktolookup):

[domainName:”\*.\*.??.com$” AND domainName:”.ru$”](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_camp...