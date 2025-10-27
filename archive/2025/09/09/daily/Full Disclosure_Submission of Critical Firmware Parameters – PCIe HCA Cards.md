---
title: Submission of Critical Firmware Parameters – PCIe HCA Cards
url: https://seclists.org/fulldisclosure/2025/Sep/34
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:52:53.716491
---

# Submission of Critical Firmware Parameters – PCIe HCA Cards

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

![](/shared/images/nst-icons.svg#search)

# Submission of Critical Firmware Parameters – PCIe HCA Cards

---

*From*: Taylor Newsome <sleepraps () gmail com>
*Date*: Wed, 20 Aug 2025 00:57:12 -0400

---

```
*To:* support () mellanox com, networking-support () nvidia com

*From:* Taylor Christian Newsome

*Date:* August 20, 2025

*Dear Mellanox/NVIDIA Networking Support Team,*

I am writing to formally submit the critical firmware parameters for
Mellanox PCI Express Host Channel Adapter (HCA) cards, as detailed in the
official documentation available here:
https://content.mellanox.com/firmware/critical_params.txt.

This document specifies essential configuration parameters that ensure
optimal performance, power efficiency, and regulatory compliance for the
following card families:

   -

   *Lion Cub / Lion Mini (P/N: MHEA28..., MHGA28...)*
   -

   *Tiger / Cheetah (P/N: MHES14..., MHES18..., MHGS18...)*

Key details include SerDes static and dynamic settings, which are critical
for maintaining hardware integrity and consistent operation. Alteration of
these parameters could impact card performance and reliability.

*Example Parameters for Lion Cub / Lion Mini Family:*

   -

   *SerDes Static Settings:*
   -

      port1_sd0_OBPreAmp = 0xf
      -

      port1_sd1_OBPreAmp = 0xf
      -

      port1_sd2_OBPreAmp = 0xf
      -

      port1_sd3_OBPreAmp = 0xf
      -

      port2_sd0_OBPreAmp = 0xf
      -

      port2_sd1_OBPreAmp = 0xf
      -

      port2_sd2_OBPreAmp = 0xf
      -

      port2_sd3_OBPreAmp = 0xf
      -

   *SerDes Dynamic Settings:*
   -

      auto_ddr_tx_options = 1
      -

      auto_ddr_rx_options = 1
      -

      auto_ddr_option_0.tx_preamp = 0xf
      -

      auto_ddr_option_1.tx_preamp = 0xf
      -

      ... (full details in the linked document)

The Tiger / Cheetah family parameters follow a similar structure and should
be preserved to maintain optimal operation.

I recommend reviewing these parameters and ensuring they are maintained as
specified. Please let me know if any further information or clarification
is required.

Thank you for your attention to this matter.

*Sincerely,*
Taylor Christian Newsome
```

**Attachment:
[mellanox\_critical\_params.txt](att-34/mellanox_critical_params.txt)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

### Current thread:

* **Submission of Critical Firmware Parameters – PCIe HCA Cards** *Taylor Newsome (Sep 08)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")