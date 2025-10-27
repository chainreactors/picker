---
title: Wi-Fi Forge: Practice Wi-Fi Security Without Hardware
url: https://www.blackhillsinfosec.com/wifi-forge/
source: Black Hills Information Security
date: 2025-02-28
fetch_date: 2025-10-06T20:39:20.618666
---

# Wi-Fi Forge: Practice Wi-Fi Security Without Hardware

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

27
Feb
2025

[Ben Bowman](https://www.blackhillsinfosec.com/category/author/ben-bowman/), [Hardware Hacking](https://www.blackhillsinfosec.com/category/how-to/hardware-hacking/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Wireless](https://www.blackhillsinfosec.com/category/red-team/wireless/)
[wi-fi](https://www.blackhillsinfosec.com/tag/wi-fi/), [Wi-Fi Forge](https://www.blackhillsinfosec.com/tag/wi-fi-forge/)

# [Wi-Fi Forge: Practice Wi-Fi Security Without Hardware](https://www.blackhillsinfosec.com/wifi-forge/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/BBowman-150x150.png)

| [Ben Bowman](https://www.blackhillsinfosec.com/team/ben-bowman/)

Ben Bowman is a Security Analyst at Black Hills Information Security. He graduated in 2024 with a degree in cyber operations. Ben conducts research as well as tool development outside of testing.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/BLOG_chalkboard_00710-1.png)

In the world of cybersecurity, it’s important to understand what attack surfaces exist. The best way to understand something is by first doing it. Whether you’re an aspiring penetration tester, a seasoned security researcher, or someone looking to improve your knowledge of wireless networks, the ability to ethically practice Wi-Fi security skills is crucial. But what if you don’t have the necessary hardware or setup to perform these tests?

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Picture7.png)

#### This Is Where Wi-Fi Forge Comes In

Wi-Fi Forge is a tool designed by Joe Boyd and me. It was created with the goal of emulating wireless networks, offering a virtual environment where you can practice Wi-Fi security techniques without needing any physical wireless hardware. With Wi-Fi Forge, you can create real-world Wi-Fi networks that your host machine can see. These networks are real to the host machine, which creates an ability for you as a tester to interact with wireless networks as if they were real. This means that the ability to test wireless networks without hardware is no longer beyond grasp.

### **Key Features of Wi-Fi Forge**

Wi-Fi Forge as a foundational tool allows for the creation of premade labs to spin up within seconds. Enabling users to immediately begin testing wireless access points and tooling. The tool supports the following protocols:

* WPS
* WEP
* WPA
* WPA2
* WPA2 Enterprise
* WPA3

But you may be wondering: What if I want to train on a network that isn’t prepackaged with the tool? This is where templating comes in. Wi-Fi Forge was built with templating in mind. Say you have a pentest coming up and you have all the access point names and want to practice attacking these access points with your tools before the engagement. By using the pre-made template and documentation, you can create access points with the same protocols and names (SSID, BSSID, and channel) to practice engaging them before the test begins. You structure the template to your liking, drop it in the tool, and you can spin up a lab identical to the real environment within minutes.

#### Who Can Benefit From Wi-Fi Forge?

This tool helps to serve the security scene at large. With new testers trying to learn about attack surfaces and inherent security risks that exist in the wireless landscape, this tool fills that gap. Wi-Fi Forge supports the security community by helping new testers learn about wireless attack surfaces and risks. It also allows researchers to test tools against wireless access points during development and provides students with practical experience in understanding wireless network vulnerabilities.

#### Why is Wi-Fi Forge Novel?

Wi-Fi Forge is the first tool to actively enable testing wireless networks from a virtualized environment. This tool also sets a precedent for future research. If wireless networks can be completely virtualized for research and testing whose to say that the next generation of research won’t be virtualized. Imagine a tool that could emulate LTE cellular infrastructure to allow researchers to study for vulnerabilities. This is exactly what’s next for the Forge family of tools. Stay tuned.

#### Getting Our Hands Dirty

This tool sounds cool! What fun would a demonstration be without hands-on activities? To begin, we need to make sure we have the prerequisites:

* Kali, Ubuntu, or Parrot OS Virtual Machine.
* 8 GB of RAM
* 15GB of storage
* A desire to learn about Wi-Fi

Cool! These requirements are low, and with these requirements met, we can continue. First, we need to install the tool.

### **Installation**

To do this you need to navigate to the terminal, for this demonstration I will be using a Kali Li...