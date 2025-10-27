---
title: Sandfly 4.4.0 - Agentless Linux Password Auditing and Data De-Duplication
url: https://sandflysecurity.com/blog/sandfly-4-4-0-agentless-linux-password-auditing-and-data-de-duplication
source: Sandfly Security Blog RSS Feed
date: 2023-04-20
fetch_date: 2025-10-04T11:33:20.826909
---

# Sandfly 4.4.0 - Agentless Linux Password Auditing and Data De-Duplication

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 4.4.0 - Agentless Linux Password Auditing and Data De-Duplication

19 April 2023

Product Update

Sandfly 4.4.0 has two major new features we are excited about sharing:

* Agentless password auditor that works across all Linux distributions.
* De-duplicating events resulting in a 99%+ reduction in data in the database and sent to SIEM tools such as Splunk.

## Agentless Password Auditor

Stolen and weak credentials on Linux are perhaps **the** major way hosts are compromised. We pay very special attention to SSH credentials with our [SSH Hunter](https://sandflysecurity.com/platform/ssh-credential-security/), but today we are closing the loop on username/password use with our agentless password auditor.

Weak passwords on Linux systems can be exploited by malware or dedicated attackers, leading to immediate system compromises. The challenge lies in effectively testing weak passwords across all Linux systems, CPU types, and doing so securely without the need to centralize password hashes for cracking.

We are introducing a mechanism where we bring the password auditing directly to each host. We check for vulnerable passwords on systems regardless of Linux distribution. We even do it on embedded Linux devices.

### Password Brute Force Threat Model

The primary threat model under consideration involves external attackers attempting to gain access to hosts through channels such as SSH, rather than individuals who have obtained password hashes and employ specialized password crackers. By focusing on this threat model, highly-targeted password auditing can be implemented, effectively shifting the attack window beyond the capabilities of most external intruders.

### Password Brute Force Attack Window

External attackers attempting brute force attacks are constrained by several factors, which limit the number of attempts they can execute:

1. Network latency
2. Time delays due to invalid authentication attempts
3. Auto-banning of IP addresses
4. Detection by security teams due to increased attack noise

Given these limitations, attackers without access to password hashes are unable to carry out extensive brute force attacks, as they would be restricted to dozens or, at most, hundreds of attempts before potentially being blocked.

As a result, a targeted audit of the most vulnerable password types on the host itself proves to be highly efficient and offers significant security improvements against simple compromises on Linux. Since attackers are more likely to begin with the weakest passwords, focusing on these vulnerabilities addresses the most probable threats while recognizing the limitations faced by external attackers.

### On Host Password Auditing Advantages

On-host password auditing for Linux offers numerous benefits, which include:

1. Compliance with organizational or industry-specific security policies such as GDPR, PCI, or HIPAA by avoiding the transfer of password hashes off-host for auditing.
2. Compatibility with a wide range of Linux distributions, including legacy systems up to a decade old.
3. Support for various CPU types, including Intel, AMD, Arm, and MIPS.
4. Capability to audit challenging situations, such as embedded Linux devices, for weak passwords.
5. Customization options allowing users to define specific passwords to be banned from use.
6. Facilitating security teams in searching for passwords linked to ongoing incident response.
7. Scalability through the deployment of the password auditing engine on each endpoint, enabling independent audits.
8. Rapid auditing of the entire Linux infrastructure for weak passwords, often completed within seconds.

By employing on-host password auditing for Linux systems, organizations can enhance security, maintain compliance, and ensure comprehensive password assessments across diverse infrastructure.

### Password Auditing Sandfly Modules

We have included several built-in password auditing modules:

* ***user\_password\_auditor\_password\_is\_username*** *-* Username is the password. This is a major risk and is enabled by default.
* ***policy\_user\_password\_auditor\_top\_100***- User has a password in the Top 100 worst passwords.
* ***policy\_user\_password\_auditor\_top\_500*** - User has a password in the Top 500 worst passwords.
* ***policy\_user\_password\_auditor\_linux\_common*** - User has a password that is a common Linux user or service name.
* ***policy\_user\_password\_auditor\_custom\_password\_check***- Customer defined template of passwords they want to make sure are not being used anywhere.

### Username is Password

This module finds a very common and serious issue (especially on embedded devices): A password that is identical to the username. This is the primary brute force method used by many kinds of Linux malware families, including most cryptominers and botnets.

For example Sandfly will find accounts such as:

* admin/admin
* ubuntu/ubuntu
* root/root
* etc.

This module is enabled by default as it executes in a split second even on embedded systems. Below you can see an example where a Raspberry Pi has a username that is identical to the password.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Password Audit Finds Username Identical to Password](https://www.datocms-assets.com/56687/1681861782-user-password-auditor-password-is-username.png?auto=format&dpr=2&q=60&w=920 "Linux Password Audit Finds Username Identical to Password")

### Top 100 and 500 Worst Passwords

Additional modules are available to audit users utilizing the Top 100 and 500 worst passwords. The Top 100 checks require minimal time on most systems, making them highly valuable. The Top 500 checks may take longer but could be worthwhile as less frequent checks for many organizations.

These modules are not enabled by default. To activate them, review the policy sandfly area and enable the desired modules or run them manually.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Top 100 worst passwords on Linux found.](https://www.datocms-assets.com/56687/1681876603-policy-user-password-auditor-top-100.png?auto=format&dpr=2&q=60&w=920 "Top 100 worst passwords on Linux found.")

### Top Linux Usernames as Passwords

We also have a module that looks for common Linux usernames (e.g. "nagios") as the password. This also finds notorious combinations such as "root/superuser", "www/administrator", and more. This module takes about as much time as the Top 100 worst password module discussed above to run. This module will again need to be enabled or run it manually.

### Custom Password Auditing

As with all Sandfly modules, the password auditing modules can be cloned and modified to search for custom parameters. For example, some organizations may have shared passwords across accounts (commonly referred to as the infamous corporate login credential). These passwords pose a particularly high risk, as they are rarely changed, their usage is difficult to track, and they often persist even after employees depart.

Sandfly enables users to tailor searches for passwords of this nature. With a small list of passwords, the check is nearly instantaneous and is a valuable addition to organizations facing this issue.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Custom password auditing on Linux.](https://www.datocms-assets.com/56687/1681862763-policy-user-password-auditor-custom.png?auto=format&dpr=2&q=60&w=920 "Custom password auditing on Linux.")

Below we see a custom password auditing module example. This module can be enabled and it then will provide continuous monitoring to make sure these banned passwords do not show up on any accounts once weeded out. Any account showin...