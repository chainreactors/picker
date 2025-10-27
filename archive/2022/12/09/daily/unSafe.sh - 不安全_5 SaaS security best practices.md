---
title: 5 SaaS security best practices
url: https://buaq.net/go-139264.html
source: unSafe.sh - 不安全
date: 2022-12-09
fetch_date: 2025-10-04T00:57:21.779899
---

# 5 SaaS security best practices

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

5 SaaS security best practices

Just about anywhere you look, organizations are relying on Software-as-
*2022-12-8 21:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-139264.htm)
阅读量:18
收藏*

---

Just about anywhere you look, organizations are relying on Software-as-a-Service (SaaS) apps like Dropbox and Hubspot to help power their businesses. With more SaaS apps, however, comes increased security risks.

While SaaS is without a doubt the easiest and most accessible way for businesses to reap the benefits of the cloud, these services are delivered online—which can make it easier for data leaks to happen or threat actors to get a hold of sensitive data. **In fact, [43 percent of organizations have dealt with one or more](https://cloudsecurityalliance.org/press-releases/2022/04/12/new-cloud-security-alliance-survey-finds-saas-misconfigurations-may-be-responsible-for-up-to-63-percent-of-security-incidents/#:~:text=At%20least%2043%20percent%20of%20organizations%20report%20that%20they%20have%20dealt%20with%20one%20or%20more%20security%20incidents%20because%20of%20a%20SaaS%20misconfiguration.) security incidents caused by a SaaS misconfiguration**.

You might be asking yourself though: Doesn’t my cloud provider [take care of security for me](https://www.malwarebytes.com/cybersecurity/business/what-is-cloud-security)? Well, yes and no.

Your cloud provider will protect your cloud infrastructure in some areas, but under the shared responsibility model, your business is responsible for handling things such as identity and access management, endpoint security, data encryption, and so on.

The good news is that there’s a set of SaaS security best practices to help keep your business from becoming another statistic.

Whether your business uses Office 365, Salesforce, Google Drive, or another SaaS app, this blog will help guide your journey to SaaS security with five best practices.

### 1. Manage SaaS sprawl

You might be surprised to find that our journey into SaaS security begins not with an answer, but with a question: **are you suffering from SaaS sprawl?**

SaaS sprawl is a situation where a business is bloated with so many different (and even duplicate) SaaS apps that IT can no longer manage them effectively.

Most departments now have 40 – 60 SaaS tools each, with 200+ apps at the company level—**and for small businesses, [only 32 percent of these apps are IT-approved](https://productiv.com/wp-content/uploads/2021/09/productiv-the-state-of-saas-sprawl-in-2021.pdf)**. Not only does SaaS sprawl waste money, but it has security risks as well.

For one, SaaS sprawl makes it harder for IT and security teams to ensure compliance or identify security risks that expose sensitive data. Admins just don’t have the time (or the visibility) to individually check and update potential issues for each app.

Another issue is that SaaS sprawl and “**shadow IT**” (i.e. SaaS apps that have bypassed IT’s typical vetting procedures) are closely related—the more shadow IT, the worse the SaaS sprawl. As if trying to manage a ton of authorized SaaS apps wasn’t enough, IT teams don’t even know about the unauthorized ones—and they definitely can’t fix what they can’t see!

All of this is to say: tackling SaaS sprawl before anything else will make it easier for you to get into the more granular aspects of SaaS security. Some best practices to manage SaaS sprawl include:

* **Discover all apps**: Regularly audit all SaaS apps being used across the business, IT-approved or not.
* **Create a vetting process**: Have a consistent method to audit app requests for security, compliance, and other details.
* **Educate employees**: IT should regularly caution employees about the risks of using unauthorized apps.
* **Bridge the gap between IT and other departments**: Put a process in place that allows team members to freely approach IT with new apps they wish to use.

### 2. Use Single Sign-On (SSO) paired with Multi-Factor Authentication (MFA)

SSO is a nonnegotiable security requirement for any company with more than five employees.

SSO solutions such as Okta, Duo, and Microsoft Azure Active Directory (AD) allow you to access all SaaS applications after entering your credentials just one time. Not only is SSO more convenient for end users, but it gives IT and Security teams the **ability to effectively manage user accounts across dozens or hundreds of vendors**.

SSO also makes it much easier to enforce **Multi-Factor Authentication (MFA)**, [a crucial extra level of SaaS security](https://www.malwarebytes.com/blog/news/2017/01/understanding-the-basics-of-two-factor-authentication), across all of your accounts.

After signing in using SSO, for example, a user is prompted with MFA to confirm the session using “something they have” (i.e by receiving a push notification or text on their phone).

### 3. Manage identity and access to SaaS applications

Each user in a cloud environment has their own roles and permissions governing the access they get to certain parts of the cloud, and because SaaS workloads are accessed online, all hackers need are your credentials to get the “keys to the kingdom.”

This is why strong [identity and access management (IAM)](https://www.malwarebytes.com/blog/explained/2022/04/why-identity-management-matters/) policies are so essential to cloud security.

Identity and access management is a means of controlling the permissions and access for users of cloud resources. You can think of IAM less as a single piece of software and more of a framework of processes, policies, and technology. Some IAM best practices include:

* **Removing dormant accounts**
* **Only giving privileged access to those who truly need it**
* **Enforcing strict password policies**

According to [Palo Alto Networks](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/executive-summary-unit-42-cloud-threat-report-volume-6), most known cloud data breaches start with misconfigured IAM policies or leaked credentials.

Specifically, researchers found that **IAM misconfigurations cause [65 percent of detected cloud data](https://www.paloaltonetworks.com/resources/research/unit42-cloud-with-a-chance-of-entropy) breaches**, with the runners up being weak password usage (53 percent) and allowing password reuse (44 percent).

### 4. Use a strong cloud malware scanner

Did you know that malware delivered through cloud storage apps such as Microsoft OneDrive, Google Drive, and Box accounted for **[69 percent of cloud malware downloads in 2021](https://www.cybersecuritydive.com/news/netskope-cloud-malware-delivery/617061/)**?

It can be difficult to monitor and control all the activity in and out of SaaS cloud storage repositories, making it easy for malware to hide in the noise as it makes its way to the cloud.

[That’s where cloud storage scanning comes in.](https://www.malwarebytes.com/cybersecurity/business/benefits-of-a-malware-scanner-for-cloud-storage#:~:text=Secure%20file%20sharing%20in%20the%20cloud&text=Running%20malware%20scans%20can%20detect,keep%20cloud%20storage%20data%20secure.)

Cloud storage scanning is exactly what it sounds like: it’s a way to scan for malware in cloud storage apps like Box, Google Drive, and OneDrive. And while most cloud storage apps have malware-scanning capabilities, it’s important to have a second-opinion scanner as well.

[Reduce risk from cloud-based malware today](https://www.malwarebytes.com/business/cloud-storage-scanning)

A second-opinion cloud storage scanner is a great second line of defense for cloud storage because it’s very possible that your ma...