---
title: Oh my .. ! - Suspicious network traffic detected including Ransomware
url: https://dfir.ch/posts/suspicious_network_traffic_ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-23
fetch_date: 2025-10-06T20:12:52.630669
---

# Oh my .. ! - Suspicious network traffic detected including Ransomware

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

# Oh my .. ! - Suspicious network traffic detected including Ransomware

22 Jan 2025

**Table of Contents**

* [Introduction](#introduction)
* [Investigation](#investigation)
* [A few hours later..](#a-few-hours-later)
* [ConnectionAttempt](#connectionattempt)
* [To have a full picture..](#to-have-a-full-picture)
* [Conclusion](#conclusion)

## Introduction

A customer contacted us due to a high-severity ransomware alert in `Windows Defender for Endpoint` (Figure 1).

![Suspicious network traffic detected, including Ransomware](/images/suspicious_network_traffic/alert.png "Suspicious network traffic detected including Ransomware")

Figure 1: Suspicious network traffic detected including Ransomware

Clicking on one of the alerts does not reveal additional details besides the IP address (Figure 2).

![Process Tree](/images/suspicious_network_traffic/process_tree.png "Process Tree")

Figure 2: Process Tree

After further clicks, we end up at the explanation in Figure 3, which doesnât inspire confidence. What exactly is happening here, and which process on the host is responsible for these network connections?

![Tibbar Ransomware](/images/suspicious_network_traffic/tibbar.png "Tibbar Ransomware")

Figure 3: Tibbar Ransomware

## Investigation

After exporting the timeline from the affected computer, we see the following details (truncated):

```
2025-01-17T14:56:35.179	malmoeb-one ConnectionAttempt
185.149.120.3 58509 185.X.X.X 25 287491

{
  "direction": "In",
  "Source Mac": "00:1d:d8:b7:1c:6c",
  "Destination Mac": "f4:cc:55:a4:29:00",
  "Tcp Flags": 2,
  "Packet Size": 60
}

TcpV4 Ransomware (alertCategory)
```

Source IP `185.149.120.3` tried to connect to our customer’s server on port 25 (SMTP) using a TCP SYN packet of size 60 bytes. However, the customer told us that this server is **not** Internet-exposed (which, however, turned out not to be true). Microsoft wrote an insightful blog post about `Internet-facing devices`. You can find the full article [here](https://learn.microsoft.com/en-us/defender-endpoint/internet-facing-devices).

Here is a `Kusto-Query` for finding internet-facing devices, provided by my colleague [Roger Eisenecher](https://www.linkedin.com/in/roger-eisenecher/):

```
DeviceNetworkEvents
| where RemoteIPType == "Public"
| where ActionType == @"InboundConnectionAccepted"
| distinct DeviceName, InitiatingProcessFileName, LocalPort
```

`RemoteIPType` is a Microsoft classification that can be used well for such queries. In addition, the following `Kusto-Query` could also be helpful in finding internet-facing servers in the network by querying the `ActionType` `InboundInternetScanInspected`, which could also indicate scanning activities.

```
DeviceNetworkEvents
// Filter on devices that have been scanned
| where ActionType == "InboundInternetScanInspected"
| project IP_Source_ScannerAttempt=LocalIP,Country_Source_ScannerAttempt=tostring(geo_info_from_ip_address(LocalIP).country), PublicScannedIP= RemoteIP,PublicScannedIP_country=tostring(geo_info_from_ip_address(RemoteIP).country), PublicScannedPort= RemotePort,DeviceName
```

The server has appeared in both queries - which means that the server is exposed on the Internet and could, therefore, potentially be attacked. A last way to check if the server is exposed - check the tags assigned to the host:

![Internet-Facing](/images/suspicious_network_traffic/internet_facing.png "Internet-Facing")

Figure 4: Internet-Facing

## A few hours later..

A few hours later on the same day - another customer reports suspicious network traffic detected by `Windows Defender for Endpoint` (DFE):

```
2025-01-17T13:21:38.775	malmoeb-two ConnectionAttempt
185.149.120.3 58509 185.X.X.X 25 287491

{
  "direction": "In",
  "Source Mac": "00:50:56:b2:9a:8b",
  "Destination Mac": "70:db:98:2d:33:31",
  "Tcp Flags": 2,
  "Packet Size": 60
}

TcpV4 Ransomware (alertCategory)
```

The same IP address appeared again, but this time it was associated with a mail server, which is intentionally exposed to the internet by design.

## ConnectionAttempt

The logs clearly show that the `ActionType` was `ConnectionAttempt` rather than `InboundConnectionAccepted`. Here is a short breakdown:

* **ConnectionAttempt** - An attempt to establish a TCP connection (syn)
* **InboundConnectionAccepted** - The connection was accepted - but it’s not so simple, see the next section

Microsoft has classified the IP address `185.149.120.3` as malicious, making a simple SYN packet enough to trigger an alert. However, the alert details are not visible through the GUI and can only be accessed by conducting a detailed review of the timeline or using a KQL query.

![Sysmon vs MDE telemetry](/images/suspicious_network_traffic/sysmon_vs_mde.png "Sysmon vs MDE telemetry")

Figure 5: Sysmon vs MDE telemetry

If you are coming from a `Sysmon` background like me, you might find the `Sysmon vs MDE telemetry` overview from [Olaf Hartong](https://www.linkedin.com/in/olafhartong/) useful (Figure 5). The full slide deck from his presentation `EDR Internals From a Defenders Perspective`, is available [here](https://www.first.org/resources/papers/conf2022/MDEInternals-FIRST.pdf).

## To have a full picture..

The site [KQL Query](https://kqlquery.com) posted an amazing (all of their blog posts are great) article named `Incident Response Part 1: IR on Microsoft Security Incidents (KQL edition)`, [here](https://kqlquery.com/posts/kql-incident-response/) is the full version. Within the analysis of the incident, they also look at `InboundConnectionAccepted` events:

*The query for this section lists all network events with a InboundConnectionAccepted ActionType. That an inbound connection has been accepted does not necessarily mean that an adversary got access to your device, because in most cases you first make a connection to a system and then perform the authentication.*

As in their case, we also saw `InboundConnectionAccepted` in combination with RDP Port `3389`.

*Is that a reason for concern? It depends, the RDP port will probably be open to the internet, but if no successuccessful full login attempt is made within that same period we still do not have to fear too much.*

Well… the question would still be whether RDP really has to be exposed to the Internet or whether there is a misconfiguration here. They use `DeviceNetworkEvents` and `DeviceLogonEvents` to tell if a login was successful and not only rely on `InboundConnectionAccepted. An excellent way for digging deeper.

## Conclusion

Determining what happened in this case without a comprehensive timeline analysis is challenging. While alerts from Windows Defender for Endpoint flag suspicious activities like `ConnectionAttempt` events, these alone do not provide sufficient context to pinpoint the root cause or responsible process.

An analyst must analyse the entire timeline to gain a better overview of the situation to make a final assessment as to whether an attacker has gained access or not. Using the GUI alone with the information available is difficult or even impossible.

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).