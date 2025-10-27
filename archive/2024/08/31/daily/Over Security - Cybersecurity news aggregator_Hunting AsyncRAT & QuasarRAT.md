---
title: Hunting AsyncRAT & QuasarRAT
url: https://dfir.ch/posts/asyncrat_quasarrat/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:07:55.218595
---

# Hunting AsyncRAT & QuasarRAT

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Hunting AsyncRAT & QuasarRAT

15 Jan 2024

**Table of Contents**

* [AsyncRAT](#asyncrat)
  + [Standard Command and Control (C2) Ports](#standard-command-and-control-c2-ports)
  + [Persistence](#persistence)
  + [Mutex](#mutex)
  + [Assembly Information](#assembly-information)
  + [Client information](#client-information)
  + [Plugins](#plugins)
  + [Mutex Hunting](#mutex-hunting)
  + [Persistence techniques](#persistence-techniques)
* [QuasarRAT](#quasarrat)
  + [Standard C2 ports](#standard-c2-ports)
  + [Mutex Hunting](#mutex-hunting-1)
  + [User Agent](#user-agent)
  + [Persistence techniques](#persistence-techniques-1)

# Introduction

[Recorded Future](https://www.recordedfuture.com/) writes in their [Adversary Infrastructure Report 2023](https://www.recordedfuture.com/2023-adversary-infrastructure-report):

*The top 5 malware families we detected this year are AsyncRAT, Quasar RAT, PlugX, ShadowPad, and DarkComet. Interestingly, the top 2 detections are open-source, and the last 3 are well-established tools, showing that our statement from last year’s report remains true:*

*[The] high level of commodity tool use indicates that threat actors are more concerned with blending in and being non-attributable rather than being undetectable, or have simply determined that their targets are not likely to detect even these well-known tools.*

![Top 20 RATs and backdoors](/images/asyncrat/top_20.png "Top 20 RATs and backdoors")

Figure 1: Top 20 Remote Access Trojans (RATs) and backdoors, ranked according to the number of unique Command and Control (C2) servers observed. (Source: Recorded Future)

The final statement in the aforementioned quote is particularly interesting: *[…] have simply determined that their targets are not likely to detect even these well-known tools.* This post combines and extends two longer threads previously shared on X (formerly Twitter) by me, discussing [AsyncRAT](https://twitter.com/malmoeb/status/1555926311738171398) and [QuasarRAT](https://twitter.com/malmoeb/status/1559994785850658817). It highlights techniques and indicators of compromise (IOCs) that we, as defenders, can leverage to identify and hunt infections in our environment caused by these two types of remote access trojans.

## AsyncRAT

AsyncRAT is a prevalent Trojan executed at the end of a (potentially longer) infection chain on target computers. [HP Security](https://threatresearch.ext.hp.com/stealthy-opendocument-malware-targets-latin-american-hotels/) and [Trellix](https://trellix.com/en-us/about/newsroom/stories/threat-labs/targeted-attack-on-government-agencies.html) have recently reported that attackers have been deploying AsyncRAT. Since the source code of AsyncRAT is [publicly available](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp), we obtained a copy of the builder to scrutinize its features and build detection capabilities for this Remote Access Trojan (RAT).

Several methods can be employed to identify endpoints infected with AsyncRAT:

* Detection of standard Command and Control (C2) ports usage.
* Search for persistence mechanisms.
* Examination of Mutexes.
* Last but not least, hunting for dropped DLL files.

### Standard Command and Control (C2) Ports

The builder shows three default ports (6606, 7707, 8808) when assembling a new AsyncRAT client. Within the same interface, users can input the C2 address, to which the AsyncRAT client will establish a connection upon successful infection. Additionally, there is an option to store the C2 address on Pastebin.

![AsyncRat’s default ports](/images/asyncrat/default_ports.png "AsyncRat's default ports")

Figure 2: AsyncRat's default ports

Analysis of 1000 AsyncRAT samples from [ThreatFox](https://threatfox.abuse.ch/) revealed that, as of January 2024, the top three ports for the Command and Control (C2) address were consistently 6606, 7707, and 8808. This indicates that many attackers did not take the effort to modify the default port within the builder. Additionally, it was observed that all samples accessible on Bazaar utilized a C2 port higher than 1024. This information might be helpful for hunts within the Firewall logs (search especially for connections to IP-only domains connecting to a high-port - but beware: this search might return many hits and, without the context of the process that created the network connection, a daunting task).

To retrieve Indicators of Compromise (IOCs) from AsyncRAT samples on ThreatFox, we used the following curl command:

```
curl -X POST https://threatfox-api.abuse.ch/api/v1/ -d '{ "query": "taginfo", "tag": "AsyncRAT", "limit": 1000 }'
```

### Persistence

In the builder, you can specify whether a persistence should be set up or not. When this option is selected, you can define a filename and choose the directory where the payload will be stored (per default, only two directories are available). However, as the source code is available, expanding the selection to include additional paths should be a straightforward task.

![Installation directories](/images/asyncrat/install.png "Installation directories")

Figure 3: Installation directories

### Mutex

AsyncRAT uses a mutex to detect an already infected system. The prefix of the mutex “AsyncMutex\_” was also mentioned in HP Security’s [tweet](https://twitter.com/hpsecurity/status/1551918502528880644), indicating that attackers use the default settings in some cases (which is good for us defenders; read the section about Mutex hunting below).

![Default Mutex](/images/asyncrat/mutex.png "Default Mutex")

Figure 4: Default Mutex

### Assembly Information

Interestingly, we can “clone” the information about the binary from another binary for blending in. In this example, I took the data from the legitimate PingCastleCloud binary - the builder then used the same information for the malicious binary.

![Tamper the assembly information](/images/asyncrat/clone.png "Tamper the assembly information")

Figure 5: Tamper the assembly information

We can also force an obfuscation of the .NET code to slow down Reverse Engineering (I haven’t looked into this feature).

![Simple obfuscation mechanism](/images/asyncrat/obfuscator.png "Simple obfuscation mechanism")

Figure 6: Simple obfuscation mechanism

The sample generated through the outlined steps above comes straight to a VT score of 48 (as of the time when I initially posted the original tweets) - anything but unknown, also detected by various YARA signatures.

![VirusTotal results](/images/asyncrat/yara_hits.jpg "VirusTotal results")

Figure 7: VirusTotal results

### Client information

After executing the AsyncRAT sample we built with the settings outlined above (in the various reports and tweets referenced so far, AsyncRAT is run at the end of a longer infection chain) on our lab machine, we see that our infected machine has reported back to the controller.

![Infected machines](/images/asyncrat/infected_machines.png "Infected machines")

Figure 8: Infected machines

### Plugins

AsyncRAT now has various built-in functions that can further extend the initial access, such as “Password Recovery”. If the function “Password Recovery” is selected, we see in the logs that a DLL (Recovery.dll) was sent to the client.

![Plugin recovery.dll sent to the client](/images/asyncrat/recovery.png "Plugin recovery.dll sent to the client")

Figure 9: Plugin recovery.dll sent to the client

Also, using other plugins, AsyncRAT sends specific files (dlls) to the client. I have yet to look into how these plugins work under the hood, but that might be a topic for another blog post.

![Sending other plugins to the client](/images/asyncrat/other_plugins.png "Sending other plugins to the client")

Figure 10: Sending other plugins to the client

Time for [Velociraptor](https://docs.velociraptor.app/) ð Utilisting the MTF-Hunt, we searched for the names of the ...