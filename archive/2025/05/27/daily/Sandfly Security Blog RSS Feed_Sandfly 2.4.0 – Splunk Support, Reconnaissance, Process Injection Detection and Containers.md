---
title: Sandfly 2.4.0 – Splunk Support, Reconnaissance, Process Injection Detection and Containers
url: https://sandflysecurity.com/blog/sandfly-2-4-0-splunk-support-reconnaissance-process-injection-detection
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:27:59.176868
---

# Sandfly 2.4.0 – Splunk Support, Reconnaissance, Process Injection Detection and Containers

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.4.0 – Splunk Support, Reconnaissance, Process Injection Detection and Containers

12 January 2020

Product Update

Sandfly 2.4.0 has been released with major new features. We have boosted our Linux intrusion detection and incident response signatures to over 700. We have also begun building out the ability to detect advanced process injection attacks and expanded our container compromise support. Finally, we have enabled new features to support our upcoming Splunk app. Let’s go over all of these changes because there are a lot of them.

## Reconnaissance Sandflies

The first major change is we have introduced a new type of reconnaissance (recon) Sandfly. Prior versions had intrusion detection sandflies that looked for file, process, directory, user and log attacks. Additional sandflies were also included for incident response and templates for custom applications. Now, we have a new *recon* Sandfly type.

Recon sandflies gather remote system information with our agentless forensic engines that can be used to build machine learning detection models and help with threat hunting. Our first application to support this feature will be available for [Splunk](https://www.splunk.com/) which will be announced shortly.

Recon sandflies gather information such as running processes, logged in users, past logins, cron jobs, and other forensic data. This data can then be queried and aggregated by analytics engines and used to detect subtle and not-so-subtle attacks. Not just this, but it can also be used to build a past record of what was running on the system, who was logged in, what user accounts existed, etc. and this can be queried like any other record. This is perfect for threat hunting, compliance and incident response.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Recon Sandflies available to pull generic data from Linux agentlessly.](https://www.datocms-assets.com/56687/1635216293-recon-sandflies.png?auto=format&dpr=2&q=60&w=920 "Recon Sandflies available to pull generic data from Linux agentlessly.")

Customers using a Security Information Event Manager (SIEM) like Splunk will be able to apply advanced analytics to a rich dataset from Linux not available before. And of course, it all happens without loading any agents on your endpoints.

## Splunk App Coming

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Security Splunk Dashboard](https://www.datocms-assets.com/56687/1635216301-splunk-sandfly-dashboard.png?auto=format&dpr=2&q=60&w=920 "Sandfly Security Splunk Dashboard")

Splunk is the industry-leading SIEM and data analytics tool. As Splunk users know, it’s powerful and able to process data to produce extensive reports and assist threat hunting. However, Splunk (like all these tools) can only analyze the data they receive. As it turns out, getting consistently rich and valuable data from Linux is very hard. Often admins need to resort to audit logs that lack details and have inconsistent formatting that makes analysis difficult. Or, they need to load agents everywhere which is risky and often not practical.

Sandfly is here to fix these problems. Our agentless approach means Splunk users will now have instant visibility to all their Linux hosts with data that is designed *specifically* for security and forensics. If you have SSH access to your Linux endpoints, then Sandfly can run on them today and get this data.

## Linux Visibility Without Agents

One of the biggest problems with Linux is that it’s very hard to get visibility across all the platforms and distributions. Many organizations run CentOS, RedHat, Ubuntu, Debian, Fedora, Amazon Linux, Suse or all of them (at once). Organizations run Linux across physical hardware, Virtual Machines, cloud providers and even embedded devices like Raspberry Pi. Running agents all over the place is impractical in these real-world scenarios. Even if you could do it, agents often lack details that are

Sandfly solves these problems. We have extensive visibility across Linux for almost every CPU type from Intel to AMD to Arm to MIPS. If it runs Linux, chances are Sandfly can work on it and provide security visibility instantly without remote system impacts.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Splunk Searches for Malicious SHA1 Hash with Sandfly](https://www.datocms-assets.com/56687/1635216313-splunk-search-sha1-process-hash.png?auto=format&dpr=2&q=60&w=920 "Splunk Searches for Malicious SHA1 Hash with Sandfly")

What can you do with this visibility? Here are some search ideas:

* Process names that are running or have run on your Linux hosts going back as far as you have saved the data.
* Process hashes to see if a known malicious or suspicious binary has ever run on your hosts or is running right *now*.
* Usernames that are logged in or have ever logged in and where they originated.
* Usernames that have passwords enabled, SSH keys present or are running obsolete password hashes.
* Past or present network ports operating and what they were connected to at the time.
* Operating System values such as kernel versions, memory available, distribution names, mounts, CPU bugs and more.

The list of possibilities here is very large. If you are running Linux and don’t have visibility to do the above today, you will now have it with Sandfly and Splunk.

## Process Injection Attacks and More

We have added in Sandfly checks to detect process injection attacks for Linux and will be expanding this capability as we move forward. This is an advanced technique, but is getting more attention today and we have coverage for it in multiple ways.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Process Injection Attack Detection](https://www.datocms-assets.com/56687/1635216321-sandfly-process-injection.png?auto=format&dpr=2&q=60&w=920 "Linux Process Injection Attack Detection")

We have also added in Sandfly checks to look for default system commands using network ports where normally we wouldn’t expect to see them. This is a masquerading tactic where a system binary is replaced or attacked to make it listen on a network port or do other malicious activity.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Default Linux Command With Malicious Network Operation](https://www.datocms-assets.com/56687/1635216329-default-process-network-operating.png?auto=format&dpr=2&q=60&w=920 "Default Linux Command With Malicious Network Operation")

In addition to the above we have made the following new or improved Sandfly checks:

* New checks for processes connecting to suspicious paste sites known to harbor malware and malicious scripts.
* Multiple process injection detection methods.
* Hidden or suspiciously named LD\_PRELOAD paths often linked to stealth rootkit activity.
* Log file tampering detection now supports Arm and MIPS CPUs along with previous Intel/AMD variants.
* Immutable files under system cron directories are now flagged as malicious.
* Improved detection of netcat, socat and other backdoors inside system init and update scripts.
* Cron backdoor detection improved and expanded.
* At job backdoor detection improved and expanded.
* Login/logout persistence attacks improved and expanded.
* Network initialization scripts now checked for backdoors and suspicious commands.
* OS identification of hosts now includes all mounted file systems.

## Docker Container Compromise Detection

Sandfly has always been able to agentlessly detect suspicious and compromised processes inside Docker containers since version 1.0. We are now formalizing this capability by building out new features specific to container compromise detection. We are able t...