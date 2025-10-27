---
title: Experts Find Flaw in Replicate AI Service Exposing Customers' Models and Data
url: https://buaq.net/go-241556.html
source: unSafe.sh - 不安全
date: 2024-05-26
fetch_date: 2025-10-06T16:49:10.025224
---

# Experts Find Flaw in Replicate AI Service Exposing Customers' Models and Data

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c7b826c15f74ae21a6b3db2483078db8.jpg)

Experts Find Flaw in Replicate AI Service Exposing Customers' Models and Data

Machine Learning / Data BreachCybersecurity researchers have discovered a critical security flaw i
*2024-5-25 17:11:0
Author: [thehackernews.com(查看原文)](/jump-241556.htm)
阅读量:8
收藏*

---

Machine Learning / Data Breach

[![Replicate AI Service](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_NYJzMwaBmPPr2xgwv5e5G3gcXxOFfosCEdWWR6SQVy3GnGtNkVghRp7Gfat-Bcx5vh5sfcLZxfOpx2pZ8tPEwdCmfYQzUsLw8aDy43NB7qpXsGl_sZciwzLhtatN60dsR6AV-N4eIag-ks44Zu_RkLd6aOI1j8OeV_DshVZU88vBAY4fWaGEZ9rOZu3W/s728-rw-e365/wiz.png "Replicate AI Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_NYJzMwaBmPPr2xgwv5e5G3gcXxOFfosCEdWWR6SQVy3GnGtNkVghRp7Gfat-Bcx5vh5sfcLZxfOpx2pZ8tPEwdCmfYQzUsLw8aDy43NB7qpXsGl_sZciwzLhtatN60dsR6AV-N4eIag-ks44Zu_RkLd6aOI1j8OeV_DshVZU88vBAY4fWaGEZ9rOZu3W/s728-rw-e365/wiz.png)

Cybersecurity researchers have discovered a critical security flaw in an artificial intelligence (AI)-as-a-service provider [Replicate](https://replicate.com/) that could have allowed threat actors to gain access to proprietary AI models and sensitive information.

"Exploitation of this vulnerability would have allowed unauthorized access to the AI prompts and results of all Replicate's platform customers," cloud security firm Wiz [said](https://www.wiz.io/blog/wiz-research-discovers-critical-vulnerability-in-replicate) in a report published this week.

The issue stems from the fact that AI models are typically packaged in formats that allow arbitrary code execution, which an attacker could weaponize to perform cross-tenant attacks by means of a malicious model.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuUUskkMH9dUT3LF77_Q_irGuaE4LGjp-Am2Ls_UzGJ5EBnZHfuFiSvKs4OPE5KmfedBHcuZZVHS4Bh48UJx8brpwtg6Vr2Gepbaw-lGMIm9HjUhyphenhyphen2W5DVm5-ymwPS691Ie32TrCqFIv6SxNRA-jOKCKZrOB5dV7BfL0zVAhOO0neNkP9yv-XePBU1hN_0/s728-e365/wing-d.png)](https://thehackernews.uk/third-party-risk-management-saas "Cybersecurity")

Replicate makes use of an open-source tool called [Cog](https://github.com/replicate/cog) to containerize and package machine learning models that could then be deployed either in a self-hosted environment or to Replicate.

Wiz said that it created a rogue Cog container and uploaded it to Replicate, ultimately employing it to achieve remote code execution on the service's infrastructure with elevated privileges.

"We suspect this code-execution technique is a pattern, where companies and organizations run AI models from untrusted sources, even though these models are code that could potentially be malicious," security researchers Shir Tamari and Sagi Tzadik said.

The attack technique devised by the company then leveraged an already-established TCP connection associated with a Redis server instance within the Kubernetes cluster hosted on the Google Cloud Platform to inject arbitrary commands.

What's more, with the centralized Redis server being used as a queue to manage multiple customer requests and their responses, it could be abused to facilitate cross-tenant attacks by tampering with the process in order to insert rogue tasks that could impact the results of other customers' models.

These rogue manipulations not only threaten the integrity of the AI models, but also pose significant risks to the accuracy and reliability of AI-driven outputs.

"An attacker could have queried the private AI models of customers, potentially exposing proprietary knowledge or sensitive data involved in the model training process," the researchers said. "Additionally, intercepting prompts could have exposed sensitive data, including personally identifiable information (PII).

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_WRs2jRYPNRPdVnIJ52g0Zo3TY_c0FSwk8ZZN085hqm-nXig4b7WIZCpqdHexadU4EmZ402vX1EghcAxIZGa9lwLkWAPPYzPbg1gc5UZCbvTtOHQ3ozwiQAgJ1ahKFoOp8SZl-JN8_URGwiu9aTe5U2wiVHGEetM-S7kKkmgPMNdL_83d5HTJrLm7iBp6/s728-e365/cis-d.png)](https://thehackernews.uk/cis-hardened-images "Cybersecurity")

The shortcoming, which was responsibly disclosed in January 2024, has since been addressed by Replicate. There is no evidence that the vulnerability was exploited in the wild to compromise customer data.

The disclosure comes a little over a month after Wiz [detailed](https://thehackernews.com/2024/04/ai-as-service-providers-vulnerable-to.html) now-patched risks in platforms like Hugging Face that could allow threat actors to escalate privileges, gain cross-tenant access to other customers' models, and even take over the continuous integration and continuous deployment (CI/CD) pipelines.

"Malicious models represent a major risk to AI systems, especially for AI-as-a-service providers because attackers may leverage these models to perform cross-tenant attacks," the researchers concluded.

"The potential impact is devastating, as attackers may be able to access the millions of private AI models and apps stored within AI-as-a-service providers."

Found this article interesting? Follow us on [Twitter **](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

文章来源: https://thehackernews.com/2024/05/experts-find-flaw-in-replicate-ai.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)