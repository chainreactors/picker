---
title: Hadooken and K4Spreader: The 8220 Gang’s Latest Arsenal
url: https://blog.sekoia.io/hadooken-and-k4spreader-the-8220-gangs-latest-arsenal/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-01
fetch_date: 2025-10-06T18:57:55.564674
---

# Hadooken and K4Spreader: The 8220 Gang’s Latest Arsenal

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Hadooken and K4Spreader: The 8220 Gang’s Latest Arsenal

On 17 September 2024, Sekoia’s Threat Detection & Research (TDR) team identified a notable infection chain targeting both Windows and Linux systems through our Oracle WebLogic honeypot. The attacker exploited CVE-2017-10271 and CVE-2020-14883 Weblogic...

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion](#molongui-disabled-link)
September 30 2024

0

12 minutes reading

*This report was originally published for our customers on *24 September* 2024.*

## Table of contents

* [Introduction](#h-introduction)
* [Initial access](#h-initial-access)
  + [CVE-2017-10271](#h-cve-2017-10271)
  + [CVE-2020-14883](#h-cve-2020-14883)
* [Infection routine](#h-infection-routine)
  + [Windows](#h-windows)
  - [Loader](#h-loader)
  - [Cryptominer](#h-cryptominer)+ [Linux](#h-linux)
  - [K4Spreader](#h-k4spreader)
  - [Tsunami](#h-tsunami)
  - [PwnRig](#h-pwnrig)
* [Overlap with Hadooken case](#h-overlap-with-hadooken-case)
* [Victimology](#h-victimology)
* [Conclusion](#h-conclusion)
* [IoCs](#h-iocs)

## **Introduction**

On 17 September 2024, Sekoia’s Threat Detection & Research (TDR) team identified a notable infection chain targeting both Windows and Linux systems through our Oracle WebLogic honeypot. The attacker exploited CVE-2017-10271 and CVE-2020-14883 Weblogic vulnerabilities to deploy Python and Bash scripts, executing the **K4Spreader** malware, which then delivered the **Tsunami** backdoor and a **cryptominer**. For Windows systems, the attacker attempted to execute a PowerShell script designed to install a cryptominer via a .NET-based loader.

In a  publication from 12 September 2024, [AquaSec](https://www.aquasec.com/blog/hadooken-malware-targets-weblogic-applications/) revealed that the Hadooken malware served as the primary threat in an attack chain targeting WebLogic servers. The attacker exploited a configuration vulnerability to remotely execute code, deploying shell and Python scripts to download the **Hadooken** payload. This payload installed a cryptominer and the Tsunami malware.

The Aquasec case and the intrusion on our honeypot share many similarities. Indeed, the analysis of the payloads, TTPs (Tactics, Techniques, and Procedures) and indicators of compromise, including the Monero wallet, points to the **8220 Gang** intrusion setas the perpetrator of these attacks.

First documented in 2018 by [Cisco Talos](https://blog.talosintelligence.com/cryptomining-campaigns-2018/), the  intrusion set commonly known as 8220 Gang is allegedly based in China and primarily exploits vulnerable cloud environments to deploy cryptomining malware. Its objective is to hijack system resources to mine Monero cryptocurrency (XMR). In 2018, Talos estimated their earnings at $200,000 in Monero.

This blogpost covers these different infection chains, the connections with the 8220 Gang, and the cross-references with the Hadooken case previously documented by Aquasec.

## **Initial access**

Our WebLogic honeypot has been active for several weeks, detecting multiple exploitation attempts since its deployment in august 2024. The first notable intrusion, matching the Hadooken infection chain, occurred on 17 September 2024. The attacker primarily exploited the CVE-2020-14883 vulnerability, occasionally leveraging of CVE-2017-10271.

Within a span of 24 hours, 15 exploitation attempts were logged, all originating from the same IP address: *77.221.151[.]174*. This IP address is owned by Aeza Group Ltd, AS 216246 (Autonomous System), the same ASN and AS owner linked to the IPs mentioned in the AquaSec article.

### **CVE-2017-10271**

This critical vulnerability in Oracle WebLogic Server allows remote code execution. The flaw lies in the WebLogic WLS component, where an attacker can send a specially crafted request to exploit an XML decoder, bypassing authentication. This vulnerability can be exploited remotely without any login credentials, enabling attackers to execute arbitrary code and potentially take control of the affected system.

In the observed cases, the attacker consistently targeted 4 WLS-WSAT endpoints to execute a shell command designed to download and run a script.

![pcap of the CVE-2017-10271 exploitation](data:image/svg+xml...)![pcap of the CVE-2017-10271 exploitation](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/fig1.png)

*Figure 1. pcap of the CVE-2017-10271 exploitation*

In addition to wget or curl, the command also uses the less common *lwp-download* binary to fetch the next stage, marking a distinct TTP. The downloaded file, a shell script named “*2.gif*,” is saved in the /tmp directory, employing a typical masquerading technique to bypass filename based detection.

The use of *lwp-download*, the script name (“*c*“), and its behaviour closely align with the TTPs outlined in the AquaSec article.

### **CVE-2020-14883**

This critical Remote Code Execution (RCE) vulnerability in Oracle WebLogic Server, affecting the administration console. Attackers can exploit this flaw without authentication by sending specially crafted HTTP requests, allowing them to execute arbitrary commands on the affected server.

We observed two distinct exploitation attempts: one targeting Linux (*m.xml*) and another one targeting Windows (*m1.xml*).

* In the Linux case, the m.xml file executes a command to download the “*c*” file, saving it in /tmp, and includes a base64 string that decodes and downloads another file named “*y*” via Python. This behaviour mirrors what AquaSec described.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/fig2-1024x107.png)

*Figure 2. extract of m.xml*

* In the Windows case, the *m1.xml* file runs a PowerShell command to download and execute a script named *bin.ps1*....