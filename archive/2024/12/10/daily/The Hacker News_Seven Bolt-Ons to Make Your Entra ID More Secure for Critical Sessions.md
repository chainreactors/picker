---
title: Seven Bolt-Ons to Make Your Entra ID More Secure for Critical Sessions
url: https://thehackernews.com/2024/12/seven-bolt-ons-to-make-your-entra-id.html
source: The Hacker News
date: 2024-12-10
fetch_date: 2025-10-06T19:43:04.674898
---

# Seven Bolt-Ons to Make Your Entra ID More Secure for Critical Sessions

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Seven Bolt-Ons to Make Your Entra ID More Secure for Critical Sessions](https://thehackernews.com/2024/12/seven-bolt-ons-to-make-your-entra-id.html)

**Dec 09, 2024**The Hacker NewsIdentity Security / Passwordless

[![Identity Security](data:image/png;base64... "Identity Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCJ7rf5bZv5r97iwifRWgnZXQbDcKNq92_y7pksIi7amFnML8YEpY9Tvy_LlUyEOgG3z7u32iYm-bqgzJcsBx6jh6uPPhrYdYJ0XU5qIfIZK6589-ckQ8DYfpa2RJXEKDWetbdA1al0NJDLsMheGzYHyVOFKDW9687s2IBBoHl4U51CjbU6gyqIfncGK8/s790-rw-e365/main.png)

Identity security is all the rage right now, and rightfully so. Securing identities that access an organization's resources is a sound security model.

But IDs have their limits, and there are many use cases when a business should add other layers of security to a strong identity. And this is what we at SSH Communications Security want to talk about today.

Let's look at seven ways to add additional security controls for critical and sensitive sessions for privileged users as a bolt-on to other systems.

## **Bolt-on 1: Securing access for high-impact IDs**

Since strong ID is a key element in privileged access, our model is to natively integrate with identity and access management (IAM) solutions, like Microsoft Entra ID. We use IAM as a source for identities and permissions and make sure your organization stays up–to–date with any changes in Entra ID on identities, groups, or permissions in real-time.

The native integration allows automating the joiners-movers-leavers process since if a user is removed from IAM, all access privileges and sessions are revoked instantaneously. This keeps HR and IT processes in sync.

Our solution maps security groups hosted in Entra ID with roles and applies them for role-based access control (RBAC) for privileged users. No role-based access is established without an identity.

With IDs linked to roles, we kick in additional security controls not available in IAMs, such as:

* **Privilege Elevation and Delegation Management (PEDM)** allows companies to employ fine-grained controls for tasks, providing just enough access with the least privilege only for the right duration of time. The access can be limited to specific tasks, applications, or scripts instead of entire servers.
* **Privileged account discovery** from cloud, hybrid and on-premises environments, including Local Administrator Accounts and Unix and Linux administrator accounts.
* **Isolated and independent identity source**: If anorganization doesn't want to introduce, for example, third-party identities to their IAM.
* External admin authorization for approving access to critical targets as an extra step of verification
* **Path to passwordless and keyless**: Mitigate the risk of shared credentials, such as passwords and authentication keys, by managing them when necessary or going for just-in-time access without passwords and keys.
* **Logging, monitoring, recording, and auditing sessions** for forensics and compliance.

[![Identity Security](data:image/png;base64... "Identity Security")](https://info.ssh.com/extending-microsoft-entra-for-critical-targets-and-data-with-ssh-zero-trust-suite)

## **Bolt-on 2: A proven-in-use, future-proof solution for hybrid cloud security in IT and OT**

A versatile critical access management solution can handle more than just IT environments. It can provide:

* **Centralized access management** to the hybrid cloud in IT and OT: Use the same, consistent and coherent logic to access any critical target in any environment.
* **Auto-discovery of cloud, on-premises and OT assets**: Get a global view into your asset estate automatically for easy access management.
* **Multi-protocol support**: IT (SSH, RDP, HTTPS, VNC, TCP/IP) and OT (Ethernet/IP, Profinet, Modbus TCP, OPC UA, IEC61850) are all supported.
* **Privileged Application security**: When you are hosting privileged applications (like GitHub repositories), we apply fine-grained security controls for each access.
* **Browser isolation for critical connections** over HTTP(S): Establishing isolated sessions to targets to control user web access to resources to protect resources from users and users from resources.

## **Bolt-on 3: Preventing security control bypass**

Some of the most common access credentials, SSH keys, go undetected by traditional PAM tools as well as the Entra product family. Thousands of sessions are run over the Secure Shell (SSH) protocol in large IT environments without proper oversight or governance. The reason is that proper SSH key management requires special expertise, since SSH keys don't work well with solutions built to manage passwords.

SSH keys have some characteristics that separate them from passwords, even though they are access credentials too:

* SSH keys are not associated with identities by default.
* They never expire.
* They are easy to generate by expert users but hard to track afterwards.
* They often outnumber passwords by 10:1.
* They are functionally different from passwords which is why password-focused tools can't handle them.

Ungoverned keys can also lead to [a privileged access management (PAM) bypass](https://www.ssh.com/blog/5-ways-to-bypass-pam). We can prevent this with our approach, as described below:

[![Identity Security](data:image/png;base64... "Identity Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuOW1nf0Zi6xGeoaMT-vRTXZMZ0fBDFAVeFMxhyIJYn55DyF1SLGMpxs91Zoy0wD0rF7831AeN_NjwnmNlVZ4Dj-6xBviBfEU3xEUoRg6ABEuUFLY_QXwzU4TZvz6GiLXklgthgPqOP3vHtZ7bjTMzIhvu_ATAMlTxL6oNocYy2EgxQvxxX6di5EbLiMw/s790-rw-e365/2.png)

## **Bolt-on 4: Better without passwords and keys –privileged credentials management done right**

Managing passwords and keys is good but going passwordless and keyless is elite. Our approach can ensure that your environment doesn't have any passwords or key-based trusts anywhere, not even in vaults. This allows companies to operate in a completely credential-free environment.

[![Identity Security](data:ima...