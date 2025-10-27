---
title: Are You Making One of These 8 Cloud Security Mistakes?
url: https://buaq.net/go-169865.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:29.179029
---

# Are You Making One of These 8 Cloud Security Mistakes?

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

![](https://8aqnet.cdn.bcebos.com/4bbe89c9f2d231efbd6622a040e59a1f.jpg)

Are You Making One of These 8 Cloud Security Mistakes?

Though mass adoption has driven an increased awareness and need for cloud security, many businesses
*2023-6-22 21:9:45
Author: [www.sentinelone.com(查看原文)](/jump-169865.htm)
阅读量:15
收藏*

---

Though mass adoption has driven an increased awareness and need for cloud security, many businesses continue to make common cloud-related mistakes along their journey. Increased dependency on the cloud has presented challenges for enterprises on two fronts.

Externally, [threat actors](https://www.sentinelone.com/cybersecurity-101/threat-actor/) continue to sharpen their focus, developing attacks targeting organizations’ cloud footprint. From an internal standpoint, security leaders face the challenge of accelerating their business objectives, such as growth and innovation, while securing day-to-day operations and the infrastructure that supports it.

To better manage their [cloud risk](https://www.sentinelone.com/blog/ciso-wins-reducing-risk-across-endpoint-identity-and-cloud-surfaces/) profile, enterprises can optimize their cloud security journeys by examining common pitfalls. In this post, learn the top eight cloud security mistakes to avoid and how to implement the right defenses in place to minimize the risk of [cloud-based attacks](https://www.sentinelone.com/blog/threat-landscape-the-most-dangerous-cloud-attack-methods-in-the-wild-today/).

![](https://www.sentinelone.com/wp-content/uploads/2023/06/Are-You-Making-One-of-These-8-Cloud-Security-Mistakes-2-1024x536.jpg)

## Mistake #1 | Misconfigured Cloud Resources

In recent years, the sheer scale and complexity of cloud infrastructures have made it an attractive target for cybercriminals seeking to exploit vulnerabilities. The complexity is what invites the first common mistake that businesses make when adopting cloud. Since the interconnected nature of cloud services increases the potential attack surface, threat actors know that a single, successful compromise in one component can potentially impact all other interconnected systems.

When grappling with all the moving elements of cloud adoption, even one [misconfiguration](https://www.sentinelone.com/blog/surviving-the-storm-defending-against-cloud-misconfigurations-vulnerabilities-and-insider-threats/) or a few inadequate security settings can expose sensitive data and services to the public internet. When this happens, businesses inadvertently provide an entry point for attackers.

One of the most common mistakes is leaving cloud resources, such as storage buckets or databases, publicly accessible without security controls. This can happen when cloud resources are initially set up and the default security settings are not properly configured. In addition, misconfigured security groups and network access control lists (ACLs) can lead to unauthorized access to cloud resources. As an example, a security group that permits traffic from all IP addresses can expose resources to external threats.

Sticking to best practices for securing cloud resources by configuring them appropriately is imperative to mitigate these risks. Here are some best practices to consider:

* Conduct regular security configuration reviews to ensure [compliance](https://www.sentinelone.com/blog/compliance-in-the-cloud-navigating-the-complexities-of-cloud-security-regulations/) with industry standards, identify any misconfigured security groups, ACLs, or user accounts, and take the necessary actions to remediate them.
* Implement identity and access management (IAM) to provide access to cloud resources based on users’ job responsibilities, thereby restricting access to only what is necessary for their job function.
* Use automated configuration tools to ensure consistent, proper configuration of cloud resources, saving time and resources while reducing the possibility of errors.
* Monitor cloud resources for unusual activity or unauthorized access, enabling quick identification and resolution of potential security threats.

## Mistake #2 | Exposed Access Keys, Credentials, and More

Another common cloud security pitfall is related to the exposure of secrets, such as access keys that are hardcoded into code. One of the most prevalent missteps in cloud security is the storage of secrets in plain text or hard coded into code, which can result in unauthorized access to cloud resources.

For instance, if developers store access keys or other sensitive information in plain text, it can be effortlessly accessed by attackers who gain access to the code repository or when the code is deployed to a publicly accessible server. Similarly, if access keys are hardcoded into code, they can be easily exposed through source code leaks or public repositories.

The following best practices can help security teams effectively manage secrets:

* Use a secure secrets management system – Employ a secure secrets management system to store all sensitive information. This system should have proper access controls and encrypted and protected secrets.
* Avoid storing secrets in plain text – Refrain from keeping secrets in plain text or hardcoding them into code. Instead, use environment variables or configuration files to store secrets.
* Restrict access to secrets – Limit access to only those requiring it. Follow IAM best practices to grant access to secrets based on job responsibilities.
* Regularly rotate secrets – Rotate secrets, such as access keys, regularly to prevent unauthorized access. This can help limit the impact of breaches and reduce the risk of unauthorized access.
* Monitor for secret usage – Monitor secret usage to detect and prevent unauthorized access. By establishing an activity baseline for critical secrets, teams can better understand normal activity versus abnormal activity. This can help identify potential security threats and take appropriate actions to mitigate them.

## Mistake #3 | Not Using Multi-Factor Authentication (MFA)

Multi-factor authentication (MFA) is an essential security measure that should be considered, especially when securing cloud resources. Without MFA in place, an attacker only needs to compromise a user’s password to gain unauthorized access to cloud resources. This can happen through various means, such as [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) attacks, [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everything-you-need-to-know/), or other methods.

Enabling MFA significantly strengthens the security posture of cloud environments by requiring an additional layer of verification, reducing the risk of account compromises, unauthorized access, and [data breaches](https://www.sentinelone.com/cybersecurity-101/what-is-a-data-breach/). It adds an extra barrier for attackers, making it harder for attackers to gain control over user accounts and access sensitive resources.

Following the best practices for using MFA are essential for warding off unauthorized access.

* Enable MFA for all user accounts – It is crucial to enable MFA for all user accounts, including administrators and privileged users. This can help prevent unauthorized access to cloud resources and ensure that all users are subject to the same level of security measures.
* Use a trusted MFA solution – A trusted MFA solution compatible with the organization’s cloud infrastructure can help ensure that MFA is correctly integrated and configured. This will make it easier to manage and monitor MFA usage and increase the overall security of the organization’s cloud resources.
* Ed...