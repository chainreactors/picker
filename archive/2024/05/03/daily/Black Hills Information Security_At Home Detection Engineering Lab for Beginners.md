---
title: At Home Detection Engineering Lab for Beginners
url: https://www.blackhillsinfosec.com/at-home-detection-engineering-lab-for-beginners/
source: Black Hills Information Security
date: 2024-05-03
fetch_date: 2025-10-06T17:15:24.081409
---

# At Home Detection Engineering Lab for Beginners

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

2
May
2024

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Guest Author](https://www.blackhillsinfosec.com/category/author/guest-author/), [How-To](https://www.blackhillsinfosec.com/category/how-to/)
[Detection](https://www.blackhillsinfosec.com/tag/detection/), [framework](https://www.blackhillsinfosec.com/tag/framework/), [homelab](https://www.blackhillsinfosec.com/tag/homelab/), [mitre att&ck](https://www.blackhillsinfosec.com/tag/mitre-attck/)

# [At Home Detection Engineering Lab for Beginners](https://www.blackhillsinfosec.com/at-home-detection-engineering-lab-for-beginners/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/NArboleda-150x150.png)

| [Niccolo Arboleda](https://www.linkedin.com/in/niccoloarboleda/) | Guest Author

*Niccolo Arboleda is a cybersecurity enthusiast and student at the University of Toronto. He is usually found in his home lab studying different cybersecurity tools and working on projects. He is passionate about defending critical infrastructure from cyber-attacks.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/BLOG_chalkboard_00665-1024x576.png)

There are always new and evolving threats that target our environments. It is essential to detect these threats before they cause actual harm to people and their livelihoods.

In this blog, we will cover how to build a simple Security Information and Event Management (SIEM) environment to simulate attacks and give us an understanding of how vital detection is in identifying threats and creating defenses against them. Links to all the software used and relevant documentation will be in the references section at the end of the blog.

\*If you get stuck at one point or another, please refer to the documentation. You will find solutions to your issues there.

### **Setting Up the Environment**

We will need the host machine (your computer), a hypervisor, a manager server, and an endpoint to build the environment.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture1-2.png)

**The Hypervisor:**

The first thing we need to do is pick a hypervisor on which to build our environment. A hypervisor is software that allows us to create virtual machines using our host machine. It is useful in this kind of scenario because we won’t need multiple physical computers to create the environment. There are many hypervisors, but in terms of accessibility and ease of use, the free versions of VMware Workstation or VirtualBox will do just fine. The hypervisor I used for this project is VirtualBox.

**The Manager Server:**

We will use Wazuh as our manager server, as it is open-source and well supported. Wazuh is a platform used for threat detection and incident response. There are other open-source SIEM solutions, such as The ELK Stack or OSSEC , if you would like to explore other options.

In this instance, I recommend using the OVA version to simplify your installation process. The OVA version is a standalone Linux (Amazon Linux 2) virtual machine image with the Wazuh server already installed. I hosted the server inside VirtualBox.

While the documentation section of the Wazuh website will have instructions on installation, there is a high level overview in the below section.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture2-2.png)

Search installation alternatives and click on the Virtual Machine (OVA) link.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture3-1.png)

Download the image by clicking on the wazuh-4.7.3.ova (sha512) link (please note the version may have changed).

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture4-2.png)

Once the image is downloaded, click the import button on VirtualBox and load the file.

Before starting the virtual machine, we will need to go to settings and change the display setting to VMSVGA to prevent the virtual machine from crashing, as outlined in the Wazuh documentation.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture5-2.png)![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture6-2.png)![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture7-2.png)![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture8-1.png)

Once we have the manager server up and running, we will need to take note of its IP address using the ipconfig command so we can load the dashboard later.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/04/Picture9-1.png)

**The Endpoint:**

The endpoint will have three main parts, which are: the operating system, the agent, and the attack-simulation framework. Note: the agent and framework will be instal...