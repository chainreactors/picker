---
title: Red Team Finds A Way  – (IN)Secure By Design
url: https://securitycafe.ro/2024/09/11/red-team-finds-a-way-insecure-by-design/
source: Security Café
date: 2024-09-12
fetch_date: 2025-10-06T18:28:18.852447
---

# Red Team Finds A Way  – (IN)Secure By Design

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

# Red Team Finds A Way – (IN)Secure By Design

[September 11, 2024](https://securitycafe.ro/2024/09/11/red-team-finds-a-way-insecure-by-design/ "3:03 pm") [Iulian Florea](https://securitycafe.ro/author/floreaiulian/ "View all posts by Iulian Florea") [Misc](https://securitycafe.ro/category/misc/) [Leave a comment](https://securitycafe.ro/2024/09/11/red-team-finds-a-way-insecure-by-design/#respond)

In our previous post, Red Team Finds A Way – Exploiting The Human Factor, we explored how the human element can often be the weakest link in a security chain, and how with proper authorization, it can be ethically exploited to enhance system security.

Today, we’re shifting our focus to the heart of many systems – the design itself. We’ll be dissecting the intricate web of (in)security that can be inadvertently woven into a system right from its inception. We’ll be exploring common design flaws, understanding how they can lead to vulnerabilities, and most importantly, discussing how to identify and rectify these issues to fortify your systems.

So, buckle up and get ready to navigate the labyrinth of secure and not-so-secure design practices. Remember, the journey to a secure system begins with understanding its potential weaknesses.

## You mentioned proxies?

During the active recon phase, an ASN scan is performed, and upon checking the scan, the following line pops up:

```
8080/tcp open  http-proxy syn-ack Squid http proxy 5.2
```

Might not be something interesting, as usually, during scanning internet facing proxies can be identified. However, it’s a good point spending some time trying to see if it can be also an ingress point. So, by editing the proxychains config we can use the proxy to try to access the internal network.

You might be wondering which ranges to scan. Upon looking up for private network ranges, we can see the following [here](https://en.wikipedia.org/wiki/Private_network):

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

For a more comprehensive range list with different destinations, you can also [check this out](https://en.wikipedia.org/wiki/Reserved_IP_addresses).

By kicking off scans, we manage to have a few hits, one of the IPs being a Domain Controller. Prior to external infrastructure checking, the red team operators looked for leaks, and identified multiple usernames and their naming convention.

Using a password spraying technique, a few users are compromised.

## Chaining vulnerabilities

Red teaming does not come only in the form of phishing, or exploiting humans. A way of getting within the organization can be exploiting internet facing systems.

If no critical vulnerabilities are identified that can grant further access within the application, or access to the underlying operating system, chaining vulnerabilities might be the only option.

Below, a broken access control was identified, allowing a low privileged user to view data about other users and organizations.

![](https://securitycafe.ro/wp-content/uploads/2024/06/image.png?w=1024)

Broken access control

Trying to access additional functionalities, such as inviting users was tried, however, that was not possible.

Looking further within the application it was noted that it was possible to upload SVG files, leading to a Stored Cross-Site Scripting (XSS).

![](https://securitycafe.ro/wp-content/uploads/2024/06/image-1.png?w=1024)

Triggered XSS

Another functionality was noted that would allow a low privileged user to assign the documents within the organization to other users. However, stealing the cookies was not an option, as the server had the ***httpOnly*** flag set.

Two options were viable at this point:

* Use the SVG file to redirect the user to a login page (which would look a little suspicious)
* Test for other attack vectors

The uploaded files were stored within the application, and upon further testing, it was observed that the application allows uploading HTML files, and due to missing security headers (such as the CSP header) – which is very common, it is possible to gather credentials.

For the initial Proof of Concept (PoC), a simple HTML login page was created by the offensive team to test the viability of this technique. Upon inputting the user and password, the credentials were successfully acquired by the team.

![](https://securitycafe.ro/wp-content/uploads/2024/06/image-3.png?w=683)

Test login panel

A custom callback server was created in order to gather the credentials, and the login page was customized in a way to mimic the default login. All that was left to be done was to assign the documents to multiple persons, including administrators.

This resulted in multiple administrator accounts compromises, allowing an attacker to login as an administrator user, resulting in the ability of the attacker to seeing confidential data pertaining to users and organizations.

## Shares, shares, and even more shares

Another very common technique upon gaining initial access to an internal network is slowly spidering the shares and looking for sensitive information.

The stored information on shares can vary, including:

* Financial information
* Configuration and backup files
* Hardcoded credentials
* Other sensitive information

How shall be this information protected within an Active Directory environment you might ask yourself. Well, one of the best methods of protecting this kind of information is implementing strict ACLs on shares to restrict access to authorized users and groups by using the principle of least privilege to ensure that users only have the necessary permissions to perform their tasks.

Going back to share spidering, there are a multitude of tools that can aid in this matter, such as:

* WinShareEnum
* Invoke-ShareFinder
* Other custom made tools or scripts

So… you spider the shares, and identify sensitive files. Now what?

You can try using them to access applications or do lateral movement, depending on the type of credentials that are discovered. Below is an example of hardcoded MSSQL credentials, which were further used to gain access to multiple databases.

![](https://securitycafe.ro/wp-content/uploads/2024/06/image-4.png?w=566)

Hardcoded credentials

![](https://securitycafe.ro/wp-content/uploads/2024/06/image-5.png?w=105)

Access to one of the databases

With access to multiple databases, an attacker would have the ability of exfiltrating sensitive information.

## Final thoughts

Many individuals believe that red teaming is solely about acquiring Domain Admin / Enterprise Admin. But that is a narrow perspective. In actuality, red teaming is about emulating real-world attacker techniques, identifying vulnerabilities, and upgrading defenses. It’s about thinking like a threat actor, not simply attempting to get the keys to the kingdom.

Red teaming’s ultimate goal is to improve an organization’s general security posture. Bu...