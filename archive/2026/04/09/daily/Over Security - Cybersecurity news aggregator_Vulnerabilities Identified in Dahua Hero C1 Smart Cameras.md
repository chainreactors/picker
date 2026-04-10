---
title: Vulnerabilities Identified in Dahua Hero C1 Smart Cameras
url: https://www.bitdefender.com/en-us/blog/labs/vulnerabilities-identified-in-dahua-hero-c1-smart-cameras
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:52.751599
---

# Vulnerabilities Identified in Dahua Hero C1 Smart Cameras

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Whitepapers](/en-us/blog/labs/tag/whitepapers "Whitepapers")[IoT Research](/en-us/blog/labs/tag/iot-research "IoT Research")

4 min read

# Vulnerabilities Identified in Dahua Hero C1 Smart Cameras

[![Bitdefender](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/02/logo_bd_social.png "Bitdefender")](/en-us/blog/labs/author/bitdefenderteam "Bitdefender")

[Bitdefender](/en-us/blog/labs/author/bitdefenderteam "Bitdefender")

July 30, 2025

  ![Vulnerabilities Identified in Dahua Hero C1 Smart Cameras](https://blogapp.bitdefender.com/labs/content/images/size/w600/2025/07/Technology_Background_-_Digital_Hand_Unlocking_Portal-1.jpg "Vulnerabilities Identified in Dahua Hero C1 Smart Cameras")

Researchers at Bitdefender have identified critical security vulnerabilities in the firmware of the **Dahua Hero C1 (DH-H4C)** smart camera series. The flaws, affecting the device's ONVIF protocol and file upload handlers, allow unauthenticated attackers to execute arbitrary commands remotely, effectively taking over the device.

The vulnerabilities were reported to Dahua for responsible mitigation and disclosure and are now patched at the time of publication.

### Affected Devices

The issues were verified on a **Dahua Hero C1 (DH-H4C)** running firmware version **V2.810.9992002.0.R (Build Date: 2024-01-23)** with **ONVIF version 21.06** and **Web UI version V3.2.1.1452137**. This version was confirmed as the latest available when starting our research through the device’s own update interface.

Other device models that were identified during the vendor’s own audit include: IPC-1XXX Series, IPC-2XXX Series, IPC-WX Series, IPC-ECXX Series, SD3A Series, SD2A Series, SD3D Series, SDT2A Series, SD2C Series with firmware versions older than 2025/04/16.

### Acknowledgement

 We would like to extend our sincere thanks to the Dahua security team for their professional handling of the vulnerabilities reported. Their prompt triage, prioritization, and resolution of the issues demonstrate a strong commitment to customer safety and product integrity. This type of collaboration between researchers and vendors is extremely valuable to the broader cybersecurity ecosystem - ensuring that vulnerabilities are addressed before they can be weaponized. We hope to see this level of responsiveness and transparency replicated across the industry.

### Disclosure Timeline

* Mar 28, 2025: Bitdefender shares the findings with the Dahua team through a secure communication channel
* Mar 29, 2025: Dahua acknowledges reception and proceeds with internal investigation
* Apr 01, 2025: Dahua confirms the reports as valid
* Apr 23, 2025: Dahua asks for an extension, Bitdefender moves disclosure timeframe for Jul 23rd.
* Jul 07, 2025: Dahua releases patches for the vulnerability and confirms the Jul 30th coordinated disclosure
* Jul 30, 2025: This report becomes public as part of the coordinated responsible disclosure efforts

### Vulnerability 1: Stack-Based Buffer Overflow in ONVIF Protocol Handler ([CVE-2025-31700](https://www.cve.org/CVERecord?id=CVE-2025-31700))

The ONVIF request handler on port 80 (function at 0x19e530) parses the Host header incorrectly, leading to an unbounded copy of the header on the stack. If the header contains a ‘]’ character that is not followed by a ‘:’ character, the strncpy function gets the size by subtracting the buffer’s address from the address of the ‘]’ character. This allows an attacker to write an arbitrary number of bytes to the stack, as long as the payload does not contain a ‘]’ character or a null byte. This oversight allows for an unauthenticated stack-based buffer overflow, ultimately overwriting the return address and several CPU registers (r4–r11).

