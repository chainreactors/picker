---
title: Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US
url: https://any.run/cybersecurity-blog/mirage2fa-phishing-targets-us-companies/
source: Over Security
date: 2026-08-18
fetch_date: 2026-08-19T02:57:41.047538
---

# Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Mirage2FA-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US

August 18, 2026

[Add comment](#comments-22613)
2538 views
11 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Mirage2FA-1024x497.png)

  #### Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US

  2538
  0](https://any.run/cybersecurity-blog/mirage2fa-phishing-targets-us-companies/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/blindspots-1024x497.png)

  #### Intelligence-Driven SOC: Modernizing Threat Monitoring and Detection Engineering for Ultimate MTTR Reduction

  11919
  0](https://any.run/cybersecurity-blog/threat-monitoring-ti-feeds/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Supply_Chain_Security-1024x497.png)

  #### Supply Chain Security: How ANY.RUN Helps US and EU Enterprises Prevent Incidents

  6980
  0](https://any.run/cybersecurity-blog/supply-chain-security-for-us-and-eu-companies/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Mirage2FA Hijacks Companies’ Microsoft 365 Sessions, with Over 4K Victims in the US

Mirage2FA is an active phishing-as-a-service toolkit built to steal Microsoft 365 credentials and authenticated sessions through Adversary-in-the-Middle (AiTM) attacks.

[ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=mirage2fa-phishing-blog&utm_term=180826&utm_content=linktolanding) research shows that **63.7% of identified victims are in the US**, with [Technologies](https://any.run/by-industry/technology/?utm_source=anyrunblog&utm_medium=article&utm_campaign=mirage2fa-phishing-blog&utm_term=180826&utm_content=linktotechnology), [Manufacturing](https://any.run/by-industry/manufacturing/?utm_source=anyrunblog&utm_medium=article&utm_campaign=mirage2fa-phishing-blog&utm_term=180826&utm_content=linktomanufacturing), and Education among the most targeted industries. The operation has generated thousands of compromise events between 2024 and 2026, including stolen session cookies, passwords, and SSO access.

Once an authenticated Microsoft 365 session is hijacked, attackers may gain access to corporate email, sensitive data, and trusted business accounts, creating a path for **impersonation, fraud, and further compromise**. Detecting the attack before stolen sessions are reused can help security teams contain account takeover earlier and reduce the potential business impact.

## Key Takeaways

* **Mirage2FA bypasses conventional MFA to hijack active Microsoft 365 sessions.** The PhaaS toolkit uses an Adversary-in-the-Middle (AiTM) flow to capture credentials, 2FA codes, and authenticated session cookies.

* **Mirage2FA activity was linked to 3,518 unique organization email domains**, showing the campaign’s broad reach across US and EU corporate environments.\*

* **The kit shows a high potential compromise rate.** Of 9,426 unique targeted email addresses, **4,532 were potentially compromised — about 48%**.\*

* **The US is the main victim market.** **2,885 victims, or 63.7% of the total**, were located in the United States, while victim activity was recorded across 94 countries.

* **Session theft is the most common compromise outcome.** The dataset contains **9,332 potential compromise events**, including 4,561 cookie-theft events, 3,044 password/2FA events, 1,339 SSO logins, and 388 other outcomes.\*

* **Mirage2FA relies on browser-based delivery rather than binary malware.** .htm, .xhtml, and .svg stagers, QR codes, JavaScript obfuscation, and WebSocket-based AiTM activity allow the attack to run largely inside the browser.

* **Mobile users make up a significant share of successful activity.** **33.3% of successful login events came from mobile devices**, where phishing pages can be harder to inspect due to limited URL visibility.

* **Recurring technical patterns remain useful even as infrastructure changes.** The /xls/\*.js loader structure, and LINX\* markers provide hunting opportunities beyond individual domains and IP addresses.

**Note:** All victim, compromise, and campaign-scale figures in this report are approximate estimates based on the available dataset and represent potential impact rather than independently confirmed compromises.

![PhantomEnigma Threat Report from ANY.RUN](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Mirage2FA_article-block.png)

### Read Complete Mirage2FA Research in TI Reports

Get a detailed version of the report for SOC and MSSP teams:

* **A complete list of IOCs**
*** **Additional info on Mirage2FA**
*** **Access to other reports******
******[Available for users with ANY.RUN TI Core and Complete plans. See details →](https://intelligence.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=mirage2fa-phishing-blog&utm_term=180826&utm_content=linktopricing)******

***...