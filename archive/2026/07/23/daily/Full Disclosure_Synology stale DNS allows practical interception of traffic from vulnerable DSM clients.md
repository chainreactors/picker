---
title: Synology stale DNS allows practical interception of traffic from vulnerable DSM clients
url: https://seclists.org/fulldisclosure/2026/Jul/28
source: Full Disclosure
date: 2026-07-23
fetch_date: 2026-07-24T05:05:43.859144
---

# Synology stale DNS allows practical interception of traffic from vulnerable DSM clients

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# Synology stale DNS allows practical interception of traffic from vulnerable DSM clients

---

*From*: shed riot <shed.riot () gmail com>
*Date*: Wed, 22 Jul 2026 09:27:45 +0100

---

```
# Synology stale DNS allows practical interception of traffic from
vulnerable DSM clients

Vendor case: 904909
Suggested severity: High

## Customer advisory

Synology customers using the affected DSM and Relayd versions listed below
should upgrade immediately.

The relevant man-in-the-middle vulnerabilities were fixed in DSM
6.2.3-25426 Update 3. Customers should install the latest DSM version
available for their device, and in no case remain on a version earlier than
DSM 6.2.3-25426 Update 3 where that update is supported.

Devices that cannot run this or a later version should be considered
unsupported and unsafe for QuickConnect or relay-based communication. They
should be replaced, retired, or isolated from Synology cloud services.

## Summary

Previously disclosed vulnerabilities in Synology DSM allowed an attacker
positioned between a NAS and Synology's infrastructure to impersonate
Synology servers, intercept sensitive information, and, in some cases,
manipulate traffic or execute commands.

Those vulnerabilities included:

* CVE-2021-26560, cleartext transmission by `synoagentregisterd`, allowing
an attacker to spoof a Synology server.
* CVE-2021-26561 and CVE-2021-26562, memory-corruption vulnerabilities
reachable through the same man-in-the-middle position.
* CVE-2021-26564 and CVE-2021-26565, allowing `synorelayd` traffic to be
intercepted or redirected.
* CVE-2021-26566, allowing manipulated inbound QuickConnect traffic to
result in command execution.

Synology fixed these issues in DSM 6.2.3-25426 Update 3.

The new finding described in this advisory is a separate infrastructure
condition that makes exploitation of those old client vulnerabilities
practical.

Synology hostnames were observed resolving to ephemeral cloud IP addresses.
Synology subsequently released those addresses back to the cloud provider
while client devices continued to retain the old DNS result in cache. When
a released address was acquired by a third party, affected clients
continued sending traffic intended for Synology to the new,
attacker-controlled system.

This does not require DNS poisoning, ARP spoofing, phishing, a malicious
website, or a conventional on-path position. The stale DNS record itself
directs the client to the attacker.

## Observed interception in the wild

During a two-week period, four separately released cloud IP addresses
previously used by Synology infrastructure were acquired and monitored.

The supplied traffic captures cover four collection events between 7 July
and 16 July 2026. They contain:

* 28 HTTP or HTTPS requests intended for Synology services.
* 23 distinct client endpoints.
* 22 unique NAS serial numbers, plus one additional client that did not
include its serial number in the captured request.
* 10 plaintext `synoagentregisterd_dsm` requests.
* 14 `Synology Relayd` requests.
* Four additional QuickConnect requests.

The traffic was received without targeting individual customers and without
interfering with Synology's DNS records. The clients contacted addresses
that had legitimately been released by Synology and subsequently assigned
to the collection system.

This is therefore not a theoretical attack scenario. It is a definitive
example of real Synology customer traffic being delivered to a
third-party-controlled endpoint.

## Information exposed

The information varied by request type, but the captured traffic included:

* Authentication keys and token values.
* NAS serial numbers and model identifiers.
* MAC addresses.
* QuickConnect aliases and server identifiers.
* HTTP session cookies.
* Internal IPv4 and IPv6 addresses.
* Internal gateways and network masks.
* DDNS hostnames.
* Enabled services and internal or externally mapped service ports.
* DSM management ports.
* Device time zones and other system metadata.

The plaintext `/finder/set.php` requests exposed device identifiers,
tokens, internal addresses and management ports directly over HTTP.

The TLS-based requests successfully connected to a collection system using
a self-signed certificate. This demonstrates that the affected clients did
not meaningfully authenticate the remote server before transmitting request
data.

Whether every captured token could subsequently be replayed is not
necessary to establish the confidentiality impact. The security failure
occurred when private customer and device data intended for Synology was
delivered to an unauthorised third party.

## Affected traffic paths

The intercepted requests were intended for hostnames including:

* `relayinfo.synology.com`
* `global.quickconnect.to`
* `dec.quickconnect.to`
* `ukc.synology.com`

The traffic included requests to:

* `/finder/set.php`
* `/Serv.php`
* `/alias_update.php`

Cisco Talos previously documented the same `synoagentregisterd` sequence. A
DSM device first requested a finder server from `global.quickconnect.to`,
then transmitted its serial number, token, network addresses and DSM ports
using plaintext HTTP. Talos concluded that both stages could be modified by
a man-in-the-middle attacker.

Talos also documented QuickConnect server impersonation capable of stealing
device credentials through the `synorelayd` and HTTP-redirection flow.

The stale-DNS condition supplies the attacker-controlled endpoint required
by these vulnerabilities without requiring the attacker to compromise DNS
or obtain an existing network position.

## Captured client versions

All captured clients pre-date DSM 6.2.3-25426 Update 3.

| Captured version         | Identified models       | Distinct endpoints |
| ------------------------ | ----------------------- | -----------------: |
| Synology Relayd 1.0-3211 | Model not disclosed     |                  1 |
| Synology Relayd 1.0-3810 | Model not disclosed     |                  1 |
| Synology Relayd 1.0-3827 | DS210j, DS212j, DS710+  |                  4 |
| Synology Relayd 1.0-4493 | DS214+, DS414slim       |                  5 |
| DSM 5.0-4528             | DS214play               |                  1 |
| DSM 5.0-4528 Update 1    | DS713+                  |                  1 |
| DSM 5.0-4528 Update 2    | DS213j                  |                  1 |
| DSM 5.2-5592 Update 4    | DS214se                 |                  1 |
| DSM 5.2-5967 Update 9    | DS1010+, DS115j, RS815+ |                  4 |
| DSM 6.0-8451             | DS416j                  |                  1 |
| DSM 6.0-8754 Update 8    | DS215+, DS216j          |                  3 |
| Total                    |                         |                 23 |

## Required remediation

### Devices that support the patched DSM release

The following identified models can install DSM 6.2.3-25426 Update 3 or a
later DSM release:

* DS212j
* DS213j
* DS214+
* DS214play
* DS214se
* DS215+
* DS216j
* DS414slim
* DS416j
* DS713+
* DS115j
* RS815+

Owners should install the latest DSM version currently offered for the
specific model. DSM 6.2.3-25426 Update 3 is only the minimum version known
to contain the relevant fixes and should not be treated as the ...