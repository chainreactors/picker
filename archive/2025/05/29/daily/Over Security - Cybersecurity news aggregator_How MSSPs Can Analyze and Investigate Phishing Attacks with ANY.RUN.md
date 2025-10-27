---
title: How MSSPs Can Analyze and Investigate Phishing Attacks with ANY.RUN
url: https://any.run/cybersecurity-blog/how-to-investigate-phishing-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-29
fetch_date: 2025-10-06T22:31:15.638980
---

# How MSSPs Can Analyze and Investigate Phishing Attacks with ANY.RUN

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

![How MSSPs Can Analyze and Investigate Phishing Attacks with ANY.RUN ](/cybersecurity-blog/wp-content/uploads/2025/05/MSSP.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# How MSSPs Can Analyze and Investigate Phishing Attacks with ANY.RUN

May 28, 2025

[Add comment](#comments-13944)
3739 views
7 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

How MSSPs Can Analyze and Investigate Phishing Attacks with ANY.RUN

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1617
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3164
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3182
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

How MSSPs Can Analyze and Investigate Phishing Attacks with ANY.RUN

Phishing attacks have become a pervasive and escalating threat across various industries, notably in finance, manufacturing, and healthcare. For [Managed Security Service Providers](https://any.run/cybersecurity-blog/expertware-success-story/) (MSSPs), the challenge lies in swiftly identifying and mitigating these threats to safeguard client infrastructures and uphold service integrity.

This case study explores how ANY.RUN’s [Threat Intelligence Lookup](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/) and [Interactive Sandbox](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_lookup_for_mssps&utm_term=280525&utm_content=linktolanding) can empower MSSPs to detect, investigate, and respond to phishing attacks more effectively.

## About the Case Study

As an example, we’ll use a payload from Delivr.to (a platform designed to help organizations assess and enhance their email security by simulating real-world threats). We’ll see how Threat Intelligence Lookup and Interactive Sandbox help with:

* **Access to real-world phishing samples**: Use our [extensive threat database](http://intelligence.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_lookup_for_mssps&utm_term=280525&utm_content=linktoti) to study current phishing samples, simulate email filter bypasses, and prepare more resilient defenses.

* **Deep behavior analysis**: Examine samples in the sandbox to uncover [IOCs, IOBs, IOAs,](https://any.run/cybersecurity-blog/iocs-iobs-ioas-explained/) TTPs, and link attacks to specific malware families and threat actors.

* **Targeted threat discovery**: Search phishing samples by country, time period, known artifacts.

* **Training and awareness**: Use real phishing cases to educate your team and clients, improving detection and response readiness.

Let’s begin.

## 1. Introducing the payload

We have chosen an HTML file Electronic\_Receipt\_ATT0001.htm from the payload sample library of Delivr.to.

![](/cybersecurity-blog/wp-content/uploads/2025/05/image-23.png)

The attachment’s description contains its ID, hash sum, payload chain deployment steps, and the tags describing the attack chain scenario.

Such payloads are meant to be emailed in order to put to test corporate cybersecurity policies. However, a full-fledged understanding of a threat implies not only the detection of email filters bypass, but a full analysis of an activated payload behavior. This is why we shall use ANY.RUN’s TI Lookup to search for this HTML file.

## 2. Detecting the payload in malware campaigns

Our request to TI Lookup includes the parameter indicating an attached file and the file’s name.

[filePath:”Electronic\_Receipt\_ATT0001″](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_lookup_for_mssps&utm_term=280525&utm_content=linktolookup#%257B%2522query%2522:%2522filePath:%255C%2522Electronic_Receipt_ATT0001%255C%2522%2522,%2522dateRange%2522:180%257D)

![](/cybersecurity-blog/wp-content/uploads/2025/05/image2-2-1024x734.png)

21 malware samples containing this payload have been discovered in TI Lookup at the moment. Besides providing links to the samples and their analyses, TI Lookup highlights the fact that most samples featuring our benign file have been tagged as malicious and attributed to Tycoon phishing kit distributed as Phishing-as-a-Service (PhaaS).

This means that the chosen payload is actually employed in real phishing campaigns.

Level up malware analysis and threat intelligence capabilities
See all ANY.RUN’s 9th Birthday offers

[Check out offers](https://app.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_lookup_for_mssps&utm_term=280525&utm_content=linktoplans)

## 3. Expanding the malware research

We can also search for other payloads related to Tycoon’s activity. The search query combines the name of the process “outlo...