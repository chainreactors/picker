---
title: Hunting for Remote Management Tools
url: https://blog.nviso.eu/2024/07/18/hunting-for-remote-management-tools/
source: NVISO Labs
date: 2024-07-19
fetch_date: 2025-10-06T17:41:04.495765
---

# Hunting for Remote Management Tools

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Hunting for Remote Management Tools

[Michel Coene](https://blog.nviso.eu/author/michel-coene/ "Posts by Michel Coene")

[Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [Application Whitelisting](https://blog.nviso.eu/category/application-whitelisting/), [Logging](https://blog.nviso.eu/category/logging/), [Forensics](https://blog.nviso.eu/category/forensics/), [Threat Hunting](https://blog.nviso.eu/category/threat-hunting/), [Awareness](https://blog.nviso.eu/category/awareness/)

July 18, 2024July 26, 2024
4 Minutes

In today’s digital landscape, Remote Management and Monitoring (RMM) tools have become indispensable for organizations seeking to streamline IT operations, enhance productivity, and ensure seamless remote support. However, within our threat hunting and incident response engagements we often see that these tools, while beneficial, can also pose significant security risks if not properly managed. This blog post aims to share our insights from numerous threat hunts focused on RMM tools as well as various incident response engagements in which we observed threat actors installing these RMM tools for prolonged access into environments, and offer recommendations on how organizations can mitigate associated risks.

### The prevalence of RMM tools

Based on our threat hunting efforts performed at clients in various industries, we identified that typically a wide variety of RMM software will be present within an organization. We observed around 30 different RMM tools, with TeamViewer, VNC, mRemoteNG and AnyDesk being the most prevalent.

![Remote management tools - most utilized](https://blog.nviso.eu/wp-content/uploads/2024/07/image-2.png)

It’s important to highlight that in nearly every organization, multiple RMM tools were observed, making it harder to ensure compliance and security best practices. Often, one RMM tool is installed on a large scale and is typically used legitimately. However, it is important to look for outlier and verify—if there are only a few systems using another or multiple RMMs, that could be a sign of malicious activity.

As mentioned earlier, threat actors also leverage these legitimate tools to gain unauthorized access or maintain persistence. Adversaries have significantly increased their use of these tools in the past. In our incident response engagements, we have seen that, for example tools like AnyDesk, VNC, or ScreenConnect, are used for malicious reasons.

In general, we see that organizations have made a big push forward in terms of their cybersecurity efforts, this means that attackers need to become more creative in finding ways around the installed security products and implemented controls (such as in most case, an EDR tool). These RMM tools are signed and trusted binaries that typically do not get picked up or get warned about by any EDR tool, as such these make for a great backdoor into your environment.

It is therefore important to:

* Limit the usage and amount of allowed RMM tools within your environment
* Scan your environment for the presence of RMM tools on a recurring basis
* Ensure visibility and auditability on the usage of RMM tools
* Following an incident, ensure that only known and trusted RMM tools are present within your environment

To allow for proper follow-up, we can resort to threat hunting.

### Hypothesis

When we start with a hunt, it’s key to build a hypothesis. Specifically for RMM software, we assume that attackers can exploit these tools to gain unauthorized access, maintain persistence, or move laterally within the network. With these tools, an attacker can conduct malicious activities without raising immediate suspicion because they are inherently trusted. Attackers can install RMM software on the systems themselves to retain persistence in the environment for an extended period, which we have observed several times in our incident response engagements.

### Let’s Hunt for It

Based on the hunting capabilities of an organization, different aspects can be monitored. An initial step could involve monitoring the installed software on a system. Additionally, it is beneficial to have an extended view by looking for files that could have been created while using RMM software, such as log files. Furthermore, attention should be given to program files for software that does not require installation, commonly referred to as portable versions. Additionally, monitoring network activity for remote URLs associated with RMM providers is a good approach.

An organization should check which data is available and can be leveraged to achieve the goals of a hunt. Depending on the hunt, there can be fewer or more hits; the results have to be refined and verified to filter out possible false positives. In general, it should be validated if the RMM tools are expected within the environment.

### Recommendations

* Standardize and limit RMM tools: Using several RMM tools within the environment makes it harder to ensure compliance with security best practices. Depending on business needs, it is recommended to have dedicated and supported RMM tools. Preventing the use of other RMM tools or software may reduce the risk of security issues.
* Legitimate use and logging: It should be validated if the identified RMM tools are expected within the environment. If the RMM tools are expected within the environment, it is advised to validate that the necessary logging has been enabled for these tools. Comprehensive logging provides visibility into the activities performed using these tools and can help in detecting any anomalies or unauthorized actions.
* Regularly audit the use of RMM tools: Conduct regular audits to ensure that all RMM tools in use are accounted for and authorized. This helps in identifying any unauthorized or suspicious installations that could pose security risks.
* Investigate logs for potential misuse: If any unexpected RMM tools are found during audits, thoroughly check their logs to identify potential misuse. Look for unusual patterns or activities that could indicate malicious behavior, such as unexpected remote connections or changes to system configurations.

> This post is provided by the NVISO Incident Response team. Through these blog posts, it is our goal to raise awareness on elements commonly seen during incident response engagements or threat hunting engagements that are or could be abu...