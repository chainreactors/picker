---
title: Bug Bounty: Insights from Our First-hand Experience
url: https://blog.compass-security.com/2024/05/bug-bounty-insights-from-our-first-hand-experience/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-08
fetch_date: 2025-10-06T17:19:07.289895
---

# Bug Bounty: Insights from Our First-hand Experience

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Bug Bounty: Insights from Our First-hand Experience](https://blog.compass-security.com/2024/05/bug-bounty-insights-from-our-first-hand-experience/ "Bug Bounty: Insights from Our First-hand Experience")

[May 7, 2024](https://blog.compass-security.com/2024/05/bug-bounty-insights-from-our-first-hand-experience/ "Bug Bounty: Insights from Our First-hand Experience")
 /
[Fabio Poloni](https://blog.compass-security.com/author/fpoloni/ "Posts by Fabio Poloni")
 /
[0 Comments](https://blog.compass-security.com/2024/05/bug-bounty-insights-from-our-first-hand-experience/#respond)

At Compass Security, we recently launched our managed bug bounty service. We openly invite hunters to probe our publicly exposed services for vulnerabilities. In return for their valuable feedback, we offer monetary bounties up to CHF 5000. This service complements our well-established penetration testing expertise, renowned for nearly 25 years.

## Out-hack the Hackers

Recently, a bug bounty hunter alerted us to a minor vulnerability in a publicly exposed WordPress instance at our subsidiary, Hacking-Lab. An API designed for administrative purposes was accessible over the Internet, allowing attackers to manipulate the web server into sending arbitrary requests to both external and internal servers.

Although we had implemented IP restrictions on the regular management interface of WordPress (a recommended practice to reduce the attack surface), we decided to expand those restrictions to cover the exposed API. We assumed the issue was resolved after patching, retesting, and notifying the hunter.

## The Bypass

Surprisingly, the hunter contacted us again, claiming continued access to the API despite our IP restrictions. Puzzled by how he had bypassed our security measures, we invited him to file another bug report, treating it as an IP restriction bypass and making him eligible for an additional bounty if he could substantiate his claim. He succeeded.

The bypass was straightforward: we had implemented the IP restriction on the Traefik reverse proxy in front of the WordPress instance, blocking all paths starting with /xmlrpc.php. However, the hunter utilized a double slash in front of the path (//xmlrpc.php), evading our filter.

Further investigation revealed that RFC2396 allows empty path segments, which are handled differently by different reverse proxies. Unlike nginx, which normalizes and removes empty paths, Traefik does not. To address this, we decided to globally ban the term xmlrpc.php in any path, accepting potential false positives but ultimately securing access to the API.

## Good things come in pairs

But that was not the end of the story. The Hacking Lab decided to create a challenge for this bug to train interested customers. In the process, a new bypass possibility was discovered. In the regex used, the dot token (.) was used to match any preceding path segments. As this token does not match newline characters the restriction could be bypassed using a URL-encoded newline (%0A) in the path.

The restriction has been improved again to cover these scenarios as well.

## Conclusion

In the end, the hunter received two bounties for discovering the bug as well as the first bypass, and we gained valuable knowledge from this incident:

1. **Sustained Vigilance:** The incident highlighted the need for a constant review of security measures. Regularly revisiting and reassessing the status quo ensures adaptability to emerging threats, contributing to continuous knowledge enhancement within the team.
2. **Transparent Communication:** Maintaining open channels with the bug bounty community is important. Encouraging researchers to share additional findings fosters collaboration and facilitates swift resolution of potential security issues.
3. **Efficency of Incentives:** The successful resolution and bounty payout act as positive reinforcement for the bug bounty program. Monetary incentives motivate security researchers to actively engage, expediting the identification and resolution of vulnerabilities.

If you are interested in receiving valuable inputs from bug bounty hunters all over the world, read more about our managed bug bounty at <https://www.compass-security.com/en/services/bug-bounty>.

If you want to find the third bypass in this series, go ahead and participate in our bug bounty program: <https://bugbounty.compass-security.com/bug-bounties/hacking-lab-bug-bounty>

[Bug Bounty](https://blog.compass-security.com/category/bug-bounty/), [Hacking-Lab](https://blog.compass-security.com/category/hacking-lab/), [Vulnerability](https://blog.compass-security.com/category/vulnerability/), [Web Application](https://blog.compass-security.com/category/webapp/)

[Bypass](https://blog.compass-security.com/tag/bypass/)[Hacking](https://blog.compass-security.com/tag/hacking/)

[##### Previous post

New Burp Extension: JWT-scanner](https://blog.compass-security.com/2024/04/new-burp-extension-jwt-scanner/ "Previous post: New Burp Extension: JWT-scanner")
[##### Next post

How to become a Hacker](https://blog.compass-security.com/2024/05/how-to-become-a-hacker/ "Next post: How to become a Hacker")

### Leave a Reply [Cancel reply](/2024/05/bug-bounty-insights-from-our-first-hand-experience/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

### Recent Posts

* [Ensuring NIS2 Compliance: The Importance of Penetration Testing](https://blog.compass-security.com/2025/09/ensuring-nis2-compliance-the-importance-of-penetration-testing/)
* [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/)
* [Taming The Three-Headed Dog -Kerberos Deep Dive Series](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/)
* [Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/)
* [xvulnhuntr](https://blog.compass-security.com/2025/07/xvulnhuntr/)

### Categories

Categories
Select Category
APT  (8)
Authentication  (18)
Bug Bounty  (6)
Entra ID  (3)
Evasion  (3)
Event  (34)
Exploiting  (18)
Forensic  (25)
Hacking-Lab  (18)
Hardening  (33)
Incident Response  (14)
Industrial Control Systems  (14)
Information Leakage  (7)
Internet of Things  (15)
Job  (2)
Linux  (8)
Log Management  (6)
Machine Learning  (3)
Malware Detection  (6)
Mobile  (10)
Networking  (17)
OS X  (1)
Patch  (6)
Penetration Test  (61)
Red Teaming  (15)
Research  (75)
Reversing  (13)
Risk Assessment  (10)
Scam  (1)
Social Engineering  (1)
Standards  (11)
SuisseID  (1)
Talk  (22)
Tools  (28)
Training  (19)
Uncategorized  (19)
Vulnerability  (46)
Web Application  (51)
Web Server  (13)
Windows  (31)
Wireless  (6)
Write-up  (26)
Youtube  (1)

### Tags

[Active Directory](https://blog.compass-security.com/tag/active-directory/)
[Advanced Metering Infrastructure](https://blog.compass-security.com/tag/advanced-metering-infrastructure/)
[Advisory](https://blog.compass-security.com/tag/advisory/)
[Application Security](https://blog.compass-security.com/tag/application-security/)
[ASFWS](https://blog.compass-security.com/tag/asfws/)
[ASP.NET](https://blog.compass-security.com/tag/asp-net/)
[Black Hat](https://blog.compass-security.com/tag/black-hat/)
[bloodhound](https://blog.compass-security....