---
title: Detecting AtlasRAT C2
url: https://www.netresec.com/?page=Blog&month=2026-10&post=Detecting-AtlasRAT-C2
source: NETRESEC Network Security Blog
date: 2026-10-12
fetch_date: 2026-10-13T08:38:26.020847
---

# Detecting AtlasRAT C2

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

Monday, 12 October 2026 14:30:00 (UTC/GMT)

## [Detecting AtlasRAT C2](/?page=Blog&month=2026-10&post=Detecting-AtlasRAT-C2)

![AtlasRAT](https://media.netresec.com/images/AtlasRAT_2000x973.webp)

Around May 2026 [Atlas RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.atlas_rat) began using a new variant of its command-and-control (C2) protocol. Earlier versions started with a distinctive byte sequence:

53 46 75 63 6b 00 00 00

In ASCII, that is “SFuck” followed by three null bytes. The newer traffic starts with “BFuck”, also followed by three null bytes:

42 46 75 63 6b 00 00 00

![CapLoader transcript of AtlasRAT traffic](https://media.netresec.com/images/AtlasRAT-BFuck_CapLoader-Transcript_1200x429.webp)

*Image: CapLoader transcript of AtlasRAT traffic in PCAP from [Triage](https://tria.ge/260925-abldyatt2l/behavioral1)*

**Attribution**

Atlas RAT has been linked to Silver Fox (银狐), a Chinese-nexus threat group also tracked as Void Arachne, TA4922, SwimSnake and UTG-Q-1000. The group has been associated with trojanized software and malware including [ValleyRAT](https://netresec.com/?b=2666e31) (Winos4.0) and Gh0st RAT.

The Atlas RAT link remains circumstantial. However, we have observed ValleyRAT and AtlasRAT using the same C2 servers on different ports, suggesting a shared operator.

**The New C2 Variant**

We found that [FlowCarp](https://flowcarp.com/) could detect the new BFuck variant even though its Atlas RAT detection model had originally been built using examples of the older “SFuck” traffic.

![Alert on win.atlas_rat malware from FlowCarp](https://media.netresec.com/images/AtlasRAT_FlowCarp-alert_1174x961.webp)

*Image: FlowCarp win.atlas\_rat alert for Atlas RAT PCAP from [ANY.RUN](https://app.any.run/tasks/912d297e-9a75-4333-84c0-3b3b92d6e9ee/)*

The updated model now includes examples of both variants. Because FlowCarp analyzes more than just the initial check-in sequence, we expect it to reliably detect Atlas RAT traffic even if that sequence changes again.

The initial check-in also reveals a change in the C2 server’s port. The older variant was primarily seen on TCP ports 886 and 9899. The new variant was observed on TCP port 443.

**Stage 1 Loader**

The initial “BFuck” or “SFuck” check-in comes from a loader. The loader retrieves 300 to 500 kB of shellcode containing a DLL with the full Atlas RAT backdoor. Atlas RAT then opens another connection to the same C2 server, this time using a different protocol.

For more details on the loader, backdoor and C2 traffic structure, see HexaStrike’s [Trust the Tunnel, Get the Trojan](https://hexastrike.com/resources/blog/threat-intelligence/trust-the-tunnel-get-the-trojan-silver-fox-delivers-atlas-rat-via-weaponized-vpn-installers/) write-up by [Maurice Fielenbach](https://www.linkedin.com/in/mauricefielenbach).

**Changes to the Legacy C2 Traffic**

Maurice determines that Atlas RAT’s C2 protocol uses ChaCha20 encryption. Each encrypted packet also carries a 56-byte header in cleartext:

* 4 bytes: sequence number
* 4 bytes: compressed size
* 4 bytes: original size
* 4 bytes: padding or flags
* 32 bytes: ChaCha20 key
* 8 bytes: ChaCha20 nonce

![CapLoader transcript of Atlas RAT C2 traffic](https://media.netresec.com/images/CapLoader-Transcript_AtlasRAT-C2_1200x472.webp)

*Image: Atlas RAT C2 traffic in PCAP from [Triage](https://tria.ge/260318-pgxrgshx2y/behavioral1)*

By the end of March 2026, just a few days after HexaStrike’s publication, we observed the actors change their approach. They began XOR-encrypting the transmitted data with a fixed key that starts with a7 3b f1 8c.

![CapLoader transcript of Atlas RAT C2 trafficw with XOR encryption](https://media.netresec.com/images/CapLoader-Transcript_AtlasRAT-C2_XOR_1200x475.webp)

*Image: Atlas RAT XOR-encrypted C2 header in PCAP from [Triage](https://tria.ge/260331-dzjf2afz9v/behavioral3)*

I won’t go into more detail about this XOR-encrypted variant here. The actors abandoned it in July 2026 in favor of a new approach.

**TLS becomes the new Atlas RAT C2**

In July 2026, Atlas RAT began using TLS for C2 communication. After the initial “BFuck” check-in, the backdoor established a new TLS-encrypted session with the C2 server.

The TLS client and server handshakes have distinctive JA3 fingerprints:

* JA3: e26606c572e55d499b0676e9095e3df8
* JA3S: f98a4985f829b6513fbeccf5b751b458

The C2 server typically presents a self-signed X.509 certificate that impersonates update.microsoft.com.

![Self-signed certificate for update.microsoft.com](https://media.netresec.com/images/X-509_a66308a1fb09c8345228ca00335e633b2dabde53_405x515.webp)

The certificate thumbprint is:

a66308a1fb09c8345228ca00335e633b2dabde53

**Suricata Signatures**

If you’re not ready to deploy [FlowCarp](https://flowcarp.com/) for C2 detection, these Suricata rules can detect the SFuck and BFuck check-ins:

alert tcp-pkt $HOME\_NET any -> $EXTERNAL\_NET any (msg:"Atlas RAT loader SFuck checkin"; flow:to\_server; content:"|53 46 75 63 6b 00 00 00|"; startswith; metadata: malware\_family win.atlas\_rat; classtype:trojan-activity; reference:url,https://netresec.com/?b=26A6cc8; sid:1471105; rev:1;)

alert tcp-pkt $HOME\_NET any -> $EXTERNAL\_NET any (msg:"Atlas RAT loader BFuck checkin"; flow:to\_server; content:"|42 46 75 63 6b 00 00 00|"; startswith; metadata: malware\_family win.atlas\_rat; classtype:trojan-activity; reference:url,https://netresec.com/?b=26A6cc8; sid:1471106; rev:1;)

This rule alerts on Atlas RAT’s C2 TLS handshake:

alert tcp-pkt $HOME\_NET any -> $EXTERNAL\_NET 443 (msg:"Atlas RAT TLS handshake"; flow:established,to\_server; content:"|00 00 0c 00 3d 00 35 00 9c 00 3c 00 2f 00 ff 01 00 00 10 00 0d 00 04 00 02 04 01 00 16 00 00 00 17 00 00|"; offset:43; metadata: malware\_family win.atlas\_rat; classtype:trojan-activity; reference:url,https://netresec.com/?b=26A6cc8; sid:1471107; rev:1;)

And this one on the self-signed X.509 certificate:

alert tls $EXTERNAL\_NET 443 -> $HOME\_NET any (msg:"Atlas RAT fake Microsoft certificate"; flow:established,to\_client; content:"|03 7d 30 82 03 79 30 82 02 61 a0 03 02 01 02 02 14 64 72 4e 8c f1 71 88 bc ff e5 19 0b 69 e0 cb 52 6d 38 9a df 30 0d 06 09 2a 86 48 86 f7 0d 01 01 0b 05 00 30 4c 31 1d 30 1b 06 03 55 04 03 0c 14 75 70 64 61 74 65 2e 6d 69 63 72 6f 73 6f 66 74 2e 63 6f 6d|"; offset:12; depth:107; classtype:trojan-activity; reference:url,https://netresec.com/?b=26A6cc8; sid:1471108; rev:1;)

These Suricata rules are also available for download from our Suricata GitHub repo:
<https://github.com/Netresec/Suricata>

**Further Reading**

More information about Atlas RAT is available in write-ups from [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/ta4922-suspected-chinese-crime-group-going-global) and [Hexastrike](https://hexastrike.com/resources/blog/threat-intelligence/trust-the-tunnel-get-the-trojan-silver-fox-delivers-atlas-rat-via-weaponized-vpn-installers/).

**IOC Lists**

IP-port:

* 23.226.57.50:443
* 38.76.177.46:443
* 43.99.101.175:443
* 45.142.152.180:443
* 116.204.169.70:443
* 150.158.50.175:443
* 156.234.7.48:443
* 192.252.180.45:443

Domains:

* laicaishuli[.]com
* yilufafafa[.]club
* zixungongsi[.]top

Other:

* JA3: e26606c572e55d499b0676e9095e3df8
* JA3S: f98a4985f829b6513fbeccf5b751b458
* Cert SHA-1: a66308a1fb09c8345228ca00335e633b2dabde53

Posted by Erik Hjelmvik on Monday, 12 October 2026 14:30:00 (UTC/GMT)

Tags:
#[Silver Fox](/?page=Blog&tag=Silver Fox)​
#[JA3](/?page=Blog&tag=JA3)​
#[Suricata](/?page=Blog&tag=Suricata)​
#[FlowCarp](/?page=Blog&tag=FlowCarp)​

Short URL:
<https://netresec.com/?b=26A...