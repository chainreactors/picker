---
title: Expanding Phishing Detection at Scale with Automatic SSL Decryption
url: https://any.run/cybersecurity-blog/automatic-ssl-decryption/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-03
fetch_date: 2026-03-04T04:04:20.154643
---

# Expanding Phishing Detection at Scale with Automatic SSL Decryption

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
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
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
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
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![Expanding Phishing Detection at Scale with Automatic SSL Decryption](/cybersecurity-blog/wp-content/uploads/2026/03/ssl.png)

[Service Updates](/cybersecurity-blog/category/service-updates/)

# Expanding Phishing Detection at Scale with Automatic SSL Decryption

March 3, 2026

[Add comment](#comments-18853)
164 views
6 min read

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Expanding Phishing Detection at Scale with Automatic SSL Decryption

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/03/ssl-1024x497.png)

  #### Expanding Phishing Detection at Scale with Automatic SSL Decryption

  164
  0](/cybersecurity-blog/automatic-ssl-decryption/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Splunk_ent_blog-1024x497.png)

  #### ANY.RUN & Splunk Enterprise: Stronger Detection, Faster Response in Your SOC

  1645
  0](/cybersecurity-blog/splunk-enterprise-integration/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Proactive-Threat-Monitoring-1024x497.png)

  #### Turn Your SOC Into a Detection Engine: Rethinking Threat Monitoring

  860
  0](/cybersecurity-blog/threat-monitoring-ti-feeds/)

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Expanding Phishing Detection at Scale with Automatic SSL Decryption

90% of modern cyberattacks start with phishing and it’s getting worse. The volume of compromise attempts keeps surging, leaving companies more exposed to credential theft and heavy financial hits.

As phishing evolves, we focus on countering the core tactics that make it effective. That’s why [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=automatic-ssl-decryption&utm_term=030326&utm_content=linktolanding) is upgrading the threat detection capabilities of the [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=automatic-ssl-decryption&utm_term=030326&utm_content=linktosandboxlanding) across all subscription tiers with **the** **new SSL decryption technology**.

By extracting encryption keys directly from process memory, it **increases the detection rate of phishing inside the sandbox**, helping every user and SOC team in our community to see critical threats early.

## Phishing Pressure Is Rising. Detection Needs to Catch Up

Phishing remains the #1 cyber risk for companies, and its scale is intensifying. [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2025-03-18-gartner-predicts-ai-agents-will-reduce-the-time-it-takes-to-exploit-account-exposures-by-50-percent-by-2027) that AI agents will cut the time required to exploit exposed accounts by 50 percent by 2027. This means that the window for early detection is shrinking.

A top challenge in identifying [modern phishing](https://any.run/cybersecurity-blog/enterprise-phishing-analysis/) is encrypted HTTPS sessions. Credential harvesting, redirect chains, and token theft often look like normal web traffic.

![Traffic encryption prevents SOC teams from detecting phishing](/cybersecurity-blog/wp-content/uploads/2026/03/image-1024x576.png)

For SOC teams, this means more uncertainty. Alerts require deeper validation. Escalations increase. Investigations take longer. The risk of missing credential compromise rises.

Encrypted traffic is typically inspected using man-in-the-middle (MITM) interception. While effective in specific scenarios, MITM is resource-intensive and can disrupt realistic analysis. As encryption becomes the default channel for phishing, this approach is no longer enough.

Detection must work at scale, without slowing confirmation or disrupting execution.

## Scaling Phishing Detection Across Every Investigation with Automatic SSL Decryption

To remove one of the biggest obstacles in phishing detection for **every ANY.RUN user**, the [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=automatic-ssl-decryption&utm_term=030326&utm_content=linktosandboxlanding) now **automatically decrypts HTTPS traffic by default,**boosting visibility into the most evasive attacks.

![Automatic SSL decryption](/cybersecurity-blog/wp-content/uploads/2026/03/image2-1024x576.png)

Here’s how it works:

* The sandbox detonates the sample.

* **Session keys are pulled straight from process memory**, instead of relying on external interception or certificate substitution.

* Traffic is decrypted internally with the full plaintext available for analysis.

* [Suricata IDS rules](https://any.run/cybersecurity-blog/detection-with-suricata-ids/), detection signatures, payload inspection, [IOC extraction](https://any.run/cybersecurity-blog/enrich-iocs-with-threat-intelligence/) all work on the decrypted content.

* **Malicious traffic gets detected instantly**, and a conclusive verdict is delivered along with an actionable report in seconds.

By allowing Suricata rules and other detection mechanisms to analyze decrypted content immediately, **phishing gets confirmed without extra steps**, saving tens of minutes of analysts’ time.

Since traffic decryption applies to **100% of sandbox sessions**, the **phishing detection** coverage is now **systematically wider and stronger** across every investigation.

![](/cybersecurity-blog/wp-content/uploads/2026/03/SSL_results-1024x576.png)

Our stats show a **5x increase in SSL-decrypted phishing**after implementing the new technology in the sandbox. This also provided an **extra 60K confirmed malicious URLs**to [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=automatic-ssl-decryption&utm_term=030326&utm_content=linktotilookuplanding) monthly.

For your SOC, this means:

* **Higher detection rate:**Analysts now can see phishing that i...