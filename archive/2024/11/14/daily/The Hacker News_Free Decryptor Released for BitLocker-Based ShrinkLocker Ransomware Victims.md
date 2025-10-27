---
title: Free Decryptor Released for BitLocker-Based ShrinkLocker Ransomware Victims
url: https://thehackernews.com/2024/11/free-decryptor-released-for-bitlocker.html
source: The Hacker News
date: 2024-11-14
fetch_date: 2025-10-06T19:32:28.468541
---

# Free Decryptor Released for BitLocker-Based ShrinkLocker Ransomware Victims

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

# [Free Decryptor Released for BitLocker-Based ShrinkLocker Ransomware Victims](https://thehackernews.com/2024/11/free-decryptor-released-for-bitlocker.html)

**Nov 13, 2024**Ravie LakshmananRansomware / Data Protection

[![ShrinkLocker Ransomware](data:image/png;base64... "ShrinkLocker Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjz_uMSBsG9ISsJ128U1vg1lTJdk_X4r_gLkjBw2fKkYkB7EQYPqTlybszrn6G3eu1E-sAd03CiVMv2V3lZMhCpf7e3yHOe2UJFFkM_gz2WUY65lhmABuRSTT_AmqvkY2L_1UxceTNGZlV161ZZDNrM4sUmd6wDBpXdgTewC2eOuU7aNCYsFHJ2VkffM15U/s790-rw-e365/ransomware.png)

Romanian cybersecurity company Bitdefender has released a free decryptor to help victims recover data encrypted using the ShrinkLocker ransomware.

The decryptor is the result of a [comprehensive analysis](https://www.bitdefender.com/en-us/blog/businessinsights/shrinklocker-decryptor-from-friend-to-foe-and-back-again) of ShrinkLocker's inner workings, allowing the researchers to discover a "specific window of opportunity for data recovery immediately after the removal of protectors from BitLocker-encrypted disks."

ShrinkLocker was [first documented](https://thehackernews.com/2024/06/rebranded-knight-ransomware-targeting.html) in May 2024 by Kaspersky, which found the malware's use of Microsoft's native BitLocker utility for encrypting files as part of extortion attacks targeting Mexico, Indonesia, and Jordan. It appears to have been adapted from benign ten-year-old code.

Bitdefender, which investigated a ShrinkLocker incident targeting an unnamed healthcare company in the Middle East, said the attack likely originated from a machine belonging to a contractor, once again highlighting how threat actors are increasingly [abusing trusted relationships](https://securelist.com/trusted-relationship-attack/112731/) to infiltrate the supply chain.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In the next stage, the threat actor moved laterally to an Active Directory domain controller by making use of legitimate credentials for a compromised account, followed by creating two scheduled tasks for activating the ransomware process.

While the first task executed a Visual Basic Script ("Check.vbs") that copied the ransomware program to every domain-joined machine, the second task – scheduled for two days later — executed the locally deployed ransomware ("Audit.vbs").

The attack, Bitdefender said, successfully encrypted systems running Windows 10, Windows 11, Windows Server 2016, and Windows Server 2019. That said, the ShrinkLocker variant used is said to be a modified version of the original version.

Described as simple yet effective, the ransomware stands out for the fact that it's written in VBScript, a scripting language that Microsoft said [is being deprecated](https://thehackernews.com/2024/05/the-end-of-era-microsoft-phases-out.html) starting the second half of 2024. Plus, instead of implementing its own encryption algorithm, the malware weaponizes BitLocker to achieve its goals.

The script is designed to gather information about the system configuration and operating system, after which it attempts to check if BitLocker is already installed on a Windows Server machine, and if not, installs it using a PowerShell command and then performs a "forced reboot" using [Win32Shutdown](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32shutdown-method-in-class-win32-operatingsystem).

[![ShrinkLocker Ransomware](data:image/png;base64... "ShrinkLocker Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj18ymenaaNKu4eoJkokHml2a2hy_pz8VNripemzpbI7EuuwovR9sCzuiR7tUIE7LI_o1TLxya1V2mZCZfoOrMnWOtdMYIXjOpHhU5cyL0lOU4uN1QJ26pwBgv17o7Iu5ieMBHPNiRA2qb5YoyTj2GxMQiY1p_6Rbl1_Y4ViMjumnthIghcav0wFBsWSORD/s790-rw-e365/domain.png)

But Bitdefender said it noted a bug that causes this request to fail with a "Privilege Not Held" error, causing the VBScript to be stuck in an infinite loop due to an unsuccessful reboot attempt.

"Even if the server is rebooted manually (e.g. by an unsuspecting administrator), the script does not have a mechanism to resume its execution after the reboot, meaning that the attack may be interrupted or prevented," Martin Zugec, technical solutions director at Bitdefender, said.

The cybersecurity vendor told The Hacker News that the bug is present in all variants of ShrinkLocker, but that it only manifests in certain older operating systems.

"This loop is triggered in the cases when BitLocker is not installed," it said. "The script will try to install it, succeed, but then get stuck in a loop waiting for reboot. BitLocker is installed (not enabled/configured) on all client operating systems, so this impacts only older versions of server OS."

The ransomware script is also designed to generate a random password that's derived from system-specific information, such as network traffic, system memory, and disk utilization, using it to encrypt the system's drives. This is done so in an attempt to resist brute-force attempts.

The unique password is then uploaded to a server controlled by the attacker. Following the restart, the user is prompted to enter the password to unlock the encrypted drive. The BitLocker screen is also configured to display the threat actor's contact email address to initiate the payment in exchange for the password.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

That's not all. The script makes several Registry modifications to restrict access to the system by disabling remote RDP connections and turning off local password-based logins. As part of its cleanup efforts, it also disables Windows Firewall rules and deletes audit files.

Bitdefender further pointed out that the name ShrinkLocker is misleading as the namesake functionality is limited to legacy Windows systems and that it doesn't actually shrink partitions on current operating systems.

"By using a combination of Group Policy Objects (GPOs) and sched...