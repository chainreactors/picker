---
title: Ransomware on ESXi: The Mechanization of Virtualized Attacks
url: https://thehackernews.com/2025/01/ransomware-on-esxi-mechanization-of.html
source: The Hacker News
date: 2025-01-14
fetch_date: 2025-10-06T20:14:14.119279
---

# Ransomware on ESXi: The Mechanization of Virtualized Attacks

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

# [Ransomware on ESXi: The Mechanization of Virtualized Attacks](https://thehackernews.com/2025/01/ransomware-on-esxi-mechanization-of.html)

**Jan 13, 2025**The Hacker NewsThreat Detection / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6aY0UvY7nKSmqsJQIBq6qrhIegLQCxxXsCcetubPU-fIIURLEB6RwGQOdRjjg31oNIK_MdSNh4s1nP4_MeIhBHu6A8A_0HtdjCz0yjdfWsTz75PxYz7SofePbCiC0SJ9q9htx_Es-fh9uy7PsHHHDEh1vqhcmTmDtlQ1ljDzVmOphoStL2xqScsw1k7I/s790-rw-e365/pentera.png)

In 2024, ransomware attacks targeting VMware ESXi servers reached alarming levels, with the average ransom demand skyrocketing to $5 million. With approximately 8,000 ESXi hosts exposed directly to the internet (according to Shodan), the operational and business impact of these attacks is profound.

Most of the Ransomware strands that are attacking ESXi servers nowadays, are variants of the infamous Babuk ransomware, adapted to avoid detection of security tools. Moreover, accessibility is becoming more widespread, as attackers monetize their entry points by selling Initial Access to other threat actors, including ransomware groups. As organizations are dealing with compounded threats on an ever-expanding front: new vulnerabilities, new entry points, monetized cyber-crime networks, and more, there is ever-growing urgency for enhanced [security measures](https://pentera.io/attack-surface-monitoring/) and vigilance.

## The architecture of ESXi

Understanding how an attacker can gain control of the ESXi host begins with understanding the architecture of virtualized environments and their components. This will help identify potential vulnerabilities and points of entry.

Building on this, attackers targeting ESXi servers might look for the central node that manages multiple ESXi hosts. This will allow them to maximize their impact.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeWNX39xOr8Dr5j0maJrLaEtit10YXG1sPXttEjtNB8zQ1NITh4H5hEqP5Gtl82dijk4XyNXPjeJICMvLxjRbd-xDdzh64GvaL5zmg5hsMNwFqAtvmA8VuNmpypMA2Dj-rClG1d_44q6_nUlXbHY5qNG2hzXnkgwdY0eGZBdtckzM9WCib4oA3jHEIxFk/s790-rw-e365/main.png)

This brings us to the vCenter, which is the central administration for VMware infrastructure and is designed to manage several ESXi hosts. The vCenter server orchestrates ESXi host management with the default "vpxuser" account. Holding root permissions, the "vpxuser" account is responsible for administrative actions on the virtual machines residing on the ESXi hosts. For example, transferring VMs between hosts and modifying configurations of active VMs.

Encrypted passwords for each connected ESXi host are stored in a table within the vCenter server. A secret key stored on the vCenter server facilitates password decryption, and, consequently, total control over each and every one of the ESXi hosts. Once decrypted, the "vpxuser" account can be used for root permissions operations, including altering configurations, changing passwords of other accounts, SSH login, and executing ransomware.

## Encryption on ESXi

Ransomware campaigns are intended to make recovery exceedingly difficult, coercing the organization toward paying the ransom. With ESXi attacks, this is achieved by targeting four file types that are essential for operational continuity:

1. **VMDK Files**: A virtual disk file that stores the contents of a virtual machine's hard drive. Encrypting these files renders the virtual machine completely inoperable.
2. **VMEM Files**: The paging file of each virtual machine. Encrypting or deleting VMEM files can result in significant data loss and complications when attempting to resume suspended VMs.
3. **VSWP Files**: Swap files, which store some of the VM's memory beyond what the physical memory of the host can provide. Encrypting these swap files can cause crashes in VMs.
4. **VMSN Files**: Snapshots for backing up VMs. Targeting these files complicates disaster recovery processes.

Since the files involved in ransomware attacks on ESXi servers are large, attackers typically employ a hybrid encryption approach. They combine the rapidity of symmetric encryption with the security of asymmetric encryption.

* **Symmetric encryption** - These methods, such as AES or Chacha20, allow speed and efficiency in encrypting large volumes of data. Attackers can quickly encrypt files, reducing the window of opportunity for detection and mitigation by security systems.
* **Asymmetric encryption** - Asymmetric methods, such as RSA, are slower since they involve a public key and a private key and require complex mathematical operations.

Therefore, in ransomware, asymmetric encryption is primarily used for securing the keys used in symmetric encryption, rather than the data itself. This ensures that the encrypted symmetric keys can only be decrypted by someone possessing the corresponding private key, i.e the attacker. Doing so prevents easy decryption, adding an extra layer of security for the attacker.

## **4 Key Strategies for Risk Mitigation**

Once we've acknowledged that vCenter security is at risk, the next step is to strengthen defenses by putting obstacles in the path of potential attackers. Here are some strategies:

1. **Regular VCSA Updates**: Always use the latest version of the VMware vCenter Server Appliance (VCSA) and keep it updated. Transitioning from a Windows-based vCenter to the VCSA can improve security, as it's designed specifically for managing vSphere.
2. **Implement MFA and Remove Default Users**: Don't just change default passwords—set up strong Multi-Factor Authentication (MFA) for sensitive accounts to add an extra layer of protection.
3. **Deploy Effective Detection Tools**: Use detection and prevention tools directly on your vCenter. Solutions like EDRs, XDRs or third-party tools can help with monitoring and alerts, making it harder for attackers to succeed. For example, setting up monitoring policies that specifically track unusual access attempts to the vpxuser account or ale...