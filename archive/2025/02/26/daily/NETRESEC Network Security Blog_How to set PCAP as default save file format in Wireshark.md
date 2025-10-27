---
title: How to set PCAP as default save file format in Wireshark
url: https://www.netresec.com/?page=Blog&month=2025-02&post=How-to-set-PCAP-as-default-save-file-format-in-Wireshark
source: NETRESEC Network Security Blog
date: 2025-02-26
fetch_date: 2025-10-06T20:48:01.139295
---

# How to set PCAP as default save file format in Wireshark

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

Tuesday, 25 February 2025 10:33:00 (UTC/GMT)

## [How to set PCAP as default save file format in Wireshark](/?page=Blog&month=2025-02&post=How-to-set-PCAP-as-default-save-file-format-in-Wireshark)

Did you know that there is a setting in Wireshark for changing the default save file format from pcapng to pcap?

In Wireshark, click Edit, Preferences. Then select Advanced and look for the **capture.pcap\_ng** setting. Change the value to FALSE if you want Wireshark to save packets in the pcap file format. You have to double-click the “TRUE” text to change it into “FALSE”.

![capture.pcap_ng in Wireshark Preferences](https://media.netresec.com/images/Wireshark-preferences-pcap_ng_FALSE_520x406.png)

This setting can also be accessed from the Capture tab in Preferences.

![Disable pcapng in Wireshark Preferences](https://media.netresec.com/images/Wireshark-Preferences-Capture-pcapng_520x244.png)

I recently learned about this setting from [Sake Blok](https://bsky.app/profile/syn-bit.nl) when he commented on my feature request to have Wireshark [use pcap as default savefile format instead of pcapng](https://gitlab.com/wireshark/wireshark/-/issues/20388). I have a feeling that this feature request will not be accepted though, since it has received several downvotes. That’s why I’m trying to spread the word about this setting instead, so that everyone who prefers the pcap file format over pcapng can change the default behavior in their own Wireshark installation.

This setting doesn’t affect command line tools, like dumpcap, tshark, mergecap etc. So if you want to capture packets with dumpcap to a pcap file then you need to use the **-P** switch like this:

dumpcap -P -i eth0 -w dump.pcap

Other command line tools in the Wireshark suite, like tshark and mergecap, require that you instead specify **-F pcap** like this:

mergecap -F pcap -w out.pcap in1.pcap in2.pcap

**What’s Wrong with PCAP-NG?**

Why all this fuss about using [PCAP](https://netresec.com/?b=22A1c18) instead of [PCAP-NG](https://pcapng.com)? Well, it turns out that most Wireshark users are happily unaware of just how much metadata there is in the pcapng files they share online. This metadata typically contains information about the CPU of their computer, the exact version and build of their operating system as well as the name of the network interface on which the capture was performed. For Windows users the network interface details even contain a GUID that [usually is a world-unique identifier](https://learn.microsoft.com/en-us/windows/win32/network-interfaces).

I was once even able to [identify a person](https://netresec.com/?b=1328C6B), who had anonymously shared a pcapng file online, by inspecting metadata in the shared capture file [github.pcapng](https://www.cloudshark.org/captures/cbdd11b20a5c/).
Here's the metadata in that capture file:

![Metadata in a PcapNG file showed in NetworkMiner Professional's capture file properties](https://media.netresec.com/images/github-pcapng_438x503.png)

This screenshot shows the output from the “Show Metadata” functionality in [NetworkMiner Professional](https://www.netresec.com/?page=BuyNetworkMiner).
There's also a great way to show pcapng metadata in Wireshark: Open the pcapng file, click View, Reload as File Format/Capture (Ctrl+Shift+F).

**Mergecap**

The previously mentioned command line tool mergecap, which joins multiple capture files into one, outputs pcapng files by default. In fact, if it is tasked to merge two pcap files (having no metadata), it then creates a pcapng file containing the packets from the two input pcap files enriched with metadata about the computer running mergecap. This metadata is typically information about the operating system as well as the version of mergecap that was used.

![Mergecap ASCII flowchart](https://media.netresec.com/images/mergecap-ascii_1040x480.webp)
![Metadata in PcapNG file created with mergecap](https://media.netresec.com/images/mergecap-c-pcapng_351x250.png)

Providing an output file with the “.pcap” suffix to mergecap will not help, mergecap still generates a pcapng file. You have to use the -F pcap switch to have it generate a pcap file without metadata about your operating system.

**What do Wireshark Users Want?**

I recently conducted two [unscientific](https://x.com/netresec/status/1889964833761833095) [polls](https://infosec.exchange/%40netresec/114058370841160289), where I asked which savefile format Wireshark should use as default.

![Poll results from X and Mastodon: 51 voted for pcap and 35 voted for pcapng](https://media.netresec.com/images/pcap-pcapng-poll-results_943x530.webp)

In total the polls got 86 votes, where 51 voted for pcap and 35 preferred pcapng.
I don't want to draw any real conclusions from these results though, primarily due to the low number of participants but also because there might be a bias among the people who were reached by these polls.

**Looking Ahead**

I reach out to people I know every now and then when I notice that they are sharing pcapng files containing potentially sensitive metadata. They then have to decide if they are okay with this or if they want to go through the process of replacing the pcapng files with pcap files. In many cases they choose the latter, which can be quite tricky if that involves [removing files from GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

I eventually got tired of doing this, especially when I realized that even very skilled Wireshark users often don’t know that pcapng files store metadata about their computers. Reminding people to select the “pcap” format every time they save a capture file doesn’t seem to be the solution. I therefore hope that this blog post can help Wireshark users avoid accidentally sharing unnecessary metadata in the future.

For more information about the pcapng format, please visit [pcapng.com](https://pcapng.com).

Posted by Erik Hjelmvik on Tuesday, 25 February 2025 10:33:00 (UTC/GMT)

Tags:
#[wireshark](/?page=Blog&tag=wireshark)​
#[PCAP](/?page=Blog&tag=PCAP)​
#[pcap-ng](/?page=Blog&tag=pcap-ng)​
#[dumpcap](/?page=Blog&tag=dumpcap)​
#[metadata](/?page=Blog&tag=metadata)​
#[ASCII-art](/?page=Blog&tag=ASCII-art)​

Short URL:
<https://netresec.com/?b=2523d40>

### Recent Posts

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

» [PureRAT = ResolverRAT = PureHVNC](/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC)

» [PureLogs Forensics](/?page=Blog&month=2025-07&post=PureLogs-Forensics)

» [CapLoader 2.0.1 Released](/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released)

» [Detecting PureLogs traffic with CapLoader](/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader)

» [CapLoader 2.0 Released](/?page=Blog&month=2025-06&post=CapLoader-2-0-Released)

» [Comparison of tools that extract files from PCAP](/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP)

### Blog Archive

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

» [2014 Blog...