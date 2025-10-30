---
title: Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit
url: https://any.run/cybersecurity-blog/cyber-attacks-october-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-29
fetch_date: 2025-10-30T03:12:39.729491
---

# Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit

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

![Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit ](/cybersecurity-blog/wp-content/uploads/2025/10/5-Major-Cyber-Attacks-in-October-2025_cover.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit

October 29, 2025

[Add comment](#comments-16563)
880 views
12 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/10/5-Major-Cyber-Attacks-in-October-2025_cover-1024x497.jpg)

  #### Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit

  880
  0](/cybersecurity-blog/cyber-attacks-october-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/5-SOC-Challenges-1024x497.jpg)

  #### 5 SOC Challenges and How Threat Intelligence Solves Them

  346
  0](/cybersecurity-blog/solving-soc-challenges-with-ti/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/Awards_blog-1024x497.jpg)

  #### ANY.RUN Recognized as Threat Intelligence Company of the Year 2025

  599
  0](/cybersecurity-blog/cybersecurity-breakthrough-awards-2025/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in October 2025: Phishing via Google Careers & ClickUp, Figma Abuse, LockBit 5.0, and TyKit

Phishing campaigns and ransomware families evolved rapidly this October, from fake **Google Careers pages and ClickUp** redirect chains to **Figma-hosted credential theft** and **LockBit’s move** into ESXi and Linux systems. ANY.RUN analysts also uncovered **TyKit**, a reusable phishing kit hiding JavaScript inside SVG files to steal Microsoft 365 credentials across multiple sectors.

Each of these threats shows how attackers are increasingly abusing legitimate cloud platforms, layering CAPTCHA checks and redirects to bypass detection. All cases were analyzed inside [ANY.RUN’s Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=October_cyber_attacks_2025&utm_term=291025&utm_content=linksandboxlanding), revealing execution flows and behavioral indicators missed by static tools; insights SOC teams can turn into actionable detection logic.

Let’s break down how these attacks unfolded, who they targeted, and what security teams can learn to strengthen their defenses before the next wave hits.

## 1. Google Careers Phishing Campaign: Legitimate Platforms Used to Steal Corporate Credentials

[Post on X](https://x.com/anyrun_app/status/1976290433417228499)

ANY.RUN analysts uncovered a **phishing campaign posing as Google Careers**, where attackers combined a **Salesforce redirect**, **Cloudflare Turnstile CAPTCHA**, and a **fake job application page** to steal corporate credentials. The campaign primarily targets employees in technology, consulting, and enterprise service sectors, exploiting the trust people place in well-known brands and cloud services.

Unlike typical phishing kits, this campaign weaves together multiple legitimate platforms to make the flow appear authentic, slipping through filters and reputation-based security tools. Once credentials are entered on the fake Google Careers portal, they’re exfiltrated to the command-and-control (C2) server, such as **satoshicommands[.]com**, enabling further compromise of work accounts, client data, and internal collaboration tools.

For organizations, this attack creates a chain reaction: compromised mailboxes, lateral movement across SaaS ecosystems, and potential exposure of customer or partner data; all while evading detection from traditional tools that trust the Salesforce and Cloudflare domains in the redirect path.

[**See full execution chain exposed in 60 seconds**](https://app.any.run/tasks/3578ccac-3963-4901-8476-92dc5738cade/?utm_source=anyrunblog&utm_medium=article&utm_campaign=October_cyber_attacks_2025&utm_term=291025&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2025/10/image-9-1024x568.png)

Adversaries in this campaign misuse legitimate platforms to host phishing flows that evade automated detection. The combination of **trusted domains** and **multi-step redirection** makes these attacks particularly hard to catch without behavioral visibility.

Below are ready-to-use [**Threat Intelligence Lookup**](https://intelligence.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=October_cyber_attacks_2025&utm_term=291025&utm_content=linktolookup) **queries** to expand visibility, uncover infrastructure overlaps, and convert findings into **detection rules**, not just IOCs:

**Google-like application domains:** [domainName:”apply.g\*.com” OR domainName:”hire.g\*.com”](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=October_cyber_attacks_2025&utm_term=291025&utm_content=linktolookup#{%22query%22:%22domainName:%5C%22apply.g*.com%5C%22%20OR%20domainName:%5C%22hire.g*.com%5C%22%22,%22dateRange%22:180}%2...