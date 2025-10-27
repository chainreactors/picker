---
title: Cobalt Strike and Outflank Security Tooling: Friends in Evasive Places
url: https://outflank.nl/blog/2023/07/19/cobalt-strike-and-outflank-security-tooling-friends-in-evasive-places/
source: Publications | Outflank
date: 2023-07-20
fetch_date: 2025-10-04T11:53:59.664111
---

# Cobalt Strike and Outflank Security Tooling: Friends in Evasive Places

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [Cobalt Strike and Outflank Security Tooling: Friends in Evasive Places](https://www.outflank.nl/blog/2023/07/19/cobalt-strike-and-outflank-security-tooling-friends-in-evasive-places/ "Cobalt Strike and Outflank Security Tooling: Friends in Evasive Places")

[Pieter Ceelen](https://www.outflank.nl/blog/author/pieter/ "Posts by Pieter Ceelen")
 |
July 19, 2023

*This is a joint blog written by the Cobalt Strike and Outflank teams. It is also available on the [Cobalt Strike site.](https://www.cobaltstrike.com/blog/cobalt-strike-and-outflank-friends-evasive-places)*

Over the past few months there has been increasing collaboration and knowledge sharing internally between the Cobalt Strike and Outflank R&D teams. We are excited about the innovation opportunities made possible by this teamwork and have decided to align Cobalt Strike and Outflank Security Tooling (OST) closely going forward. Although we are actively collaborating, Cobalt Strike will continue to be the industry standard Command & Control (C2) framework, while OST will continue to offer a red team toolbox for all environments containing custom tradecraft that is OPSEC safe, evasive by design, and simple to use. Our vision is that Cobalt Strike and OST together will provide the best red team offering on the planet.

This blog will provide an update of the technical strategy of each product individually before giving a glimpse into the future of the two combined.

### **Cobalt Strike**

Cobalt Strike is the industry standard Command & Control framework. Following the acquisition of Cobalt Strike by Fortra in 2020, a conscious decision was taken to follow the technical strategy employed by founder Raphael Mudge in taking Cobalt Strike to the next level. The core tenets of this strategy are:

* **Stability**: Cobalt Strike must remain reliable and stable; nobody wants to lose their Beacons.
* **Evasion through flexibility**: Since its inception, Cobalt Strike has always been an adversary emulation tool. *It is designed to enable operators to mimic other malware and the TTPs they desire*. Hence, in its default state, Beacon is pretty trivial to detect. This however has never been the point; Cobalt Strike has flexibility built into key aspects of its offensive chain. You can tinker with how Beacon is loaded into memory, how process injection is done, what your C2 traffic looks like etc. We don’t want to bake TTPs into Beacon which become signatured over time (Cobalt Strike’s implementation of module stomping is a good example of this). We want to enable operators to [customise](https://www.cobaltstrike.com/blog/what-took-so-long-a-little-product-philosophy/) Beacon to use their own original TTPs.  Our R&D effort will continue to focus on building in flexibility into all aspects of the offensive chain and to give operators as much control as possible over the TTPs they employ.

### **Outflank & OST**

In September last year we were acquired by Fortra. Outflank is a security consultancy based in Amsterdam with deep expertise in red teaming and a proven track record of world class research. Our team is best known for our work on [Direct Sys Calls in Beacon Object Files,](https://outflank.nl/blog/2020/12/26/direct-syscalls-in-beacon-object-files/)  various [public tools](https://github.com/outflanknl/C2-Tool-Collection), Microsoft Office tradecraft ([derbycon](https://www.youtube.com/watch?v=xY2DIRfqNvA), [troopers](https://www.youtube.com/watch?v=iXvvQ5XML7g), [Blackhat Asia](https://i.blackhat.com/asia-19/Thu-March-28/bh-asia-Hegt-MS-Office-in-Wonderland.pdf), [brucon](https://www.youtube.com/watch?v=ll-ViQT9Oew), [x33fcon](https://www.youtube.com/watch?v=CR5YAwkGJQo)), or on the red team SIEM [Redelk.](https://github.com/outflanknl/RedELK)

In recent years, we have taken our internal research & development and created [Outflank Security Tooling (OST)](https://outflank.nl/datasheets/security-tooling-ost/).

OST is not a C2 product but a collection of **offensive tools and tradecraft**, offering:

* A **broad** arsenal of offensive tools for different stages of red teaming.

* Tools that are designed to be **OPSEC** safe and **evade existing security controls** (AV/EDR).
* Advanced tradecraft via **understandable** interfaces, instead of an operator needing to write or compile custom low-level code.
* A **knowledge sharing hub** where trusted & vetted red teamers discuss tradecraft, evasion, and R&D.
* An **innovative cloud delivery platform** which enables fast release cycles, and complex products such as ‘compilation as a service’, while still allowing any customer to run and manage their own offensive infrastructure. Although OST is offered as a cloud model, it is possible to use the offensive tools and features offline and in air gapped environments.

Hence, it is a toolbox for red teamers made by red teamers, enabling operators to work more efficiently and focus on their job at hand. It contains features such as: a payload generator to build sophisticated artifacts and evade anti-virus / EDR products, a custom .NET obfuscator, credential dumpers, kernel level capabilities, and custom BOF implementations of offensive tools (such as KerberosAsk as an alternative to Rubeus).

Going forward, OST will continue to provide a full suite of bleeding-edge tools to solve the main challenges facing security consultants today (i.e., on prem/workstation attacks, recon, cloud etc.). Our R&D team remain active in red teaming engagements and so all these tools are being [continually battle tested](https://twitter.com/OutflankNL/status/1679856467115929604) on live red team operations. Furthermore, OST will continue to grow as a vetted knowledge hub and an offensive R&D powerhouse that brings novel evasion, tradecraft, and tooling for its customers.

### **Combining forces: Cobalt Strike and Outflank Security Tooling**

Having outlined the technical strategies of Cobalt Strike and OST above, it is clear that both products naturally complement each other. Therefore, we have decided to align the two products closely going forward.

In our joint roadmap, both products will stay true to their visions as outlined above. Cobalt Strike will continue to push the boundaries of building flexibility into every stage of the offensive chain, e.g. via technologies such as BOFs, and OST will continue to leverage this flexibility to deploy novel tradecraft, as well as continuously releasing stand-alone tools.

Furthermore, both teams are already cooperating extensively, which is further advancing innovation and product development. Outflank’s experience in red teaming is providing valuable insight and feedb...