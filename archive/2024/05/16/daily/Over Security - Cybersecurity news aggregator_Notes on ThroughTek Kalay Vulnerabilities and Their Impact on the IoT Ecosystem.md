---
title: Notes on ThroughTek Kalay Vulnerabilities and Their Impact on the IoT Ecosystem
url: https://www.bitdefender.com/blog/labs/notes-on-throughtek-kalay-vulnerabilities-and-their-impact/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-16
fetch_date: 2025-10-06T17:17:34.427827
---

# Notes on ThroughTek Kalay Vulnerabilities and Their Impact on the IoT Ecosystem

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[IoT Research](/en-us/blog/labs/tag/iot-research "IoT Research")

min read

# Notes on ThroughTek Kalay Vulnerabilities and Their Impact on the IoT Ecosystem

[![Bitdefender](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/02/logo_bd_social.png "Bitdefender")](/en-us/blog/labs/author/bitdefenderteam "Bitdefender")

[Bitdefender](/en-us/blog/labs/author/bitdefenderteam "Bitdefender")

May 15, 2024

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![Notes on ThroughTek Kalay Vulnerabilities and Their Impact on the IoT Ecosystem](https://blogapp.bitdefender.com/labs/content/images/size/w600/2024/05/computer-8037837_1920.jpg "Notes on ThroughTek Kalay Vulnerabilities and Their Impact on the IoT Ecosystem")

Since 2014, Bitdefender IoT researchers have been looking into the world's most popular IoT devices, hunting for vulnerabilities and undocumented attack avenues. This report documents four vulnerabilities affecting devices powered by the ThroughTek Kalay Platform. Due to the platform’s massive presence in IoT integrations, these flaws have a significant downstream impact on several vendors.

In the interconnected landscape of the Internet of Things (IoT), the reliability and security of devices, infrastructure and data are paramount. Among the many frameworks facilitating the operation of IoT devices, ThroughTek's Kalay platform stands as a linchpin, powering [more than 100 million devices worldwide](https://www.throughtek.com/advantages/). With a predominant presence in surveillance cameras and security devices, ThroughTek Kalay's influence underscores its significance in safeguarding homes, businesses, and integrators alike.

*NOTE: the vulnerabilities presented in this paper have been responsibly disclosed to the affected vendors. Specific firmware information is available in each report below. We would like to extend our thanks to the involved vendors for their prompt acknowledgement of vulnerability and rapid patch release.*

## *Timeline*

* Oct 19, 2023: Bitdefender contacts ThroghTek and sends the vulnerability report.
* Oct 20, 2023: Vendor confirms the issues.
* Oct 26, 2023: Vendor asks for over 90-day time extension to implement and deploy the fix.
* Mar 15, 2024: Additional extension is requested.
* Apr 12, 2024: Coordinated vulnerability disclosure is scheduled for May 15 2024 to allow all affected parties to apply the patches
* Apr 16, 2024: Vendor confirms that all affected SDK versions have been patched.
* May 15, 2024: This report becomes public.

## Vulnerabilities Exposed

* [CVE-2023-6321](https://www.cve.org/CVERecord?id=CVE-2023-6321) allows an authenticated user to run system commands as the root user leading to the full compromise of the device.
* [CVE-2023-6322](https://www.cve.org/CVERecord?id=CVE-2023-6322)  enables attackers to gain root access through a stack-based buffer overflow vulnerability in the handler of an IOCTL message, typically employed in configuring motion detection zones in cameras. This is a vulnerability specific to some devices that use motion detection features.
* [CVE-2023-6323](https://www.cve.org/CVERecord?id=CVE-2023-6323), for instance, exposes a loophole wherein a local attacker can illicitly obtain the AuthKey secret, effectively helping an attacker establish a preliminary connection to the victim device.
* Lastly, [CVE-2023-6324](https://www.cve.org/CVERecord?id=CVE-2023-6324) exploits a vulnerability allowing attackers to infer the pre-shared key for a DTLS session, a critical prerequisite for connecting and talking to the victim devices.

When chained together, these vulnerabilities facilitate unauthorized root access from within the local network, as well as remote\* code execution to completely subvert the victim device.

\*Remote code execution is only possible after the device has been probed from the local network.

## Affected vendors

While these vulnerabilities affect the TUTK platform and subsequently impact most implementations, our research was conducted on three major devices sold worldwide. Given that some vendors had device-specific vulnerabilities, individual timelines are available in each report.

### Owlet Cam v1 and v2

Owlet Cam uses the ThroughTek Kalay solution to communicate with clients over the Internet.  The three vulnerabilities ([CVE-2023-6323](https://www.cve.org/CVERecord?id=CVE-2023-6323), [CVE-2023-6324](https://www.cve.org/CVERecord?id=CVE-2023-6324), and [CVE-2023-6321](https://www.cve.org/CVERecord?id=CVE-2023-6321)) can be chained together to allow an attacker to obtain root access from the local network and then to execute commands on the device. On Owlet Cam, command execution is obtained via [CVE-2023-6321](https://www.cve.org/CVERecord?id=CVE-2023-6321) - a vulnerability in IOCTL message 0x6008E, which is used to unpack archives containing OTA updates.

A technical dive into the vulnerabilities and how they are daisy-chained to compromise the Owlet Cam is available below:

[Download the whitepaper](https://blogapp.bitdefender.com/labs/content/files/2024/05/Bitdefender-PReport-owlet-7745.pdf)

### Wyze Cam v3

Bitdefender researchers have identified three vulnerabilities in Wyze Cam v3. They are tracked as CVE-[2023-6322](https://www.cve.org/CVERecord?id=CVE-2023-6322), [CVE-2023-6323](https://www.cve.org/CVERecord?id=CVE-2023-6323), and [CVE-2023-6324](https://www.cve.org/CVERecord?id=CVE-2023-6324). Chained together, these vulnerabilities allow an attacker to obtain root access from the local network. In this case, command execution on the Wyze Cam v3 is obtained via [CVE-2023-6322](https://www.cve.org/CVERecord?id=CVE-2023-6322) - a stack-based buffer overflow vulnerability in the handler of IOCTL message 0x284C that is used to set the motion detection zone.

A technical dive into the vulnerabilities and how they are daisy-chained to compromise the Wyze Cam v3 is available below:

[Download the whitepaper](https://blogapp.bitdefender.com/labs/content/files/2024/05/Bitdefender-PReport-Wyze-7745.pdf)

### Roku Indoor Camera SE

The vulnerabilities in the Roku Indoor Camera SE are identical to those in Wyze Cam v3 (and potentially other security cameras). Bitdefender researchers have daisy-chained CVE-[2023-6322](https://www.cve.org/CVERecord?id=CVE-2023-6322), [CVE-2023-6323](https://www.cve.org/CVERecord?id=CVE-2023-6323), and [CVE-2023-6324](https://www.cve.org/CVERecord?id=CVE-2023-6324)to obtain the necessary prerequisites for talking to the camera and for running OS commands as root user.

A technical dive into the vulnerabilities and how they are daisy-chained to compromise the Roku Indoor Camera SE is available below:

[Download the whitepaper](https://blogapp.bitdefender.com/labs/content/files/2024/05/Bitdefender-PReport-roku-7745.pdf)

## Implications and Remediation:

The ramifications of these vulnerabilities extend far beyond the realm of theoretical exploits, as they directly impact on the privacy and safety of users relying on devices powered by ThroughTek Kalay. Our findings have been responsibly disclosed both to the platform vendor, as well as to the tested integrators. Updated versions of firmware and SDKs have been made available for the impacted devices to prevent these issues from being exploited in real-life scenarios.

tags

[IoT Research](/en-us/blog/labs/tag/iot-research "IoT Research")

---

### Author

---

[![Bitdefender](https://blogapp.bitdefender.com/labs/content/images/size/w300/2022/02/logo_bd_social.png "Bitdefender")](/en-us/blog/labs/author/bitdefenderteam "Bitdefender")

[#...