**The strncpy call at 0x0019e898:**

![A screenshot of a computer code  AI-generated content may be incorrect.](https://blogapp.bitdefender.com/labs/content/images/2025/07/data-src-image-59b8454b-3bf5-4103-9207-ff725d05a12d.png)

Exploitation is possible without prior authentication, and a successful attack results in full code execution. The proof-of-concept (PoC) developed by researchers shows the attacker writing system commands into memory and then invoking them through carefully crafted return-oriented programming (ROP) chains. The PoC drops an ELF payload using tftp and spawns a bind shell on port 4444 using LD\_PRELOAD, bypassing binary signature checks.

![A close up of a computer screen  AI-generated content may be incorrect.](https://blogapp.bitdefender.com/labs/content/images/2025/07/data-src-image-d0a03cad-fe51-4274-8fd4-51f03c4d90f3.png)

---

### Vulnerability 2: .bss Segment Overflow via RPC Upload Handler ([CVE-2025-31701](https://www.cve.org/CVERecord?id=CVE-2025-31701))

A second vulnerability exists in the handler for the undocumented endpoint POST /RPC2\_UploadFileWithName/\*. Here, the camera copies the Cseq HTTP header directly into a buffer located in the .bss memory section using a flawed strncpy implementation.

The **strncpy**call at 0x00583948:

![A screenshot of a computer program  AI-generated content may be incorrect.](https://blogapp.bitdefender.com/labs/content/images/2025/07/data-src-image-d2db59c6-8497-4890-a222-84d084011976.png)

The variable at 0x03955c38 stores a pointer to a structure that can be overwritten by **strncpy**. The functions at 0x00586dd4 and 0x00586d18 continuously check this structure for expired sessions. Because no bounds checking is performed, an attacker can **overwrite adjacent global variables**, including a structure that stores pointers to session management functions. These are routinely invoked by the firmware to manage timeouts. By planting a crafted structure in memory, the attacker can redirect execution to a call to system(), again resulting in full remote code execution—no authentication needed.

Function 0x00586dd4 using a function pointer from the controlled structure:

![A computer code with many colored text  AI-generated content may be incorrect.](https://blogapp.bitdefender.com/labs/content/images/2025/07/data-src-image-8b827042-1b32-428d-b636-737dd21781bf.png)

This exploit is similarly demonstrated in a PoC which uses a long header value to overflow the target structure and redirect execution.

![A screenshot of a computer code  AI-generated content may be incorrect.](https://blogapp.bitdefender.com/labs/content/images/2025/07/data-src-image-8890de44-c45e-49f9-974e-5c9d07474611.png)

### Security Impact

Both vulnerabilities are unauthenticated and exploitable over the local network. Devices exposed to the internet through port forwarding or UPnP are especially at risk. Successful exploitation provides root-level access to the camera with no user interaction.

Because the exploit path bypasses firmware integrity checks, attackers can load unsigned payloads or persist via custom daemons, making cleanup difficult.

### Recommendations

* **Users should avoid exposing the Dahua camera web interface of vulnerable models to the internet.** Disable UPnP and remove port forwarding rules if present.
* **Isolate the camera on a separate VLAN** or dedicated IoT network to limit lateral movement.
* **Monitor vendor updates** and apply patches as soon as available. As of writing, firmware versions after 2025/04/16 fix the issues.

tags

[Whitepapers](/en-us/blog/labs/tag/whitepapers "Whitepapers")[IoT Research](/en-us/blog/labs/tag/iot-research "IoT Research")

---

### Author

---

[![Bitdefender](https://blogapp.bitdefender.com/labs/content/images/size/w300/2022/02/logo_bd_social.png "Bitdefender")](/en-us/blog/labs/author/bitdefenderteam "Bitdefen...