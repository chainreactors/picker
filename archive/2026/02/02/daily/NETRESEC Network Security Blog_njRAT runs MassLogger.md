---
title: njRAT runs MassLogger
url: https://www.netresec.com/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger
source: NETRESEC Network Security Blog
date: 2026-02-02
fetch_date: 2026-02-03T04:10:50.161753
---

# njRAT runs MassLogger

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

Monday, 02 February 2026 19:39:00 (UTC/GMT)

## [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

![njRAT](https://media.netresec.com/images/njRAT-purple_2000x1323.webp)

njRAT is a remote access trojan that has been around for more than 10 years and still remains one of the most popular RATs among criminal threat actors. This blog post demonstrates how [NetworkMiner Professional](https://www.netresec.com/?page=BuyNetworkMiner) can be used to decode the njRAT C2 traffic to extract artifacts like screenshots, commands and transferred files.

A PCAP file with njRAT traffic was [published on malware-traffic-analysis.net](https://malware-traffic-analysis.net/2026/01/29/index.html) last week. After loading this PCAP file, NetworkMiner Professional reveals that the attacker downloaded full resolution screenshots of the victim’s screen.

![Overview of screenshots sent to C2 server](https://media.netresec.com/images/NetworkMinerProfessional_3-1_njRAT_images_523x582.webp)

*Image: Overview of screenshots sent to C2 server*

![Screenshot extracted from njRAT traffic by NetworkMiner](https://media.netresec.com/images/njRAT_Desktop_260129030346.jpg)

*Image: Screenshot extracted from njRAT traffic by NetworkMiner*

The file “New Purchase Order and Specifications.exe” in this screenshot is the njRAT binary that was used to infect the PC.

A list of njRAT commands sent from the C2 server to the victim can be viewed on NetworkMiner’s Parameters tab by filtering for ”njRAT server command”.

![njRAT commands](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Parameters_njRAT_523x479.webp)

The following njRAT commands are present here:

* CAP = take screenshot
* inv = invoke (run) a plugin (dll)
* rn = run a tool (executable)

Additional njRAT commands can be found in our writeup for the [Decoding njRAT traffic with NetworkMiner video](https://netresec.com/?b=2541a39), which we published last year.

**njRAT File Transfers**

The “inv” and “rn” commands both transfer and execute additional code on the victim machine. The “inv” command typically transfers a DLL file that is used as a plugin, while the “rn” commands sends an executable file. These DLL and EXE files are transferred in gzip compressed format, which is why NetworkMiner extracts them as .gz files.

![njRAT files extracted from PCAP](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Files_njRAT_516x296.webp)

*Image: Gzip compressed files extracted from njRAT traffic*

This oneliner command lists the internal/original file names and corresponding MD5 hashes of the gzip compressed executables sent to the victim PC:

* for f in njRAT-rn\*.gz; do echo $f; gunzip -c $f | exiftool - | grep Original; gunzip -c $f | md5sum; done
* njRAT-rn-260129030403.gz
* Original File Name : Stub.exe
* ca819e936f6b913e2b80e9e4766b8e79 -
* njRAT-rn-260129030433.gz
* Original File Name : Stub.exe
* e422a4ce321be1ed989008d74ddb6351 -
* njRAT-rn-260129030451.gz
* Original File Name : CloudServices.exe
* fcbb7c0c68afa04139caa55efe580ff5 -
* njRAT-rn-260129031041.gz
* Original File Name : Stub.exe
* 0ae3798c16075a9042c5dbb18bd10a5c -

The MD5 hashes of the files inside the gzip compressed streams can also be seen on the Parameters tab in NetworkMiner.

![njRAT file MD5 hashes](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Parameters_njRAT_md5_516x296.webp)

**MassLogger**

The “CloudServices.exe” executable is a known credential stealer called MassLogger. This particular [MassLogger sample](https://bazaar.abuse.ch/sample/ea32ac24bd8dbac770beec79fa78d790a6156ceb5ff28d2bdba9b1f28a8b4628/) is hard coded to exfiltrate data in an email to kingsnakeresult@mcnzxz[.]com. The email is sent through the SMTP server cphost14.qhoster[.]net. See the execution of this sample [on Triage](https://tria.ge/260129-qpr2msg16c) for additional details regarding the MassLogger payload in CloudServices.exe.

**IOC List**

njRAT

* 58f1a46dba84d31257f1e0f8c92c59ec = njRAT sample
* 104.248.130.195:7492 = njRAT C2 server
* 801a5d1e272399ca14ff7d6da60315ef = sc2.dll
* ca819e936f6b913e2b80e9e4766b8e79 = Stub.exe
* e422a4ce321be1ed989008d74ddb6351 = Stub.exe
* fcbb7c0c68afa04139caa55efe580ff5 = CloudServices.exe
* 0ae3798c16075a9042c5dbb18bd10a5c = Stub.exe

MassLogger

* fcbb7c0c68afa04139caa55efe580ff5
* kingsnakeresult@mcnzxz[.]com
* cphost14.qhoster.net:587
* 78.110.166.82:587

Posted by Erik Hjelmvik on Monday, 02 February 2026 19:39:00 (UTC/GMT)

Tags:
#[njRAT](/?page=Blog&tag=njRAT)​
#[NetworkMiner Professional](/?page=Blog&tag=NetworkMiner Professional)​
#[malware-traffic-analysis.net](/?page=Blog&tag=malware-traffic-analysis.net)​

Short URL:
<https://netresec.com/?b=262adb9>

### Recent Posts

» [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

» [Decoding malware C2 with CyberChef](/?page=Blog&month=2026-01&post=Decoding-malware-C2-with-CyberChef)

» [Latrodectus BackConnect](/?page=Blog&month=2025-12&post=Latrodectus-BackConnect)

» [NetworkMiner 3.1 Released](/?page=Blog&month=2025-12&post=NetworkMiner-3-1-Released)

» [Optimizing IOC Retention Time](/?page=Blog&month=2025-11&post=Optimizing-IOC-Retention-Time)

» [Online Network Forensics Class](/?page=Blog&month=2025-10&post=Online-Network-Forensics-Class)

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

### Blog Archive

» [2026 Blog Posts](?page=Blog&year=2026)

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)