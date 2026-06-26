---
title: Ping32 RMM and ValleyRAT
url: https://www.netresec.com/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT
source: NETRESEC Network Security Blog
date: 2026-06-25
fetch_date: 2026-06-26T06:09:29.675371
---

# Ping32 RMM and ValleyRAT

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Thursday, 25 June 2026 09:27:00 (UTC/GMT)

## [Ping32 RMM and ValleyRAT](/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT)

![malware infected laptop](https://media.netresec.com/images/malware-laptop_1000x975.webp)

Fareed Radzi recently [blogged about a malware campaign](https://securelist.com/whatsapp-vbs-rmm-campaign/120290/) observed earlier in June by Kaspersky’s GReAT team. The malware campaign embedded malicious code in VBScripts, which were distributed through WhatsApp DMs. The VBScript then dropped the legitimate Remote Monitoring and Management (RMM) tool ManageEngine Endpoint Central.

Fareed included the IOCs for the following Endpoint Central server IP addresses:

* 202.61.160.208
* 202.61.160.202
* 202.61.160.201
* 202.61.160.160
* 202.61.160.137
* 38.55.151.63

He also noted a link to [ValleyRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.valley_rat):
> Notably, 202.61.160[.]201 had previously been observed as command-and-control infrastructure associated with ValleyRAT and Gh0st RAT activity. Although the overlap raises the possibility of the VBS campaign being linked to the operator of these known malware families, the available evidence is insufficient to confidently attribute the campaign to a known threat actor.

Attribution is difficult, so it makes sense not to call out any specific threat actor just because of a single overlapping IP address. Nevertheless, the threat actor that typically comes to mind when talking about ValleyRAT is [Silver Fox](https://malpedia.caad.fkie.fraunhofer.de/actor/void_arachne) (银狐).

**Retrohunting in Sandboxes**

I searched various online sandboxes for the IP addresses and MD5 hashes that were published in Fareed's blog post. To my delight I found plenty of samples on ANY.RUN as well as Triage. But what was even more interesting was the sandbox executions on Triage for the sample with MD5 hash d43fdaa1f0ee09d7e5f0f94ee9df7b6c. One of the known filenames for this sample was "Bitte füllen Sie das Formular für Umsatzsteuer-Nullsatz-Verkäufe aus..vbs".

Sample executions on Recorded Future Triage Sandbox:

* <https://tria.ge/260325-z4xp4sew7y>
* <https://tria.ge/260325-z763ysex41>

I can’t determine how this sample was originally connected to the ManageEngine Endpoint Central campaign, but it shared several traits with what was described in Fareed’s Securelist write-up.
However, this particular VBScript didn’t install the ManageEngine RMM. Instead it reached out to f004.backblazeb2[.]com and downloaded a dropper.

![Traffic to f004.backblazeb2[.]com on Triage Sandbox](https://media.netresec.com/images/Triage_backblazeb2_1594x429.png)

The dropper then deployed NSecRTS.exe, which turned out to be another RMM tool called “Ping32” from the Chinese company Shandong Anzai Information Technology, aka NSecsoft. This RMM tool has a [history](https://ti.qianxin.com/blog/articles/genuine-surveillance-software-used-by-hackers/) of [being](https://medium.com/%40cipherx9fsec/a-fake-income-tax-email-that-delivered-a-rat-inside-the-attack-0a7b0373e110) [abused](https://www.seqrite.com/blog/indian-income-tax-themed-phishing-campaign-targets-local-businesses/) as a Remote Access Trojan (RAT) by hackers.

The Ping32 RMM used HTTP over multiple TCP ports on 143.92.37.168, and it also communicated via UDP port 18987 on the same server.

![CapLoader transcript of Ping32 RMM UDP traffic](https://media.netresec.com/images/CapLoader_Transcript_Ping32-RMM_538x483.png)

*Image: UDP traffic to 143.92.37.168:18987*

**Pivot to ValleyRAT**

I pivoted on the C2 IP 143.92.37.168, which was used by the malicious Ping32 RMM, and got a [hit on Triage Sandbox](https://tria.ge/260514-agrsxacw6n). Triage classified this sample as DonutLoader and ValleyRAT, and its malware config extractor identified the following attributes:

|  |  |
| --- | --- |
| Family | valleyrat\_s2 |
| Version | 1.0 |
| C2 | 143.92.37.168:10086 |
| Campaign date | 2026-02-02 |

This is interesting, because this is another link between the campaign mentioned in Fareed’s blog post and ValleyRAT. When I examined the ValleyRAT C2 traffic from the Triage sandbox execution I noticed that [CapLoader](https://www.netresec.com/?page=CapLoader) as well as [FlowCarp](https://flowcarp.com/) identified it as [Gh0stKCP](https://netresec.com/?b=259a5af), which is a UDP-based protocol that ValleyRAT sometimes uses to transport its C2 traffic.

![Gh0stKCP flows in CapLoader](https://media.netresec.com/images/CapLoader_Flows_Gh0stKCP_535x845.png)

Use this oneliner to upload the PcapNG file from Triage to the free [FlowCarp](https://flowcarp.com/) demo server and extract IP:port IOCs from FlowCarp alerts.

curl -fSs --data-binary @260514-agrsxacw6n-behavioral1.pcapng https://demo.flowcarp.com | jq -s -c 'map(select(.event\_type=="alert")|[(.dest\_ip + ":" + (.dest\_port|tostring)), .alert.signature])|unique[]'

["143.92.37.168:10086","MALWARE protocol detected: Gh0stKCP"]

If you prefer Suricata, use these custom signatures to detect Gh0stKCP:
<https://github.com/Netresec/Suricata/blob/main/netresec.rules>

You can then use the same jq query as in the FlowCarp example to extract the alert IOCs from Suricata’s eve.json output.

cat eve.json | jq -s -c 'map(select(.event\_type=="alert")|[(.dest\_ip + ":" + (.dest\_port|tostring)), .alert.signature])|unique[]'

["143.92.37.168:10086","Gh0stKCP / HP-Socket ARQ handshake"]
["143.92.37.168:10086","Gh0stKCP close"]

**Silver Fox**

It is difficult to attribute the analyzed malware samples to a specific threat actor, but it is possible that they were used by the notorious Silver Fox group, which is one of China’s largest and most active cybercrime groups.

On a positive note, China Daily recently [reported](https://global.chinadaily.com.cn/a/202606/16/WS6a30cb04a310986e2b460401.html) that Chinese police have taken “criminal compulsory measures” against 27 suspects linked to Silver Fox. The same article also stated that “The gang allegedly sent phishing emails in bulk, stole corporate data and built fraud scenarios to carry out criminal activities totaling more than 7 million yuan ($1 million)”.

Let’s hope this puts a stop to, or at least significantly reduces, the massive flood of malware that has been coming from this threat actor.

**IOC List**

Unknown Downloader

* d43fdaa1f0ee09d7e5f0f94ee9df7b6c (Bitte füllen..vbs)
* hxxps://f004.backblazeb2[.]com/file/fadaoxiao/uamcd.pdf
* hxxps://f004.backblazeb2[.]com/file/gaosu2/CoreShield.msi
* hxxps://fadaoxiao.s3.us-west-004.backblazeb2[.]com/pacc.vbs
* ac63eb8814f20ffd89ce81f51cba6916 (uamcd.pdf)
* 9ca134a5ed592a0fb57e2ad910a71c80 (pacc.vbs)

NSecsoft Ping32 RMM C2

* 143.92.37.168:18987 (UDP)
* 143.92.37.168:38987 (TCP)
* 143.92.37.168:48988 (TCP)
* 143.92.37.168:48991 (TCP)
* 143.92.37.168:48992 (TCP)

DonutLoader/ValleyRAT

* 8266b00c4e45d728cef78b3f5a865f68 (ManagementTool.exe)
* 143.92.37.168:10086 (UDP)

Posted by Erik Hjelmvik on Thursday, 25 June 2026 09:27:00 (UTC/GMT)

Tags:
#[Gh0stKCP](/?page=Blog&tag=Gh0stKCP)​
#[ValleyRAT](/?page=Blog&tag=ValleyRAT)​
#[Suricata](/?page=Blog&tag=Suricata)​
#[FlowCarp](/?page=Blog&tag=FlowCarp)​
#[CapLoader](/?page=Blog&tag=CapLoader)​

Short URL:
<https://netresec.com/?b=2666e31>

### Recent Posts

» [Ping32 RMM and ValleyRAT](/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT)

» [Maximizing IOC Impact](/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact)

» [PolarProxy 2.0.1 Released](/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released)

» [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

» [PolarProxy 2.0 Released]...