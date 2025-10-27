---
title: Who put the "Dark" in DarkVNC&#x3f;, (Wed, Nov 2nd)
url: https://isc.sans.edu/diary/rss/29210
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-03
fetch_date: 2025-10-03T21:40:47.202855
---

# Who put the "Dark" in DarkVNC&#x3f;, (Wed, Nov 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29208)
* [next](/diary/29214)

# [Who put the "Dark" in DarkVNC?](/forums/diary/Who%2Bput%2Bthe%2BDark%2Bin%2BDarkVNC/29210/)

**Published**: 2022-11-02. **Last Updated**: 2022-11-02 05:07:52 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[1 comment(s)](/diary/Who%2Bput%2Bthe%2BDark%2Bin%2BDarkVNC/29210/#comments)

***Introduction***

VNC is an acronym for Virtual Network Computing.  It is a way of controlling a computer remotely from another computer.  VNC is similar to a Remote Access Tool (RAT).  But unlike a RAT, VNC is a cross-platform screen sharing system that allows full keyboard and visual control, as if you were physically present at the remote host.

VNC-based malware has been part of our threat landscape for a long time.  In recent years, some VNC-based malware has been referred to as [DarkVNC](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win32/DarkVnc!MSR&ThreatID=2147753136) or [HiddenVNC](http://github.com/bartblaze/Yara-rules/blob/e891267014af1f91a64e50d52bbf53b4ec89f804/rules/hacktools/HiddenVNC.yar).

During the past year or so, I've referred to ***any*** VNC activity I've run across as DarkVNC.  But not all VNC traffic is necessarily DarkVNC, so let's figure out who put the "Dark" in DarkVNC.  To answer that question, this diary reviews VNC-based malware samples and activity since 2013.

***VirusTotal's first DarkVNC sample***

VirusTotal's sandbox C2AE will flag certain samples with tags indicating various malware families.  One such flag is [RAT (DarkVNC)](https://www.virustotal.com/gui/search/c2ae%253ADarkVNC/files).  This is a searchable flag for people with a VirusTotal Intelligence subscription.  The first DarkVNC-flagged sample was submitted to VirusTotal on 2013-04-03.  This sample shows a creation date of 2012-12-24.  The SHA256 hash is:

* [811aac3c419782890d5d83a1446d0e045dfc9a6aebdfed0e151fabcc051fe557](https://bazaar.abuse.ch/sample/811aac3c419782890d5d83a1446d0e045dfc9a6aebdfed0e151fabcc051fe557/)

I found my first DarkVNC sample in 2017 as [one of the payloads from a Terror Exploit Kit (EK) infection](https://www.malware-traffic-analysis.net/2017/10/17/index.html).  That [DarkVNC sample](https://bazaar.abuse.ch/sample/dda0f5b8759220bdbd8e5dba8bff49868b12e1d5e3bd273b366050dab0c8dd4f/) generated traffic to 85.17.29.102:443 and triggered an alert for ***ETPRO TROJAN W32/DarkVNC Checkin***.  This activity was referenced in a ReaQta blog in 2017 about DarkVNC that is [currently available through archive.org](https://web.archive.org/web/20171108141600/https%3A//reaqta.com/2017/11/short-journey-darkvnc/).

I didn't see DarkVNC again until mid-2021, when I started discovering newer examples of VNC activity. [One VNC-based malware sample](https://bazaar.abuse.ch/sample/7b844cc75f594f536f486b137817a497407b689725ab45c7904444e82374d4ac/) triggered an alert for ***ETPRO MALWARE VNCStartServer USR Variant CnC Beacon*** on 172.241.27.226:443.  The associated [Twitter thread](https://twitter.com/malware_traffic/status/1409664178357379075) reveals that sample is possibly a HiddenVNC variant of DarkVNC.  Or HiddenVNC is likely another term for samples that others have identified as DarkVNC.

***Current example of VNC-based malware traffic***

What does VNC-based malware traffic look like?  In recent months, I've occasionally found VNC traffic as follow-up activity from IcedID and Qakbot infections.  For Qakbot, follow-up VNC activity has been on 78.31.67.7:443 since as early as June 2022.  When Qakbot's VNC is active, we see two TCP streams using the same IP and port, both running at the same time.

The first TCP stream appears to be a VNC beacon that sends mostly the same sequence of 13 bytes from the infected host.  The infected host then receives mostly the same 13 bytes from the VNC server.  This traffic keeps repeating as long as the VNC session is active.  See the below image for details.

[![](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-01a.jpg)](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-01.jpg)
*Shown above:  TCP stream of the VNC beacon activity shown in Wireshark.*

The second TCP stream for VNC traffic contains much more data, most of it encoded or encrypted, likely related to the screen sharing and keyboard/mouse control used in VNC activity.  This traffic is easily identified by the ASCII characters ***VNC*** somewhere within the first hundred bytes of the TCP stream.  The initial traffic contains a repeating pattern of bytes that provide a distinct visual when viewing the TCP stream.  See the image below for details.

[![](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-02a.jpg)](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-02.jpg)
*Shown above: The second TCP stream for VNC traffic that contains much more data than the first stream.*

Later in the TCP stream, we start seeing data possibly related to the screen sharing and keyboard/mouse control for VNC traffic.  See the image below for details.

[![](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-03a.jpg)](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-03.jpg)
*Shown above:  Data in the second TCP stream possibly related to VNC screen sharing and keyboard/mouse control.*

Of note, VNC activity from Qakbot infections prior to June 2022 has three TCP streams (two beaconing and one data stream) that looked much more like traffic from older samples identified as DarkVNC.  [Here is a previous diary](https://isc.sans.edu/forums/diary/Qakbot%2Binfection%2Bwith%2BCobalt%2BStrike%2Band%2BVNC%2Bactivity/28448/) from March 2022 featuring a Qakbot infection with VNC activity that more closely matches what many think of as DarkVNC or HiddenVNC.  This includes strings with the infected hostname and Windows user account name in the two beaconing TCP streams.

However, in recent months, VNC activity from Qakbot infections match patterns we've seen for VNC activity from IcedID infections.  Below is an example of IcedID with VNC traffic from May 2021.  It looks remarkably similar to VNC from IcedID and Qakbot today.

[![](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-04a.jpg)](https://isc.sans.edu/diaryimages/images/2022-11-02-ISC-diary-image-04.jpg)
*Shown above:  VNC traffic from an IcedID infection on 2021-05-24 similar to VNC from a Qakbot infection on 2022-11-01.*

***Previous examples of follow-up VNC activity from other malware***

Below is a list of blog posts where pcaps are available with VNC traffic from BazarLoader, IcedID, Qakbot, and Trickbot infections since May 2021.  Some of these I didn't realize had VNC traffic at the time.  I originally called most of this activity DarkVNC, but that's not exactly correct.  [According to Netresec](https://www.netresec.com/?page=Blog&month=2022-10&post=IcedID-BackConnect-Protocol), VNC traffic typically seen with IcedID is part of the IcedID BackConnect protocol.  Since June 2022, I'm seeing the same sort of VNC traffic from Qakbot infections, so I wonder if Qakbot has adopted parts of the same protocol.  I also saw similar VNC traffic from BazarLoader in November 2021.

Click on links in the dates to access my blog pages for the associated pcaps.

* [2021-05-24](https://www.malware-traffic-analysis.net/2021/05/24/index.html): TA551 IcedID with VNC over IcedID BackConnect C2 194.5.249.150:8080
* [2021-06-02](https://www.malware-traffic-analysis.net/2021/06/02/index.html): TA551 IcedID with VNC over IcedID BackConnect C2 38.135.122.194:8080
* [2021-06-30](https://www.malware-traffic-analysis.net/2021/06/30/index.html): TA551 Trickbot with DarkVNC on 172.241.27.226:443
* [2021-11-05](https://w...