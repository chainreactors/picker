---
title: Okta breached last month, no customers compromised
url: https://buaq.net/go-144070.html
source: unSafe.sh - 不安全
date: 2023-01-04
fetch_date: 2025-10-04T02:58:48.483945
---

# Okta breached last month, no customers compromised

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

![]()

Okta breached last month, no customers compromised

Some of Okta’s source code fell into the hands of an unauthorized party
*2023-1-3 17:45:0
Author: [www.malwarebytes.com(查看原文)](/jump-144070.htm)
阅读量:17
收藏*

---

Some of Okta’s source code fell into the hands of an unauthorized party. The code was stolen from GitHub in the first part of December, according to a [statement](https://sec.okta.com/articles/2022/12/okta-code-repositories) issued by the company. In the same statement the company reassured users that there was no impact to any customers.

## Okta

Okta is an access management company based in San Francisco. According to its own website, Okta serves over 15,000 organizations. Essentially, Okta software allows employees to log in using single sign-on—a central platform where employees can log in once in order to access resources that have been assigned to them by an organization’s IT staff. The kind of identity-first approach to security is seen by some as an important underpinning of a [Zero Trust](https://www.malwarebytes.com/blog/explained/2020/01/explained-the-strengths-and-weaknesses-of-the-zero-trust-model/) security model.

## Stolen source code

GitHub alerted Okta about a possible breach in early December. An investigation by Okta revealed that the unauthorized access was used to copy code from the Okta Workforce Identity Cloud (WIC) code repositories.

Okta Workforce Identity Cloud provides a unified solution for secure access to any resource from any user that needs it, while maintaining the "Principle of Least Privilege" (POLP). The principle of least privilege is the idea that at any user, program, or process should have only the bare minimum privileges necessary to perform its function.

## Customers unaffected

In the statement that was also sent out by mail to security contacts, Okta told their customers that there was no unauthorized access to the Okta service, and no unauthorized access to customer data. This includes Okta's HIPAA, FedRAMP, and DoD customers. This is because Okta does not rely on the confidentiality of its source code for the security of its services. The Okta service remains fully functional and secure.

## Auth0

A few months ago, Okta subsidiary Auth0 disclosed a [similar incident](https://www.bleepingcomputer.com/news/security/auth0-warns-that-some-source-code-repos-may-have-been-stolen/), where code repository archives that predated Okta’s acquisition of Auth0 were stolen. It never became clear how the unauthorized party, that notified Okta about the possession of the archives, exfiltrated them.

## LAPSUS$

Okta themselves admitted to a [breach that happened in January of 2022](https://www.malwarebytes.com/blog/news/2022/03/okta-admits-366-customers-may-have-been-impacted-by-lapsus-breach), where the LAPSUS$ cybercriminal group accessed two active customer tenants within their SuperUser application and viewed limited additional information in certain other applications like Slack and Jira that could not be used to perform actions in Okta customer tenants. The January breach was initially believed to have a much larger impact and there was talk of possibly 366 customers that might be affected.

## Measures

When Okta learned of the latest incident, it placed temporary restrictions on access to Okta GitHub repositories and suspended all GitHub integrations with third-party applications. The company also reviewed the integrity of all the code that was recently placed on GitHub, and rotated GitHub credentials. Law enforcement has also been notified of the breach.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/01/okta-breached-again-no-customers-compromised
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)