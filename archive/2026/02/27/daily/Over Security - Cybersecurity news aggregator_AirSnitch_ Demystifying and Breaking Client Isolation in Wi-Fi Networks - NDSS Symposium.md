---
title: AirSnitch: Demystifying and Breaking Client Isolation in Wi-Fi Networks - NDSS Symposium
url: https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-27
fetch_date: 2026-02-28T04:01:27.010400
---

# AirSnitch: Demystifying and Breaking Client Isolation in Wi-Fi Networks - NDSS Symposium

[![ndss logo](https://www.ndss-symposium.org/wp-content/themes/ndss2/resources/assets/images/NDSS-Logo-120x37.svg)](https://www.ndss-symposium.org/)

Menu Navigation

* [About](https://www.ndss-symposium.org/about/)
  + [Test of Time Award](https://www.ndss-symposium.org/ndss-test-of-time-award/)
  + [Why NDSS Symposium](https://www.ndss-symposium.org/why-ndss/)
  + [Sponsorship](https://www.ndss-symposium.org/sponsorship/)
* [2026 Symposium](https://www.ndss-symposium.org/ndss2026/)
  + [Attend](https://www.ndss-symposium.org/ndss2026/attend/)
  + [Accepted Papers](https://www.ndss-symposium.org/ndss2026/accepted-papers/)
  + [Program](https://www.ndss-symposium.org/ndss2026/program/)
  + [Co-located Events](https://www.ndss-symposium.org/ndss2026/co-located-events/)
  + [Leadership](https://www.ndss-symposium.org/ndss2026/leadership/)
  + [Sponsorship](https://www.ndss-symposium.org/ndss2026/sponsorship/)
* [2025 Symposium](https://www.ndss-symposium.org/ndss2025/)
  + [Accepted Papers](https://www.ndss-symposium.org/ndss2025/accepted-papers/)
  + [Accepted Posters](https://www.ndss-symposium.org/ndss2025/accepted-posters/)
  + [Program](https://www.ndss-symposium.org/ndss2025/program/)
  + [Co-located Events](https://www.ndss-symposium.org/ndss2025/co-located-events/)
  + [Leadership](https://www.ndss-symposium.org/ndss2025/leadership/)
* Previous Events
  + [Previous NDSS Symposia](https://www.ndss-symposium.org/previous-ndss-symposia/)
  + [Previous Co-located Events](https://www.ndss-symposium.org/previous-co-located-events/)

![Search Icon](https://www.ndss-symposium.org/wp-content/uploads/search-bar-21px-21px.svg)

[Register](https://www.ndss-symposium.org/ndss2026/attend/)

Search for:Search Button

# AirSnitch: Demystifying and Breaking Client Isolation in Wi-Fi Networks

**Xin'an Zhou (University of California, Riverside), Juefei Pu (University of California, Riverside), Zhutian Liu (University of California, Riverside), Zhiyun Qian (University of California, Riverside), Zhaowei Tan (University of California, Riverside), Srikanth V. Krishnamurthy (University of California, Riverside), Mathy Vanhoef (DistriNet, KU Leuven)**

To prevent malicious Wi-Fi clients from attacking other clients on the same network, vendors have introduced client isolation, a combination of mechanisms that block direct communication between clients. However, client isolation is not a standardized feature, making its security guarantees unclear.

In this paper, we undertake a structured security analysis of Wi-Fi client isolation and uncover new classes of attacks that bypass this protection. We identify several root causes behind these weaknesses. First, Wi-Fi keys that protect broadcast frames are improperly managed and can be abused to bypass client isolation. Second, isolation is often only enforced at the MAC or IP layer, but not both. Third, weak synchronization of a client's identity across the network stack allows one to bypass Wi-Fi client isolation at the network layer instead, enabling the interception of uplink and downlink traffic of other clients as well as internal backend devices. Every tested router and network was vulnerable to at least one attack. More broadly, the lack of standardization leads to inconsistent, ad hoc, and often incomplete implementations of isolation across vendors.

Building on these insights, we design and evaluate end-to-end attacks that enable full machine-in-the-middle capabilities in modern Wi-Fi networks. Although client isolation effectively mitigates legacy attacks like ARP spoofing, which has long been considered the only universal method for achieving machine-in-the-middle positioning in local area networks, our attack introduces a general and practical alternative that restores this capability, even in the presence of client isolation.

[Paper](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf)

## View More Papers

### [Porting NASA's core Flight System to the Formally Verified...](https://www.ndss-symposium.org/ndss-paper/porting-nasas-core-flight-system-to-the-formally-verified-sel4-microkernel/)

Juliana Furgala (MIT Lincoln Laboratory), Samuel Jero (MIT Lincoln Laboratory), Andrea Lin (MIT Lincoln Laboratory), Rick Skowyra (MIT Lincoln Laboratory)

[Read More](https://www.ndss-symposium.org/ndss-paper/porting-nasas-core-flight-system-to-the-formally-verified-sel4-microkernel/)

### [Les Dissonances: Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered...](https://www.ndss-symposium.org/ndss-paper/les-dissonances-cross-tool-harvesting-and-polluting-in-pool-of-tools-empowered-llm-agents/)

Zichuan Li (University of Illinois Urbana-Champaign), Jian Cui (University of Illinois Urbana-Champaign), Xiaojing Liao (University of Illinois Urbana-Champaign), Luyi Xing (University of Illinois Urbana-Champaign)

[Read More](https://www.ndss-symposium.org/ndss-paper/les-dissonances-cross-tool-harvesting-and-polluting-in-pool-of-tools-empowered-llm-agents/)

### [IoTBec: An Accurate and Efficient Recurring Vulnerability Detection Framework...](https://www.ndss-symposium.org/ndss-paper/iotbec-an-accurate-and-efficient-recurring-vulnerability-detection-framework-for-black-box-iot-devices/)

Haoran Yang (Institute of Information Engineering, Chinese Academy of Sciences), Jiaming Guo (Institute of Information Engineering, Chinese Academy of Sciences), Shuangning Yang (School of Internet, Anhui University), Guoli Zhao (Institute of Information Engineering, Chinese Academy of Sciences), Qingqi Liu (Institute of Information Engineering, Chinese Academy of Sciences), Chi Zhang (Institute of Information Engineering, Chinese Academy…

[Read More](https://www.ndss-symposium.org/ndss-paper/iotbec-an-accurate-and-efficient-recurring-vulnerability-detection-framework-for-black-box-iot-devices/)

### About

* [About](/about/)
* [Test of Time Award](https://www.ndss-symposium.org/ndss-test-of-time-award/)
* [Why NDSS Symposium](https://www.ndss-symposium.org/why-ndss/)
* [Sponsorship](https://www.ndss-symposium.org/sponsorship/)
* [News](https://www.ndss-symposium.org/news/)

### NDSS Symposium 2023

* [2026 Symposium](https://www.ndss-symposium.org/ndss2026/)
* [Attend](https://www.ndss-symposium.org/ndss2026/attend/)
* [Accepted Papers](https://www.ndss-symposium.org/ndss2026/accepted-papers/)
* [Program](https://www.ndss-symposium.org/ndss2026/program/)
* [Co-located Events](https://www.ndss-symposium.org/ndss2026/co-located-events/)
* [Leadership](https://www.ndss-symposium.org/ndss2026/leadership/)

### NDSS Symposium 2022

* [2025 Symposium](https://www.ndss-symposium.org/ndss2025/)
* [Accepted Papers](https://www.ndss-symposium.org/ndss2025/accepted-papers/)
* [Program](https://www.ndss-symposium.org/ndss2025/program/)
* [Co-located Events](https://www.ndss-symposium.org/ndss2025/co-located-events/)
* [Leadership](https://www.ndss-symposium.org/ndss2025/leadership/)

### Previous Events

* Previous Events
* [Previous NDSS Symposia](https://www.ndss-symposium.org/previous-ndss-symposia/)
* [Previous Co-located Events](https://www.ndss-symposium.org/previous-co-located-events/)

[![Facebook](https://www.ndss-symposium.org/wp-content/uploads/fb-12px-25px.svg)](https://www.facebook.com/NDSSSymposium/)
[![X home](https://www.ndss-symposium.org/wp-content/uploads/logo-white.png)](https://twitter.com/NDSSSymposium)
[![LinkedIn](https://www.ndss-symposium.org/wp-content/uploads/in-25px-24px.svg)](https://www.linkedin.com/company/network-and-distributed-system-symposium-ndss-/)
[![Youtube](https://www.ndss-symposium.org/wp-content/uploads/yt-38px-26px.svg)](https://www.youtube.com/ndsssymposium)

[Privacy Policy](https://www.ndss-symposium.org/privacy-policy/) | [Terms of Use](https://www.ndss-symposium.org/terms-of-use/) | [NDSS Code of Conduct](https://www.ndss-symposium.org/ndss-code-of-conduct/) | [Contact Us](/cdn-cgi/l/email-protection#254b4156566540494c5651560b4c564a460b4a5742)

The Internet Society has be...