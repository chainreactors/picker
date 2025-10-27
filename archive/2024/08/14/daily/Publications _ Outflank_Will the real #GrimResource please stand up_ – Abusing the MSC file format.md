---
title: Will the real #GrimResource please stand up? – Abusing the MSC file format
url: https://www.outflank.nl/blog/2024/08/13/will-the-real-grimresource-please-stand-up-abusing-the-msc-file-format/
source: Publications | Outflank
date: 2024-08-14
fetch_date: 2025-10-06T18:02:45.110884
---

# Will the real #GrimResource please stand up? – Abusing the MSC file format

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

# [Will the real #GrimResource please stand up? – Abusing the MSC file format](https://www.outflank.nl/blog/2024/08/13/will-the-real-grimresource-please-stand-up-abusing-the-msc-file-format/ "Will the real #GrimResource please stand up? – Abusing the MSC file format")

[Cedric Van Bockhaven](https://www.outflank.nl/blog/author/cedric/ "Posts by Cedric Van Bockhaven")
 |
August 13, 2024

In this blog post we describe how the MSC file format can be leveraged to execute arbitrary code via MMC (Microsoft Management Console) for initial access or lateral movement purposes. A sample payload that implements this technique was publicly shared recently. This sample was generated using our Outflank Security Tooling (OST) offering and hence we decided to publish additional details on this method and its discovery.

### Context of this blog post

Recently, [Elastic released details](https://www.elastic.co/security-labs/grimresource) on a new initial access vector technique leveraging MSC files, which they dubbed “GrimResource”. These files can be used to execute code within MMC (Microsoft Management Console). This technique was researched and developed by Outflank as part of the [Outflank Security Tooling (OST) toolkit](https://outflank.nl/ost). The analyzed sample was a payload generated using our In-Phase Builder, which is one of the tools in our OST offering that allows you to create script-based payloads for initial access.

As part of our OST toolkit we develop initial access payload formats for our customers. These payloads then get used in attack simulations (“red teaming”), and eventually it happens that some payloads get uploaded to VirusTotal (accidentally – for example, by a blue team that picked up a sample). Our clients are vetted and we ensure we comply with export control regulations while delivering these payloads. In this case, an initial access vector used for attack simulations was picked up and documented publicly, which could potentially extend its use beyond the vetted community.

Now that the cat is out of the bag, we wanted to clarify a few aspects why we sometimes release techniques and tools publicly or keep them internally, for vetted clients, to be used in attack simulations. Secondly, we will go into the technical details of how this vector was built, why it works and provide additional guidance on the great detection rules published by Elastic.

### History of discovery

We started looking into MSC files about five years ago, which is long before North Korean actors [started abusing this file format](https://www.genians.co.kr/blog/threat_intelligence/facebook). We were triggered by the file format’s presence in the [Outlook blocked attachment list](https://support.microsoft.com/en-us/office/blocked-attachments-in-outlook-434752e1-02d3-4e90-9124-8b81e49a8519).

While we quite quickly discovered a way to leverage MSC files for process execution, we did not find the file format of real interest compared to more prevalent techniques back then. Remember that this was the period in which macros and XLL files were much better options for initial access. This changed over the years when Microsoft Office files came under more scrutiny and when additional effort from our team on researching the MSC file format led to a novel way for abusing this file format for in-process shellcode loading (more on that later).

So who’s the real GrimResource? It’s a combination of the following of our researchers: Stan doing the intial research on the file format, Cedric developing the in-process shellcode loading technique. Kyle developing the actual loader and Max pulling it into our initial access framework so that we could deliver it to our OST clients.

![](https://www.outflank.nl/wp-content/uploads/2024/07/grimresource-1024x295.png)

As you may know, we publish quite some of our research on this blog and our [GitHub page](https://github.com/outflanknl). We believe in sharing. We believe that a more knowledgeable and equipped red teaming community will increase the security posture of organisations and their resilience against real threat actors on the long run. However, some techniques are just too dangerous to disclose to the public. This is one of them. That’s why we decided to release our implementation of weaponizing MSC files (and several other initial access techniques) to vetted members of our OST community only. Below is a screenshot of what this looks like to our customers.

![](https://www.outflank.nl/wp-content/uploads/2024/07/builder-1024x697.jpg)

One of our OST customers used the MSC file format in one of their red teaming operations. The blue team picked up this curious file and uploaded it to VirusTotal, where it was spotted by the Elastic team and they [blogged about their discovery](https://www.elastic.co/security-labs/grimresource). Later on FalconForce [blogged](https://falconforce.nl/falconfriday-detecting-mmc-abuse-using-grimresource-with-mde-0xff24/) and provided [MDE](https://github.com/FalconForceTeam/FalconFriday/blob/master/Execution/0xFF-0544-Script_Interpreter_Loading_DotNet_Assembly_From_Memory-Win.md) [detection](https://github.com/FalconForceTeam/FalconFriday/blob/master/Initial%20Access/0xFF-0545-Suspicious_MSC_File_Launched-Win.md) [rules](https://github.com/FalconForceTeam/FalconFriday/blob/master/Defense%20Evasion/0xFF-0546-Process_Injection_Initiated_By_MMC-Win.md) as well. Now that you know who the real GrimResource is, we publish this blog post with some additional technical details. Our weaponization in OST remains exclusively available to vetted OST customers and will not be published.

### MMC Background

First of all: MMC is the console. MSC is the file format understood by MMC. MMC allows administrators to create consoles, which can manage all sorts of settings on either the local computer or remote computers. Within the console they can add “snap-ins” that provide specific management functionality, such as user account management, system services, device drivers, etc. The custom configuration of these consoles and their snap-ins can then be saved to an XML representation on disk, which is the MSC format.

![](https://www.outflank.nl/wp-content/uploads/2024/06/image-7-1024x656.png)

In the MMC GUI above, we have the scope pane, the results pane, and the actions pane. Interacting with MMC, for our purposes, requires knowledge of a few basic building blocks that we can interact with programmatically:

* **Document**: The loaded MMC console, which includes both the scope pane and the result pane.
* **Scope Nodes**: Items in the hierarchical tree view on the left side of the MMC. It defines t...