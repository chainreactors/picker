---
title: Hunt for Weak Spots in Your Wireless Network with Airodump-ng from the Aircrack-ng Suite
url: https://www.blackhillsinfosec.com/hunt-for-weak-spots-in-your-wireless-network-with-airodump-ng/
source: Black Hills Information Security, Inc.
date: 2025-07-31
fetch_date: 2025-10-06T23:49:56.423054
---

# Hunt for Weak Spots in Your Wireless Network with Airodump-ng from the Aircrack-ng Suite

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

30
Jul
2025

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Physical](https://www.blackhillsinfosec.com/category/red-team/physical/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Sean Verity](https://www.blackhillsinfosec.com/category/author/sean-verity/), [Wireless](https://www.blackhillsinfosec.com/category/red-team/wireless/)
[aircrack-ng](https://www.blackhillsinfosec.com/tag/aircrack-ng/), [airodump-ng](https://www.blackhillsinfosec.com/tag/airodump-ng/)

# [Hunt for Weak Spots in Your Wireless Network with Airodump-ng from the Aircrack-ng Suite](https://www.blackhillsinfosec.com/hunt-for-weak-spots-in-your-wireless-network-with-airodump-ng/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/Untitled-design-3-150x150.png)

| [Sean Verity](https://www.blackhillsinfosec.com/team/sean-verity/)

*Sean Verity began working for Black Hills Information Security (BHIS) in March of 2022 as a Security Analyst. Sean is excited to be on a team with like-minded individuals and to participate in passing on knowledge. Outside of work, Sean enjoys laughing at his wife’s jokes, hunting, mountain biking, and all things outdoors.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/aircrackng_header.png)

One of the biggest challenges with wireless penetration testing is sifting through all the access points that are out there. Everything, and I mean everything, is using WiFi these days. From personal vehicles to coffee makers, or egg dispensers. That’s not to mention the dozens, hundreds, or thousands of access points that are in scope during a wireless penetration test.

In this blog, I’m going to walk you through how to get started with airodump-ng and some of the techniques that you can use to home in on access points of interest. First, a quick review of terminology that will be used throughout the blog:

* **BSSID:** MAC address of an access point
* **SSID:** Network name
* **Band:** Frequency range of access points. This is typically 2.4 or 5Ghz. When shopping for wireless adapters, make sure that it is 2.4 and 5 GHz capable.
* **Channel:** Frequency within a band. Channels are subdivisions of the frequency bands.
* **Encryption type:** Open, Personal, and Enterprise. Open has no encryption. Personal oftentimes refers to WPA-PSK (pre-shared key). There are many flavors of EAP. Technically, EAP isn’t even a “wireless thing.” It’s also commonly applied to network access control for ethernet ports. 802.1x to be specific. We’re not going to get into wired equivalent privacy (WEP). WEP has been broken for decades and there are countless tools and videos to teach you how to find and break WEP almost instantaneously.
* **Probe request / response:** Wireless devices send probe requests to look for wireless networks they’ve been connected to before. “Hidden” networks rely on wireless clients to send a probe request with the correct SSID before they respond. This is a form of security through obscurity.

## Introduction to Aircrack-ng

Aircrack-ng’s operating system support is just okay-ish. I mean…it doesn’t support [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs). I’m joking! Aircrack-ng’s support is amazing. All the major OSs and BSDs are supported and I’m pretty sure they’ve cornered the market for WiFi hacking tools that run on Solaris.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/aircrackng_01.png)

Below, is a list of tools in Aircrack-ng. We’re going to dig into two of them: `airmon-ng` and `airodump-ng`.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/aircrackng_02.png)

## Airmon-ng

### **Hardware Setup**

The first thing you’ll want to do is find a wireless card that is supported by `aircrack-ng`. The `aircrack-ng` team publishes a thorough tutorial that describes the process of finding a supported card that I recommend you look at here: <https://www.aircrack-ng.org/doku.php?id=compatible_cards>.

The material for this blog was generated with Kali Linux virtual machines running ASUS AWUS036ACH wireless cards. The AWUS036ACH card used to be very reliable and worked well for wireless pentesting. However, I ran into some very serious issues in running AWUS036ACH on Kali last year. Hat tips to [Heyholiday067](https://github.com/Heyholiday067) for writing a patch and [JsphByd](https://github.com/JsphByd) for finding it.

Here’s a quick fix if you’re running into issues while following along with the same set up.

```
sudo apt update && sudo apt upgrade
sudo reboot now
git clone https://github.com/Heyholiday067/rtl8812au
cd rtl8812au
sudo apt install linux-headers...