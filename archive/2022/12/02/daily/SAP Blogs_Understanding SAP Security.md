---
title: Understanding SAP Security
url: https://blogs.sap.com/2022/12/01/understanding-sap-security/
source: SAP Blogs
date: 2022-12-02
fetch_date: 2025-10-04T00:17:00.973878
---

# Understanding SAP Security

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* Understanding SAP Security

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5392&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Understanding SAP Security](/t5/financial-management-blog-posts-by-members/understanding-sap-security/ba-p/13563816)

![integritty](https://avatars.profile.sap.com/f/d/idfd9f90b41e871f7d3624472d01a265f983c78378f786ae3da2fb8bc5fefa3b52_small.jpeg "integritty")

[integritty](https://community.sap.com/t5/user/viewprofilepage/user-id/45250)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5392)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5392)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563816)

‎2022 Dec 01
11:23 PM

[23
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5392/tab/all-users "Click here to see who gave kudos to this post.")

23,666

* SAP Managed Tags
* [Governance, Risk, Compliance (GRC) and Cybersecurity](https://community.sap.com/t5/c-khhcw49343/Governance%252C%2520Risk%252C%2520Compliance%2520%28GRC%29%2520and%2520Cybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)

* [Governance, Risk, Compliance (GRC) and Cybersecurity

  Product Category](/t5/c-khhcw49343/Governance%25252C%2BRisk%25252C%2BCompliance%2B%252528GRC%252529%2Band%2BCybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)

View products (1)

As cyber threats grow more dangerous and frequent, the once clear boundaries between SAP security, cyber security and compliance have started to blur. Traditionally, SAP security comprised the tools and processes that controlled what users can access inside an SAP landscape. With malicious actors now penetrating and lurking deep inside corporate networks, SAP security must go far beyond its basic access control function.

**Why Does an SAP Landscape Need Protection?**

Strong security countermeasures more critical than ever to protect SAP landscapes from threats that range from cyber criminals, industrial spies and nation state actors to malicious insiders. There are two primary reasons to implement rigorous defensive measures. First, the data held in the SAP landscape is attractive to hackers. Your SAP hosting environment contains lots of confidential information (such as financial records) and sensitive procedures (such as paying inventory). It may contain personal information about customers as well as bank account data and intellectual property. Data from an SAP system could be used for identity theft, fraud, industrial espionage and international espionage as well as “CEO frauds,” which involve hackers tricking employees into wiring funds to offshore bank accounts.

The other risk has to do with disruption. Malicious actors can cause your business to cease operations through Denial of Service (DoS) attacks, root access abuse and ransomware. Without proper countermeasures and controls, your business is vulnerable.

**What is SAP Security vs. Cyber Security?**

The answer to this question used to be simple. Cyber security services primarily protected organizations against external threats and SAP security, in contrast, focused on internal risks. Perimeter-oriented, cyber security countermeasures used to concentrate on keeping bad actors out of the network and away from SAP systems. This involved activities like intrusion detection, firewall monitoring and Identity and Access Management (IAM). If there was suspicious behavior, the Security Operations (SecOps) team would detect and investigate the issue and if it appeared to pose a threat – neutralize it.

The assumption of SAP security was that any user on the network was allowed to be there. The goal was to ensure that users had a level of access appropriate to their role, and in compliance with the company’s SAP Governance, Risk Management and Compliance (GRC) program. Segregation of Duties (SoD) offers an example. If an employee has the ability to create vendors in the SAP accounting system, he or she should not have the power to pay vendors as well. Having this SoD risk would create a compliance problem and expose the company to fraud.

**THOUGH ALWAYS INTERDEPENDENT, CYBER SECURITY AND SAP SECURITY ARE NOW MUCH MORE CLOSELY LINKED.**

If an employee’s SAP access patterns raise suspicions, SecOps should investigate to see if the person is doing something wrong or if a hacker is impersonating the user with stolen credentials. However, SecOps has to notice the problematic behavior, which doesn’t always happen. This overlap has grown far more intense.

Highly sophisticated hackers, sometimes even from foreign intelligence services, can lurk inside SAP landscapes for months, amassing information on who’s who and where the most valuable data is located. Then, using encryption, they can exfiltrate massive amounts of confidential data before being discovered. That is, if they’re discovered at all. For this reason, organizations benefit more than ever from an integrated security and compliance model that addresses insider, outsider and regulatory risks.

**SAP Security Concepts**

SAP security encompasses three core areas of cyber security: access control, data security and application security. To be secure, an SAP landscape is subject to strict access controls, and the system data should be protected as well as possible. Finally, the application itself should be subject to strong security safeguards.

In practice, getting all three of these SAP security concepts to work in harmony means applying the best available security tools and practices to the SAP landscape. For example, if the organization uses Multi-Factor Authentication (MFA) to grant network access permission to external, mobile users, that control should also be applied to anyone else wishing to access the SAP systems.

Then, within SAP, a data security policy should enforce restrictions on data access by role. Securing the application involves patch management and strict Privileged Access Management (PAM) controls to ensure that no unauthorized person can get administrative access to the SAP back end.

**What is SAP Security and Authorization?**

Controlling access to data on an SAP system, or any system, for that matter, is a process with three elements. First is identity. The user must establish his or her identity to gain access to the data. This might mean being an employee or showing credentials like a driver’s license to get permission to log on. Then, there is authentication, the step where the SAP system checks to see if the user is really who they say they are. This is typically a username and password. After authentication comes authorization.

Authorization is a step in access control that matches the user with the systemic and data access privileges held by the user. For example, an accounting department staff member should only have permission to use the accounting module and make use of (appropriate) accounting d...