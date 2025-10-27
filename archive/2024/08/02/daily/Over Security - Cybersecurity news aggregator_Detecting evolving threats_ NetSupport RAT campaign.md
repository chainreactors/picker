---
title: Detecting evolving threats: NetSupport RAT campaign
url: https://blog.talosintelligence.com/detecting-evolving-threats-netsupport-rat/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-02
fetch_date: 2025-10-06T18:04:57.402297
---

# Detecting evolving threats: NetSupport RAT campaign

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Detecting evolving threats: NetSupport RAT campaign

By
[Christopher Morrison](https://blog.talosintelligence.com/author/christopher-morrison/)

Thursday, August 1, 2024 06:00

[The Deep Dive with NTDR](https://blog.talosintelligence.com/category/the-deep-dive-with-ntdr/)

* Cisco Talos is actively tracking multiple malware campaigns that utilize NetSupport RAT for persistent infections.
* These campaigns evade detection through obfuscation and updates.
* [Snort](https://snort.org/) can provide a strong defense before this malware reaches endpoints.
* In this first Deep Dive with NTDR, we explore how defenders can leverage Snort for the detection of evasive malware threats.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-3cf4f7e5-c0e7-49e0-b865-729d01c4a2c4.png)

In November 2023, security vendors identified a new NetSupport RAT campaign that used fake browser updates from compromised and malicious websites to trick users into downloading a stager that downloads and invokes PowerShell commands to install the NetSupport manager agent onto the victim’s machine and establish persistence.

In January 2024, security researchers published [another analysis](https://www.esentire.com/blog/smartapesg-delivering-netsupport-rat) of the same campaign, although with some differences in the initial JavaScript payload, which demonstrates a threat actor re-focusing on the obfuscation of the initial stager. There are also modifications observed in the agent installation including new paths for the randomized installation.

So, Cisco Talos followed suit with our own in-depth analysis. We identified multiple obfuscation and evasion techniques being used by the campaign and created appropriate detection to keep users protected. By identifying specific weaknesses in the campaign’s obfuscation techniques and [identifying indicators of compromise (IOCs)](https://github.com/Cisco-Talos/IOCs/tree/main/2024/08), we can create highly accurate detection of this campaign. Talos is also in a unique position of having primarily open-source detection tools such as Snort and ClamAV. To highlight these capabilities, we will provide a detailed explanation of our detection methodology.

## Campaign history

NetSupport Manager has been commercially available for remote device administration since 1989. Like many tools in the IT remote support industry, NetSupport Manager has been weaponized by threat actors who either cannot or do not wish to develop their own RAT. Adversaries first started using NetSuport for malicious purposes in 2017, and at this point, most security vendors widely recognize this software as a RAT. The 2020s' shift to remote work for many office workers marked an increased use of NetSupport RAT in more phishing and drive-by download campaigns, as well as being used alongside other loaders. This campaign is the most notable use of NetSupport RAT in recent years, with hundreds of known stager variants across dozens of domains used in a large-scale malicious advertising campaign.

## Component summary

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-99182cd2-3108-4ddf-9781-5905ad5ae54c.png)

Components in VirusTotal graph.

1. Stage 1 is a JavaScript file that is downloaded from one of several malicious advertisements or compromised websites. It’s an obfuscated downloader, keeping a Stage 2 JavaScript and PowerShell payload in memory, which is the actual meat of the dropper. Stage 1 is obfuscated and embedded within otherwise benign JavaScript libraries.
2. In Stage 2, a PowerShell script is run via JavaScript. Both are obfuscated, and the PowerShell is embedded in the JavaScript, and the JavaScript is embedded within large comment blocks of random ASCII hex. The PowerShell makes another HTTP GET to retrieve the base64-encoded ZIP. On receipt, the PowerShell extracts the payload into a semi-random path, starts execution, and then establishes basic registry persistence.
3. The end payload is a completely portable install of the commercial NetSupport Manager RAT utility. Some of the installs come with additional scripts or slight filename changes to avoid more narrow detection.

## Stage 1: JavaScript stager

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-846ace0b-3d10-414b-a861-196c05a43753.png)

From 3b587d0c311e8ebc3bb104d564235c41ef8e64592c7419f17f48e0cee9ebc878.

The screenshot above shows the normalized inner payload for an older version of the JavaScript Stage 1. In this older sample, the actual malicious code is embedded within an otherwise benign JavaScript library. Several libraries are used, including jQuery, moment.js and SheetJS. However, this stage's actual malicious payload is barely obfuscated. The next stage download URL is in plain text. The call to “activeXObject” to create the HTTP connection is in plain text. And similarly, the eval call is in plain text.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-ab795f2c-bd62-4256-a6f3-6a62fd4deeda.png)

From 01d867d552a06bd778c812810a476441681c4bebabf967e80f8024b3856cb03e

Here, we have the normalized content of a very recent (first seen 2024.03.09) sample of the stager from the same campaign. Similarly to the older version, the malicious payload is wrapped in an otherwise benign library. Improving over the previous versions, the malicious payload within is further obfuscated with the open-source tool [javascript-obfuscator](https://github.com/javascript-obfuscator/javascript-obfuscator). This results in the removal of the plaintext “activeXObject” and “eval,” however, the output pattern of JavaScript-obfuscator is highly identifiable, as every variable and function name is a random hexadecimal value prefixed by an underscore.

![](https://blog.talosintelligence.com/content/im...