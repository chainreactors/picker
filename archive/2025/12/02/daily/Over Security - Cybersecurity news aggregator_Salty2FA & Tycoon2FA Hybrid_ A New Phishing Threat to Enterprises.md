---
title: Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises
url: https://any.run/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-02
fetch_date: 2025-12-03T03:16:59.926067
---

# Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* + Search

![Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises ](/cybersecurity-blog/wp-content/uploads/2025/12/Salty2FA-Tycoon2FA-chimera-samples_-shutdown-or-operational-shift_.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises

December 2, 2025

[Add comment](#comments-17088)
2757 views
12 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/12/Salty2FA-Tycoon2FA-chimera-samples_-shutdown-or-operational-shift_-1024x497.png)

  #### Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises

  2757
  0](/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/12/Threat-coverage-updates-1024x497.png)

  #### Threat Coverage Digest: New Malware Reports and 5K+ Detection Rules

  405
  0](/cybersecurity-blog/threat-coverage-digest-november-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/11/5-Major-Cyber-Attacks-in-November-2025_cover-1024x497.png)

  #### Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More

  1878
  0](/cybersecurity-blog/major-cyber-attacks-november-2025/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises

 Phishing kits usually have distinct signatures in their delivery methods, infrastructure, and client-side code, which makes attribution fairly predictable. But recent samples began showing traits from two different kits at once, blurring those distinctions.

That’s exactly what [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Salty2fa_Tycoon2fa_hybrid_phishing_2025&utm_term=021225&utm_content=linktolanding) analysts saw with Salty2FA and Tycoon2FA: a sudden drop in Salty activity, the appearance of Tycoon indicators inside Salty-linked chains, and eventually single payloads carrying code from both frameworks. This overlap marks a meaningful shift; one that weakens kit-specific rules, complicates attribution, and gives threat actors more room to slip past early detection.

Let’s examine how this hybrid emerged, why it signals a shift in 2FA phishing, and what measures defenders should take in response.

## Key Takeaways

* **Salty2FA activity collapsed abruptly in late October 2025**, dropping from hundreds of weekly uploads to [ANY.RUN’s Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Salty2fa_Tycoon2fa_hybrid_phishing_2025&utm_term=021225&utm_content=linksandboxlanding) to just a few dozen.

* **New samples began showing overlapping indicators from both Salty2FA and Tycoon2FA**, including shared IOCs, TTPs, and detection rule triggers.

* **Code-level analysis confirmed hybrid payloads**: early stages matched Salty2FA, while later stages reproduced Tycoon2FA’s execution chain almost line-for-line.

* **Salty2FA infrastructure showed signs of operational failure**, forcing samples to fall back to Tycoon-based hosting and payload delivery.

* The overlap aligns with earlier hypotheses suggesting a **possible connection to Storm-1747**, who are known operators of Tycoon2FA.

* **Attribution remains essential**: Distinguishing between these “2FA” phishing kits helps analysts maintain accurate hunting hypotheses and track operator behavior.

* **Defenders should update detection logic** to account for scenarios where Salty2FA and Tycoon2FA appear within the same campaign or even a single payload.

* **More cross-kit overlap is likely**, meaning future phishing campaigns may blend infrastructures, payloads, and TTPs across frameworks.

## Part 1: Numbers Don’t Lie – A Sudden Drop in Salty2FA Activity

It all started around the end of October 2025, when the number of [the ANY.RUN sandbox submissions](https://app.any.run/submissions/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Salty2fa_Tycoon2fa_hybrid_phishing_2025&utm_term=021225&utm_content=linktoservice) showing activity linked to Salty2FA dropped sharply compared to previous periods.

Weekly phishing reports (see the [company’s X posts](https://x.com/search?q=from%3Aanyrun_app%20%22Phishing%20activity%20in%20the%20past%207%20days%22&src=typed_query&f=live)) show that, despite the usual fluctuations in overall upload volume, the average number of Salty2FA-related analysis sessions consistently stayed in the range of several hundred per week.

However, once November began, the decline became dramatic: By [November 11, 2025](https://x.com/anyrun_app/status/1988139884796600506), Salty2FA had fallen to the bottom of the weekly threat rankings, with only **51 submissions**, compared to its typical **250+ per week**.

![](/cybersecurity-blog/wp-content/uploads/2025/12/image-1024x495.jpg)

Along with indicators of compromise (IOCs) and hunting rules, the ANY.RUN sandbox’s **network block** previously triggered a near-constant alert tied to Salty-specific HTTP activity.

![](/cybersecurity...