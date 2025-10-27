---
title: MITM6 Strikes Again: The Dark Side of IPv6
url: https://www.blackhillsinfosec.com/mitm6-strikes-again-the-dark-side-of-ipv6/
source: Black Hills Information Security
date: 2023-02-15
fetch_date: 2025-10-04T06:37:34.650975
---

# MITM6 Strikes Again: The Dark Side of IPv6

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

14
Feb
2023

[Dale Hobbs](https://www.blackhillsinfosec.com/category/author/dale-hobbs/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/)
[IPv6](https://www.blackhillsinfosec.com/tag/ipv6/), [Machine-in-the-Middle](https://www.blackhillsinfosec.com/tag/machine-in-the-middle/), [MITM6](https://www.blackhillsinfosec.com/tag/mitm6/), [ntlmrelayx](https://www.blackhillsinfosec.com/tag/ntlmrelayx/), [Replication-Get-Changes-All](https://www.blackhillsinfosec.com/tag/replication-get-changes-all/)

# [MITM6 Strikes Again: The Dark Side of IPv6](https://www.blackhillsinfosec.com/mitm6-strikes-again-the-dark-side-of-ipv6/)

[Dale Hobbs](https://www.blackhillsinfosec.com/team/dale-hobbs/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/BLOG_chalkboard_00613-1024x576.jpg)

As the world becomes increasingly connected through the internet, cyber attacks have become more sophisticated and prevalent. One type of attack that you may not have heard of is the Machine-in-the-Middle IPv6 (MITM6) attack. In this article, we’ll explore what MITM6 attacks are, how they work, and what you can do to protect yourself and your organization against them.

## What is an MITM6 Attack?

MITM6  is a type of attack that involves intercepting and manipulating the communication between two parties. In this attack, the attacker positions themselves between the two parties and acts as a proxy, allowing them to intercept and alter the communication between the parties.

One common method for carrying out an MITM6 attack is through the use of a rogue IPv6 DHCP server. The attacker can set up a rogue DHCP server and advertise itself as the default DNS server to devices on the network. When a device sends a request to communicate with another device, the rogue router intercepts the request and establishes a connection with the target device on behalf of the original sender. The attacker can then use this position to intercept and alter the communication between the two devices.

## DNS Takeover attacks via IPv6

Typically, people are running IPv4 on their networks. However, IPv6 is also enabled by default on your network. If you look at the network adapter properties on your system, you will likely find that IPv6 is turned on, even though you’re using IPv4.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture1-2.png)

To top it off, IPv6 is most likely set to obtain an IPv6 address automatically from a DHCP server, but in most cases, people are not actively managing IPv6 on the network. As such, DHCP is usually not configured to manage IPv6 on the network.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture2-2.png)

This brings up the question: who or what is providing DNS services for IPv6 on the network? A majority of the time, the answer to that is nobody and nothing!

This means that an attacker can set up a system to listen for IPv6 DNS requests and respond to them by telling the client to send all of its IPv6 traffic to the attacker’s system. Often, this can allow an attacker to get authentication to a Domain Controller via LDAP or SMB.

How, you ask? Well, when an attacker’s machine is intercepting IPv6 traffic, they can intercept authentication requests, intercept the NTLM credentials, and relay them using ntlmrelayx to a Domain Controller. If the relayed authentication request was from a Domain Administrator, the attacker can then use that NTLM credential to create a user account for themselves on the domain. The best part about this is that the mitm6 tool automagically does all of this for you.

Let’s walk through what this attack looks like. First things first, you need to download and install the mitm6 tool from <https://github.com/dirkjanm/mitm6>. Once that’s done, simply run the tool as seen below. In my case, the domain we’re testing with is called adlab.com; you should replace it with your own domain name.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture3-2.png)

As you can see, we pretty quickly started to see IPv6 requests on the network indicating that IPv6 addressing is not managed on the network.

Next, we’re going to set up ntlmrelayx to relay the requests to LDAPS on a domain controller, send the client a fake WPAD file, and automatically dump out any information we find to a folder called ‘loot’ on the local system. As you can see below, a connection request came in, our attacking system relayed the connection attempt to the Domain Contr...