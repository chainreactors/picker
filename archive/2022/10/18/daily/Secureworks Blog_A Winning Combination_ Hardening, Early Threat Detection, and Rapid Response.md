---
title: A Winning Combination: Hardening, Early Threat Detection, and Rapid Response
url: https://www.secureworks.com/blog/a-winning-combination-hardening-early-threat-detection-and-rapid-response
source: Secureworks Blog
date: 2022-10-18
fetch_date: 2025-10-03T20:07:55.894220
---

# A Winning Combination: Hardening, Early Threat Detection, and Rapid Response

[Skip to Main Content](#main-content)[Skip to Footer](#cmp-footer-a1fbb96a)

[Sophos completes Secureworks acquisition](https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition)

* [Experiencing a Breach?](https://www.sophos.com/en-us/products/incident-response-services/emergency-response)
* Contact Us
* Support
* [Blog](/blog)
* English

[![logo](/-/media/images/logos/logo_new.svg?iar=0&hash=61254867B6545667A8E17DD1352849AF)](/ "Secureworks")

* Platform
* Services
* Solutions
* About
* Partners
* Resources

[Request Demo](/contact/request-demo-xdr)

Research & Intelligence

# A Winning Combination: Hardening, Early Threat Detection, and Rapid Response

How proactively hardening Active Directory and investing in the Taegis ManagedXDR service quickly contained a breach.

![](/-/media/images/insights/blog/2022/a-winning-combination-hardening-early-detection/hardening_early_threat_rapid_response_web_360x190.png?h=190&iar=0&w=360&hash=9AD3F7AF3660CE95E6644FAED981E74D?io=transform:fit,width:4568,height:2568)

[Alexandros Papadopoulos](/author/Alexandros-Papadopoulos)

October 17, 2022

When a security partner does a great job, nothing bad happens. Sometimes, “nothing bad happens” is mistaken for “nothing happens.” This misperception may prompt an organization to question if the partnership is worth the investment.

A story from the Secureworks® incident response (IR) trenches reveals how much work went into ensuring that "nothing bad happened" after a customer missed a patch on a web server. It also shows how the organization avoided disaster by proactively implementing three defensive strategies.

## Strategy #1: Make your organization a hard target

After signing up for a Secureworks Incident Management Retainer, the customer requested an [Active Directory Security Assessment](https://docs.ctpx.secureworks.com/services/incident-response/imr-services-catalog/active_directory_security_assessment/). Active Directory (AD) misconfigurations are common in corporate networks. By exploiting this type of misconfiguration, an attacker can elevate their access from a single system to “domain administrator” within minutes. This level grants unlimited access to every system on the network (also known as “god mode”).

The assessment revealed easy privilege escalation paths to the domain administrator account, a few accounts vulnerable to [Kerberoasting](https://adsecurity.org/?p=3458), and a vulnerable end-of-life server. The customer followed Secureworks AD experts' remediation guidance and addressed the findings, making their AD a “hard target.” Hardening the environment slows attackers' progress, giving network defenders time to react.

## Strategy #2: Invest in early threat detection

The most fundamental defensive control is to apply patches for known software vulnerabilities. However, it is virtually impossible to implement patches correctly 100% of the time. This customer missed a critical patch on an internet-exposed web server. Systems exposed to the internet are scanned for vulnerabilities multiple times a day, often by threat actors seeking to exploit vulnerabilities for profit. In this case, a threat actor scanned the web server, noticed the vulnerability, and exploited it to deploy a web shell. This web shell gave the attacker a foothold in the customer's network.

The customer had invested in Taegis™ ManagedXDR. The XDR agents deployed across the network immediately alerted on the malicious activity. The agents continued alerting as the attacker struggled to escalate AD privileges (see Figure 1).

![](/-/media/images/insights/blog/2022/a-winning-combination-hardening-early-detection/a-wining-combination_figure-1.png)
*Figure 1. Taegis XDR alerts during the first 40 minutes of the breach. (Source: Secureworks)*

## Strategy #3: Enable 24x7 rapid response

Many Taegis ManagedXDR customers pre-authorize Secureworks to contain threats as soon as a breach is detected. Because this customer had not granted pre-authorization, explicit approval was required to take containment actions: isolate the compromised hosts and disable the compromised account.

Two Secureworks incident responders were assigned to the incident:

* Responder A reviewed telemetry from the breached network, applying targeted forensic analysis when needed. They confirmed the full scope of the threat activity (e.g., checking if the attacker moved to another system not monitored by XDR agents) and the root cause.
* Responder B guided the customer through the immediate containment actions over the next few hours and negotiated the execution of a full remediation plan.

This customer had invested in several Taegis XDR telemetry sources: endpoint agents, network devices, and cloud platforms. These sources created a "single pane of glass" that enabled Secureworks incident responders to work closely with the customer's incident response team to fully understand the extent of the intrusion.

## Conclusion

This breach could easily have become a post-intrusion ransomware incident with a large-scale impact to the customer's network and months of recovery effort. But the customer's proactive defense strategies minimized the impact:

* The targeted organization made themselves a hard target by proactively securing their Active Directory. This slowed down the attacker, forcing them to spend a lot of time and triggering many alerts as they struggled to elevate their privileges to domain administrator.
* Investing in early threat detection generated warnings that quickly drew attention to the malicious activity and revealed the root cause.
* Enabling rapid response ensured that incident responders had access to the right tools, data, and intelligence to rapidly investigate and contain the malicious activity.

The success of a security partner can be measured by the lack of major breaches. With the correct preparation, this outcome is achievable. Mistakes such as missed patches happen. Compensating controls can identify exploitation of these mistakes so that damage is rapidly contained.

Protect your organization with a Secureworks [Incident Management Retainer](/services/incident-management-retainer) and [Taegis ManagedXDR](/services/mdr). Learn more about Taegis XDR with an [XDR demo](/contact/request-demo-xdr).

If you need urgent assistance with an incident, [contact the Secureworks Incident Response team](/contact/emergency-response). We are here to assist, 24x7.

* **Tags:**
* [Research](/blog?tag=Research)
* [Blog](/blog?tag=Blog)

Secureworks has been acquired by Sophos. To view all new blogs, including those on threat intelligence from the Counter Threat Unit, visit: [https://news.sophos.com/en-us/](https://news.sophos.com/en-us/.).

---

ABOUT THE AUTHOR

[ALEXANDROS PAPADOPOULOS

Incident Response Consulting](/author/Alexandros-Papadopoulos)

---

[Back to all Blogs](/blog)

#### Now Trending...

* [2024 Global State of the Threat Report](/resources/rp-state-of-the-threat-2024 "2024 Global State of the Threat Report")
* [Modernize Your Security Operation Center with XDR](/resources/eb-modernize-you-security-operation-center-with-xdr "Modernize Your Security Operation Center with XDR")
* [MDR Done Right](/resources/eb-mdr-done-right "MDR Done Right")

![rp_Threat-Intelligence-Summary-Report-01_4-3-xl](https://dam.secureworks.com/transform/6fd9f362-cc09-4bfd-b389-381ac61abf24/rp_Threat-Intelligence-Summary-Report-01_4-3-xl?io=transform:fit,width:4568,height:2568)

Report

### Threat Intelligence Executive Report Volume 2025 Number 1

[Read More](/resources/rp-irs-threat-intelligence-executive-report-vol-2025-num-1)

## Additional Resources

![cyberpredictions24_4-3-xl (1)](https://dam.secureworks.com/transform/9a08d532-71c6-455c-809f-bdfb03543277/cyberpredictions24_4-3-xl-1?io=transform:fit,width:4568,height:2568)

Blog

### Three Cybersecurity Platform Predictions for 2024

[Read Now](/blog/three-cybersecurity-platform-predictions-for-2024)

![Young bus...