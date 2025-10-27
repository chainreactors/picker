---
title: SUDO_KILLER – Auditing Sudo Configurations for Privilege Escalation Paths
url: https://www.darknet.org.uk/2025/05/sudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2025-05-13
fetch_date: 2025-10-06T22:25:22.444869
---

# SUDO_KILLER – Auditing Sudo Configurations for Privilege Escalation Paths

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# SUDO\_KILLER – Auditing Sudo Configurations for Privilege Escalation Paths

May 12, 2025

Views: 884

`sudo` is a powerful utility in Unix-like systems that allows permitted users to execute commands with elevated privileges. However, misconfigurations and certain vulnerabilities can be exploited to escalate privileges, potentially compromising system security.

![SUDO_KILLER - Auditing Sudo Configurations for Privilege Escalation Paths](data:image/svg+xml...)![SUDO_KILLER - Auditing Sudo Configurations for Privilege Escalation Paths](https://www.darknet.org.uk/wp-content/uploads/2025/05/SUDO_KILLER-Auditing-Sudo-Configurations-for-Privilege-Escalation-Paths-640x351.jpeg)

**SUDO\_KILLER** is a shell script designed to assist security professionals in identifying such misconfigurations and vulnerabilities within `sudo` configurations.

It focuses on vulnerabilities tied to SUDO usage, including misconfigurations in sudo rules, version-based weaknesses (CVEs and other vulnerabilities), and risky binary deployments (GTFOBINS). These weak points can be exploited to gain ROOT-level privileges or impersonate other users.

---

## **What is SUDO\_KILLER?**

Developed by [TH3xACE](https://github.com/TH3xACE/SUDO_KILLER), SUDO\_KILLER is a Bash script that performs a series of checks to identify:

* Misconfigurations in `sudo` rules
* Presence of dangerous binaries (e.g., those listed in GTFOBins)
* Vulnerable versions of `sudo` susceptible to known CVEs
* Dangerous environment variables
* Writable directories containing scripts
* Binaries that might be replaced
* Missing scripts referenced in `sudo` configurations

The tool generates a report detailing potential privilege escalation vectors but does not perform any exploitation itself.

---

## **Key Features**

* **Comprehensive Checks**: Identifies various misconfigurations and vulnerabilities related to `sudo`.
* **CVE Detection**: Checks for known vulnerabilities in the installed version of `sudo`.
* **Export Functionality**: Can export `sudo` rules and configurations for offline analysis.
* **Offline Mode**: Supports analyzing extracted data from a target system without direct execution on it.
* **Report Generation**: Produces detailed reports outlining findings and potential exploitation paths.

---

## **Usage**

To run SUDO\_KILLER:

./SUDO\_KILLERv3.sh -c -e -r report.txt -p /tmp

|  |  |
| --- | --- |
| 1 | ./SUDO\_KILLERv3.sh -c -e -r report.txt -p /tmp |

**Options:**

* `-c`: Include CVE checks
* `-e`: Export `sudo` rules and configurations
* `-r`: Specify report filename
* `-p`: Specify path to save exports and report
* `-s`: Supply user password for `sudo` checks (if required)
* `-h`: Display help message

## **Conclusion**

SUDO\_KILLER is a valuable tool for security professionals aiming to audit `sudo` configurations for potential privilege escalation vectors. By identifying misconfigurations and known vulnerabilities, it aids in strengthening system security.

You can download SUDO\_KILLER or read more [here](https://github.com/TH3xACE/SUDO_KILLER).

## Related Posts:

* [Windows\_EndPoint\_Audit - Endpoint Security Auditing Toolkit](https://www.darknet.org.uk/2025/07/windows_endpoint_audit-endpoint-security-auditing-toolkit/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [Emerging Threats ETOpen - Anti-malware IDS/IPS Ruleset](https://www.darknet.org.uk/2016/08/emerging-threats-etopen-anti-malware-idsips-ruleset/)
* [Privacy Implications of Web 3.0 and Darknets](https://www.darknet.org.uk/2023/03/privacy-implications-of-web-3-0-and-darknets/)
* [Bantam - Advanced PHP Backdoor Management Tool For…](https://www.darknet.org.uk/2025/05/bantam-advanced-php-backdoor-management-tool-for-post-exploitation/)
* [Pulled Pork - Suricata & Snort Rule Management](https://www.darknet.org.uk/2016/11/pulled-pork-suricata-snort-rule-management/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fsudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths%2F)

[Tweet](https://twitter.com/intent/tweet?text=SUDO_KILLER+-+Auditing+Sudo+Configurations+for+Privilege+Escalation+Paths&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fsudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fsudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fsudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths%2F&text=SUDO_KILLER+-+Auditing+Sudo+Configurations+for+Privilege+Escalation+Paths)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fsudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths%2F)

[Email](/cdn-cgi/l/email-protection#fbc4888e99919e988fc6a8aebfb4a4b0b2b7b7bea9dec9cbd6dec9cbba8e9f928f92959cdec9cba88e9f94dec9cbb894959d929c8e899a8f92949588dec9cb9d9489dec9cbab89928d92979e9c9edec9cbbe88989a979a8f929495dec9cbab9a8f9388dd99949f82c6a8aebfb4a4b0b2b7b7bea9dec9cb9288dec9cb9adec9cbb99a8893dec9cb889889928b8fdec9cb8f939a8fdec9cb9a8e9f928f88dec9cb888e9f94dec9cb9894959d929c8e899a8f92949588dec9cb9495dec9cbae959283d69792909edec9cb8882888f9e9688dec9b8dec9cb929f9e958f929d8292959cdec9cb9692889894959d929c8e899a8f92949588dec9cb9a959fdec9cb8d8e97959e899a999297928f929e88dec9cb9d9489dec9cb8b948f9e958f929a97dec9cb8b89928d92979e9c9edec9cb9e88989a979a8f929495d5decbbfdecbbadecbbfdecbbaa99e9a9fdbb694899edbb39e899ec1dbdec9cb938f8f8b88dec8badec9bddec9bd8c8c8cd59f9a8990959e8fd594899cd58e90dec9bdc9cbc9cedec9bdcbcedec9bd888e9f94a4909297979e89d69a8e9f928f92959cd6888e9f94d69894959d929c8e899a8f92949588d69d9489d68b89928d92979e9c9ed69e88989a979a8f929495d68b9a8f9388dec9bd)

Filed Under: [Linux Hacking](https://www.darknet.org.uk/category/linux-hacking/)

## Primary Sidebar

### Search Darknet

Search the site ...

* [Email](https://www.darknet.org.uk/contact-darknet/)
* [Facebook](https://www.facebook.com/darknet.org.uk/)
* [LinkedIn](https://www.linkedin.com/company/25076296/)
* [RSS](https://www.darknet.org.uk/feed/)
* [Twitter](https://x.com/THEdarknet)

**[Advertise on Darknet](https://www.darknet.org.uk/contact-darknet/advertise/)**

### Latest Posts

[![RustRedOps - Rust Native Offensive Toolkit Collection for Red Teams](data:image/svg+xml...)![RustRedOps - Rust Native Offensive Toolkit Collection for Red Teams](https://www.darknet.org.uk/wp-content/uploads/2025/10/RustRedOps-Rust-Native-Offensive-Toolkit-Collection-for-Red-Teams-100x100.jpg)](https://www.darknet.org.uk/2025/10/rustredops-rust-native-offensive-toolkit-collection-for-red-teams/)

#### [RustRedOps – Rust Native Offensive Toolkit Collection for Red Teams](https:...