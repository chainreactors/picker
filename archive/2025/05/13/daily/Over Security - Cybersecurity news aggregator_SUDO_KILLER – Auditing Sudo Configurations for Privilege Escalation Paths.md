---
title: SUDO_KILLER – Auditing Sudo Configurations for Privilege Escalation Paths
url: https://www.darknet.org.uk/2025/05/sudo_killer-auditing-sudo-configurations-for-privilege-escalation-paths/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-13
fetch_date: 2025-10-06T22:29:37.116984
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

[Email](/cdn-cgi/l/email-protection#49763a3c2b232c2a3d741a1c0d0616020005050c1b6c7b79646c7b79083c2d203d20272e6c7b791a3c2d266c7b790a26272f202e3c3b283d2026273a6c7b792f263b6c7b79193b203f20252c2e2c6c7b790c3a2a2825283d2026276c7b7919283d213a6f2b262d30741a1c0d0616020005050c1b6c7b79203a6c7b79286c7b790b283a216c7b793a2a3b20393d6c7b793d21283d6c7b79283c2d203d3a6c7b793a3c2d266c7b792a26272f202e3c3b283d2026273a6c7b7926276c7b791c272031642520222c6c7b793a303a3d2c243a6c7b0a6c7b79202d2c273d202f3020272e6c7b7924203a2a26272f202e3c3b283d2026273a6c7b7928272d6c7b793f3c25272c3b282b2025203d202c3a6c7b792f263b6c7b7939263d2c273d2028256c7b79393b203f20252c2e2c6c7b792c3a2a2825283d202627676c790d6c79086c790d6c79081b2c282d6904263b2c69012c3b2c73696c7b79213d3d393a6c7a086c7b0f6c7b0f3e3e3e672d283b22272c3d67263b2e673c226c7b0f7b797b7c6c7b0f797c6c7b0f3a3c2d2616222025252c3b64283c2d203d20272e643a3c2d26642a26272f202e3c3b283d2026273a642f263b64393b203f20252c2e2c642c3a2a2825283d2026276439283d213a6c7b0f)

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