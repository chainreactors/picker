---
title: How To Replay RF Signals Using SDR - Black Hills Information Security
url: https://www.blackhillsinfosec.com/how-to-replay-rf-signals-using-sdr/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-22
fetch_date: 2025-10-04T04:33:54.101001
---

# How To Replay RF Signals Using SDR - Black Hills Information Security

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

23
Jan
2020

[Author](https://www.blackhillsinfosec.com/category/author/), [Hardware Hacking](https://www.blackhillsinfosec.com/category/how-to/hardware-hacking/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Ray Felch](https://www.blackhillsinfosec.com/category/author/ray-felch/)
[Raymond Felch](https://www.blackhillsinfosec.com/tag/raymond-felch/), [SDR](https://www.blackhillsinfosec.com/tag/sdr/), [Software Defined Radio](https://www.blackhillsinfosec.com/tag/software-defined-radio/)

# [How To Replay RF Signals Using SDR](https://www.blackhillsinfosec.com/how-to-replay-rf-signals-using-sdr/)

**[Ray Felch](https://twitter.com/llcoder) //**

![](https://www.blackhillsinfosec.com/wp-content/uploads/2020/01/00430_01222020_HowToReplayRFSignalsSDR-1-1024x576.png)

##### **SOFTWARE DEFINED RADIO: RF Signal Replay Techniques**

![](https://lh5.googleusercontent.com/BUiUHsY8ecfrAch7xVBh3adl701EWJZGnZKuEyR1oVCg88n72YrW048ta7LWL7p-WvSB4rjjyHW1N2XSVYpBxcOOJHAeDcsI7nEmPB50Nt7jm1Z1LP5IYzWuSqlbcqbJzvVcMIKq)

**Disclaimer**: Be sure to use a faraday bag or cage before transmitting any data so you don’t accidentally break any laws by illegally transmitting on regulated frequencies. Additionally, intercepting and decrypting someone else’s data is illegal, so be careful when researching your traffic.

**Preface**: Recently, I was invited to collaborate with a few of my colleagues (many thanks to [BB King](https://www.blackhillsinfosec.com/team/brian-king/) for bringing me into his project) regarding the troubleshooting of an RF signal replay lab.

Although I owned an inexpensive ($20) RTL dongle and the higher-priced ($350) HackRF One device, I did not possess the Yardstick One ($100) dongle being used in BB King’s lab. Furthermore, I was not familiar with a few of the tools (RfCat) and scripts unique to the Yardstick One dongle.

As you might guess, I immediately ordered the Yardstick One and also purchased an inexpensive ($12) wireless doorbell at a local retail store. While waiting for the delivery of the Yardstick, I decided to power up my HackRF One and attempt to capture the doorbell remote’s RF signal and replay it using the HackRF.

Realizing that there are a few different ways to perform RF Signal replay attacks, I decided to document my findings so that others might benefit from what I discovered along the way. Hopefully, armed with this information, the methods can be chosen based upon your needs and the cost, complexity, and versatility of the devices and tools available.

**SDR USB Devices**:

* [RTL-SDR](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/) – Inexpensive ($20), Receive only (Frequency range: 500KHz to 1.75GHz)
* [Yardstick One](https://greatscottgadgets.com/yardstickone/) – Moderately priced ($100), Receive and Transmit (Frequency range: 300-348MHz, 391-464MHz, and 782-928MHz), Half-Duplex
* [HackRF One](https://greatscottgadgets.com/hackrf/) – Higher priced ($350), Receive and Transmit (Frequency range: 1 MHz and 6 GHz), Half-Duplex
* [BladeRF](https://www.nuand.com/product/bladerf-x40/) – Higher priced ($420), Receive and Transmit (Frequency range: 47MHz to 6GHz, 61.44MHz sampling rate, and 2×2 MIMO streaming), Full Duplex

**RF Signal Replay examples using a wireless doorbell**:

FCC search (<https://fccid.io/>) of the device FCC Identifier results:

![](https://lh4.googleusercontent.com/QGR1yJLqR_PTJKy5gdwgMZGF8NWkbL89jtmtjseXjjkFAoeWaluXluKYwI673O8FxrHO466opqlTNFPlvtwITK32D_bgN5-IL-kbmFR8qzV5fnGbvXocudNXqUFuA-5n9Rn-XEy8)
![](https://lh4.googleusercontent.com/8Gli_1w8zrMR9Q0wC5GtXlMBeNiw5kNuZERcZ23ba_9TJ0AFxijwSnPp2Da7x1ed7IgkzdDmgrhsdV1gIcboUUeuvR3YQX2TCskZ-zjLy2lbuqdThcelvyXmZleBiw_5vU2qDvYq)
![](https://lh3.googleusercontent.com/Aalhhba6KySPybqISTiDABAROWzj83CKBguXtW46szqcX4-dtfSpfxwWi9B53epPFyGLqVi985OKQKLKNXKTaZjcWhRv7PLpRxH4UaailUZCHZZzlIO6oZiwnLnwzD7Xj2jOzGjI)

**The RTL-SDR – RF Signal receive and capture using Gqrx**: (Note: RTL-SDR can not transmit!)

![](https://lh6.googleusercontent.com/GrWUZseUUi5HQ2d-WG5FIHpa4hdBdYFAtcPVho16NsbDwK_A_FnRy2TgfJE_UH1il06tOUswjiNiA96tx4wHAiKPcvPDZl7F78aJgIdnIw3SxuSf2SJFSz5_fhoZOEV0nU67zpeb)

After adjusting the center frequency for optimum gain and clarity (433.89MHz), we can click the “REC” radio button and then press the peripheral remote button and ultimately capture the RF signal burst to a file.

![](https://lh6.googleusercontent.com/uYrVCi-fqPTORrTdkntr_b2xXeM9WYXV6dMIAp8xbTfqsjCPMPNf5uZGUPS0otfdHqtT2lY-5AlxdkHGf9_oZnVSygWJehRpQOshktgJ6YzeRIiFQBIAEi71uP__BaFdhtCIvYIr)

Obviously, we can not transmit this signal due to the limitations of the RTL-SDR dongle, but the captured file could be t...