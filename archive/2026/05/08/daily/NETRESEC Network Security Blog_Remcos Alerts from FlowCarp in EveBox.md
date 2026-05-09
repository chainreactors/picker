---
title: Remcos Alerts from FlowCarp in EveBox
url: https://www.netresec.com/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox
source: NETRESEC Network Security Blog
date: 2026-05-08
fetch_date: 2026-05-09T05:09:01.881849
---

# Remcos Alerts from FlowCarp in EveBox

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

Friday, 08 May 2026 11:49:00 (UTC/GMT)

## [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

There is a wonderful little web-based alert and event front-end called EveBox, which renders Eve JSON formatted data to a web UI. This blog post demonstrates how EveBox can be used to show alert and flow information that FlowCarp has extracted from a Remcos malware infection.

![pcap to FlowCarp to json to EveBox](https://media.netresec.com/images/pcap-FlowCarp-json-EveBox_3000x1500.webp)

**Remcos RAT**

The starting point of my analysis will be a PCAP file with network traffic from a [Remcos RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.remcos) infection, which [Brad Duncan](https://infosec.exchange/%40malware_traffic) has [published on Malware-Traffic-Analysis.net](https://malware-traffic-analysis.net/2026/03/12/index.html). The password scheme for the zip file containing the PCAP can be found [here](https://malware-traffic-analysis.net/about.html), in case you'd like to follow along and perform the same analysis steps yourself. All commands and examples in this blog post can be run in both Linux and Windows.

JSON formatted alerts and flow data can be extracted from the PCAP file with [FlowCarp](https://flowcarp.com/) like this:

flowcarp --input 2026-03-12-SmartApeSG-ClickFix-activity-for-Remcos-RAT.pcap --format EveJson --output -

But the free community license of [FlowCarp](https://flowcarp.com/) doesn't include a protocol model for Remcos, which is why this command will generate flow events but no alerts about detected Remcos malware traffic. I will therefore submit the pcap file to the free FlowCarp demo server instead, which has a [commercial license](https://www.netresec.com/?page=FlowCarp) that can identify over 600 protocols. No registration or API key is required to use this demo server (as long as users behave − please behave).

curl --data-binary @2026-03-12-SmartApeSG-ClickFix-activity-for-Remcos-RAT.pcap -o remcos-eve.json https://demo.flowcarp.com

The downloaded remcos-eve.json file uses the [Suricata Eve JSON format](https://docs.suricata.io/en/latest/output/eve/eve-json-format.html), so [jq](https://jqlang.org/) queries typically used to process Suricata eve.json log files can be used to parse and filter the JSON output from FlowCarp as well.

* jq -c 'select(.event\_type=="alert")|[.dest\_ip, .dest\_port, .proto, .alert.signature]' < remcos-eve.json
* ["193.178.170.155",443,"TCP","MALWARE protocol detected: TLS, Remcos"]

This FlowCarp alert indicates that the PCAP file contains TLS-encrypted Remcos traffic, which means that FlowCarp has performed a so-called sub-protocol match to detect the protocol inside of TLS without decrypting the TLS layer. A quick way to verify if this traffic is Remcos in TLS is to check the JA3 hash or JA4 fingerprint of the client's TLS handshake.

* tshark -r 2026-03-12-SmartApeSG-ClickFix-activity-for-Remcos-RAT.pcap -Y "ip.dst == 193.178.170.155 and tls.handshake" -T fields -e tls.handshake.ja3 -e tls.handshake.ja4
* a85be79f7b569f1df5e6087b69deb493 t13i010400\_0f2cb44170f4\_5c4c70b73fa0

This nicely matches what we expect to see from TLS encrypted Remcos traffic. For reference these are the JA3 and JA4 fingerprints typically associated with Remcos:

* JA3: a85be79f7b569f1df5e6087b69deb493
* JA4: t13i010400\_0f2cb44170f4\_5c4c70b73fa0
* JA4: t13i010400\_0f2cb44170f4\_1b583af8cc09

There is always a risk of false positives associated with JA3 or JA4 fingerprints, so a rule of thumb is to not blindly trust JA3/JA4 based alerts without having additional indicators of compromise. FlowCarp performs a much deeper identification of sub-TLS protocols than JA3/JA4, but there's still a false positive risk associated with detection of encrypted malware traffic — so make sure to verify alerts like this with other types of data sources, such as event logs from the infected device or OSINT information about the suspected C2 server. For this alert we can see that [@DonPasci](https://x.com/DonPasci) has reported [193.178.170.155:443](https://threatfox.abuse.ch/ioc/1740873/) to ThreatFox as being a Remcos C2 server.

**EveBox**

EveBox is a web-based front-end for Suricata "EVE" alerts and events, created by [Jason Ish](https://infosec.exchange/%40ish). The EveBox source code lives on [GitHub](https://github.com/jasonish/evebox) and pre-built EveBox binaries for Linux and Windows are available on [evebox.org](https://evebox.org/).

This evebox command will fire up a browser and render information about the flows and alerts in the Eve JSON file from FlowCarp:

evebox oneshot remcos-eve.json

![Remcos events from FlowCarp in EveBox](https://media.netresec.com/images/Remcos-events-from-FlowCarp-in-EveBox_1122x1405.png)

The flows and alerts are displayed in reverse order, so that the most recent events are on top. The Remcos alert stands out in red and immediately catches your eye. Let's change Event Type from "All" to "Alert" just to make sure there are no other alerts.

![Remcos alert from FlowCarp in EveBox](https://media.netresec.com/images/Remcos-alert-from-FlowCarp-in-EveBox_1148x648.png)

Looks like this was the only alert in this JSON file.

EveBox is built for Suricata, but it's really nice that it can be used out-of-the-box to read FlowCarp's JSON logs as well. For reference, let's also see what it looks like when we run the same PCAP file through [Suricata](https://suricata.io/) and import eve.json into EveBox.

![Remcos events from Suricata in EveBox](https://media.netresec.com/images/Remcos-events-from-Suricata-in-EveBox_1148x1405.png)

I'm happy to see that Suricata also alerts on the same TCP session as [FlowCarp](https://flowcarp.com/). This alert was raised by the Emerging Threats signature ID 2036594, which triggers whenever the JA3 hash of a TLS handshake is a85be79f7b569f1df5e6087b69deb493.

Posted by Erik Hjelmvik on Friday, 08 May 2026 11:49:00 (UTC/GMT)

Tags:
#[FlowCarp](/?page=Blog&tag=FlowCarp)​
#[Remcos](/?page=Blog&tag=Remcos)​
#[a85be79f7b569f1df5e6087b69deb493](/?page=Blog&tag=a85be79f7b569f1df5e6087b69deb493)​
#[t13i010400\_0f2cb44170f4\_5c4c70b73fa0](/?page=Blog&tag=t13i010400_0f2cb44170f4_5c4c70b73fa0)​
#[t13i010400\_0f2cb44170f4\_1b583af8cc09](/?page=Blog&tag=t13i010400_0f2cb44170f4_1b583af8cc09)​

Short URL:
<https://netresec.com/?b=2659fc0>

### Recent Posts

» [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

» [FlowCarp Identifies Protocols](/?page=Blog&month=2026-05&post=FlowCarp-Identifies-Protocols)

» [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

» [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

» [Decoding malware C2 with CyberChef](/?page=Blog&month=2026-01&post=Decoding-malware-C2-with-CyberChef)

» [Latrodectus BackConnect](/?page=Blog&month=2025-12&post=Latrodectus-BackConnect)

» [NetworkMiner 3.1 Released](/?page=Blog&month=2025-12&post=NetworkMiner-3-1-Released)

» [Optimizing IOC Retention Time](/?page=Blog&month=2025-11&post=Optimizing-IOC-Retention-Time)

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

» [2016 ...