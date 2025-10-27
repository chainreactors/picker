---
title: Major Cyber Attacks in August 2025: 7-Stage Tycoon2FA Phishing, New ClickFix Campaign, and Salty2FA
url: https://any.run/cybersecurity-blog/cyber-attacks-august-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-27
fetch_date: 2025-10-07T00:49:34.891253
---

# Major Cyber Attacks in August 2025: 7-Stage Tycoon2FA Phishing, New ClickFix Campaign, and Salty2FA

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

![Major Cyber Attacks in August 2025: 7-Stage Tycoon2FA Phishing, New ClickFix Campaign, and Salty2FA](/cybersecurity-blog/wp-content/uploads/2025/08/3-Major-Cyber-Attacks- in-August-2025_cover.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Major Cyber Attacks in August 2025: 7-Stage Tycoon2FA Phishing, New ClickFix Campaign, and Salty2FA

August 26, 2025

[Add comment](#comments-15633)
4273 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in August 2025: 7-Stage Tycoon2FA Phishing, New ClickFix Campaign, and Salty2FA

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

Major Cyber Attacks in August 2025: 7-Stage Tycoon2FA Phishing, New ClickFix Campaign, and Salty2FA

Phishing kits and stealers didn’t slow down this August, and neither did we. ANY.RUN analysts tracked some of the month’s most dangerous campaigns, from a **7-stage Tycoon2FA phishing chain** to **Rhadamanthys delivered via ClickFix**, and the discovery of **Salty2FA, a brand-new PhaaS framework linked to Storm-1575**.

All were analyzed inside [**ANY.RUN’s Interactive Sandbox**](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_august_25&utm_term=260825&utm_content=linktolanding), revealing full execution chains, decrypted traffic, and behavior missed by static tools. Combined with [**Threat Intelligence Lookup**](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_august_25&utm_term=260825&utm_content=linktolookup), these insights help SOC teams turn raw IOCs into actionable detection rules and cut investigation time when it matters most.

Let’s explore how these attacks worked, what they targeted, and the insights SOC teams can take away.

## Tycoon2FA: New 7-Stage Phishing Attack Beats Top Security Systems

[**Post on X**](https://x.com/anyrun_app/status/1950910894826758276)

ANY.RUN analysts uncovered a **multi-stage** [**Tycoon2FA campaign**](https://any.run/cybersecurity-blog/tycoon2fa-evasion-analysis/) that takes phishing beyond the usual fake login page. Instead, it runs victims through a **seven-step execution chain** packed with CAPTCHAs, button-hold checks, and validation screens; each designed to wear down humans and outsmart automated security tools. By the time the final phishing panel appears, most defenses have already failed.

Unlike mass phishing kits that cast a wide net, **Tycoon2FA is highly selective**. It goes after accounts that unlock access to **critical systems and sensitive data**, not just ordinary inboxes.

![](/cybersecurity-blog/wp-content/uploads/2025/08/Screenshot-2025-08-26-at-08.40.31-1024x440.png)

Recent campaigns have zeroed in on **government and military agencies**, as well as **financial institutions** ranging from global banks to regional insurers. Activity has been observed across the **US, UK, Canada, and Europe**, where a single stolen login can cause major financial losses or even disrupt national operations.

ANY.RUN data shows that **26% of Tycoon2FA cases analyzed in our sandbox involved the banking sector;** clear evidence that attackers are deliberately aiming at high-value targets.

### 7-Stage Execution Flow Exposed inside ANY.RUN

In a recent ANY.RUN analysis, Tycoon2FA unfolded in this order:

[Check Real Case: Multi-Stage Tycoon2FA Attack](https://app.any.run/tasks/f21e7c8b-abe8-4df5-b124-b6240354cb80/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_august_25&utm_term=260825&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2025/08/GxMHHE2W4AAxRpg-1024x1024.jpeg)

1. **Phishing email link →** The attack begins with a voicemail-themed phishing email containing a malicious link to lure the victim.

2. **PDF attachment →** Clicking the link triggers a fake PDF download, masking the next redirection step.

3. **Link inside PDF →** The PDF itself hides another embedded hyperlink, pushing the victim deeper into the chain.

4. **Cloudflare Turnstile CAPTCHA →** A CAPTCHA challenge filters out automated scanners by requiring human interaction.

5. **“Press & Hold” anti-bot check →** A second verification forces a hold-and-release gesture, further blocking automation.

6. **Email validation page →** The victim is asked to “verify” their email, confirming they are real and a worthwhile target.

7. **Final phishing panel →** At the end, a fake Microsoft login page is revealed, ready to steal the victim’s credentials....